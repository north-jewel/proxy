import requests
# 本文件主要让大家了解这个网站是什么作用
target_url = 'http://httpbin.org/get'

proxy_url = ''

response = requests.get(target_url)
print(response.url)
print(response.status_code)
print(response.text)

# "origin": "103.254.71.70 自己的ip, 103.254.71.70 代理ip",