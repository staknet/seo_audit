# seo_checks/canonical.py

import requests
from bs4 import BeautifulSoup

def get_canonical_tag(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        canonical_tag = soup.find('link', rel='canonical')
        canonical_url = canonical_tag['href'] if canonical_tag else "None"
        return {'url': url, 'canonical_tag': canonical_url, 'status': 'success' if canonical_url != "None" else 'warning'}
    except Exception as e:
        return {'url': url, 'canonical_tag': 'Not available', 'status': 'error'}
