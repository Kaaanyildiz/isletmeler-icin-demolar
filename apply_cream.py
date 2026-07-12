import re

with open('mehtap_isler_demo.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix broken images
html = html.replace('1519014816548-bf5fe059e98b', '1560066984-138dadb4c035')
html = html.replace('1516975080661-46383e20e5e0', '1522337360788-8b13dee7a37e')

# 2. Cream background colors in Tailwind config
html = re.sub(r"surface:\s*'[^']+'", "surface: '#FDF1E3'", html) # Warm cream
html = re.sub(r"primary:\s*'[^']+'", "primary: '#FFF8EE'", html) # Lighter cream
html = re.sub(r"light:\s*'[^']+'", "light: '#FFFFFF'", html) # Pure white for text overrides if any
# Change sections that I hardcoded as bg-white to bg-brand-primary so they are cream too
html = html.replace('class="py-32 bg-white"', 'class="py-32 bg-brand-primary"')
html = html.replace('class="py-20 bg-white border-y border-brand-accent/20"', 'class="py-20 bg-brand-primary border-y border-brand-accent/20"')
html = html.replace('bg-white p-10', 'bg-brand-primary p-10')
html = html.replace('bg-white text-brand-gray w-full py-2', 'bg-brand-primary text-brand-dark w-full py-2')

# 3. Fix the header background to be slightly cream so it blends better
html = html.replace('rgba(255, 255, 255, 0.95)', 'rgba(253, 241, 227, 0.95)')
html = html.replace('rgba(255, 255, 255, 0.98)', 'rgba(253, 241, 227, 0.98)')

with open('mehtap_isler_demo.html', 'w', encoding='utf-8') as f:
    f.write(html)
