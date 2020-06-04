____ ?.?C.. ______ *
____ ?.QtWidgets ______ *
____ ?.QtGui ______ *
____ ?.QtWebEngineWidgets ______ *
____ ?.QtPrintSupport ______ *

______ os
______ ___


c_ AboutDialog(QDialog):
    ___  - (self, $ $$
        s__(AboutDialog, self). - ($ $$)

        QBtn = QDialogButtonBox.Ok  # No cancel
        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.accepted.c__(accept)
        buttonBox.rejected.c__(reject)

        layout = QVBoxLayout()

        title = QLabel("Mozarella Ashbadger")
        font = title.font()
        font.sPS..(20)
        title.sF..(font)

        layout.addWidget(title)

        logo = ?L..
        logo.sP..(?P..(os.pa__.join('images', 'ma-icon-128.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 23.35.211.233232"))
        layout.addWidget(QLabel("Copyright 2015 Mozarella Inc."))

        ___ i __ ra..(0, layout.count()):
            layout.itemAt(i).setAlignment(__.AlignHCenter)

        layout.addWidget(buttonBox)

        setLayout(layout)


c_ MainWindow(?MW..):
    ___  - (self, $ $$
        s__(MainWindow, self). - ($ $$)

        tabs = ?TW..()
        tabs.setDocumentMode( st.
        tabs.tabBarDoubleClicked.c__(tab_open_doubleclick)
        tabs.currentChanged.c__(current_tab_changed)
        tabs.setTabsClosable( st.
        tabs.tabCloseRequested.c__(close_current_tab)

        setCentralWidget(tabs)

        status = QStatusBar()
        setStatusBar(status)

        navtb = QToolBar("Navigation")
        navtb.setIconSize(?S..(16, 16))
        aTB..(navtb)

        back_btn = ?A..(?I..(os.pa__.join('images', 'arrow-180.png')), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.t___.c__(l___: tabs.currentWidget().back())
        navtb.aA..(back_btn)

        next_btn = ?A..(?I..(os.pa__.join('images', 'arrow-000.png')), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.t___.c__(l___: tabs.currentWidget().forward())
        navtb.aA..(next_btn)

        reload_btn = ?A..(?I..(os.pa__.join('images', 'arrow-circle-315.png')), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.t___.c__(l___: tabs.currentWidget().reload())
        navtb.aA..(reload_btn)

        home_btn = ?A..(?I..(os.pa__.join('images', 'home.png')), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.t___.c__(navigate_home)
        navtb.aA..(home_btn)

        navtb.addSeparator()

        httpsicon = ?L..  # Yes, really!
        httpsicon.sP..(?P..(os.pa__.join('images', 'lock-nossl.png')))
        navtb.addWidget(httpsicon)

        urlbar = QLineEdit()
        urlbar.rP__.c__(navigate_to_url)
        navtb.addWidget(urlbar)

        stop_btn = ?A..(?I..(os.pa__.join('images', 'cross-circle.png')), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.t___.c__(l___: tabs.currentWidget().stop())
        navtb.aA..(stop_btn)

        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        file_menu = menuBar().addMenu("&File")

        new_tab_action = ?A..(?I..(os.pa__.join('images', 'ui-tab--plus.png')), "New Tab", self)
        new_tab_action.setStatusTip("Open a new tab")
        new_tab_action.t___.c__(l___ _: add_new_tab())
        file_menu.aA..(new_tab_action)

        open_file_action = ?A..(?I..(os.pa__.join('images', 'disk--arrow.png')), "Open file...", self)
        open_file_action.setStatusTip("Open from file")
        open_file_action.t___.c__(open_file)
        file_menu.aA..(open_file_action)

        save_file_action = ?A..(?I..(os.pa__.join('images', 'disk--pencil.png')), "Save Page As...", self)
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.t___.c__(save_file)
        file_menu.aA..(save_file_action)

        print_action = ?A..(?I..(os.pa__.join('images', 'printer.png')), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.t___.c__(print_page)
        file_menu.aA..(print_action)

        help_menu = menuBar().addMenu("&Help")

        about_action = ?A..(?I..(os.pa__.join('images', 'question.png')), "About Mozarella Ashbadger", self)
        about_action.setStatusTip("Find out more about Mozarella Ashbadger")  # Hungry!
        about_action.t___.c__(about)
        help_menu.aA..(about_action)

        navigate_mozarella_action = ?A..(?I..(os.pa__.join('images', 'lifebuoy.png')),
                                            "Mozarella Ashbadger Homepage", self)
        navigate_mozarella_action.setStatusTip("Go to Mozarella Ashbadger Homepage")
        navigate_mozarella_action.t___.c__(navigate_mozarella)
        help_menu.aA..(navigate_mozarella_action)

        add_new_tab(?U..('http://www.google.com'), 'Homepage')

        s..

        sWT..("Mozarella Ashbadger")
        setWindowIcon(?I..(os.pa__.join('images', 'ma-icon-64.png')))

    ___ add_new_tab(self, qurl=None, label="Blank"):

        if qurl is None:
            qurl = ?U..('')

        browser = QWebEngineView()
        browser.setUrl(qurl)
        i = tabs.aT..(browser, label)

        tabs.sCI..(i)

        # More difficult! We only want to update the url when it's from the
        # correct tab
        browser.urlChanged.c__(l___ qurl, browser=browser:
                                   update_urlbar(qurl, browser))

        browser.loadFinished.c__(l___ _, i=i, browser=browser:
                                     tabs.setTabText(i, browser.page().title()))

    ___ tab_open_doubleclick(self, i):
        if i __ -1:  # No tab under the click
            add_new_tab()

    ___ current_tab_changed(self, i):
        qurl = tabs.currentWidget().u..
        update_urlbar(qurl, tabs.currentWidget())
        update_title(tabs.currentWidget())

    ___ close_current_tab(self, i):
        if tabs.count() < 2:
            return

        tabs.removeTab(i)

    ___ update_title(self, browser):
        if browser != tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        title = tabs.currentWidget().page().title()
        sWT..("%s - Mozarella Ashbadger" % title)

    ___ navigate_mozarella
        tabs.currentWidget().setUrl(?U..("https://www.udemy.com/522076"))

    ___ about
        dlg = AboutDialog()
        dlg.e..()

    ___ open_file
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All files (*.*)")

        if filename:
            with open(filename, 'r') as f:
                html = f.r..

            tabs.currentWidget().setHtml(html)
            urlbar.setText(filename)

    ___ save_file
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")

        if filename:
            html = tabs.currentWidget().page().toHtml()
            with open(filename, 'w') as f:
                f.write(html.encode('utf8'))

    ___ print_page
        dlg = QPrintPreviewDialog()
        dlg.paintRequested.c__(browser.print_)
        dlg.e..()

    ___ navigate_home
        tabs.currentWidget().setUrl(?U..("http://www.google.com"))

    ___ navigate_to_url   # Does not receive the Url
        q = ?U..(urlbar.text())
        if q.scheme() __ "":
            q.setScheme("http")

        tabs.currentWidget().setUrl(q)

    ___ update_urlbar(self, q, browser=None):

        if browser != tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        if q.scheme() __ 'https':
            # Secure padlock icon
            httpsicon.sP..(?P..(os.pa__.join('images', 'lock-ssl.png')))

        ____:
            # Insecure padlock icon
            httpsicon.sP..(?P..(os.pa__.join('images', 'lock-nossl.png')))

        urlbar.setText(q.toString())
        urlbar.setCursorPosition(0)


app = ?A..(___.a..
app.setApplicationName("Mozarella Ashbadger")
app.setOrganizationName("Mozarella")
app.setOrganizationDomain("mozarella.org")

window = MainWindow()

app.e..()
