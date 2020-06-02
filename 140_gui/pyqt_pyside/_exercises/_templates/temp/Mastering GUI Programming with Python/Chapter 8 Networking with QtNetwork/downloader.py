______ ___
____ os ______ pa__
____ ? ______ QtNetwork __ qtn
____ ? ______ ?C.. __ qtc


c_ Downloader(qtc.?O..):

    ___  -   url):
        s_. - ()
        manager _ qtn.QNetworkAccessManager(
            finished_self.on_finished)
        request _ qtn.QNetworkRequest(qtc.QUrl(url))
        manager.g..(request)

    ___ on_finished  reply):
        filename _ reply.url().fileName() or 'download'
        __ pa__.e..(filename):
            print('File already exists, not overwriting.')
            ___.e..(1)
        w__ o..(filename, 'wb') __ fh:
            fh.w..(reply.readAll())
        print(f"{filename} written")
        ___.e..(0)

__ ______ __ ______
    __ le.(___.a.. < 2:
        print(f'Usage: {___.argv[0]} <download url>')
        ___.e..(1)
    app _ qtc.QCoreApplication(___.a..
    d _ Downloader(___.argv[1])
    ___.e..(app.exec_())
