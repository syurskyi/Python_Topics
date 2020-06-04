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

        title = QLabel("MooseAche")
        font = title.font()
        font.sPS..(20)
        title.sF..(font)

        layout.addWidget(title)

        logo = ?L..
        logo.sP..(?P..(os.pa__.join('images', 'ma-icon-128.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 23.35.211.233232"))
        layout.addWidget(QLabel("Copyright 2015 MooseAche Inc."))

        ___ i __ ra..(0, layout.count()):
            layout.itemAt(i).setAlignment(__.AlignHCenter)

        layout.addWidget(buttonBox)

        setLayout(layout)


c_ MainWindow(?MW..):
    ___  - (self, $ $$
        s__(MainWindow, self). - ($ $$)

        browser = QWebEngineView()
        browser.setUrl(?U..("http://google.com"))

        browser.urlChanged.c__(update_urlbar)
        browser.loadFinished.c__(update_title)
        setCentralWidget(browser)

        status = QStatusBar()
        setStatusBar(status)

        navtb = QToolBar("Navigation")
        navtb.setIconSize(?S..(16, 16))
        aTB..(navtb)

        back_btn = ?A..(?I..(os.pa__.join('images', 'arrow-180.png')), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.t___.c__(browser.back)
        navtb.aA..(back_btn)

        next_btn = ?A..(?I..(os.pa__.join('images', 'arrow-000.png')), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.t___.c__(browser.forward)
        navtb.aA..(next_btn)

        reload_btn = ?A..(?I..(os.pa__.join('images', 'arrow-circle-315.png')), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.t___.c__(browser.reload)
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
        stop_btn.t___.c__(browser.stop)
        navtb.aA..(stop_btn)

        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        file_menu = menuBar().addMenu("&File")

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

        about_action = ?A..(?I..(os.pa__.join('images', 'question.png')), "About MooseAche", self)
        about_action.setStatusTip("Find out more about MooseAche")  # Hungry!
        about_action.t___.c__(about)
        help_menu.aA..(about_action)

        navigate_mozarella_action = ?A..(?I..(os.pa__.join('images', 'lifebuoy.png')), "MooseAche Homepage", self)
        navigate_mozarella_action.setStatusTip("Go to MooseAche Homepage")
        navigate_mozarella_action.t___.c__(navigate_mozarella)
        help_menu.aA..(navigate_mozarella_action)

        s..

        setWindowIcon(?I..(os.pa__.join('images', 'ma-icon-64.png')))

    ___ update_title
        title = browser.page().title()
        sWT..("%s - MooseAche" % title)

    ___ navigate_mozarella
        browser.setUrl(?U..("https://www.udemy.com/522076"))

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

            browser.setHtml(html)
            urlbar.setText(filename)

    ___ save_file
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")

        if filename:
            html = browser.page().toHtml()
            with open(filename, 'w') as f:
                f.write(html)

    ___ print_page
        dlg = QPrintPreviewDialog()
        dlg.paintRequested.c__(browser.print_)
        dlg.e..()

    ___ navigate_home
        browser.setUrl(?U..("http://www.google.com"))

    ___ navigate_to_url   # Does not receive the Url
        q = ?U..(urlbar.text())
        if q.scheme() __ "":
            q.setScheme("http")

        browser.setUrl(q)

    ___ update_urlbar(self, q):

        if q.scheme() __ 'https':
            # Secure padlock icon
            httpsicon.sP..(?P..(os.pa__.join('images', 'lock-ssl.png')))

        ____:
            # Insecure padlock icon
            httpsicon.sP..(?P..(os.pa__.join('images', 'lock-nossl.png')))

        urlbar.setText(q.toString())
        urlbar.setCursorPosition(0)


app = ?A..(___.a..
app.setApplicationName("MooseAche")
app.setOrganizationName("MooseAche")
app.setOrganizationDomain("MooseAche.org")

window = MainWindow()

app.e..()
