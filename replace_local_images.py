import os

file_path = 'c:\\Users\\Msi\\işletmeler için demo üretimi\\omer_kati_demo.html'

replacements = {
    './doktor_gorsel_1.png': 'https://images.unsplash.com/photo-1579684385127-1ef15d508118?q=80&w=800&auto=format&fit=crop',
    './doktor_gorsel_2.jpg': 'https://images.unsplash.com/photo-1551076805-e1869033e561?q=80&w=800&auto=format&fit=crop',
    './info_1.jpg': 'https://images.unsplash.com/photo-1581056771107-24ca5f033842?q=80&w=800&auto=format&fit=crop',
    './info_2.jpg': 'https://images.unsplash.com/photo-1631217868264-e5b90bb7e133?q=80&w=800&auto=format&fit=crop',
    './info_3.jpg': 'https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?q=80&w=800&auto=format&fit=crop',
    './info_4.jpg': 'https://images.unsplash.com/photo-1584982751601-97dcc096659c?q=80&w=800&auto=format&fit=crop'
}

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            changed = True

    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated omer_kati_demo.html")
    else:
        print("No replacements needed.")

except Exception as e:
    print(e)
