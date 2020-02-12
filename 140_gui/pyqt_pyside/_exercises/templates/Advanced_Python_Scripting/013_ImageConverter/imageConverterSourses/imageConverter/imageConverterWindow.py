from PySide.QtCore import *
from PySide.QtGui import *
from widgets import imageConverter_UIs as ui
from widgets import filesWidget
import converter
import os


class imageConverterClass(QMainWindow, ui.Ui_imageConverter):
    def __init__(self):
        super(imageConverterClass, self).__init__()
        self.setupUi(self)
        self.list = filesWidget.listWidgetClass()
        self.files_ly.addWidget(self.list)
        self.start_btn.clicked.connect(self.start)
        self.progressBar.setValue(40)


    def start(self):
        files = self.list.getAllFiles()
        if files:
            out = self.out_le.text()
            inc = 100 / len(files)
            for f in files:
                converter.convert(f, out)
                self.progressBar.setValue(self.progressBar.value()+inc)
        self.progressBar.setValue(0)

if __name__ == '__main__':
    app = QApplication([])
    w = imageConverterClass()
    w.show()
    app.exec_()