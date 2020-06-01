______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc
____ ? ______ QtWebEngineWidgets __ qtwe


c_ MainWindow(qtw.QMainWindow):

    ___  -  
        """MainWindow constructor."""
        s_. - ()
        # Main UI code goes here
        # navigation toolbar
        navigation _ addToolBar('Navigation')
        style _ style()
        back _ navigation.aA..('Back')
        back.setIcon(style.standardIcon(style.SP_ArrowBack))
        forward _ navigation.aA..('Forward')
        forward.setIcon(style.standardIcon(style.SP_ArrowForward))
        reload _ navigation.aA..('Reload')
        reload.setIcon(style.standardIcon(style.SP_BrowserReload))
        stop _ navigation.aA..('Stop')
        stop.setIcon(style.standardIcon(style.SP_BrowserStop))
        urlbar _ qtw.?LE..
        navigation.aW..(urlbar)
        go _ navigation.aA..('Go')
        go.setIcon(style.standardIcon(style.SP_DialogOkButton))

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
        tabs _ qtw.QTabWidget(
            tabsClosable_True, movable_True)
        tabs.tabCloseRequested.c..(tabs.removeTab)
        new _ qtw.?PB..('New')
        tabs.setCornerWidget(new)
        sCW..(tabs)

        back.t__.c..(on_back)
        forward.t__.c..(on_forward)
        reload.t__.c..(on_reload)
        stop.t__.c..(on_stop)
        go.t__.c..(on_go)
        urlbar.rP__.c..(on_go)
        new.c__.c..(add_tab)

        # Profile sharing
        profile _ qtwe.QWebEngineProfile()

        # History
        history_dock _ qtw.QDockWidget('History')
        addDockWidget(qtc.__.RightDockWidgetArea, history_dock)
        history_list _ ?.?LW..
        history_dock.setWidget(history_list)
        tabs.currentChanged.c..(update_history)
        history_list.itemDoubleClicked.c..(navigate_history)

        # Altering Settings
        settings _ qtwe.QWebEngineSettings.defaultSettings()
        settings.setFontFamily(
            qtwe.QWebEngineSettings.SansSerifFont, 'Impact')
        settings.setAttribute(
            qtwe.QWebEngineSettings.PluginsEnabled, True)


        # Text search feature
        find_dock _ qtw.QDockWidget('Search')
        addDockWidget(qtc.__.BottomDockWidgetArea, find_dock)
        find_text _ qtw.?LE..
        find_dock.setWidget(find_text)
        find_text.textChanged.c..(text_search)
        # init javascript
        w__ o..('finder.js', 'r') __ fh:
            finder_js _ fh.read()
        # using QWebEngineScript
        finder_script _ qtwe.QWebEngineScript()
        finder_script.setSourceCode(finder_js)
        # Ensure that our created functions exist within the main JS environment
        finder_script.setWorldId(qtwe.QWebEngineScript.MainWorld)

        add_tab()
        # End main UI code
        s..

    ##########################
    # Browser Tabs Functions #
    ##########################

    ___ add_tab  *args):
        webview _ qtwe.QWebEngineView()
        tab_index _ tabs.addTab(webview, 'New Tab')

        webview.urlChanged.c..(
            lambda x: tabs.setTabText(tab_index, x.toString()))
        webview.urlChanged.c..(
            lambda x: urlbar.sT..(x.toString()))

        # make it so pop-up windows call this method
        webview.createWindow _ add_tab

        # History
        webview.urlChanged.c..(update_history)

        # Profile
        page _ qtwe.QWebEnginePage(profile)
        webview.setPage(page)

        # Add the finder script
        page.scripts().insert(finder_script)

        # set default content
        webview.setHtml(
            '<h1>Blank Tab</h1><p>It is a blank tab!</p>',
            qtc.QUrl('about:blank'))

        r_ webview

    ___ on_back 
        tabs.currentWidget().back()

    ___ on_forward 
        tabs.currentWidget().forward()

    ___ on_reload 
        tabs.currentWidget().reload()

    ___ on_stop 
        tabs.currentWidget().stop()

    ___ on_go 
        tabs.currentWidget().load(
            qtc.QUrl(urlbar.t__()))

    ##################
    # History Method #
    ##################

    ___ update_history  *args):
        # show history
        history_list.clear()
        webview _ tabs.currentWidget()
        __ webview:
            history _ webview.history()
            ___ history_item __ reversed(history.items()):
                list_item _ qtw.QListWidgetItem()
                list_item.setData(qtc.__.DisplayRole, history_item.url())
                history_list.addItem(list_item)

    ___ navigate_history  item):
        qurl _ item.data(qtc.__.DisplayRole)
        __ tabs.currentWidget
            tabs.currentWidget().load(qurl)

    ###############
    # Text Search #
    ###############

    ___ text_search  term):
        """Highlight all occurrences of "term" in the page"""
        term _ term.replace('"', '')
        page _ tabs.currentWidget().page()
        #page.runJavaScript(self.finder_js)
        js _ f'highlight_term("{term}");'
        page.runJavaScript(js, match_count)

    ___ match_count  count):
        __ count:
            statusBar().showMessage(f'{count} matches ')
        ____
            statusBar().clearMessage()


__ ______ __ ______
    app _ qtw.?A..(___.a..
    mw _ MainWindow()
    ___.e..(app.e..
