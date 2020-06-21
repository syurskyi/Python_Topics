____ ?.?C.. ______ *
____ ?.?W.. ______ *
____ ?.?G.. ______ *
____ ?.?WEW.. ______ *
____ ?.?PS.. ______ *

______ __
______ ___


c_ AboutDialog(?D..):
    ___  -   $ $$
        s__(AboutDialog, self). - ($ $$)

        QBtn _ ?DBB....Ok  # No cancel
        buttonBox _ ?DBB...(QBtn)
        buttonBox.a___.c__(accept)
        buttonBox.r___.c__(reject)

        layout _ ?VBL..()

        title _ ?L..("MooseAche")
        font _ title.font()
        font.sPS..(20)
        title.sF..(font)

        layout.aW..(title)

        logo _ ?L..
        logo.sP..(?P..(__.pa__.join('images', 'ma-icon-128.png')))
        layout.aW..(logo)

        layout.aW..(?L..("Version 23.35.211.233232"))
        layout.aW..(?L..("Copyright 2015 MooseAche Inc."))

        ___ i __ ra..(0, layout.count()):
            layout.itemAt(i).setAlignment(__.AlignHCenter)

        layout.aW..(buttonBox)

        sL..(layout)


c_ MainWindow(?MW..):
    ___  -   $ $$
        s__(MainWindow, self). - ($ $$)

        browser _ QWebEngineView()
        browser.setUrl(?U..("http://google.com"))

        browser.urlChanged.c__(update_urlbar)
        browser.loadFinished.c__(update_title)
        setCentralWidget(browser)

        status _ ?SB..
        sSB..(status)

        navtb _ QToolBar("Navigation")
        navtb.setIconSize(?S..(16, 16))
        aTB..(navtb)

        back_btn _ ?A..(?I..(__.pa__.join('images', 'arrow-180.png')), "Back", self)
        back_btn.sST..("Back to previous page")
        back_btn.t___.c__(browser.back)
        navtb.aA..(back_btn)

        next_btn _ ?A..(?I..(__.pa__.join('images', 'arrow-000.png')), "Forward", self)
        next_btn.sST..("Forward to next page")
        next_btn.t___.c__(browser.forward)
        navtb.aA..(next_btn)

        reload_btn _ ?A..(?I..(__.pa__.join('images', 'arrow-circle-315.png')), "Reload", self)
        reload_btn.sST..("Reload page")
        reload_btn.t___.c__(browser.reload)
        navtb.aA..(reload_btn)

        home_btn _ ?A..(?I..(__.pa__.join('images', 'home.png')), "Home", self)
        home_btn.sST..("Go home")
        home_btn.t___.c__(navigate_home)
        navtb.aA..(home_btn)

        navtb.aS..)

        httpsicon _ ?L..  # Yes, really!
        httpsicon.sP..(?P..(__.pa__.join('images', 'lock-nossl.png')))
        navtb.aW..(httpsicon)

        urlbar _ ?LE..
        urlbar.rP__.c__(navigate_to_url)
        navtb.aW..(urlbar)

        stop_btn _ ?A..(?I..(__.pa__.join('images', 'cross-circle.png')), "Stop", self)
        stop_btn.sST..("Stop loading current page")
        stop_btn.t___.c__(browser.stop)
        navtb.aA..(stop_btn)

        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        file_menu _ mB...aM..("&File")

        open_file_action _ ?A..(?I..(__.pa__.join('images', 'disk--arrow.png')), "Open file...", self)
        open_file_action.sST..("Open from file")
        open_file_action.t___.c__(open_file)
        file_menu.aA..(open_file_action)

        save_file_action _ ?A..(?I..(__.pa__.join('images', 'disk--pencil.png')), "Save Page As...", self)
        save_file_action.sST..("Save current page to file")
        save_file_action.t___.c__(save_file)
        file_menu.aA..(save_file_action)

        print_action _ ?A..(?I..(__.pa__.join('images', 'printer.png')), "Print...", self)
        print_action.sST..("Print current page")
        print_action.t___.c__(print_page)
        file_menu.aA..(print_action)

        help_menu _ mB...aM..("&Help")

        about_action _ ?A..(?I..(__.pa__.join('images', 'question.png')), "About MooseAche", self)
        about_action.sST..("Find out more about MooseAche")  # Hungry!
        about_action.t___.c__(about)
        help_menu.aA..(about_action)

        navigate_mozarella_action _ ?A..(?I..(__.pa__.join('images', 'lifebuoy.png')), "MooseAche Homepage", self)
        navigate_mozarella_action.sST..("Go to MooseAche Homepage")
        navigate_mozarella_action.t___.c__(navigate_mozarella)
        help_menu.aA..(navigate_mozarella_action)

        s..

        sWI..(?I..(__.pa__.join('images', 'ma-icon-64.png')))

    ___ update_title
        title _ browser.page().title()
        sWT..("%s - MooseAche" % title)

    ___ navigate_mozarella
        browser.setUrl(?U..("https://www.udemy.com/522076"))

    ___ about
        dlg _ AboutDialog()
        dlg.e..()

    ___ open_file
        filename, _ _ QFileDialog.getOpenFileName  "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All files (*.*)")

        __ filename:
            w__ open(filename, 'r') __ f:
                html _ f.r..

            browser.setHtml(html)
            urlbar.sT..(filename)

    ___ save_file
        filename, _ _ QFileDialog.getSaveFileName  "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")

        __ filename:
            html _ browser.page().toHtml()
            w__ open(filename, 'w') __ f:
                f.write(html)

    ___ print_page
        dlg _ QPrintPreviewDialog()
        dlg.paintRequested.c__(browser.print_)
        dlg.e..()

    ___ navigate_home
        browser.setUrl(?U..("http://www.google.com"))

    ___ navigate_to_url   # Does not receive the Url
        q _ ?U..(urlbar.text())
        __ q.scheme() __ "":
            q.setScheme("http")

        browser.setUrl(q)

    ___ update_urlbar  q):

        __ q.scheme() __ 'https':
            # Secure padlock icon
            httpsicon.sP..(?P..(__.pa__.join('images', 'lock-ssl.png')))

        ____:
            # Insecure padlock icon
            httpsicon.sP..(?P..(__.pa__.join('images', 'lock-nossl.png')))

        urlbar.sT..(q.toString())
        urlbar.setCursorPosition(0)


app _ ?A..(___.a..
app.setApplicationName("MooseAche")
app.setOrganizationName("MooseAche")
app.setOrganizationDomain("MooseAche.org")

window _ MainWindow()

app.e..()
