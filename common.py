import argparse


def initial_setup():
    parser = argparse.ArgumentParser()

    required = parser.add_argument_group('required arguments')
    required.add_argument('-p', '--path', help='Path to files to ingest', required=True)

    parsed_args = parser.parse_args()
    print('Executing %s with path=%s' % (parser.prog, parsed_args.path))

    return parsed_args
