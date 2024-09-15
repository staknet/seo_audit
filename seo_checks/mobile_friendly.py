# seo_checks/mobile_friendly.py

import requests
from bs4 import BeautifulSoup

def check_mobile_friendly(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        viewport_tag = soup.find('meta', attrs={'name': 'viewport'})
        is_mobile_friendly = bool(viewport_tag)
        return {'url': url, 'has_viewport': is_mobile_friendly, 'status': 'success' if is_mobile_friendly else 'warning'}
    except Exception as e:
        return {'url': url, 'has_viewport': False, 'status': 'error'}