import requests
from bs4 import BeautifulSoup

# 定义目标网站的URL
url = 'http://yhdm94.com/'  # 替换为你想要抓取的网站的URL

# 发送HTTP请求获取网页内容
response = requests.get(url)

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(response.text, 'lxml')

# # 查找新闻标题和链接
# news_titles = soup.find_all('a', class_='class')  # 根据实际情况修改选择器
# news_links = soup.find_all('i', class_='class')  # 根据实际情况修改选择器
#
# # 打印抓取到的新闻标题和链接
# for title, link in zip(news_titles, news_links):
#     print(f'标题: {title.text}')
#     print(f'链接: {link.get("href")}')
#     print()
# # 首先找到所有包含 'index-list-r' 类的div容器
# container = soup.find('div', class_='index-list-r')
#
# # 如果找到了这样的容器，继续在这个容器内查找<a>标签
# if container:
#     links = container.find_all('a')

links = soup.find_all('a')

for link in links:
    # 获取每个<a>标签的href属性
    href = link.get('href')
    # 获取<a>标签的文本内容，使用strip()去除多余的空格
    text = link.text.strip()
    print(f'链接: {href}, 文本: {text}')
