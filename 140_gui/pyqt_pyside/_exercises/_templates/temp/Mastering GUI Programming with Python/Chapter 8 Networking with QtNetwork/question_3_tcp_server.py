______ ___
____ ? ______ ?C.. __ qtc
____ ? ______ QtNetwork __ qtn

c_ Server(qtn.QTcpServer):

    ___  -
        s_. - ()
        newConnection.c..(on_new_connection)
        connections _   # list
        listen(qtn.QHostAddress.Any, 8080)

    ___ on_new_connection
        w__ hasPendingConnections
            cx _ nextPendingConnection()
            connections.ap..(cx)
            cx.readyRead.c..(process_datastream)

    ___ process_datastream
        ___ cx __ connections:
            datastream _ qtc.QDataStream(cx)
            print(datastream.readRawData(cx.bytesAvailable()))
            datastream.writeRawData(b'PyQt5 Rocks!')
            cx.disconnectFromHost()

__ ______ __ ______
    app _ qtc.QCoreApplication(___.a..
    server _ Server()
    ___.exit(app.exec())
