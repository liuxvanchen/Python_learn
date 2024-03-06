import requests

url = 'https://yiyan.baidu.com/'  # 替换为你想要访问的网址
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    print('请求成功！')
    # 以写入模式打开文件，如果文件不存在则创建它
    with open('saved_page.html', 'w', encoding='utf-8') as file:
        # 将网页的HTML内容写入文件
        file.write(response.text)
    print('HTML内容已成功保存到文件 saved_page.html')
else:
    print('请求失败，状态码：', response.status_code)
