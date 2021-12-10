import sys
import time

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_main_window import Ui_Countdown

class MainWindow(QMainWindow, Ui_Countdown):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    @pyqtSignature("")
    def on_countdownButton_clicked(self):
        self.progressBox = QProgressDialog(
            "Counting to 100...", "Cancel", 0, 100, parent=self)
        self.progressBox.forceShow()
        self.progressBox.setModal(True)
        self.progressBox.setAutoClose(True)

        self.Thread = QThread()
        self.WorkerProcess = Worker()
        self.WorkerProcess.status.connect(self.on_progress_status)
        self.WorkerProcess.finished.connect(self.Thread.quit)
        self.progressBox.canceled.connect(self.WorkerProcess.abort)
        self.WorkerProcess.moveToThread(self.Thread)

        self.Thread.start()
        QMetaObject.invokeMethod(self.WorkerProcess, "calculate",
                                 Qt.QueuedConnection,
                                 Q_ARG(int, 0),
                                 Q_ARG(int, 110))


    def on_progress_status(self, status):
        self.progressBox.setLabelText(status["string"])
        self.progressBox.setValue(status["progress"])


class Worker(QObject):
    finished = pyqtSignal()
    status = pyqtSignal(dict)
    
    @pyqtSlot(int, int)
    def calculate(self, start, stop):
        statusGen = counter(start, stop)
        self.cancel = False
        for stat in statusGen:
            if self.cancel:
                self.finished.emit()
                break
            else:
                self.status.emit(stat)
        else:
            self.finished.emit()

    def abort(self):
        self.cancel = True


def counter(start, stop):
    "Simulates long process that periodically yields status"
    for number in range(start, stop):
        yield {"progress" : number, "string" : str(number)}
        if number == 100:
            break
        else:
            time.sleep(0.1)
                
def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
