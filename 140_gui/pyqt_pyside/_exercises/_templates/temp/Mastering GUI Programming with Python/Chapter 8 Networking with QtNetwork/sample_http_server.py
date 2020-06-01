____ http.server ______ HTTPServer, BaseHTTPRequestHandler

PORT _ 8000


c_ TestHandler(BaseHTTPRequestHandler):

    ___ _print_request_data 
        print('POST request received')
        print("Content-length: {}".format(content_length))
        print(data.decode('utf-8'))

    ___ _send_200 
        send_response(200)
        send_header('Content-type', 'text/html')
        end_headers()

    ___ do_POST  *args, **kwargs):
        content_length _ headers['Content-Length']
        data _ rfile.read(int(content_length))
        _print_request_data()
        _send_200()
        wfile.w..('POST successful; received this: \n'.encode('utf-8'))
        wfile.w..(data)


___ run(server_class_HTTPServer, handler_class_TestHandler):
    print(f"Launching server at  http://localhost:{PORT}")
    server_address _ ('', PORT)
    httpd _ server_class(server_address, handler_class)
    httpd.serve_forever()

run()
