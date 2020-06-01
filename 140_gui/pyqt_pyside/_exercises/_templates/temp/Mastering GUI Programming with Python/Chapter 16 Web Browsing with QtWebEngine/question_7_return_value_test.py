______ sys
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ QtCore __ qtc
____ ? ______ QtWebEngineWidgets __ qtwe


c_ WebView(qtwe.QWebEngineView):

    ___ __init__(self):
        super().__init__()
        script _ qtwe.QWebEngineScript()
        script.setSourceCode(
            'function object(){ return {a: 1, b: 2}; }\n'
            'function string(){ return "Test String";}\n'
            'function array() { return ["a", 7, {a: 2}];}\n'
        )
        script.setWorldId(qtwe.QWebEngineScript.MainWorld)
        self.page().scripts().insert(script)
        self.loadFinished.c..(self.on_load)

    ___ on_load  ok):
        self.page().runJavaScript('object()', print)
        self.page().runJavaScript('string()', print)
        self.page().runJavaScript('array()', print)


c_ MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor."""
        super().__init__()
        # Main UI code goes here
        wv _ WebView()
        self.sCW..(wv)
        wv.load(qtc.QUrl('about:blank'))
        # End main UI code
        self.s..


__ __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    mw _ MainWindow()
    sys.exit(app.exec())
