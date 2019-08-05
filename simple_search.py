import globals
from flask import Flask, request
from elasticsearch import Elasticsearch

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
    result = es.search_template(index=globals.INDEX_NAME, body=body)
    return result


if __name__ == '__main__':
    app.run()