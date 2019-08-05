#!/usr/bin/python

import os, re
import globals, common
from elasticsearch import Elasticsearch

from bs4 import BeautifulSoup # library for parsing html
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


def main(parsed_args):
    # traverse root directory, and list directories as dirs and files as files
    base_dir = parsed_args.path
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".html"):
                rel_dir = os.path.relpath(root, base_dir)
                rel_file = os.path.join(rel_dir, file)
                print("indexing %s" % rel_file)

                abs_file_path = os.path.join(base_dir, rel_file)
                infile = open(abs_file_path)
                html_from_file = infile.read()
                json_to_index = extract_fields_from_html(html_from_file)
                json_to_index['rel_file'] = rel_file
                es.index(index=globals.INDEX_NAME, id=None,
                         body=json_to_index)


if __name__ == '__main__':
    parsed_args = common.initial_setup()
    main(parsed_args)



