from bs4 import BeautifulSoup

# 假设这是你从网页获取的HTML字符串
html_doc = """
<div class="index-list-r">
    <div class="h1">
        <style>.ul fan a cs{}</style>
        <ul class="am-tabs-nav am-cf" style="font-size:60%;"></ul>
    </div>
    <ul id="dm ul 2">
        <li style="margin-bottom:15px">
            <a href="/acg/74758/" title="我独自升级第一季"><span class="qt">9集</span> "我独自升级第一季"</a>
        </li>
    </ul>
</div>
"""

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_doc, 'html.parser')

# 使用find_all寻找所有的<a>标签
links = soup.find_all('a')

for link in links:
    # 获取每个<a>标签的href属性
    href = link.get('href')
    # 获取<a>标签的文本内容，使用strip()去除多余的空格
    text = link.text.strip()
    print(f'链接: {href}, 文本: {text}')
