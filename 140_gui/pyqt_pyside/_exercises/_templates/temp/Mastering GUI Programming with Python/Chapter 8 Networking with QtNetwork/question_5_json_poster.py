______ ___
______ json
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc
____ ? ______ QtNetwork __ qtn


c_ Poster(qtc.?O..):

    # emit body of reply
    replyReceived _ qtc.pS.. st.

    ___  -
        s_. - ()
        nam _ qtn.QNetworkAccessManager()
        nam.finished.c..(on_reply)

    ___ make_request  url, data, filename):
        print(f"Making request to {url}")
        # Create the request object
        request _ qtn.QNetworkRequest(url)

        # create the multipart object
        multipart _ qtn.QHttpMultiPart(qtn.QHttpMultiPart.FormDataType)

        # Write the key-value data to the multipart
        json_string _ json.dumps(data)
        http_part _ qtn.QHttpPart()
        http_part.setHeader(
            qtn.QNetworkRequest.ContentTypeHeader,
            'text/json'
        )
        http_part.setBody(json_string.encode('utf-8'))
        multipart.ap..(http_part)

        # Write the file data to the multipart
        __ filename:
            file_part _ qtn.QHttpPart()
            filedata _ o..(filename, 'rb').read()
            file_part.setHeader(
                qtn.QNetworkRequest.ContentDispositionHeader,
                f'form-data; name="attachment"; filename="{filename}"'
            )
            file_part.setBody(filedata)
            multipart.ap..(file_part)

        # Post the request with the form data
        nam.post(request, multipart)

    ___ on_reply  reply):
        # reply.readAll() returns a QByteArray
        reply_bytes _ reply.readAll()
        reply_string _ bytes(reply_bytes).decode('utf-8')

        # emit reply
        replyReceived.e..(reply_string)



c_ MainWindow(qtw.?MW..):

    ___  -
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        s_. - ()
        # Main UI code goes here
        widget _ qtw.?W..(minimumWidth_600)
        sCW..(widget)
        widget.sL.. ?.?VBL..
        url _ qtw.?LE..
        table _ qtw.QTableWidget(columnCount_2, rowCount_5)
        table.horizontalHeader().setSectionResizeMode(
            qtw.QHeaderView.Stretch)
        table.setHorizontalHeaderLabels(['key', 'value'])
        fname _ qtw.?PB..(
            '(No File)', c___self.on_file_btn)
        submit _ qtw.?PB..('Submit Post', c___self.submit)
        response _ ?.?TE..readOnly_ st.
        ___ w __ (url, table, fname, submit, response):
            widget.la__ .aW..(w)

        # Create the poster object
        poster _ Poster()
        poster.replyReceived.c..(response.sT..)

        # End main UI code
        s..

    ___ on_file_btn 
        filename, accepted _ qtw.?FD...gOFN..()
        __ accepted:
            fname.sT..(filename)

    ___ submit 
        url _ qtc.?U..(url.t__())
        filename _ fname.t__()
        __ filename __ '(No File)':
            filename _ N..
        data _   # dict
        ___ rownum __ ra..(table.rowCount()):
            key_item _ table.item(rownum, 0)
            key _ key_item.t__() __ key_item ____ N..
            __ key:
                data[key] _ table.item(rownum, 1).t__()
        poster.make_request(url, data, filename)


__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.e..(app.e..
