

from flask import render_template
import globals


def show_home_page(search_text, input_files_root):
    generated_html = render_template('home_page.html',
                                     search_text=search_text,
                                     input_files_root=input_files_root,
                                     index_name=globals.INDEX_NAME)
    return generated_html


def present_results(search_text, input_files_root, list_of_results):
    """Displays the documents returned from the search
    Keyword arguments:
    list_of_results -- the hits from the search
    """

    generated_html = render_template('show_search_results.html',
                                     search_text=search_text,
                                     input_files_root=input_files_root,
                                     index_name=globals.INDEX_NAME,
                                     pages=list_of_results)
    return generated_html
