import os, argparse, socket, socketserver, binascii

class tcpServer(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(512).strip()
        if data.startswith(b"send:"):
            fle = data.split(b":")[1]
            print("Receiving File: " + fle.decode())
            with open(str(fle.decode("utf-8")), 'wb') as f:
                while data:
                    data = bytearray(self.request.recv(512).strip())
                    if len(data) % 2 == 0:
                        f.write(binascii.unhexlify(data))
                    else:
                        f.write(binascii.unhexlify(data.append(0)))
        print ("File Received.\n-----------------------------------")

def startServer(args):
    server = socketserver.TCPServer(("", args.port), tcpServer)
    print("[Server Started]")
    server.serve_forever()

def startClient(args):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((args.ip, args.port))
    path, fle = os.path.split(args.file)
    print("Sending file: " + args.file)
    sock.sendall(b"send:" + bytes(fle, "utf-8"))
    with open(args.file, 'rb') as f:
        data = f.read(512)
        while (data):
            sock.sendall(binascii.hexlify(data))
            data = f.read(512)
    sock.close()
    print("File sent: " + args.file)


def main(args):
    if (args.client):
        startClient(args)
    elif (args.server):
        startServer(args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--client", action="store", help="start client", type=str,
    nargs='?', default=False, const=True)
    parser.add_argument("-s", "--server", action="store", help="start server", type=str,
    nargs='?', default=False, const=True)
    parser.add_argument("-i", "--ip", action="store", help="remote server ip", type=str)
    parser.add_argument("-p", "--port", action="store", help="remote server port", type=int)
    parser.add_argument("-f", "--file", action="store", help="file to send", type=str)

    args = parser.parse_args() # Declare argumnets object to args
    if (not args.client and not args.server):
        parser.print_help()
        print ("\n\nYou must specify --client or --server")
        parser.exit()
    main(args)