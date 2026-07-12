import urllib.request
import base64
import re

url = "https://scontent.cdninstagram.com/v/t51.82787-19/651545818_18080508191617880_3790980419478725916_n.jpg?_nc_cat=103&ccb=7-5&_nc_sid=bf7eb4&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=4fzmZdHkZn0Q7kNvwER5YrW&_nc_oc=AdroOzqUQKGDCYOIwzhenCzwEaP-M06-6_LrrT0WJG2jgI-G1cC6wZIzy5ZcK-wwnVI&_nc_zt=24&_nc_ht=scontent.cdninstagram.com&_nc_gid=E5tfZVZ05iSMW5y88nb_sQ&_nc_ss=7b6a8&oh=00_AQBzLA1RlHTBau2W8n_-dF1VXFwPs0VjRuRADiRtCcNxqg&oe=6A53751E"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        img_data = response.read()
    
    b64_data = base64.b64encode(img_data).decode('utf-8')
    data_uri = f"data:image/jpeg;base64,{b64_data}"
    
    html_path = r"c:\Users\Msi\işletmeler için demo üretimi\omer_kati_demo.html"
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace the existing base64 image or any instagram URL in that spot
    # Since I already replaced it with a base64 string in the last step, I need to match that.
    # We can match `src="data:image/jpeg;base64,[^"]+"`
    new_html, num_subs = re.subn(r'src="data:image/jpeg;base64,[^"]+"', f'src="{data_uri}"', html)
    
    if num_subs == 0:
        # Maybe it's still a URL if previous attempt failed?
        new_html, num_subs = re.subn(r'src="https://[^"]*instagram[^"]+"', f'src="{data_uri}"', html)
        if num_subs == 0:
            print("Could not find the image to replace.")
            exit(1)
            
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    print(f"Successfully downloaded, converted, and replaced {num_subs} instance(s) in HTML.")
except Exception as e:
    print(f"Error: {e}")
