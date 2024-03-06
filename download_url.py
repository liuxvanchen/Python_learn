import requests

url = 'https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Flxy.bjfu.edu.cn%2Fdocs%2F%2F2024-03%2F02992378c0034cdda8a4147cc0d30d50.xlsx&wdOrigin=BROWSELINK'  # 替换为你要下载的文件URL
response = requests.get(url, stream=True)

# 检查请求是否成功
if response.status_code == 200:
    with open('somefile.html', 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print('文件下载成功！')
else:
    print('文件下载失败，状态码：', response.status_code)