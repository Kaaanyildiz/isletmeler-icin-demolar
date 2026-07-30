import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ids = [
    '1542037104857-ffbb0b9155fb', # family
    '1511895426328-dc8714191300', # family 2
    '1540829016147-36240d9d033a', # car
    '1512917774080-9991f1c4c750', # home
    '1576091160399-112ba8d25d1d', # health
    '1560250097-0b93528c311a'  # handshake
]

for img_id in ids:
    url = f'https://images.unsplash.com/photo-{img_id}?w=1000&q=80'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, context=ctx)
        print(f'OK - {img_id}')
    except Exception as e:
        print(f'FAIL - {img_id}: {e}')
