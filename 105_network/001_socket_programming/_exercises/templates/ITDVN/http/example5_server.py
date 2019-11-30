import json
from http import server


class CustomHandler(server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(400)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"CSV UPLOADING")

    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.send_header('Server', 'CoolServer')
        self.end_headers()
        self.wfile.write(json.dumps({'result': True}).encode())

    def do_PUT(self):
        self.send_response(200)
        self.send_header('content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'PUT request\n')

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()


server_address = ('', 8888)
httpd = server.HTTPServer(server_address, CustomHandler)
httpd.serve_forever()
