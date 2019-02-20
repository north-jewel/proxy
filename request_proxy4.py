import requests

import json

import random
# 找到一堆可以使用的ip,request_proxy3 的升级版
# 筛选可以使用的ip,输出到 vip.txt中
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

vips = [] # 可用的vip


def add_a_ip_tofile(filename, vip_list):
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write('\n'.join(vip_list))


while len(ips) > 0:
    try:
        rand_ip = random.choice(ips)
        print(rand_ip)
        proxies = {
            'http': 'http://' + rand_ip
        }
        response = requests.get(target_url, proxies=proxies,timeout=2) # 不写这个太浪费时间,如果不写timeout参数,某些服务器会耗死你
        # response.encoding = 'ISO-8859-1'
        response.encoding = 'utf-8'
        print(response.url)
        print(response.status_code)
        print(response.encoding)

        print(response.text)

        print(rand_ip, '可以使用')
        vips.append(rand_ip)

        # todo 没加分割..
    except Exception as e:
        print(rand_ip, '不能用')
        print(e)
    ips.remove(rand_ip)  # 不管可用不可用都 删除

    print('这次完成后:ips的长度',len(ips))

# ips.remove(rand_ip)
add_a_ip_tofile('vip.txt', vips)
# 将可用ip 放到vip.txt 中
