import urllib.request
import base64
import os

file_path = 'c:\\Users\\Msi\\işletmeler için demo üretimi\\omer_kati_demo.html'
insta_url = 'https://instagram.fist2-3.fna.fbcdn.net/v/t51.82787-19/651545818_18080508191617880_3790980419478725916_n.jpg?efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmNhbmFyeSJ9&_nc_ht=instagram.fist2-3.fna.fbcdn.net&_nc_cat=108&_nc_oc=Q6cZ2gF9aRsFJNhfOobEVwHMeM-Lks6axroK2rdH9Kj9SqrU0jrgJwdeP6TfGIKkA383Cp8&_nc_ohc=dj6z_7SuHhIQ7kNvwHCHDDW&_nc_gid=MF8LSM2W00okYOjx5eLjgA&edm=APoiHPcBAAAA&ccb=7-5&oh=00_AQDHCUdz2uFAQcW87C-OhxO1bJuqn7sTD9g4a-EjiUVe7Q&oe=6A533CDE&_nc_sid=22de04'

try:
    req = urllib.request.Request(insta_url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    img_data = response.read()
    b64_str = base64.b64encode(img_data).decode('utf-8')
    data_uri = f'data:image/jpeg;base64,{b64_str}'

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where we put it last time
    target_str = 'referrerpolicy="no-referrer" src="' + insta_url + '"'
    if target_str in content:
        content = content.replace(target_str, f'src="{data_uri}"')
    else:
        # Maybe it's just src="..."
        target_str2 = 'src="' + insta_url + '"'
        if target_str2 in content:
            content = content.replace(target_str2, f'src="{data_uri}"')
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print('Converted to base64 successfully!')

except Exception as e:
    print(f'Error: {e}')
