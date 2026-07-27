import re

html_file = "erpa_avm_demo.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Regular expression to extract img src and the closest heading text (context)
# This is a basic parser to see what image is used for what product/banner
pattern = r'<img[^>]*src="([^"]+)"[^>]*>.*?<h[23][^>]*>(.*?)</h[23]>'
matches = re.findall(pattern, content, re.DOTALL)

print("--- ERPA AVM GÖRSEL ALAKA DURUMU KONTROLÜ ---")
for src, context in matches:
    # Clean HTML tags from context
    context_clean = re.sub(r'<[^>]+>', '', context).strip()
    
    # We will do a basic keyword check to determine if the placeholder ID matches the context
    # Since these are Pexels placeholders, we just flag them for manual review/replacement
    print(f"Kategori/Ürün: {context_clean}")
    print(f"Kullanılan Görsel: {src}")
    
    # Basic relevance suggestion logic based on keywords
    suggestion = ""
    if "Koltuk" in context_clean or "Mobilya" in context_clean:
        suggestion = "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=600&q=80 (Sofa/Koltuk)"
    elif "Halı" in context_clean or "Yolluk" in context_clean:
        suggestion = "https://images.unsplash.com/photo-1600166898405-da9535204843?auto=format&fit=crop&w=600&q=80 (Carpet/Halı)"
    elif "Tencere" in context_clean or "Züccaciye" in context_clean or "Yemek Takımı" in context_clean or "Çeyiz" in context_clean or "Bardak" in context_clean or "Airfryer" in context_clean:
        suggestion = "https://images.unsplash.com/photo-1584990347449-a6ab06d72861?auto=format&fit=crop&w=600&q=80 (Glassware/Kitchen)"
    elif "Yatak" in context_clean or "Baza" in context_clean:
        suggestion = "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=600&q=80 (Bed/Yatak Odası)"
    elif "Masa" in context_clean:
        suggestion = "https://images.unsplash.com/photo-1617806118233-18e1c12d40b7?auto=format&fit=crop&w=600&q=80 (Dining Table)"
    else:
        suggestion = "Spesifik bir görsel bulunmalı."
        
    print(f"Önerilen Doğru Link Tipi: {suggestion}")
    print("-" * 50)
