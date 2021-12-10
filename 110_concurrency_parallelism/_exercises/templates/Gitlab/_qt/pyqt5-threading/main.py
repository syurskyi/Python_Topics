______ sys
______ t__
from PyQt5.QtWidgets ______ QApplication, QWidget, QCheckBox
from PyQt5.QtGui ______ QIcon
from PyQt5.QtCore ______ QThread, pyqtSignal, QThreadPool, pyqtSlot, QRunnable, QObject


c_ Signals(QObject):
    return_signal = pyqtSignal(s..)


c_ ?(QRunnable):
    signal = pyqtSignal(s..)

    ___ - 
        super(?, self).- ()     
        signal = Signals()    

    @pyqtSlot()
    ___ run
        t__.s..(5)
        result = "Some String"
        signal.return_signal.emit(result)


c_ App(QWidget):
    ___ - 
            super().- ()
            title='Hello, world!'
            left=2100
            top=500
            width=640
            height=480
            threadpool = QThreadPool()
            initUI()

    ___ initUI
            setWindowTitle(title)
            setGeometry(left,top,width,height)
            checkbox = QCheckBox('Check Box', self)
            checkbox.stateChanged.connect(clickCheckbox)
            show()

    ___ clickCheckbox
        thread = ?()
        thread.signal.return_signal.connect(function_thread)
        threadpool.start(thread)

    ___ function_thread(self, signal):
        print(signal)


__ __name__=='__main__':
        app=QApplication(sys.argv)
        ex=App()
        sys.exit(app.exec_())