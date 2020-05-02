import json
from urllib.request import urlopen

url = input('Input the url\n')
response = urlopen(url)
data = response.read()
info = json.loads(data)
sum = 0
count = 0
for item in info['comments']:
    count += 1
    sum+=item['count']
print(len(info['comments']))
print('User count:', count)
print('Sum is: ', sum)
