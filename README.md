# Introduction
ES Local Indexer is a system that indexes data into Elasticsearch, and that generates an intuitive interface for searching through the ingested data. The ES Local Indexer project is composed of two main components:
1. The "indexing app" - This walks through all of the documents that will be indexed into Elasticserach.
2. The "searching app" - this will generate and display the search-engine-like search results. 

For example, ES Local Indexer allows you perform an offline search through a website that has been downloaded to local storage. The "indexing app" will first index the downloaded html into Elasticsearch, and the "searching app" provides a search-engine-like interface for searching within the ingested web pages. In order to ingest html documents into Elasticsearch and then search them, you just have to start a local instance of Elasticsearch and then point ES Local Indexer at the directory to that contains the html documents! 

The code given in this project is intended to provide a base that can be used as a reference or enhanced to add new functionality -- I do not consider ES Local Indexer to fully-featured or fully production-ready code. Nevertheless, ES Local Indexer would be useful if one has a need to search documents while offline. 

# Requirements

The code is written in Python3 and is tested on Mac OSX. 

ES Local Indexer also relies on the following Python libraries:
* [Elasticsearch python client](https://pypi.org/project/elasticsearch/) - For connecting to Elasticsearch.
* [Beautiful soup](https://pypi.org/project/beautifulsoup4/) - For scraping html.
* [Flask](https://pypi.org/project/Flask/) - Lightweight web application framework.

Installation of these is covered in the next section.

# Installation
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

# Ensure Elasticsearch is installed and running
This code will send data to a locally running Elasticsearch instance. It assumes that the Elasticsearch server is running at localhost:9200 (you can change this in globals.py if necessary).

Installing and executing Elasticsearch is outside of the scope of this readme.

# Ingesting local documents data into Elasticsearch
For demonstration purposes, you may download offline Elasticsearch documentation in html form from https://github.com/elastic/built-docs. Once you have downloaded the documentation, the html documents are ready for ingestion into Elasticsearch. 

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
The PATH_TO_DOCS and INDEX_NAME should be the same as the values specified when ingesting the documents into Elasticsearch. This will allow you to connct to http://127.0.0.1:5000/ with your web browser, and to begin searching the documents that you previously downloaded and indexed into Elasticsearch.

# Contributions
The functionality provided here is bare-bones, and there is a lot of room for improvements. Feel free to copy/fork/modify this code and contribute back. 

