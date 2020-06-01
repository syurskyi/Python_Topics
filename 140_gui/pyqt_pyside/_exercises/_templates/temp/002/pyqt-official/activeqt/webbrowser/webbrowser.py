#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


______ sys

____ ?.QtCore ______ pyqtSlot
____ ?.?W.. ______ (?A.., QLabel, QLineEdit, QMainWindow,
        QMessageBox, QProgressBar)

______ mainwindow_rc
____ ui_mainwindow ______ Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    # Maintain the list of browser windows so that they do not get garbage
    # collected.
    _window_list _ []

    ___ __init__(self):
        super(MainWindow, self).__init__()

        MainWindow._window_list.append(self)

        self.setupUi(self)

        # Qt Designer (at least to v4.2.1) can't handle arbitrary widgets in a
        # QToolBar - even though uic can, and they are in the original .ui
        # file.  Therefore we manually add the problematic widgets.
        self.lblAddress _ QLabel("Address", self.tbAddress)
        self.tbAddress.insertWidget(self.actionGo, self.lblAddress)
        self.addressEdit _ QLineEdit(self.tbAddress)
        self.tbAddress.insertWidget(self.actionGo, self.addressEdit)

        self.addressEdit.returnPressed.c..(self.actionGo.trigger)
        self.actionBack.triggered.c..(self.WebBrowser.GoBack)
        self.actionForward.triggered.c..(self.WebBrowser.GoForward)
        self.actionStop.triggered.c..(self.WebBrowser.Stop)
        self.actionRefresh.triggered.c..(self.WebBrowser.Refresh)
        self.actionHome.triggered.c..(self.WebBrowser.GoHome)
        self.actionSearch.triggered.c..(self.WebBrowser.GoSearch)

        self.pb _ QProgressBar(self.statusBar())
        self.pb.setTextVisible(False)
        self.pb.hide()
        self.statusBar().addPermanentWidget(self.pb)

        self.WebBrowser.dynamicCall('GoHome()')

    ___ closeEvent(self, e):
        MainWindow._window_list.remove(self)
        e.accept()

    ___ on_WebBrowser_TitleChange(self, title):
        self.setWindowTitle("Qt WebBrowser - " + title)

    ___ on_WebBrowser_ProgressChange(self, a, b):
        if a <_ 0 or b <_ 0:
            self.pb.hide()
            return

        self.pb.s..
        self.pb.setRange(0, b)
        self.pb.setValue(a)

    ___ on_WebBrowser_CommandStateChange(self, cmd, on):
        if cmd == 1:
            self.actionForward.setEnabled(on)
        elif cmd == 2:
            self.actionBack.setEnabled(on)

    ___ on_WebBrowser_BeforeNavigate(self):
        self.actionStop.setEnabled(True)

    ___ on_WebBrowser_NavigateComplete(self, _):
        self.actionStop.setEnabled(False)

    @pyqtSlot()
    ___ on_actionGo_triggered(self):
        self.WebBrowser.dynamicCall('Navigate(const QString&)',
                self.addressEdit.text())

    @pyqtSlot()
    ___ on_actionNewWindow_triggered(self):
        window _ MainWindow()
        window.s..
        if self.addressEdit.text().isEmpty
            return;

        window.addressEdit.sT..(self.addressEdit.text())
        window.actionStop.setEnabled(True)
        window.on_actionGo_triggered()

    @pyqtSlot()
    ___ on_actionAbout_triggered(self):
        QMessageBox.about(self, "About WebBrowser",
                "This Example has been created using the ActiveQt integration into Qt Designer.\n"
                "It demonstrates the use of QAxWidget to embed the Internet Explorer ActiveX\n"
                "control into a Qt application.")

    @pyqtSlot()
    ___ on_actionAboutQt_triggered(self):
        QMessageBox.aboutQt(self, "About Qt")


if __name__ == "__main__":
    a _ ?A..(sys.argv)
    w _ MainWindow()
    w.s..
    sys.exit(a.exec_())
