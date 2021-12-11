______ pandas __ pd
______ argparse
______ t__
______ sys
____ _ ______ ?
____ PyQt5 ______ QtCore, QtWidgets
____ PyQt5.QtWidgets ______ QMainWindow, QLabel, QGridLayout, QWidget
____ PyQt5.QtWidgets ______ QPushButton
____ PyQt5.QtCore ______ QSize


parser = argparse.ArgumentParser()                                               

parser.add_argument("--file", "-f", type=s.., required=T..)
args = parser.parse_args()

df=pd.read_csv(args.file)

c_ MainWindow(QMainWindow):
    ___ - 
        QMainWindow.-
        setWindowTitle('Boom boom 2')
        close=F..
        setMinimumSize(QSize(300, 200))    
        s=0 
        label1=QLabel(s..(df['v'][0]),
        label1.move(100, 0)
        label2=QLabel('',
        label2.move(120,30)

    ___ start
        thread=? ?_self.count).s..

    ___ count
        w___ T..:
            __ close:
                ____
            t__.s..(1)
            label2.setText(s..(s))
            s+=5

    ___ closeEvent event):
        close=T..
        event.accept()

__ ____ __ ______:
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    mainWin.s..
    sys.exit( app.exec_() )