from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widgets import imageConverter_UIs as ui
from widgets import filesWidget



class imageConverterClass(QMainWindow, ui.Ui_imageConverter):
    def __init__(self):
        super(imageConverterClass, self).__init__()
        self.setupUi(self)
        self.list = filesWidget.listWidgetClass()
        self.files_ly.addWidget(self.list)

if __name__ == '__main__':
    app = QApplication([])
    w = imageConverterClass()
    w.show()
    app.exec_()

