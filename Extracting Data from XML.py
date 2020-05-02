import ssl
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



while True:
    summary = 0
    i = 0
    url = input('Enter url: ')
    if len(url) < 1: break

    parms = dict()
    parms['url'] = url
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')
    for a in counts:
        i = i + 1
        summary +=int(a.text)
    print('Count: ', i)
    print('Sum: ', summary)
