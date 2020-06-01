______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc
____ ? ______ QtWebEngineWidgets __ qtwe


c_ MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor."""
        super().__init__()
        # Main UI code goes here
        # navigation toolbar
        navigation _ self.addToolBar('Navigation')
        style _ self.style()
        self.back _ navigation.aA..('Back')
        self.back.setIcon(style.standardIcon(style.SP_ArrowBack))
        self.forward _ navigation.aA..('Forward')
        self.forward.setIcon(style.standardIcon(style.SP_ArrowForward))
        self.reload _ navigation.aA..('Reload')
        self.reload.setIcon(style.standardIcon(style.SP_BrowserReload))
        self.stop _ navigation.aA..('Stop')
        self.stop.setIcon(style.standardIcon(style.SP_BrowserStop))
        self.urlbar _ qtw.?LE..
        navigation.aW..(self.urlbar)
        self.go _ navigation.aA..('Go')
        self.go.setIcon(style.standardIcon(style.SP_DialogOkButton))

        # single browser view
        #webview = qtwe.QWebEngineView()
        #self.setCentralWidget(webview)
        #webview.load(qtc.QUrl('http://www.alandmoore.com'))
        #self.go.triggered.connect(lambda: webview.load(
        #    qtc.QUrl(self.urlbar.text())))
        #self.back.triggered.connect(webview.back)
        #self.forward.triggered.connect(webview.forward)
        #self.reload.triggered.connect(webview.reload)
        #self.stop.triggered.connect(webview.stop)

        # browser tabs
        self.tabs _ qtw.QTabWidget(
            tabsClosable_True, movable_True)
        self.tabs.tabCloseRequested.c..(self.tabs.removeTab)
        self.new _ qtw.?PB..('New')
        self.tabs.setCornerWidget(self.new)
        self.sCW..(self.tabs)

        self.back.t__.c..(self.on_back)
        self.forward.t__.c..(self.on_forward)
        self.reload.t__.c..(self.on_reload)
        self.stop.t__.c..(self.on_stop)
        self.go.t__.c..(self.on_go)
        self.urlbar.rP__.c..(self.on_go)
        self.new.c__.c..(self.add_tab)

        # Profile sharing
        self.profile _ qtwe.QWebEngineProfile()

        # History
        history_dock _ qtw.QDockWidget('History')
        self.addDockWidget(qtc.__.RightDockWidgetArea, history_dock)
        self.history_list _ qtw.QListWidget()
        history_dock.setWidget(self.history_list)
        self.tabs.currentChanged.c..(self.update_history)
        self.history_list.itemDoubleClicked.c..(self.navigate_history)

        # Altering Settings
        settings _ qtwe.QWebEngineSettings.defaultSettings()
        settings.setFontFamily(
            qtwe.QWebEngineSettings.SansSerifFont, 'Impact')
        settings.setAttribute(
            qtwe.QWebEngineSettings.PluginsEnabled, True)


        # Text search feature
        find_dock _ qtw.QDockWidget('Search')
        self.addDockWidget(qtc.__.BottomDockWidgetArea, find_dock)
        self.find_text _ qtw.?LE..
        find_dock.setWidget(self.find_text)
        self.find_text.textChanged.c..(self.text_search)
        # init javascript
        w__ o..('finder.js', 'r') __ fh:
            self.finder_js _ fh.read()
        # using QWebEngineScript
        self.finder_script _ qtwe.QWebEngineScript()
        self.finder_script.setSourceCode(self.finder_js)
        # Ensure that our created functions exist within the main JS environment
        self.finder_script.setWorldId(qtwe.QWebEngineScript.MainWorld)

        self.add_tab()
        # End main UI code
        self.s..

    ##########################
    # Browser Tabs Functions #
    ##########################

    ___ add_tab  *args):
        webview _ qtwe.QWebEngineView()
        tab_index _ self.tabs.addTab(webview, 'New Tab')

        webview.urlChanged.c..(
            lambda x: self.tabs.setTabText(tab_index, x.toString()))
        webview.urlChanged.c..(
            lambda x: self.urlbar.sT..(x.toString()))

        # make it so pop-up windows call this method
        webview.createWindow _ self.add_tab

        # History
        webview.urlChanged.c..(self.update_history)

        # Profile
        page _ qtwe.QWebEnginePage(self.profile)
        webview.setPage(page)

        # Add the finder script
        page.scripts().insert(self.finder_script)

        # set default content
        webview.setHtml(
            '<h1>Blank Tab</h1><p>It is a blank tab!</p>',
            qtc.QUrl('about:blank'))

        r_ webview

    ___ on_back(self):
        self.tabs.currentWidget().back()

    ___ on_forward(self):
        self.tabs.currentWidget().forward()

    ___ on_reload(self):
        self.tabs.currentWidget().reload()

    ___ on_stop(self):
        self.tabs.currentWidget().stop()

    ___ on_go(self):
        self.tabs.currentWidget().load(
            qtc.QUrl(self.urlbar.t__()))

    ##################
    # History Method #
    ##################

    ___ update_history  *args):
        # show history
        self.history_list.clear()
        webview _ self.tabs.currentWidget()
        __ webview:
            history _ webview.history()
            for history_item in reversed(history.items()):
                list_item _ qtw.QListWidgetItem()
                list_item.setData(qtc.__.DisplayRole, history_item.url())
                self.history_list.addItem(list_item)

    ___ navigate_history  item):
        qurl _ item.data(qtc.__.DisplayRole)
        __ self.tabs.currentWidget
            self.tabs.currentWidget().load(qurl)

    ###############
    # Text Search #
    ###############

    ___ text_search  term):
        """Highlight all occurrences of "term" in the page"""
        term _ term.replace('"', '')
        page _ self.tabs.currentWidget().page()
        #page.runJavaScript(self.finder_js)
        js _ f'highlight_term("{term}");'
        page.runJavaScript(js, self.match_count)

    ___ match_count  count):
        __ count:
            self.statusBar().showMessage(f'{count} matches ')
        ____
            self.statusBar().clearMessage()


__ __name__ == '__main__':
    app _ qtw.?A..(___.argv)
    mw _ MainWindow()
    ___.exit(app.exec())
