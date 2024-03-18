import socket


def send_http_request(host, port, path='/', protocol='HTTP/1.1'):
    # 创建一个socket对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 连接到服务器
        s.connect((host, port))

        # 构建HTTP请求
        request = f'GET {path} {protocol}\r\nHost: {host}\r\n\r\n'

        # 发送请求
        s.sendall(request.encode('utf-8'))

        # 接收响应
        response = s.recv(4096)

        # 打印响应
        print(response.decode('utf-8'))

    # 使用


host = 'localhost'
port = 8000
path = '/'
send_http_request(host, port, path)