import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='the path to the export file')
    parser.add_argument('--format', default='json', choices=['json', 'csv'], type=str.lower)
    return parser