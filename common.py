"""
This file contains routines that are common to both indexing and searching.
"""

import argparse

def parse_arguments():
    """Parses the arguments passed on the command line
    """
    parser = argparse.ArgumentParser()

    required = parser.add_argument_group('required arguments')
    required.add_argument('-p', '--path', help='Path to files to ingest', required=True)
    required.add_argument('-i', '--index_name', help='Name of the Elasticsearch index', required=True)

    parsed_args = parser.parse_args()
    print('Executing %s with path=%s' % (parser.prog, parsed_args.path))

    return parsed_args
