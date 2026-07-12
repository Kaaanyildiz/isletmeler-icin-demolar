import re

# 1. Fix signature in Omer Kati
try:
    with open("omer_kati_demo.html", "r", encoding="utf-8") as f:
        c = f.read()
    c = re.sub(
        r'<img src="https://upload\.wikimedia\.org[^"]*Signature_placeholder\.png"[^>]*>',
        r'<div class="font-serif italic text-3xl opacity-50 mt-4 text-brand-dark">Op. Dr. Ömer Katı</div>',
        c
    )
    with open("omer_kati_demo.html", "w", encoding="utf-8") as f:
        f.write(c)
    print("Fixed Omer Kati Signature")
except Exception as e:
    print(f"Error Omer Kati: {e}")

# 2. Lighten Mehtap Isler
try:
    with open("mehtap_isler_demo.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Colors
    html = re.sub(
        r"light:\s*'[#A-Fa-f0-9]+',.*",
        r"light: '#FFFFFF',", html
    )
    html = re.sub(
        r"surface:\s*'[#A-Fa-f0-9]+',.*",
        r"surface: '#FDFBF7',", html
    )
    html = re.sub(
        r"accent:\s*'[#A-Fa-f0-9]+',.*",
        r"accent: '#C49A45',", html
    )
    html = re.sub(
        r"primary:\s*'[#A-Fa-f0-9]+',.*",
        r"primary: '#FFFFFF',", html
    )
    html = re.sub(
        r"dark:\s*'[#A-Fa-f0-9]+',.*",
        r"dark: '#1C1C1C',", html
    )
    html = re.sub(
        r"gray:\s*'[#A-Fa-f0-9]+'.*",
        r"gray: '#666666'", html
    )

    # CSS
    html = html.replace('background: rgba(17, 17, 17, 0.95);', 'background: rgba(255, 255, 255, 0.95);')
    html = html.replace('background: rgba(17, 17, 17, 0.98);', 'background: rgba(255, 255, 255, 0.98);')
    html = html.replace('rgba(17,17,17,0.8)', 'rgba(255,255,255,0.7)')
    html = html.replace('rgba(17,17,17,0)', 'rgba(255,255,255,0)')
    html = html.replace("bg-[#0a0a0a]", "bg-brand-surface")
    html = html.replace("bg-[#1a1510]", "bg-white")
    html = html.replace("border-white/5", "border-brand-dark/5")
    html = html.replace("border-white/10", "border-brand-dark/10")
    html = html.replace("border-white/20", "border-brand-dark/20")
    html = html.replace("bg-white/5", "bg-brand-dark/5")
    
    # HTML Classes
    html = html.replace('text-white', 'text-brand-dark')
    html = html.replace('text-brand-light', 'text-brand-dark')
    html = html.replace('bg-brand-dark/50', 'bg-white/80') # Instagram feed hover overlay

    with open("mehtap_isler_demo.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Lightened Mehtap Isler")
except Exception as e:
    print(f"Error Mehtap Isler: {e}")
