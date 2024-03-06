from http.server import BaseHTTPRequestHandler, HTTPServer


# HTTPRequestHandler class
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # 发送响应状态码
        self.send_response(200)

        # 设置响应头
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # 发送响应内容
        message = "Hello, this is a simple HTTP server!"
        # 将消息编码为UTF-8
        self.wfile.write(bytes(message, "utf8"))
        return


def run():
    print('starting server...')

    # Server settings
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()