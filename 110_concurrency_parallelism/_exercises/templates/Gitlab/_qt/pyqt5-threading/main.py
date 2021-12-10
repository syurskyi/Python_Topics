______ sys
______ t__
from PyQt5.QtWidgets ______ QApplication, QWidget, QCheckBox
from PyQt5.QtGui ______ QIcon
from PyQt5.QtCore ______ QThread, pyqtSignal, QThreadPool, pyqtSlot, QRunnable, QObject


class Signals(QObject):
    return_signal = pyqtSignal(s..)


class ?(QRunnable):
    signal = pyqtSignal(s..)

    ___ __init__(self):
        super(?, self).__init__()     
        self.signal = Signals()    

    @pyqtSlot()
    ___ run(self):
        t__.s..(5)
        result = "Some String"
        self.signal.return_signal.emit(result)


class App(QWidget):
    ___ __init__(self):
            super().__init__()
            self.title='Hello, world!'
            self.left=2100
            self.top=500
            self.width=640
            self.height=480
            self.threadpool = QThreadPool()
            self.initUI()

    ___ initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left,self.top,self.width,self.height)
            checkbox = QCheckBox('Check Box', self)
            checkbox.stateChanged.connect(self.clickCheckbox)
            self.show()

    ___ clickCheckbox(self):
        thread = ?()
        thread.signal.return_signal.connect(self.function_thread)
        self.threadpool.start(thread)

    ___ function_thread(self, signal):
        print(signal)


if __name__=='__main__':
        app=QApplication(sys.argv)
        ex=App()
        sys.exit(app.exec_())