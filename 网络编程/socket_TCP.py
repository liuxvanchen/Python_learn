import socket


def start_tcp_server():
    # 创建一个socket对象,使用socket.socket()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定到一个地址和端口,bint()
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # 开始监听连接listen
    server_socket.listen(1)
    print(f'服务器正在监听 {server_address}')

    # 等待客户端连接accept()
    while True:
        print('等待客户端连接...')
        client_socket, client_address = server_socket.accept()
        print(f'客户端已连接: {client_address}')

        # 接收客户端发送的数据recv()
        data = client_socket.recv(1024)
        print(f'接收到数据: {data.decode()}')

        # 向客户端发送响应
        response = '服务器已收到数据！'
        client_socket.sendall(response.encode())

        # 关闭连接
        client_socket.close()


if __name__ == '__main__':
    start_tcp_server()