____ http.server ______ HTTPServer, BaseHTTPRequestHandler

PORT _ 8000


class TestHandler(BaseHTTPRequestHandler):

    ___ _print_request_data(self):
        print('POST request received')
        print("Content-length: {}".format(self.content_length))
        print(self.data.decode('utf-8'))

    ___ _send_200(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    ___ do_POST(self, *args, **kwargs):
        self.content_length _ self.headers['Content-Length']
        self.data _ self.rfile.read(int(self.content_length))
        self._print_request_data()
        self._send_200()
        self.wfile.write('POST successful; received this: \n'.encode('utf-8'))
        self.wfile.write(self.data)


___ run(server_class_HTTPServer, handler_class_TestHandler):
    print(f"Launching server at  http://localhost:{PORT}")
    server_address _ ('', PORT)
    httpd _ server_class(server_address, handler_class)
    httpd.serve_forever()

run()
