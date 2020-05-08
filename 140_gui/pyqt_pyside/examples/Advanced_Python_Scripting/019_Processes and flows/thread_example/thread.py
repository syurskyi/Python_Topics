from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os, time

class folderSizeCompute(QWidget):
    def __init__(self):
        super(folderSizeCompute, self).__init__()
        self.ly = QVBoxLayout(self)
        self.start_btn = QPushButton('Compute')
        self.ly.addWidget(self.start_btn)
        self.start_btn.clicked.connect(self.compute)
        self.path_le = QLineEdit()
        self.ly.addWidget(self.path_le)
        self.info_lb = QLabel()
        self.ly.addWidget(self.info_lb)
        self.path_le.setText('C:/Python27')
        self.resize(300,100)

    def compute(self):
        path = self.path_le.text()
        self.obj = worker(path)
        self.t = QThread()
        self.obj.moveToThread(self.t)
        self.t.started.connect(self.obj.start)
        self.obj.finishSignal.connect(self.t.quit)
        self.obj.updateSignal.connect(self.setInfo)

        self.t.start()


    def setInfo(self, i):
        self.info_lb.setText('%s bytes' % i)


class worker(QObject):
    finishSignal = Signal()
    updateSignal = Signal(int)
    def __init__(self, path):
        super(worker, self).__init__()
        self.path = path

    def start(self):
        size = 0
        st = time.time()
        for path, dirs, files in os.walk(self.path):
            for f in files:
                b = os.path.getsize(os.path.join(path,f))
                size += int(b/1024.0)
                if (time.time() - st) > 0.5:
                    self.updateSignal.emit(size)
                    st = time.time()

        self.finishSignal.emit()


if __name__ == '__main__':
    app = QApplication([])
    w = folderSizeCompute()
    w.show()
    app.exec_()