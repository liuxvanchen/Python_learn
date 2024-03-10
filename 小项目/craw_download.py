import requests


def download_page(url, filename):
    try:
        # 发送 GET 请求获取网页内容
        response = requests.get(url)

        # 检查响应状态码，200 表示成功
        if response.status_code == 200:
            # 将内容写入到本地文件中
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"网页内容已成功下载到 {filename}")
        else:
            print(f"下载失败：响应状态码为 {response.status_code}")
    except requests.RequestException as e:
        print(f"下载失败：{e}")


# 要下载的链接和保存的文件名
url = "http://yhdm94.com/acg/74758/"
filename = "page.html"

# 调用函数进行下载
download_page(url, filename)
