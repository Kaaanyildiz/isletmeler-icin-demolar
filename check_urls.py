import re
import urllib.request
import urllib.error

html_file = 'erpa_avm_demo.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

urls = re.findall(r'<img[^>]*src="([^"]+)"[^>]*>', content)
unique_urls = list(set(urls))

print('Testing URLs:')
broken_urls = []
for url in unique_urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        urllib.request.urlopen(req)
        print(f'[OK] {url}')
    except urllib.error.HTTPError as e:
        print(f'[FAILED HTTP {e.code}] {url}')
        broken_urls.append(url)
    except Exception as e:
        print(f'[FAILED ERROR {e}] {url}')
        broken_urls.append(url)

print("Broken URLs:", broken_urls)
