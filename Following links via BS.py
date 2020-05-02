import ssl
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: \n')
countEnter = input('Input count: \n')
countEnter = int(countEnter)
posEnter = input('Input position: \n')
posEnter = int(posEnter) - 1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
count = 0
while count <= countEnter:
    print('Retrieving: ', url)
    url = (tags[posEnter].get('href', None))
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count += 1
