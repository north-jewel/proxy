import requests
import bs4
from bs4 import BeautifulSoup

import os
import hashlib

target_url = 'https://www.xicidaili.com/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}


def tofile(path, text):
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(text)


def fromfile(path):
    with open(path, mode='r', encoding='utf-8') as f:
        return f.read()


def download(target_url):
    resp = requests.get(target_url, headers=headers)
    print(resp.status_code)
    return resp.text


ip_list = []


def parse_text(res):
    soup = BeautifulSoup(res, 'lxml')
    ips = soup.select('table tr')
    ips.remove(ips[0])
    for i in ips:
        for j, k in enumerate(i):
            if j == 3:
                port = k.find_next_sibling().get_text()
                ip = k.get_text()
                if ip.startswith('代理'):
                    continue
                ip_list.append(ip + ':' + port)


import hashlib


def getmd5text(text):
    m2 = hashlib.md5()
    m2.update(text.encode('utf-8'))
    return m2.hexdigest()


if os.path.exists(getmd5text(target_url)):
    print('meiyouzouwangluo')
    parse_text(fromfile(getmd5text(target_url)))
else:
    print('zoule wangluo')
    rep = download(target_url)
    tofile(getmd5text(target_url), rep)
    parse_text(fromfile(getmd5text(target_url)))

print(ip_list)
import json

# print(type(json.dumps(ip_list)))
tofile('ips.txt', json.dumps(ip_list))
