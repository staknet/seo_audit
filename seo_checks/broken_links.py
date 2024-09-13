# seo_checks/broken_links.py
import requests
from bs4 import BeautifulSoup

def check_broken_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)
        
        total_links = len(links)
        broken_links = 0
        redirected_links = 0
        other_not_reachable_links = 0
        broken_links_details = []

        for link in links:
            href = link['href']
            anchor_text = link.get_text(strip=True)
            if not href.startswith('http'):
                other_not_reachable_links += 1
                continue
            try:
                r = requests.head(href, allow_redirects=True, timeout=5)
                if r.status_code >= 400:
                    broken_links += 1
                    broken_links_details.append({'href': href, 'anchor_text': anchor_text})
                elif 300 <= r.status_code < 400:
                    redirected_links += 1
                else:
                    continue
            except requests.RequestException:
                broken_links += 1
                broken_links_details.append({'href': href, 'anchor_text': anchor_text})
        
        broken_links_details = sorted(broken_links_details, key=lambda x: x['href'])[:10]
        
        return {
        'total_links': total_links,
        'broken_links': broken_links,
        'redirected_links': redirected_links,
        'other_not_reachable_links': other_not_reachable_links,
        'details': broken_links_details  # Make sure 'details' key is included
        }
    except Exception as e:
        return {
            'total_links': 0,
            'broken_links': 0,
            'redirected_links': 0,
            'other_not_reachable_links': 0,
            'broken_links_details': [],
            'status': 'error'
        }

# For debugging and refinement
if __name__ == '__main__':
    result = check_broken_links("https://google.com")
    print("Total Links:", result['total_links'])
    print("Broken Links:", result['broken_links'])
    print("Redirected Links:", result['redirected_links'])
    print("Other Not Reachable Links:", result['other_not_reachable_links'])
    print("Top 10 Broken Links and Anchor Text:")
    for detail in result['broken_links_details']:
        print(f"Link: {detail['href']}, Anchor Text: {detail['anchor_text']}")
