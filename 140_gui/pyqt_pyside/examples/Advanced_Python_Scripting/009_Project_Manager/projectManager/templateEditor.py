from PySide.QtCore import *
from PySide.QtGui import *

from widgets import templateEditor_UIs as ui

class templateEditorClass(QWidget, ui.Ui_templateEditor):
    def __init__(self):
        super(templateEditorClass, self).__init__()
        self.setupUi(self)
