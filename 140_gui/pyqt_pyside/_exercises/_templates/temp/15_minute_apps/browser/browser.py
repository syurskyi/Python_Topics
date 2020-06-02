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

        title = QLabel("MooseAche")
        font = title.font()
        font.setPointSize(20)
        title.sF..(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(?P..(os.pa__.join('images', 'ma-icon-128.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 23.35.211.233232"))
        layout.addWidget(QLabel("Copyright 2015 MooseAche Inc."))

        ___ i __ ra..(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(buttonBox)

        setLayout(layout)


class MainWindow(?MW..):
    def  - (self, $ $$
        super(MainWindow, self). - ($ $$)

        browser = QWebEngineView()
        browser.setUrl(?U..("http://google.com"))

        browser.urlChanged.connect(update_urlbar)
        browser.loadFinished.connect(update_title)
        setCentralWidget(browser)

        status = QStatusBar()
        setStatusBar(status)

        navtb = QToolBar("Navigation")
        navtb.setIconSize(?S..(16, 16))
        aTB..(navtb)

        back_btn = QAction(QIcon(os.pa__.join('images', 'arrow-180.png')), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction(QIcon(os.pa__.join('images', 'arrow-000.png')), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction(QIcon(os.pa__.join('images', 'arrow-circle-315.png')), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction(QIcon(os.pa__.join('images', 'home.png')), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        httpsicon = QLabel()  # Yes, really!
        httpsicon.setPixmap(?P..(os.pa__.join('images', 'lock-nossl.png')))
        navtb.addWidget(httpsicon)

        urlbar = QLineEdit()
        urlbar.returnPressed.connect(navigate_to_url)
        navtb.addWidget(urlbar)

        stop_btn = QAction(QIcon(os.pa__.join('images', 'cross-circle.png')), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(browser.stop)
        navtb.addAction(stop_btn)

        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        file_menu = menuBar().addMenu("&File")

        open_file_action = QAction(QIcon(os.pa__.join('images', 'disk--arrow.png')), "Open file...", self)
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect(open_file)
        file_menu.addAction(open_file_action)

        save_file_action = QAction(QIcon(os.pa__.join('images', 'disk--pencil.png')), "Save Page As...", self)
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect(save_file)
        file_menu.addAction(save_file_action)

        print_action = QAction(QIcon(os.pa__.join('images', 'printer.png')), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(print_page)
        file_menu.addAction(print_action)

        help_menu = menuBar().addMenu("&Help")

        about_action = QAction(QIcon(os.pa__.join('images', 'question.png')), "About MooseAche", self)
        about_action.setStatusTip("Find out more about MooseAche")  # Hungry!
        about_action.triggered.connect(about)
        help_menu.addAction(about_action)

        navigate_mozarella_action = QAction(QIcon(os.pa__.join('images', 'lifebuoy.png')), "MooseAche Homepage", self)
        navigate_mozarella_action.setStatusTip("Go to MooseAche Homepage")
        navigate_mozarella_action.triggered.connect(navigate_mozarella)
        help_menu.addAction(navigate_mozarella_action)

        show()

        setWindowIcon(QIcon(os.pa__.join('images', 'ma-icon-64.png')))

    def update_title
        title = browser.page().title()
        sWT..("%s - MooseAche" % title)

    def navigate_mozarella
        browser.setUrl(?U..("https://www.udemy.com/522076"))

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

            browser.setHtml(html)
            urlbar.setText(filename)

    def save_file
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")

        if filename:
            html = browser.page().toHtml()
            with open(filename, 'w') as f:
                f.write(html)

    def print_page
        dlg = QPrintPreviewDialog()
        dlg.paintRequested.connect(browser.print_)
        dlg.exec_()

    def navigate_home
        browser.setUrl(?U..("http://www.google.com"))

    def navigate_to_url   # Does not receive the Url
        q = ?U..(urlbar.text())
        if q.scheme() __ "":
            q.setScheme("http")

        browser.setUrl(q)

    def update_urlbar(self, q):

        if q.scheme() __ 'https':
            # Secure padlock icon
            httpsicon.setPixmap(?P..(os.pa__.join('images', 'lock-ssl.png')))

        ____:
            # Insecure padlock icon
            httpsicon.setPixmap(?P..(os.pa__.join('images', 'lock-nossl.png')))

        urlbar.setText(q.toString())
        urlbar.setCursorPosition(0)


app = QApplication(sys.a..
app.setApplicationName("MooseAche")
app.setOrganizationName("MooseAche")
app.setOrganizationDomain("MooseAche.org")

window = MainWindow()

app.exec_()
