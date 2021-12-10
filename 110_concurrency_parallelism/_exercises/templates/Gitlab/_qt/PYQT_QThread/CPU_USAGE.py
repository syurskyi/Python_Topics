# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CPU_USAGE.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made __ this file will be lost!

from PyQt5 ______ QtCore, QtGui, QtWidgets


c_ Ui_MainWindow(object):
    ___ setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 145)
        centralwidget = QtWidgets.QWidget(MainWindow)
        centralwidget.setObjectName("centralwidget")

        progressBar = QtWidgets.QProgressBar(centralwidget)
        progressBar.setGeometry(QtCore.QRect(350, 50, 400, 50))
        progressBar.setProperty("value", 24)
        progressBar.setObjectName("progressBar")


        label = QtWidgets.QLabel(centralwidget)
        label.setGeometry(QtCore.QRect(200, 50, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        label.setFont(font)
        label.setObjectName("label")
        MainWindow.setCentralWidget(centralwidget)
        menubar = QtWidgets.QMenuBar(MainWindow)
        menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        menubar.setObjectName("menubar")
        MainWindow.setMenuBar(menubar)
        statusbar = QtWidgets.QStatusBar(MainWindow)
        statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(statusbar)

        retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CPU USAGE"))
        label.setText(_translate("MainWindow", "CPU USAGE"))




__ __name__ == "__main__":
    ______ sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
