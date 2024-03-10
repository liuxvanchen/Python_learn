import acg as acg
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'http://yhdm94.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
# 首先找到所有包含 'index-list-r' 类的div容器
container = soup.find('div', class_='index-list-r')

links = soup.find_all('a')
# 如果找到了这样的容器，继续在这个容器内查找<a>标签

if container:
    for link in links:
        href = link.get('href')  # 获取href属性，即链接
        # 假设`url`是你最初用来获取`response`的URL
        full_url = urljoin(url, href)  # 使用urljoin构造完整的URL
        page_response = requests.get(full_url)
        # 确保你的网络请求有适当的异常处理（如try/except）
        page_content = BeautifulSoup(page_response.text, 'html.parser')

        # 对page_content进行解析，抓取你感兴趣的信息

        print(page_content)
        # 对page_content进行解析，抓取你感兴趣的信息
