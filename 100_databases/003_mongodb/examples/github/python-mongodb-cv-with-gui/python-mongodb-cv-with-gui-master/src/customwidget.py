from PyQt5 import QtWidgets, QtGui, QtCore, Qt, uic
from pathlib import Path
from user_window import MiniUserWindow
# from controller_ui import Ui

import os
import sys
import time
import copy


class MyCustomWidget(QtWidgets.QWidget):
    def __init__(self,
                 Ui,
                #  fileNameLastImageUsed: str,
                 userPixmap: QtGui.QPixmap,
                 userName: str,
                 userDescription: str,
                 itemReference: QtWidgets.QListWidgetItem,
                 parentList: QtWidgets.QListWidget,
                 parent=None):
        super(MyCustomWidget, self).__init__(parent)

        self.mainUi=Ui

        self.userName=userName
        self.userDescription=userDescription

        self.itemReference = itemReference

        self.row = QtWidgets.QHBoxLayout()

        self.label_user_image = QtWidgets.QLabel()

        self.pixmap = userPixmap.scaled(100, 100, QtCore.Qt.IgnoreAspectRatio)
        self.label_user_image.setPixmap(self.pixmap)
        self.QPushButtonDeleteUser = QtWidgets.QPushButton('delete')
        self.QPushButtonDeleteUser.clicked.connect(self.DeleteUser)

        self.parentList = parentList
        self.QPushButtonViewUser = QtWidgets.QPushButton('view profile')
        self.QPushButtonViewUser.clicked.connect(
            lambda: self.ViewUser(userName, userPixmap, userDescription))
        # construct custom widget
        self.row.addWidget(self.label_user_image)
        self.row.addWidget(QtWidgets.QLabel(userName))
        self.row.addWidget(self.QPushButtonViewUser)
        self.row.addWidget(self.QPushButtonDeleteUser)

        self.setLayout(self.row)
        # create a list of windows
        self.dialogs = list()

    def ViewUser(self,
                 userName: str,
                 userPixmap: QtGui.QPixmap,
                 userDescription: str,):
        # print('user is:', userName, ' pixmap is:', userPixmap,
        #       ' descritpion is: ', userDescription)
        test = MiniUserWindow(userName,
                              userDescription,
                              userPixmap)
        self.dialogs.append(test)

    def DeleteUser(self):
        #get item reference
        itemRow = self.parentList.row(self.itemReference)
        self.parentList.takeItem(itemRow)
        # print('new CVlist count:', self.parentList.count())
        print(__name__,' passing user= <',self.userName,'> description= <',self.userDescription,'>')
        self.mainUi.DeleteUser(self.userName,self.userDescription)
