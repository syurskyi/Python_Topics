import sys
from pytube import YouTube
from math import *
from PySide.QtCore import *
from PySide.QtGui import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.intext = QTextEdit()
        self.outtext = QTextBrowser()
        self.bt1 = QPushButton()
        self.output = ""

        self.bt1.setText("Download")

        grid = QGridLayout()
        grid.addWidget(self.intext, 1, 0)
        grid.addWidget(self.outtext, 2, 0)
        grid.addWidget(self.bt1, 1, 1)
        self.setLayout(grid)

        self.connect(self.bt1, SIGNAL("clicked()"), self.updateUi)
        self.setWindowTitle("PyTube : Download Videos From Youtube")
        pass

    def updateUi(self):
        self.outtext.append("Download has started!!")
        yt = YouTube()
        yt.from_url(self.intext.toPlainText())
        yt.set_filename("Temp")
        video = yt.videos[0]
        video.download()
        self.outtext.append("Download Finished!!")
        pass


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()