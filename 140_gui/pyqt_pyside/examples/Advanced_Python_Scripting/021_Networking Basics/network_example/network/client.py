from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtNetwork import *
from widgets import client_UIs as ui
import util

class clientWindow(QWidget, ui.Ui_client):
    def __init__(self):
        super(clientWindow, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.ip_le.setText(util.IP)
        self.server = None
        self.connect_btn.clicked.connect(self.connectToServer)
        self.progress_sle.sliderReleased.connect(self.messageToServer)

    def connectToServer(self):
        ip = self.ip_le.text()
        self.server = QTcpSocket()
        self.server.connectToHost(ip, util.PORT)
        self.server.disconnected.connect(self.serverError)
        self.server.error.connect(self.serverError)
        self.connect_btn.setEnabled(0)
        self.ip_le.setEnabled(0)

    def messageToServer(self):
        msg = str(self.progress_sle.value())
        if not self.server:
            return
        self.request = QByteArray()
        stream = QDataStream(self.request, QIODevice.WriteOnly)
        stream.setVersion(QDataStream.Qt_4_2)
        stream.writeUInt32(0)
        stream << msg
        stream.device().seek(0)
        stream.writeUInt32(self.request.size() - util.UINT32)
        self.server.write(self.request)
        self.nextBlockSize = 0

    def serverError(self):
        self.server.close()
        self.connect_btn.setEnabled(1)
        self.ip_le.setEnabled(1)

if __name__ == '__main__':
    app = QApplication([])
    w = clientWindow()
    w.show()
    app.exec_()