import argparse

parser = argparse.ArgumentParser(description='Foreca command line interface')
parser.add_argument('search_term', type=str, nargs='+', help='Search term for Foreca location search')
args = parser.parse_args()
