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

____ ?.?C.. ______ pyqtSlot
____ ?.?W.. ______ (?A.., QLabel, QLineEdit, QMainWindow,
        ?MB.., QProgressBar)

______ mainwindow_rc
____ ui_mainwindow ______ Ui_MainWindow


c_ MainWindow(QMainWindow, Ui_MainWindow):
    # Maintain the list of browser windows so that they do not get garbage
    # collected.
    _window_list _   # list

    ___ __init__(self):
        super(MainWindow, self).__init__()

        MainWindow._window_list.ap..(self)

        self.setupUi(self)

        # Qt Designer (at least to v4.2.1) can't handle arbitrary widgets in a
        # QToolBar - even though uic can, and they are in the original .ui
        # file.  Therefore we manually add the problematic widgets.
        self.lblAddress _ QLabel("Address", self.tbAddress)
        self.tbAddress.insertWidget(self.actionGo, self.lblAddress)
        self.addressEdit _ QLineEdit(self.tbAddress)
        self.tbAddress.insertWidget(self.actionGo, self.addressEdit)

        self.addressEdit.rP__.c..(self.actionGo.trigger)
        self.actionBack.t__.c..(self.WebBrowser.GoBack)
        self.actionForward.t__.c..(self.WebBrowser.GoForward)
        self.actionStop.t__.c..(self.WebBrowser.Stop)
        self.actionRefresh.t__.c..(self.WebBrowser.Refresh)
        self.actionHome.t__.c..(self.WebBrowser.GoHome)
        self.actionSearch.t__.c..(self.WebBrowser.GoSearch)

        self.pb _ QProgressBar(self.statusBar())
        self.pb.setTextVisible F..
        self.pb.hide()
        self.statusBar().addPermanentWidget(self.pb)

        self.WebBrowser.dynamicCall('GoHome()')

    ___ closeEvent  e):
        MainWindow._window_list.remove(self)
        e.accept()

    ___ on_WebBrowser_TitleChange  title):
        self.setWindowTitle("Qt WebBrowser - " + title)

    ___ on_WebBrowser_ProgressChange  a, b):
        __ a <_ 0 or b <_ 0:
            self.pb.hide()
            r_

        self.pb.s..
        self.pb.setRange(0, b)
        self.pb.setValue(a)

    ___ on_WebBrowser_CommandStateChange  cmd, on):
        __ cmd == 1:
            self.actionForward.setEnabled(on)
        ____ cmd == 2:
            self.actionBack.setEnabled(on)

    ___ on_WebBrowser_BeforeNavigate(self):
        self.actionStop.setEnabled(True)

    ___ on_WebBrowser_NavigateComplete  _):
        self.actionStop.setEnabled F..

    @pyqtSlot()
    ___ on_actionGo_triggered(self):
        self.WebBrowser.dynamicCall('Navigate(const QString&)',
                self.addressEdit.t__())

    @pyqtSlot()
    ___ on_actionNewWindow_triggered(self):
        window _ MainWindow()
        window.s..
        __ self.addressEdit.t__().isEmpty
            r_;

        window.addressEdit.sT..(self.addressEdit.t__())
        window.actionStop.setEnabled(True)
        window.on_actionGo_triggered()

    @pyqtSlot()
    ___ on_actionAbout_triggered(self):
        ?MB...about  "About WebBrowser",
                "This Example has been created using the ActiveQt integration into Qt Designer.\n"
                "It demonstrates the use of QAxWidget to embed the Internet Explorer ActiveX\n"
                "control into a Qt application.")

    @pyqtSlot()
    ___ on_actionAboutQt_triggered(self):
        ?MB...aboutQt  "About Qt")


__ __name__ == "__main__":
    a _ ?A..(sys.argv)
    w _ MainWindow()
    w.s..
    sys.exit(a.exec_())
