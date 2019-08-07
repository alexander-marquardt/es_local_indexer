# Elastic Local Indexer
## Introduction
This code is designed to show how Elasticsearch can be used for indexing data from a local disk into Elasticsearch and then searching data. This could be useful (for example) if you wish have documentation available _and_ searchable while you are offline.

The code given here is designed to provide a base that one can use for reference or to build upon, but this is not considered fully-featured or production-ready code. 

The code is written in Python3 and is tested on Mac OSX. 

# Installation
Once you have downloaded the code, if you are running on OSX, then you can likely just enable the virtual environment and execute the code as follows:
```
source venv/bin/activate
python3 index_pages_app.py -h
python3 search_app.py -h
```

If you are not running on OSX or are unable to successfully execute the above commands, then you may consider installing a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/) to avoid having to deal with system-wide installations. 

In order to install required Python dependencies, execute 
```
pip3 install -r requirements.txt
```
If the above was sucessfull, then you should be able to check if you code is functioning by executing the following commands:
```
python3 index_pages_app.py -h
python3 search_app.py -h
```

# Ensure Elasticsearch is installed and running
This code will send data to a locally running Elasticsearch instance. It assumes that the server is running at localhost:9200 (you can change this in globals.py if necessary).

Installing and executing Elasticsearch is outside of the scope of this readme.

# Ingesting local documents data into Elasticsearch
For demonstration purposes, you may download offline Elasticsearch documentation in html form from: https://github.com/elastic/built-docs. Once you have downloaded the documents, they are ready for ingestion into Elasticsearch. 

In order to ingest these documents, execute the following command replacing PATH_TO_DOCS with the location of the documents that you wish to ingest, and INDEX_NAME with the name of the Elasticsearch index that will contain the information that has been ingested from the documents:
```
python3 index_pages_app.py -p PATH_TO_DOCS -i INDEX_NAME

```
Wait for the above process to complete before moving on to the next step.

# Searching local documents
Once the documents have been ingested into Elasticsearch, they can be searched with the following command. 
```
python3 search_app.py -p PATH_TO_DOCS -i INDEX_NAME
```
The PATH_TO_DOCS and INDEX_NAME should be the same as the values specified when ingesting the documents into Elasticsearch. This will allow you to connct to http://127.0.0.1:5000/ with your web browser, and to begin searching the documents that you previously downloaded.


