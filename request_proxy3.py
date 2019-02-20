import requests

import json

import random
# 找到一条能使用的代理ip
target_url = 'http://httpbin.org/get'
# target_url = 'http://www.baidu.com'

proxy_url = '111.177.171.20'  # 连接失败
# proxy_url = '116.209.52.54:9999'  # 高匿 可用
# proxy_url = '180.118.77.10:9999' # 超时
proxy_url = '123.117.37.196:9000'


def fromfile(path):
    with open(path, mode='r', encoding='utf-8') as f:
        return f.read()


ip_path = 'ips.txt'
ips_text = fromfile(ip_path)
ips = json.loads(ips_text)

print(type(ips))
# proxies = {
#     'http': 'http://' + proxy_url
# }



find_a_vip = False

while not find_a_vip:
    try:
        rand_ip = random.choice(ips)
        print(rand_ip)
        proxies = {
            'http': 'http://' + rand_ip
        }
        response = requests.get(target_url, proxies=proxies)
        # response.encoding = 'ISO-8859-1'
        response.encoding = 'utf-8'
        print(response.url)
        print(response.status_code)
        print(response.encoding)

        print(response.text)

        print(rand_ip, '可以使用')
        find_a_vip = True
    except Exception as e:
        print(rand_ip,'不能用')
        print(e)
        ips.remove(rand_ip)

# ips.remove(rand_ip)

