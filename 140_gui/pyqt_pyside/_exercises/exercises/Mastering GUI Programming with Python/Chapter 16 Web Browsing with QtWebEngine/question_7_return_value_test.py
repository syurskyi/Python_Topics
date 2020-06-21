______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc
____ ? ______ ?WEW.. __ qtwe


c_ WebView(qtwe.QWebEngineView):

    ___  -
        s_. - ()
        script _ qtwe.QWebEngineScript()
        script.setSourceCode(
            'function object(){ return {a: 1, b: 2}; }\n'
            'function string(){ return "Test String";}\n'
            'function array() { return ["a", 7, {a: 2}];}\n'
        )
        script.setWorldId(qtwe.QWebEngineScript.MainWorld)
        page().scripts().insert(script)
        loadFinished.c..(on_load)

    ___ on_load  ok):
        page().runJavaScript('object()', print)
        page().runJavaScript('string()', print)
        page().runJavaScript('array()', print)


c_ MainWindow(qtw.?MW..):

    ___  -
        """MainWindow constructor."""
        s_. - ()
        # Main UI code goes here
        wv _ WebView()
        sCW..(wv)
        wv.load(qtc.?U..('about:blank'))
        # End main UI code
        s..


__ ______ __ ______
    app _ qtw.?A..(___.a..
    mw _ MainWindow()
    ___.e.. ?.e..
