from flask import Flask, request
from elasticsearch import Elasticsearch

import globals, presentation, common

app = Flask(__name__)
es = Elasticsearch([globals.ES_HOST], http_auth=(globals.ES_USER, globals.ES_PASSWORD))


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

    body = {
        "id": "search_es_docs_template",
        "params": {
            "query_string": search_text
        }
    }
    search_result = es.search_template(index=globals.INDEX_NAME, body=body)
    generated_html=presentation.present_results(search_result['hits']['hits'])
    return generated_html


@app.route('/offlinesearch/display')
def open_file():

    # get the value of abs_path (i.e. ?abs_path=some-value)
    abs_path = request.args.get('abs_path')
    infile = open(abs_path)
    html_from_file = infile.read()
    return html_from_file


if __name__ == '__main__':
    parsed_args = common.initial_setup()
    app.run()