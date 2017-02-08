#!venv/bin/python

import argparse

import requests
from bs4 import BeautifulSoup

from args import args
from lib import get_temp

search_url = '/json-complete.php?term='
base_url = 'http://www.foreca.fi'


def search(term):
	return requests.get(base_url + search_url + term).json()[0]


def get_location(search_result):
	return search_result['value'] + ', ' + search_result['country_name']


def fetch_page(search_result):
	post_body = {
		'loc_id': search_result['label'],
		'continent_id': 'NAM',
		'country_id': search_result['country_id'],
		'geolocation_lon': '',
		'geolocation_lat': '',
		'q': get_location(search_result)
	}
	return requests.post(base_url + '/search', data=post_body)


if __name__ == '__main__':
	search_term = ' '.join(args.search_term)
	search_result = search(search_term)
	print(get_location(search_result))
	print(get_temp(fetch_page(search_result)))
