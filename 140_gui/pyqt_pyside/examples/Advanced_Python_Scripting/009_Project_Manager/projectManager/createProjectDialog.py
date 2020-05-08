from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from widgets import createProject_UIs as ui

class createProjectDialogClass(QDialog, ui.Ui_createDialog):
    def __init__(self, parent):
        super(createProjectDialogClass, self).__init__(parent)
        self.setupUi(self)

        # connect
        self.create_btn.clicked.connect(self.doCreate)
        self.cancel_btn.clicked.connect(self.reject)

    def doCreate(self):
        if self.name_lb.text():
            self.accept()

    def getDialogData(self):
        return dict(
            name=self.name_lb.text(),
            comment=self.comment_te.toPlainText()
        )