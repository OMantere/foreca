#!venv/bin/python
import requests
from bs4 import BeautifulSoup
from lib import get_temp

url = 'http://www.foreca.fi/Finland/Helsinki'

if __name__ == '__main__':
    print(get_temp(requests.get(url)))

