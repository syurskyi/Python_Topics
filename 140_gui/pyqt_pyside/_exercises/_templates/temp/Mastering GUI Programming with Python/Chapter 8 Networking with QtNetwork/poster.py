______ sys
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ QtCore __ qtc
____ ? ______ QtNetwork __ qtn


c_ Poster(qtc.QObject):

    # emit body of reply
    replyReceived _ qtc.pyqtSignal(str)

    ___ __init__(self):
        super().__init__()
        self.nam _ qtn.QNetworkAccessManager()
        self.nam.finished.c..(self.on_reply)

    ___ make_request  url, data, filename):
        print(f"Making request to {url}")
        # Create the request object
        self.request _ qtn.QNetworkRequest(url)

        # create the multipart object
        self.multipart _ qtn.QHttpMultiPart(qtn.QHttpMultiPart.FormDataType)

        # Write the key-value data to the multipart
        for key, value in (data or {}).items
            http_part _ qtn.QHttpPart()
            http_part.setHeader(
                qtn.QNetworkRequest.ContentDispositionHeader,
                f'form-data; name="{key}"'
            )
            http_part.setBody(value.encode('utf-8'))
            self.multipart.append(http_part)

        # Write the file data to the multipart
        __ filename:
            file_part _ qtn.QHttpPart()
            filedata _ o..(filename, 'rb').read()
            file_part.setHeader(
                qtn.QNetworkRequest.ContentDispositionHeader,
                f'form-data; name="attachment"; filename="{filename}"'
            )
            file_part.setBody(filedata)
            self.multipart.append(file_part)

        # Post the request with the form data
        self.nam.post(self.request, self.multipart)

    ___ on_reply  reply):
        # reply.readAll() returns a QByteArray
        reply_bytes _ reply.readAll()
        reply_string _ bytes(reply_bytes).decode('utf-8')

        # emit reply
        self.replyReceived.emit(reply_string)



c_ MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here
        widget _ qtw.QWidget(minimumWidth_600)
        self.sCW..(widget)
        widget.setLayout(qtw.QVBoxLayout())
        self.url _ qtw.QLineEdit()
        self.table _ qtw.QTableWidget(columnCount_2, rowCount_5)
        self.table.horizontalHeader().setSectionResizeMode(
            qtw.QHeaderView.Stretch)
        self.table.setHorizontalHeaderLabels(['key', 'value'])
        self.fname _ qtw.?PB..(
            '(No File)', c___self.on_file_btn)
        submit _ qtw.?PB..('Submit Post', c___self.submit)
        response _ qtw.QTextEdit(readOnly_True)
        for w in (self.url, self.table, self.fname, submit, response):
            widget.layout().addWidget(w)

        # Create the poster object
        self.poster _ Poster()
        self.poster.replyReceived.c..(response.sT..)

        # End main UI code
        self.s..

    ___ on_file_btn(self):
        filename, accepted _ qtw.?FD...gOFN..()
        __ accepted:
            self.fname.sT..(filename)

    ___ submit(self):
        url _ qtc.QUrl(self.url.text())
        filename _ self.fname.text()
        __ filename == '(No File)':
            filename _ N..
        data _ {}
        for rownum in range(self.table.rowCount()):
            key_item _ self.table.item(rownum, 0)
            key _ key_item.text() __ key_item else N..
            __ key:
                data[key] _ self.table.item(rownum, 1).text()
        self.poster.make_request(url, data, filename)


__ __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
