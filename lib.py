# -*- coding: utf8 -*-
from bs4 import BeautifulSoup


def get_temp(response):
	soup = BeautifulSoup(response.text, 'html.parser')
	return (soup.find('h3', text='Viimeisimmät havainnot')
			.parent
			.find('div', {'class': 'left'})
			.find('span', 'txt-xxlarge')
			.text)
