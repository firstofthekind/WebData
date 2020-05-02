import ssl
from urllib.request import urlopen

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
count=0
sum=0
for tag in tags:
    count+=1
    var=tag.contents[0].encode()
    var1=int(var)
    sum+=var1
    # Look at the parts of a tag
print(count)
print(sum)
