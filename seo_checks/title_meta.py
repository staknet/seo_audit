# seo_checks/title_meta.py

import requests
from bs4 import BeautifulSoup

def get_meta_details(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        title_tag = soup.find('title')
        title = title_tag.string if title_tag else None
        title_length = len(title) if title else 0
        title_status = 'success' if 50 <= title_length <= 60 else 'warning'

        meta_tag = soup.find('meta', attrs={'name': 'description'})
        meta_description = meta_tag['content'] if meta_tag else None
        meta_length = len(meta_description) if meta_description else 0
        meta_status = 'success' if 150 <= meta_length <= 160 else 'warning'

        return {
            'url': url,
            'title': title,
            'title_length': title_length,
            'title_status': title_status,
            'meta_description': meta_description,
            'meta_length': meta_length,
            'meta_status': meta_status
        }
    except Exception as e:
        return {
            'url': url,
            'title': None,
            'title_length': 0,
            'title_status': 'error',
            'meta_description': None,
            'meta_length': 0,
            'meta_status': 'error'
        }