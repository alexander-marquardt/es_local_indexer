from flask import render_template


def show_home_page(index_name, input_files_root):
    """Generates the html with the initial search box

    Keyword arguments:
    index_name -- name of the index that will be used
    input_files_root -- the base directory which the html files reside in
    """
    generated_html = render_template('home_page.html',
                                     search_text='',
                                     input_files_root=input_files_root,
                                     index_name=index_name)
    return generated_html


def present_results(search_text, index_name, input_files_root, list_of_results):
    """Generates html to display the documents returned from the search

    Keyword arguments:
    search_text -- text entered by gthe user
    index_name -- name of the index that will be used
    input_files_root -- the base directory which the html files reside in
    list_of_results -- the hits from the search
    """

    generated_html = render_template('show_search_results.html',
                                     search_text=search_text,
                                     input_files_root=input_files_root,
                                     index_name=index_name,
                                     pages=list_of_results)
    return generated_html
