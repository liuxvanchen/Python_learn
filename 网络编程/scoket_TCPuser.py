import socket


def start_tcp_client():
    # 创建一个socket对象，使用socket.socket()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接到服务器
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    # 向服务器发送数据
    message = '你好，服务器！'
    client_socket.sendall(message.encode())

    # 接收服务器的响应
    data = client_socket.recv(1024)
    print(f'服务器的响应: {data.decode()}')

    # 关闭连接
    client_socket.close()


if __name__ == '__main__':
    start_tcp_client()