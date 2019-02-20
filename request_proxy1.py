import requests

target_url = 'http://httpbin.org/get'
# target_url = 'http://www.baidu.com'

# 我们对于不同类型的代理进行访问,观察程序运行结果
# 可用与不不用的ip 报什么错?
# 对于高匿和透明代理 ,返回数据的origin 字段有何不同?
proxy_url = '111.177.171.20' # 连接失败
# proxy_url = '116.209.52.54:9999'  # 高匿 可用
# proxy_url = '180.118.77.10:9999' # 超时
proxy_url = '123.117.37.196:9000'
proxies ={
    'http':'http://'+proxy_url
}

response = requests.get(target_url,proxies=proxies)
# response.encoding = 'ISO-8859-1'
response.encoding = 'utf-8'
print(response.url)
print(response.status_code)
print(response.encoding)

print(response.text)

