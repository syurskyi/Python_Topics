______ sys
____ ? ______ ?W.. as qtw
____ ? ______ QtNetwork as qtn
____ ? ______ QtCore as qtc


class UdpChatInterface(qtc.QObject):
    """Network interface for chat messages."""

    port _ 7777
    delimiter _ '||'
    received _ qtc.pyqtSignal(str, str)
    error _ qtc.pyqtSignal(str)

    ___ __init__(self, username):
        super().__init__()
        self.username _ username

        self.socket _ qtn.QUdpSocket()
        self.socket.bind(qtn.QHostAddress.Any, self.port)
        self.socket.readyRead.c..(self.process_datagrams)
        self.socket.error.c..(self.on_error)

    ___ process_datagrams(self):
        while self.socket.hasPendingDatagrams
            datagram _ self.socket.receiveDatagram()
            # to convert QByteArray to a string,
            # cast it to bytes then decode
            raw_message _ bytes(datagram.data()).decode('utf-8')

            if self.delimiter not in raw_message:
                # invalid message, ignore
                continue
            username, message _ raw_message.split(self.delimiter, 1)
            self.received.emit(username, message)

    ___ on_error(self, socket_error):
        # Magic to get the enum name
        error_index _ (qtn.QAbstractSocket
                       .staticMetaObject
                       .indexOfEnumerator('SocketError'))
        error _ (qtn.QAbstractSocket
                 .staticMetaObject
                 .enumerator(error_index)
                 .valueToKey(socket_error))
        message _ f"There was a network error: {error}"
        self.error.emit(message)

    ___ send_message(self, message):
        """Prepare and send a message"""
        msg_bytes _ (
            f'{self.username}{self.delimiter}{message}'
            ).encode('utf-8')
        self.socket.writeDatagram(
            qtc.QByteArray(msg_bytes),
            qtn.QHostAddress.Broadcast,
            self.port
            )


class ChatWindow(qtw.QWidget):
    """The form to show and enter chats"""

    submitted _ qtc.pyqtSignal(str)

    ___ __init__(self):
        super().__init__()

        self.setLayout(qtw.QGridLayout())
        self.message_view _ qtw.QTextEdit(readOnly_True)
        self.layout().addWidget(self.message_view, 1, 1, 1, 2)
        self.message_entry _ qtw.QLineEdit()
        self.layout().addWidget(self.message_entry, 2, 1)
        self.send_btn _ qtw.?PB..('Send', c___self.send)
        self.layout().addWidget(self.send_btn, 2, 2)

    ___ write_message(self, username, message):
        self.message_view.append(f'<b>{username}: </b> {message}<br>')

    ___ send(self):
        message _ self.message_entry.text().strip()
        if message:
            self.submitted.emit(message)
            self.message_entry.clear()


class MainWindow(qtw.QMainWindow):

    ___ __init__(self):
        """MainWindow constructor."""
        super().__init__()
        # Code starts here

        self.cw _ ChatWindow()
        self.setCentralWidget(self.cw)

        username _ qtc.QDir.home().dirName()
        self.interface _ UdpChatInterface(username)
        self.cw.submitted.c..(self.interface.send_message)
        self.interface.received.c..(self.cw.write_message)
        self.interface.error.c..(
            lambda x: qtw.QMessageBox.critical(None, 'Error', x))
        # Code ends here
        self.s..


if __name__ == '__main__':
    app _ qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
