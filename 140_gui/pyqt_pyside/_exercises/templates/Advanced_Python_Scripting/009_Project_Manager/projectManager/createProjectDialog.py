from PySide.QtCore import *
from PySide.QtGui import *

from widgets import createProject_UIs as ui

class projectManagerClass(QDialog, ui.Ui_createDialog):
    def __init__(self, parent):
        super(projectManagerClass, self).__init__(parent)
        self.setupUi(self)

        # connect

        self.create_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)
