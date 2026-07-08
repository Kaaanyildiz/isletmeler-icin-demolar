import urllib.request
import re
import os

files = ['betul_sel_demo.html', 'kizilcazade_demo.html', 'omer_kati_demo.html']

urls = set()

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            # find src="http..."
            srcs = re.findall(r'src="(http[^"]+)"', content)
            urls.update(srcs)
            # find url('http...')
            url_props = re.findall(r"url\(['\"]?(http[^'\"]+)['\"]?\)", content)
            urls.update(url_props)
    except Exception as e:
        pass

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5)
        print(f"OK: {res.status} - {url}")
    except Exception as e:
        print(f"FAIL: {e} - {url}")
