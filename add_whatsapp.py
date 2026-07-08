import os

def add_whatsapp(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'whatsapp-float' in content or 'ph-whatsapp-logo' in content.lower():
        print(f'{file_path} already has whatsapp')
        return

    wa_html = '''
    <!-- WhatsApp Floating Button -->
    <a href="https://wa.me/905000000000" target="_blank" class="fixed bottom-8 right-8 z-[9999] bg-[#25D366] text-white w-16 h-16 rounded-full flex items-center justify-center shadow-2xl hover:scale-110 hover:bg-[#1ebe57] transition-all duration-500 group" style="animation: pulse-wa 2s infinite;">
        <i class="ph-fill ph-whatsapp-logo text-4xl"></i>
        <span class="absolute -top-12 right-0 bg-white text-slate-800 text-sm font-semibold px-4 py-2 rounded-xl shadow-lg opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none whitespace-nowrap">Sipariş Ver / İletişim</span>
    </a>
    <style>
        @keyframes pulse-wa {
            0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
            70% { box-shadow: 0 0 0 20px rgba(37, 211, 102, 0); }
            100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
        }
    </style>
    '''
    
    content = content.replace('</body>', wa_html + '\n</body>')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Added whatsapp to {file_path}')

files = [
    'c:\\Users\\Msi\\işletmeler için demo üretimi\\betul_sel_demo.html', 
    'c:\\Users\\Msi\\işletmeler için demo üretimi\\kizilcazade_demo.html', 
    'c:\\Users\\Msi\\işletmeler için demo üretimi\\omer_kati_demo.html'
]

for f in files:
    add_whatsapp(f)
