import urllib.request
import re

files = [
    r"c:\Users\Msi\işletmeler için demo üretimi\lusse_home_demo.html",
    r"c:\Users\Msi\işletmeler için demo üretimi\betul_sel_demo.html",
    r"c:\Users\Msi\işletmeler için demo üretimi\kizilcazade_demo.html",
    r"c:\Users\Msi\işletmeler için demo üretimi\omer_kati_demo.html"
]

broken_count = 0
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    urls = re.findall(r'src="(http[^"]+)"', content)
    for url in urls:
        if 'instagram' in url or 'fbcdn' in url: 
            continue
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            res = urllib.request.urlopen(req, timeout=5)
            if res.getcode() >= 400:
                print(f"Broken ({res.getcode()}): {url} in {fpath}")
                broken_count += 1
        except Exception as e:
            if "HTTP Error 403" in str(e):
                pass
            print(f"Error accessing {url} in {fpath}: {e}")
            broken_count += 1

print(f"Finished checking. Total broken: {broken_count}")
