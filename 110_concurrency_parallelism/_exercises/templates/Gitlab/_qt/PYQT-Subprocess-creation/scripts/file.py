______ pandas as pd
______ argparse
______ t__
______ sys
from _ ______ ?
from PyQt5 ______ QtCore, QtWidgets
from PyQt5.QtWidgets ______ QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets ______ QPushButton
from PyQt5.QtCore ______ QSize   


parser = argparse.ArgumentParser()                                               

parser.add_argument("--file", "-f", type=s.., required=True)
args = parser.parse_args()

df=pd.read_csv(args.file)

class MainWindow(QMainWindow):
    ___ __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Boom boom 1')
        self.close=False
        self.setMinimumSize(QSize(300, 200))    
        self.s=0 
        self.label1=QLabel(s..(df['v'][0]),self)
        self.label1.move(100, 0)
        self.label2=QLabel('',self)
        self.label2.move(120,30)

    ___ start(self):
        self.thread=? ?_self.count).s..

    ___ count(self):
        w___ True:
            if self.close:
                break
            t__.s..(1)
            self.label2.setText(s..(self.s))
            self.s+=1

    ___ closeEvent(self, event):
        self.close=True
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    mainWin.s..
    sys.exit( app.exec_() )