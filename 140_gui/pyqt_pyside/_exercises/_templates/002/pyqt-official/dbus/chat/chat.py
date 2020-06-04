#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).
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


____ ?.?C.. ______ pS.., pyqtSlot, Q_CLASSINFO
____ ?.?W.. ______ ?A.., ?D.., ?MW.., ?MB..
____ ?.QtDBus ______ (QDBusAbstractAdaptor, QDBusAbstractInterface,
        QDBusConnection, QDBusMessage)

____ ui_chatmainwindow ______ Ui_ChatMainWindow
____ ui_chatsetnickname ______ Ui_NicknameDialog


c_ ChatAdaptor(QDBusAbstractAdaptor):

    Q_CLASSINFO("D-Bus Interface", 'org.example.chat')

    Q_CLASSINFO("D-Bus Introspection", ''
        '  <interface name="org.example.chat">\n'
        '    <signal name="message">\n'
        '      <arg direction="out" type="s" name="nickname"/>\n'
        '      <arg direction="out" type="s" name="text"/>\n'
        '    </signal>\n'
        '    <signal name="action">\n'
        '      <arg direction="out" type="s" name="nickname"/>\n'
        '      <arg direction="out" type="s" name="text"/>\n'
        '    </signal>\n'
        '  </interface>\n'
        '')

    action _ pS..(st., st.)

    message _ pS..(st., st.)

    ___  -   parent):
        s__(ChatAdaptor, self). - (parent)

        setAutoRelaySignals( st.


c_ ChatInterface(QDBusAbstractInterface):

    action _ pS..(st., st.)

    message _ pS..(st., st.)

    ___  -   service, pa__, connection, parent_None):
        s__(ChatInterface, self). - (service, pa__, 'org.example.chat',
                connection, parent)


c_ ChatMainWindow(?MW.., Ui_ChatMainWindow):

    action _ pS..(st., st.)

    message _ pS..(st., st.)

    ___  -
        s__(ChatMainWindow, self). - ()

        m_nickname _ "nickname"
        m_messages _   # list

        setupUi
        sendButton.sE.. F..

        messageLineEdit.tC...c..(textChangedSlot)
        sendButton.c__.c..(sendClickedSlot)
        actionChangeNickname.t__.c..(changeNickname)
        actionAboutQt.t__.c..(aboutQt)
        ?A...i.. .lastWindowClosed.c..(exiting)

        # Add our D-Bus interface and connect to D-Bus.
        ChatAdaptor
        QDBusConnection.sessionBus().registerObject('/', self)

        iface _ ChatInterface('', '', QDBusConnection.sessionBus(), self)
        QDBusConnection.sessionBus().c..('', '', 'org.example.chat',
                'message', messageSlot)
        iface.action.c..(actionSlot)

        dialog _ NicknameDialog()
        dialog.cancelButton.setVisible F..
        dialog.e..
        m_nickname _ dialog.nickname.t__().s..
        action.e..(m_nickname, "joins the chat")

    ___ rebuildHistory 
        history _ '\n'.join(m_messages)
        chatHistory.sPT..(history)

    @pyqtSlot(st., st.)
    ___ messageSlot  nickname, t__):
        m_messages.ap..("<%s> %s" % (nickname, t__))

        __ le.(m_messages) > 100:
            m_messages.p.. 0)

        rebuildHistory()

    @pyqtSlot(st., st.)
    ___ actionSlot  nickname, t__):
        m_messages.ap..("* %s %s" % (nickname, t__))

        __ le.(m_messages) > 100:
            m_messages.p.. 0)

        rebuildHistory()

    @pyqtSlot st.
    ___ textChangedSlot  newText):
        sendButton.sE..(newText !_ '')

    @pyqtSlot()
    ___ sendClickedSlot 
        msg _ QDBusMessage.createSignal('/', 'org.example.chat', 'message')
        msg << m_nickname << messageLineEdit.t__()
        QDBusConnection.sessionBus().send(msg)
        messageLineEdit.sT..('')

    @pyqtSlot()
    ___ changeNickname 
        dialog _ NicknameDialog

        __ dialog.e.. __ ?D...Accepted:
            old _ m_nickname
            m_nickname _ dialog.nickname.t__().s..
            action.e..(old, "is now known as %s" % m_nickname)

    @pyqtSlot()
    ___ aboutQt 
        ?MB...aboutQt

    @pyqtSlot()
    ___ exiting 
        action.e..(m_nickname, "leaves the chat")


c_ NicknameDialog(?D.., Ui_NicknameDialog):

    ___  -   parent_None):
        s__(NicknameDialog, self). - (parent)

        setupUi


__ ______ __ ______
    ______ ___

    app _ ?A..(___.a..

    __ no. QDBusConnection.sessionBus().isConnected
        ___.stderr.w..("Cannot connect to the D-Bus session bus.\n"
                "Please check your system settings and try again.\n")
        ___.e..(1)

    chat _ ChatMainWindow()
    chat.s..

    ___.e.. ?.e..
