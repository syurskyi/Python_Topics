______ sys
____ ? ______ QtCore as qtc
____ ? ______ QtNetwork as qtn

class Server(qtn.QTcpServer):

    ___ __init__(self):
        super().__init__()
        self.newConnection.c..(self.on_new_connection)
        self.connections _ []
        self.listen(qtn.QHostAddress.Any, 8080)

    ___ on_new_connection(self):
        while self.hasPendingConnections
            cx _ self.nextPendingConnection()
            self.connections.append(cx)
            cx.readyRead.c..(self.process_datastream)

    ___ process_datastream(self):
        for cx in self.connections:
            self.datastream _ qtc.QDataStream(cx)
            print(self.datastream.readRawData(cx.bytesAvailable()))
            self.datastream.writeRawData(b'PyQt5 Rocks!')
            cx.disconnectFromHost()

if __name__ == '__main__':
    app _ qtc.QCoreApplication(sys.argv)
    server _ Server()
    sys.exit(app.exec())
