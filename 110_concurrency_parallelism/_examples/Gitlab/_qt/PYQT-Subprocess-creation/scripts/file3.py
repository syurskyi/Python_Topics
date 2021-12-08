import pandas as pd
import argparse
import time
import sys
from threading import Thread
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize   


parser = argparse.ArgumentParser()                                               

parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()

df=pd.read_csv(args.file)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Boom boom 3')
        self.close=False
        self.setMinimumSize(QSize(300, 200))    
        self.s=0 
        self.label1=QLabel(str(df['v'][0]),self)
        self.label1.move(100, 0)
        self.label2=QLabel('',self)
        self.label2.move(120,30)

    def start(self):
        self.thread=Thread(target=self.count).start()

    def count(self):
        while True:
            if self.close:
                break
            time.sleep(1)
            self.label2.setText(str(self.s))
            self.s+=10

    def closeEvent(self, event):
        self.close=True
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    mainWin.start()
    sys.exit( app.exec_() )