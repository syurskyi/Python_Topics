from PyQt5 import QtWidgets, QtGui, QtCore, Qt, uic
import sys
import secrets
from pathlib import Path


guiFolder = Path(__file__).resolve().parent
uiFilePath = guiFolder.__str__() + \
    '/user_window.ui'
# print('uiFilePath= ', uiFilePath)


class MiniUserWindow(QtWidgets.QMainWindow):
    def __init__(self,
                 userName: str,
                 userDescription: str,
                 userPixmap: QtGui.QPixmap,
                 parent=None):
        super(MiniUserWindow, self).__init__(parent)

        uic.loadUi(uiFilePath, self)

        self.CVDescription: QtWidgets.QTextEdit
        self.CVDescription = self.findChild(
            QtWidgets.QTextEdit, 'CVUserDescription')

        self.CVUserName: QtWidgets.QTextEdit
        self.CVUserName = self.findChild(QtWidgets.QTextEdit, 'CVUserName')

        self.CVImage: QtWidgets.QLabel
        self.CVImage = self.findChild(QtWidgets.QLabel, 'CVImage')

        self.QListWidgetCVList: QtWidgets.QListWidget
        self.QListWidgetCVList = self.findChild(
            QtWidgets.QListWidget, 'QListWidgetCVList')

        #set user text
        self.CVUserName.setText(userName)
        self.CVDescription.setText(userDescription)

        #set and configure user image
        self.pixmap = userPixmap.scaled(100, 100, QtCore.Qt.IgnoreAspectRatio)
        self.CVImage.setPixmap(self.pixmap)

        self.show()

if __name__ == "__main__":
    # app =
    tmp_app = QtWidgets.QApplication(sys.argv)
    window = MiniUserWindow()
    tmp_app.exec_()
    