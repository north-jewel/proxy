import requests
import bs4
from bs4 import BeautifulSoup

# target_url = 'https://www.xicidaili.com/'
target_url = 'http://httpbin.org/get'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
resp=requests.get(target_url,headers=headers)
print(resp.status_code)
soup = BeautifulSoup(resp.text,'lxml')
print(soup)