import re
import urllib.request
import urllib.error

html_file = 'birdoy_kebap_demo.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

urls = re.findall(r'<img[^>]*src="([^"]+)"[^>]*>', content)
unique_urls = list(set(urls))

print('Testing URLs in birdoy_kebap_demo.html:')
broken_urls = []
for url in unique_urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        urllib.request.urlopen(req)
        print(f'[OK] {url}')
    except Exception as e:
        print(f'[FAILED] {url} - {e}')
        broken_urls.append(url)

print('Broken URLs:', broken_urls)
