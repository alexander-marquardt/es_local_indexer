import os

from flask import Flask, request, render_template
from elasticsearch import Elasticsearch

import globals
import presentation
import common

es = Elasticsearch([globals.ES_HOST], http_auth=(globals.ES_USER, globals.ES_PASSWORD))
app = Flask(__name__)


@app.route('/')
def my_form():
    return """
    <div>Search in %s index for: </div>
    <div><form method="POST">
        <input name="text">
        <input type="submit">
    </form></div>
    """ % globals.INDEX_NAME


@app.route('/', methods=['POST'])
def my_form_post():
    search_text = request.form['text'].lower()

    body = render_template("search_body.json", query_string=search_text)
    search_result = es.search(index=globals.INDEX_NAME, body=body)
    generated_html=presentation.present_results(search_result['hits']['hits'])
    return generated_html


@app.route('/offline_search/display/<path:relative_path>')
def open_file(relative_path):

    full_path = os.path.join(app.config['input_files_root'], relative_path)
    infile = open(full_path)
    html_from_file = infile.read()
    return html_from_file


def configure_global_app():
    parsed_args = common.initial_setup()
    app.config['input_files_root'] = parsed_args.path
    print('Files root: ', app.config['input_files_root'])
    return


if __name__ == '__main__':
    configure_global_app()
    app.run()
