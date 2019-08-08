# Introduction
ES Local Indexer is a desktop search system that indexes data into Elasticsearch and that provides an intuitive browser-based interface for searching and paging through the ingested data. The ES Local Indexer project consists of two main components:
1. An "indexing app" - indexes all documents in a given directory tree into Elasticsearch.
2. A "searching app" - generates and displays the search-engine-like search results. 

ES Local Indexer is simple to use. In order to ingest html documents into Elasticsearch and then search them, you just have to start a local instance of Elasticsearch, ingest data into Elasticsearch with the "indexing app", and then start the "searching app". You then use your browser to connect to the "searching app" to search through the ingested data. 

# Purpose
The ES Local Indexer project is intended for the following scenarios:

* It can be used as a reference for implementing search functionality within larger project or as a base for implementing a full-featured search application.
* It can be used for indexing previously downloaded html documents, and providing search capabilities across those documents.

ES Local Indexer is not fully-featured or production-ready and is currently intended to be used locally (i.e. not exposed to the internet).

# Related blog article
See [this blog article](https://alexmarquardt.com/es-local-indexer-using-elasticsearch-for-searching-locally-stored-documents/) for a general overview about ES Local Indexer.

# Requirements

ES Local Indexer is written in Python3 and is tested on Mac OSX. 

ES Local Indexer also relies on the following Python libraries:
* [Elasticsearch python client](https://pypi.org/project/elasticsearch/) - For connecting to Elasticsearch.
* [Beautiful soup](https://pypi.org/project/beautifulsoup4/) - For scraping html.
* [Flask](https://pypi.org/project/Flask/) - Lightweight web application framework.

Installation of these is covered in the next section.

# Installation of Elasticsearch
ES Local Indexer relies on Elasticsearch for core search functionality. If you have not yet done so, follow instructions for [installing Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html).The code assumes that the Elasticsearch server is running at localhost:9200, and you can change this in globals.py if necessary.

# Installation of Python dependencies
We suggest using a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/) to avoid system-wide installation of the required libraries. If you are running on OSX, then you can likely enable the pre-built virtual environment that includes required libraries as follows:
```
source venv/bin/activate
```
If the virtual environment has been sucessfully activated, then the following commands can be executed to ensure that the environment is configured correctly. 
```
python3 indexing_app.py -h
python3 searching_app.py -h
```

If you are not running on OSX or are unable to successfully execute the above commands, then you may need to install required Python dependencies. This can be done as follows: 
```
pip3 install -r requirements.txt
```
If the above was sucessfull, then you should be able to check if you code is functioning by executing the following commands:
```
python3 indexing_app.py -h
python3 searching_app.py -h
```

# Ingesting local documents data into Elasticsearch
To test this code with real documents, you may download offline Elasticsearch documentation in html form from https://github.com/elastic/built-docs. Once you have downloaded the documentation, the html documents are ready for ingestion into Elasticsearch.

In order to ingest the html documents, execute the following command replacing PATH_TO_DOCS with the path to the documentation directory, and INDEX_NAME with the name of the Elasticsearch index that will ingest the html from each page:
```
python3 indexing_app.py -p PATH_TO_DOCS -i INDEX_NAME
```
Once the ingestion process has started, you can move on to the next step (although search results will be more meaningful if you wait for ingestion to complete).

# Searching local documents
Once the documents have been ingested into Elasticsearch, the code to launch the search interface can be executed as follows: 
```
python3 searching_app.py -p PATH_TO_DOCS -i INDEX_NAME
```
The PATH_TO_DOCS and INDEX_NAME should be the same as the values specified when ingesting the documents into Elasticsearch. This will allow you to connect to http://127.0.0.1:5000/ with your web browser, and to begin searching the documents that you previously downloaded and indexed into Elasticsearch.

# How does the UI look
ES Local Indexer provides an HTML-based UI that shows search results and highlights matching words. 
![ES Local Indexer screenshot](https://alexmarquardtcom.files.wordpress.com/2019/08/screenshot-2019-08-07-at-22.06.21.png)

# Contributions
The functionality provided here is bare-bones, and there is a lot of room for improvements. Feel free to copy/fork/modify this code and contribute back. 

