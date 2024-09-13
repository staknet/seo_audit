# seo_checks/image_alt.py

import requests
from bs4 import BeautifulSoup

def get_image_alt_text(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')
        total_images = len(images)
        missing_alt_text = sum(1 for img in images if not img.get('alt'))
        return {'url': url, 'total_images': total_images, 'missing_alt_text': missing_alt_text, 'status': 'success' if missing_alt_text == 0 else 'warning'}
    except Exception as e:
        return {'url': url, 'total_images': 0, 'missing_alt_text': 0, 'status': 'error'}
