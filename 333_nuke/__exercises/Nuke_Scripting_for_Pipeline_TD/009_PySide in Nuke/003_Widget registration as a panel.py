import nuke
import nukescripts
from nukescripts import panels

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class simplePanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setLayout(QVBoxLayout())
        self.locationEdit = QCalendarWidget()
        self.layout().addWidget(self.locationEdit)

panels.registerWidgetAsPanel('simplePanel', 'Simple','')

########################################################################################################################

______ modulefinder
w _ m__.sP..
