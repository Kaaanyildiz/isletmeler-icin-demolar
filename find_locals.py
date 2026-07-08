import re

files = ['betul_sel_demo.html', 'kizilcazade_demo.html', 'omer_kati_demo.html']
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # src="..."
            srcs = re.findall(r'src="([^"]+)"', content)
            # url('...') or url("...") or url(...)
            urls = re.findall(r"url\(['\"]?([^'\"()]+)['\"]?\)", content)
            
            locals = []
            for s in srcs + urls:
                if not s.startswith('http') and not s.startswith('//') and not s.startswith('data:'):
                    locals.append(s)
            
            if locals:
                print(f'{f} local images: {list(set(locals))}')
    except Exception as e:
        print(e)
