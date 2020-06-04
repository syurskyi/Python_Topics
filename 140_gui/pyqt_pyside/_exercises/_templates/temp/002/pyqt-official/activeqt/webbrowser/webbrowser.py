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


______ ___

____ ?.?C.. ______ pyqtSlot
____ ?.?W.. ______ (?A.., ?L.., QLineEdit, ?MW..,
        ?MB.., QProgressBar)

______ mainwindow_rc
____ ui_mainwindow ______ Ui_MainWindow


c_ MainWindow(?MW.., Ui_MainWindow):
    # Maintain the list of browser windows so that they do not get garbage
    # collected.
    _window_list _   # list

    ___  -
        s__(MainWindow, self). - ()

        MainWindow._window_list.ap..

        setupUi

        # Qt Designer (at least to v4.2.1) can't handle arbitrary widgets in a
        # QToolBar - even though uic can, and they are in the original .ui
        # file.  Therefore we manually add the problematic widgets.
        lblAddress _ ?L..("Address", tbAddress)
        tbAddress.insertWidget(actionGo, lblAddress)
        addressEdit _ QLineEdit(tbAddress)
        tbAddress.insertWidget(actionGo, addressEdit)

        addressEdit.rP__.c..(actionGo.trigger)
        actionBack.t__.c..(WebBrowser.GoBack)
        actionForward.t__.c..(WebBrowser.GoForward)
        actionStop.t__.c..(WebBrowser.Stop)
        actionRefresh.t__.c..(WebBrowser.Refresh)
        actionHome.t__.c..(WebBrowser.GoHome)
        actionSearch.t__.c..(WebBrowser.GoSearch)

        pb _ QProgressBar(statusBar())
        pb.setTextVisible F..
        pb.hide()
        sB.. .addPermanentWidget(pb)

        WebBrowser.dynamicCall('GoHome()')

    ___ closeEvent  e):
        MainWindow._window_list.remove
        e.accept()

    ___ on_WebBrowser_TitleChange  title):
        sWT..("Qt WebBrowser - " + title)

    ___ on_WebBrowser_ProgressChange  a, b):
        __ a <_ 0 or b <_ 0:
            pb.hide()
            r_

        pb.s..
        pb.setRange(0, b)
        pb.sV..(a)

    ___ on_WebBrowser_CommandStateChange  cmd, on):
        __ cmd __ 1:
            actionForward.sE..(on)
        ____ cmd __ 2:
            actionBack.sE..(on)

    ___ on_WebBrowser_BeforeNavigate
        actionStop.sE..( st.

    ___ on_WebBrowser_NavigateComplete  _):
        actionStop.sE.. F..

    @pyqtSlot()
    ___ on_actionGo_triggered
        WebBrowser.dynamicCall('Navigate(const QString&)',
                addressEdit.t__())

    @pyqtSlot()
    ___ on_actionNewWindow_triggered
        window _ MainWindow()
        window.s..
        __ addressEdit.t__().isEmpty
            r_;

        window.addressEdit.sT..(addressEdit.t__())
        window.actionStop.sE..( st.
        window.on_actionGo_triggered()

    @pyqtSlot()
    ___ on_actionAbout_triggered
        ?MB...about  "About WebBrowser",
                "This Example has been created using the ActiveQt integration into Qt Designer.\n"
                "It demonstrates the use of QAxWidget to embed the Internet Explorer ActiveX\n"
                "control into a Qt application.")

    @pyqtSlot()
    ___ on_actionAboutQt_triggered
        ?MB...aboutQt  "About Qt")


__ __name__ __ "__main__":
    a _ ?A..(___.a..
    w _ MainWindow()
    w.s..
    ___.e..(a.e..
