from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os

worker = 'python ' + os.path.join(os.path.dirname(__file__), 'worker.py')
arnold = 'C:/cg/solidangle/mtoadeploy/2014/bin/kick.exe -i J:/WORK/pw_projects/evgen_render/assData/horse_render(arnold)/shot2.258-260/masterLayer.0259.ass  -o J:/WORK/pw_projects/evgen_render/render/3d/horse_render(arnold)/shot2.258-260/masterLayer.0259.exr  -l C:/cg/solidangle/mtoadeploy/2014/shaders -nokeypress -nocrashpopup -dp -dw -v 2 -t 7 -nstdin'

class workerClass(QWidget):
    def __init__(self):
        super(workerClass, self).__init__()
        self.ly = QVBoxLayout(self)

        self.start_btn = QPushButton('Start')
        self.ly.addWidget(self.start_btn)
        self.start_btn.clicked.connect(self.start)

        self.out = QTextBrowser()
        self.ly.addWidget(self.out)

        self.progress = QProgressBar()
        self.ly.addWidget(self.progress)
        self.progress.setValue(0)
        self.p = QProcess()
        self.p.setProcessChannelMode(QProcess.MergedChannels)
        self.p.finished.connect(self.finish)
        self.p.readyRead.connect(self.readOut)

    def start(self):
        self.p.start(arnold)
        self.start_btn.setEnabled(0)

    def readOut(self):
        out = str(self.p.readAll()).strip()
        self.showMesasge(out)
        try:
            prcnt = int(out.split('|')[-1].strip().split('%')[0])
            self.progress.setValue(prcnt)
        except: pass

    def finish(self):
        self.start_btn.setEnabled(1)
        self.progress.setValue(0)
        self.showMesasge('COMPLETE')
        self.p.deleteLater()

    def showMesasge(self, msg):
        self.out.append(msg)

if __name__ == '__main__':
    app = QApplication([])
    w = workerClass()
    w.show()
    app.exec_()


