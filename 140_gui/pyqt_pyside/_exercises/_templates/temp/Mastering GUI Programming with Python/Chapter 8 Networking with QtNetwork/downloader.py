______ sys
____ os ______ path
____ ? ______ QtNetwork __ qtn
____ ? ______ ?C.. __ qtc


c_ Downloader(qtc.QObject):

    ___ __init__  url):
        super().__init__()
        self.manager _ qtn.QNetworkAccessManager(
            finished_self.on_finished)
        self.request _ qtn.QNetworkRequest(qtc.QUrl(url))
        self.manager.g..(self.request)

    ___ on_finished  reply):
        filename _ reply.url().fileName() or 'download'
        __ path.exists(filename):
            print('File already exists, not overwriting.')
            sys.exit(1)
        w__ o..(filename, 'wb') __ fh:
            fh.w..(reply.readAll())
        print(f"{filename} written")
        sys.exit(0)

__ __name__ == '__main__':
    __ le.(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <download url>')
        sys.exit(1)
    app _ qtc.QCoreApplication(sys.argv)
    d _ Downloader(sys.argv[1])
    sys.exit(app.exec_())
