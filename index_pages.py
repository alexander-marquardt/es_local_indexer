#!/usr/bin/python

import os, re
import globals
from elasticsearch import Elasticsearch

# Beautiful Soup is a library for parsing html
from bs4 import BeautifulSoup
from bs4.element import Comment

es = Elasticsearch([globals.ES_HOST], http_auth=(globals.ES_USER, globals.ES_PASSWORD))


# Specify the fields that we want removed from the html
def tags_to_filter_out_for_just_content(element):
    if element.parent.name in ['style', 'script', 'head', 'meta', '[document]', 'title']:
        return False
    if isinstance(element, Comment):
        return False
    return True


# Get the title and text content from the html (ie. strip out scripts, comments, etc.)
def extract_fields_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')

    # Some pages just redirect to others, and so might not have a title set
    try:
        title = soup.title.contents[0]
        title = re.sub('\s+', ' ', title)
    except:
        title = ""

    all_text = soup.findAll(text=True)
    filtered_content = filter(tags_to_filter_out_for_just_content, all_text)
    content = u" ".join(t for t in filtered_content)
    content = re.sub('\s+', ' ', content)
    return {
        "title": title,
        "content": content
    }


# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    for file in files:
        if file.endswith(".html"):
            abs_path = os.path.join(os.path.abspath(root), file)
            print("indexing %s" % abs_path)

            infile = open(abs_path)
            html_from_file = infile.read()
            json_to_index = extract_fields_from_html(html_from_file)
            json_to_index['abs_path'] = abs_path
            es.index(index=globals.INDEX_NAME, doc_type='doc', id=None,
                     body=json_to_index)







