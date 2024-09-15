# app.py

from flask import Flask, request, render_template
from seo_checks import (
    get_meta_details, get_headers, get_image_alt_text,
    check_mobile_friendly, check_broken_links, check_sitemap_robots,
    get_canonical_tag, analyze_links
)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    url = request.form.get('url')
    
    if not url:
        return "URL is required", 400

    # Perform SEO checks
    title_meta = get_meta_details(url)
    headers = get_headers(url)
    image_alt = get_image_alt_text(url)
    mobile_friendly = check_mobile_friendly(url)
    broken_links = check_broken_links(url)
    sitemap_robots = check_sitemap_robots(url)
    canonical_tag = get_canonical_tag(url)
    link_analysis = analyze_links(url)
    
    return render_template(
        'results.html',
        url=title_meta['url'],
        title=title_meta['title'],
        title_length=title_meta['title_length'],
        title_status=title_meta['title_status'],
        meta_description=title_meta['meta_description'],
        meta_length=title_meta['meta_length'],
        meta_status=title_meta['meta_status'],
        headers=headers['headers'],
        total_images=image_alt['total_images'],
        missing_alt_text=image_alt['missing_alt_text'],
        has_viewport=mobile_friendly['has_viewport'],
        total_links = broken_links['total_links'],
        broken_links_count=broken_links['broken_links'],
        redirected_links_count=broken_links['redirected_links'],
        other_not_reachable_links_count=broken_links['other_not_reachable_links'],
        broken_links_details=broken_links.get('details', []),
        has_sitemap=sitemap_robots['has_sitemap'],
        has_robots_txt=sitemap_robots['has_robots_txt'],
        final_sitemap_url=sitemap_robots['final_sitemap_url'],
        final_robots_url=sitemap_robots['final_robots_url'],
        canonical_tag=canonical_tag['canonical_tag'],
        internal_links=link_analysis['internal_links'],
        external_links=link_analysis['external_links']
    )

if __name__ == '__main__':
    app.run(debug=True)
