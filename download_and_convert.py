import urllib.request
import base64

url = "https://scontent.cdninstagram.com/v/t51.82787-19/651545818_18080508191617880_3790980419478725916_n.jpg?_nc_cat=103&ccb=7-5&_nc_sid=bf7eb4&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=4fzmZdHkZn0Q7kNvwER5YrW&_nc_oc=AdroOzqUQKGDCYOIwzhenCzwEaP-M06-6_LrrT0WJG2jgI-G1cC6wZIzy5ZcK-wwnVI&_nc_zt=24&_nc_ht=scontent.cdninstagram.com&_nc_gid=E5tfZVZ05iSMW5y88nb_sQ&_nc_ss=7b6a8&oh=00_AQBzLA1RlHTBau2W8n_-dF1VXFwPs0VjRuRADiRtCcNxqg&oe=6A53751E"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        img_data = response.read()
    
    b64_data = base64.b64encode(img_data).decode('utf-8')
    data_uri = f"data:image/jpeg;base64,{b64_data}"
    
    # Read HTML
    html_path = r"c:\Users\Msi\işletmeler için demo üretimi\omer_kati_demo.html"
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We need to replace the image in the 'Hakkımda' section.
    # We'll look for the src containing instagram.fist2-3.fna.fbcdn.net or scontent.cdninstagram.com
    import re
    # Find the current instagram url in the html
    new_html = re.sub(r'src="https://instagram\.fist2-3\.fna\.fbcdn\.net[^"]+"', f'src="{data_uri}"', html)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    print("Successfully downloaded, converted to base64, and updated HTML.")
except Exception as e:
    print(f"Error: {e}")
