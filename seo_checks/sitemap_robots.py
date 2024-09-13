# seo_checks/sitemap_robots.py

import requests

def check_sitemap_robots(url):
    try:
        # URLs for sitemap and robots
        sitemap_url = url.rstrip('/') + '/sitemap.xml'
        robots_url = url.rstrip('/') + '/robots.txt'
        
        # Function to check URL existence, handle redirects, and get final URL
        def check_url(url):
            try:
                response = requests.get(url, allow_redirects=True)  # Follow redirects
                final_url = response.url
                exists = response.status_code == 200
                return final_url, exists
            except requests.RequestException:
                return None, False
        
        # Check sitemap and robots
        final_sitemap_url, has_sitemap = check_url(sitemap_url)
        final_robots_url, has_robots_txt = check_url(robots_url)
        
        return {
            'url': url,
            'final_sitemap_url': final_sitemap_url,
            'has_sitemap': has_sitemap,
            'final_robots_url': final_robots_url,
            'has_robots_txt': has_robots_txt,
            'status': 'success' if has_sitemap or has_robots_txt else 'warning'
        }
    except Exception as e:
        return {
            'url': url,
            'final_sitemap_url': None,
            'has_sitemap': False,
            'final_robots_url': None,
            'has_robots_txt': False,
            'status': 'error'
        }
if __name__ == '__main__':
    check_sitemap_robots("https://zentekinfosoft.com/")