# seo_checks/links.py

import requests
from bs4 import BeautifulSoup

def analyze_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)
        
        internal_links = 0
        external_links = 0    
        for link in links:
            href = link['href']
            if href.startswith(url):
                internal_links += 1
            else:
                external_links += 1
        return {'url': url, 'internal_links': internal_links, 'external_links': external_links, 'status': 'success'}
    except Exception as e:
        return {'url': url, 'internal_links': 0, 'external_links': 0, 'status': 'error'}