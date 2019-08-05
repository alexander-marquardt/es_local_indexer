from flask import render_template


def present_results(list_of_results):
    """Displays the documents returned from the search
    Keyword arguments:
    list_of_results -- the hits from the search
    """

    generated_html = render_template('index.html', pages=list_of_results)
    return generated_html
