______ ___
____ ? ______ ?C.. __ qtc
____ ? ______ QtNetwork __ qtn

c_ Server(qtn.QTcpServer):

    ___ __init__(self):
        super().__init__()
        self.newConnection.c..(self.on_new_connection)
        self.connections _   # list
        self.listen(qtn.QHostAddress.Any, 8080)

    ___ on_new_connection(self):
        w__ self.hasPendingConnections
            cx _ self.nextPendingConnection()
            self.connections.ap..(cx)
            cx.readyRead.c..(self.process_datastream)

    ___ process_datastream(self):
        for cx in self.connections:
            self.datastream _ qtc.QDataStream(cx)
            print(self.datastream.readRawData(cx.bytesAvailable()))
            self.datastream.writeRawData(b'PyQt5 Rocks!')
            cx.disconnectFromHost()

__ __name__ == '__main__':
    app _ qtc.QCoreApplication(___.argv)
    server _ Server()
    ___.exit(app.exec())
