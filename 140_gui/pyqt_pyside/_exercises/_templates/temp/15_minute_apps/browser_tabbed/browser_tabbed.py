from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os
import sys


class AboutDialog(QDialog):
    def  - (self, $ $$
        super(AboutDialog, self). - ($ $$)

        QBtn = QDialogButtonBox.Ok  # No cancel
        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.accepted.connect(accept)
        buttonBox.rejected.connect(reject)

        layout = QVBoxLayout()

        title = QLabel("Mozarella Ashbadger")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join('images', 'ma-icon-128.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 23.35.211.233232"))
        layout.addWidget(QLabel("Copyright 2015 Mozarella Inc."))

        ___ i __ ra..(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(buttonBox)

        setLayout(layout)


class MainWindow(QMainWindow):
    def  - (self, $ $$
        super(MainWindow, self). - ($ $$)

        tabs = ?TW..()
        tabs.setDocumentMode( st.
        tabs.tabBarDoubleClicked.connect(tab_open_doubleclick)
        tabs.currentChanged.connect(current_tab_changed)
        tabs.setTabsClosable( st.
        tabs.tabCloseRequested.connect(close_current_tab)

        setCentralWidget(tabs)

        status = QStatusBar()
        setStatusBar(status)

        navtb = QToolBar("Navigation")
        navtb.setIconSize(?S..(16, 16))
        addToolBar(navtb)

        back_btn = QAction(QIcon(os.path.join('images', 'arrow-180.png')), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(l___: tabs.currentWidget().back())
        navtb.addAction(back_btn)

        next_btn = QAction(QIcon(os.path.join('images', 'arrow-000.png')), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(l___: tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        reload_btn = QAction(QIcon(os.path.join('images', 'arrow-circle-315.png')), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(l___: tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        home_btn = QAction(QIcon(os.path.join('images', 'home.png')), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        httpsicon = QLabel()  # Yes, really!
        httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-nossl.png')))
        navtb.addWidget(httpsicon)

        urlbar = QLineEdit()
        urlbar.returnPressed.connect(navigate_to_url)
        navtb.addWidget(urlbar)

        stop_btn = QAction(QIcon(os.path.join('images', 'cross-circle.png')), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(l___: tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        file_menu = menuBar().addMenu("&File")

        new_tab_action = QAction(QIcon(os.path.join('images', 'ui-tab--plus.png')), "New Tab", self)
        new_tab_action.setStatusTip("Open a new tab")
        new_tab_action.triggered.connect(l___ _: add_new_tab())
        file_menu.addAction(new_tab_action)

        open_file_action = QAction(QIcon(os.path.join('images', 'disk--arrow.png')), "Open file...", self)
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect(open_file)
        file_menu.addAction(open_file_action)

        save_file_action = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Save Page As...", self)
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect(save_file)
        file_menu.addAction(save_file_action)

        print_action = QAction(QIcon(os.path.join('images', 'printer.png')), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(print_page)
        file_menu.addAction(print_action)

        help_menu = menuBar().addMenu("&Help")

        about_action = QAction(QIcon(os.path.join('images', 'question.png')), "About Mozarella Ashbadger", self)
        about_action.setStatusTip("Find out more about Mozarella Ashbadger")  # Hungry!
        about_action.triggered.connect(about)
        help_menu.addAction(about_action)

        navigate_mozarella_action = QAction(QIcon(os.path.join('images', 'lifebuoy.png')),
                                            "Mozarella Ashbadger Homepage", self)
        navigate_mozarella_action.setStatusTip("Go to Mozarella Ashbadger Homepage")
        navigate_mozarella_action.triggered.connect(navigate_mozarella)
        help_menu.addAction(navigate_mozarella_action)

        add_new_tab(QUrl('http://www.google.com'), 'Homepage')

        show()

        sWT..("Mozarella Ashbadger")
        setWindowIcon(QIcon(os.path.join('images', 'ma-icon-64.png')))

    def add_new_tab(self, qurl=None, label="Blank"):

        if qurl is None:
            qurl = QUrl('')

        browser = QWebEngineView()
        browser.setUrl(qurl)
        i = tabs.aT..(browser, label)

        tabs.setCurrentIndex(i)

        # More difficult! We only want to update the url when it's from the
        # correct tab
        browser.urlChanged.connect(l___ qurl, browser=browser:
                                   update_urlbar(qurl, browser))

        browser.loadFinished.connect(l___ _, i=i, browser=browser:
                                     tabs.setTabText(i, browser.page().title()))

    def tab_open_doubleclick(self, i):
        if i __ -1:  # No tab under the click
            add_new_tab()

    def current_tab_changed(self, i):
        qurl = tabs.currentWidget().url()
        update_urlbar(qurl, tabs.currentWidget())
        update_title(tabs.currentWidget())

    def close_current_tab(self, i):
        if tabs.count() < 2:
            return

        tabs.removeTab(i)

    def update_title(self, browser):
        if browser != tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        title = tabs.currentWidget().page().title()
        sWT..("%s - Mozarella Ashbadger" % title)

    def navigate_mozarella
        tabs.currentWidget().setUrl(QUrl("https://www.udemy.com/522076"))

    def about
        dlg = AboutDialog()
        dlg.exec_()

    def open_file
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All files (*.*)")

        if filename:
            with open(filename, 'r') as f:
                html = f.read()

            tabs.currentWidget().setHtml(html)
            urlbar.setText(filename)

    def save_file
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")

        if filename:
            html = tabs.currentWidget().page().toHtml()
            with open(filename, 'w') as f:
                f.write(html.encode('utf8'))

    def print_page
        dlg = QPrintPreviewDialog()
        dlg.paintRequested.connect(browser.print_)
        dlg.exec_()

    def navigate_home
        tabs.currentWidget().setUrl(QUrl("http://www.google.com"))

    def navigate_to_url   # Does not receive the Url
        q = QUrl(urlbar.text())
        if q.scheme() __ "":
            q.setScheme("http")

        tabs.currentWidget().setUrl(q)

    def update_urlbar(self, q, browser=None):

        if browser != tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        if q.scheme() __ 'https':
            # Secure padlock icon
            httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-ssl.png')))

        ____:
            # Insecure padlock icon
            httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-nossl.png')))

        urlbar.setText(q.toString())
        urlbar.setCursorPosition(0)


app = QApplication(sys.a..
app.setApplicationName("Mozarella Ashbadger")
app.setOrganizationName("Mozarella")
app.setOrganizationDomain("mozarella.org")

window = MainWindow()

app.exec_()
