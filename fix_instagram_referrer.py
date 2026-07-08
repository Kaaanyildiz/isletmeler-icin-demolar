import os

file_path = 'c:\\Users\\Msi\\işletmeler için demo üretimi\\omer_kati_demo.html'
insta_url = 'https://instagram.fist2-3.fna.fbcdn.net/v/t51.82787-19/651545818_18080508191617880_3790980419478725916_n.jpg?efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmNhbmFyeSJ9&_nc_ht=instagram.fist2-3.fna.fbcdn.net&_nc_cat=108&_nc_oc=Q6cZ2gF9aRsFJNhfOobEVwHMeM-Lks6axroK2rdH9Kj9SqrU0jrgJwdeP6TfGIKkA383Cp8&_nc_ohc=dj6z_7SuHhIQ7kNvwHCHDDW&_nc_gid=MF8LSM2W00okYOjx5eLjgA&edm=APoiHPcBAAAA&ccb=7-5&oh=00_AQDHCUdz2uFAQcW87C-OhxO1bJuqn7sTD9g4a-EjiUVe7Q&oe=6A533CDE&_nc_sid=22de04'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

if insta_url in content:
    # Adding referrerpolicy so Instagram servers don't block the request from our local html
    content = content.replace('src="' + insta_url + '"', 'referrerpolicy="no-referrer" src="' + insta_url + '"')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed!")
else:
    print("Not found.")
