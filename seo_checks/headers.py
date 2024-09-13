# seo_checks/headers.py

import requests
from bs4 import BeautifulSoup

def get_headers(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headers = {f'h{i}': len(soup.find_all(f'h{i}')) for i in range(1, 7)}
        return {'url': url, 'headers': headers, 'status': 'success'}
    except Exception as e:
        return {'url': url, 'headers': {}, 'status': 'error'}
