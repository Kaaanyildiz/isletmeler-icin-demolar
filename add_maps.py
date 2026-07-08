import os

def inject_maps(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'google.com/maps' in content:
        print(f'{file_path} already has maps')
        return

    map_html = '''
    <!-- Google Maps Integration -->
    <section class="w-full h-[400px] grayscale hover:grayscale-0 transition-all duration-1000 overflow-hidden">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12175.760193154865!2d37.0163351!3d39.7554903!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x407eaa0a96ef8b13%3A0xcdaee506b3a32f6!2zS2FyZGXFn2xlciwgU2l2YXMgTWVya2V6L1NpdmFz!5e0!3m2!1str!2str!4v1700000000000!5m2!1str!2str" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </section>
    '''
    
    # inject before footer
    if '<footer' in content:
        content = content.replace('<footer', map_html + '\n<footer')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Added maps to {file_path}')
    else:
        print(f'No footer found in {file_path}')

files = [
    'c:\\Users\\Msi\\işletmeler için demo üretimi\\betul_sel_demo.html', 
    'c:\\Users\\Msi\\işletmeler için demo üretimi\\kizilcazade_demo.html', 
    'c:\\Users\\Msi\\işletmeler için demo üretimi\\omer_kati_demo.html'
]

for f in files:
    inject_maps(f)
