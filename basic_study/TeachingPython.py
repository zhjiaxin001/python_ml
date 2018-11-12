import os
import requests

print(os.getcwd())
r = requests.get("http://www.baidu.com")
r.encoding = r.apparent_encoding
print (r.url)
print (r.encoding)
print (r.text)