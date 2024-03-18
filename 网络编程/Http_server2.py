from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 发送响应状态码
        self.send_response(200)

        # 设置响应头部
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # 发送响应内容
        response = 'Hello, this is a simple HTTP server!'
        self.wfile.write(response.encode('utf-8'))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting server...')
    httpd.serve_forever()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()