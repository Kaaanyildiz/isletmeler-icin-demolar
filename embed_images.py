import urllib.request
import base64
import re
from io import BytesIO
from PIL import Image

# High quality relevant image URLs (we will download, resize, and embed these)
images = {
    # 1. Hero Hair Coloring
    "hero_1": "https://images.unsplash.com/photo-1595476108010-b4d1f10d5e43?w=1200&q=70",
    # 2. Hero Bridal
    "hero_2": "https://images.unsplash.com/photo-1541216970279-affbfdd55aa8?w=1200&q=70",
    # 3. Hero Haircut
    "hero_3": "https://images.unsplash.com/photo-1560066984-138dadb4c035?w=1200&q=70",
    # 4. About Us
    "about": "https://images.unsplash.com/photo-1522337660859-02fbefca4702?w=800&q=70",
    # 5. Service 1
    "serv_1": "https://images.unsplash.com/photo-1620916297397-a4a5402a3c6c?w=600&q=70",
    # 6. Service 2
    "serv_2": "https://images.unsplash.com/photo-1512412046876-f386342eddb3?w=600&q=70",
    # 7. Service 3
    "serv_3": "https://images.unsplash.com/photo-1519014816548-bf5fe059e98b?w=600&q=70",
    # 8. Service 4
    "serv_4": "https://images.unsplash.com/photo-1562322140-8baeececf3df?w=600&q=70",
    # 9. Gelin
    "gelin": "https://images.unsplash.com/photo-1478144592103-25e218a04891?w=800&q=70"
}

def get_base64(url, max_width=800):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            img_data = response.read()
        
        img = Image.open(BytesIO(img_data)).convert("RGB")
        
        # Resize
        if img.width > max_width:
            wpercent = (max_width / float(img.width))
            hsize = int((float(img.height) * float(wpercent)))
            img = img.resize((max_width, hsize), Image.Resampling.LANCZOS)
            
        buffer = BytesIO()
        img.save(buffer, format="JPEG", quality=60)
        b64_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return f"data:image/jpeg;base64,{b64_data}"
    except Exception as e:
        print(f"Failed for {url}: {e}")
        return url

html_path = r"c:\Users\Msi\işletmeler için demo üretimi\kokos_demo.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("Downloading and converting images...")
b64_images = {k: get_base64(v) for k, v in images.items()}

# Now we find all img tags and replace their srcs in order
# Or better, we just use regex to find all background images and img srcs and replace them sequentially.
# It's easier to just match the URLs currently in the HTML and replace them.

# Let's extract all current URLs in the HTML
matches = re.findall(r'(https://images\.unsplash\.com/[^"\']*)', html)

# We will replace them one by one.
replacements = [
    b64_images["hero_1"],
    b64_images["hero_2"],
    b64_images["hero_3"],
    b64_images["about"],
    b64_images["serv_1"],
    b64_images["serv_2"],
    b64_images["serv_3"],
    b64_images["serv_4"],
    b64_images["gelin"],
    b64_images["hero_1"], # IG 1
    b64_images["serv_1"], # IG 2
    b64_images["serv_2"], # IG 3
    b64_images["serv_3"]  # IG 4
]

for i, match in enumerate(matches):
    if i < len(replacements):
        # replace only the first occurrence
        html = html.replace(match, replacements[i], 1)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done embedding images!")
