import re
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with open('mehtap_isler_demo.html', 'r', encoding='utf-8') as f:
    html = f.read()

urls = re.findall(r'<img[^>]+src="([^"]+)"', html)
for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, context=ctx)
        print(f'OK: {url}')
    except Exception as e:
        print(f'BROKEN: {url} - {e}')
