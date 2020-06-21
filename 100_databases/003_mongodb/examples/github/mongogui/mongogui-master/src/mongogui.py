import sys
from PyQt5 import QtGui,QtCore, QtWidgets
from mainwindow import MainWindow

def main():
    app=QtWidgets.QApplication(sys.argv)
   # app.setStyleSheet("QWidget{background:darkgray} QMenu{background:darkgray} QToolButton{background:darkgray}")
    mw=MainWindow()
    mw.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
