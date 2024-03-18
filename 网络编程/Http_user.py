import http.client


def run():
    # 创建一个连接，提供主机和端口号
    conn = http.client.HTTPConnection("localhost:8000")

    # 发送GET请求
    conn.request("GET", "/")

    # 获取响应
    response = conn.getresponse()

    print(response.status, response.reason)

    # 读取响应内容
    data = response.read()

    # 打印响应内容
    print(data.decode("utf-8"))


if __name__ == "__main__":
    run()