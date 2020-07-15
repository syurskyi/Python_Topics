import nuke
import nukescripts
from nukescripts import panels

from PySide.QtCore import *
from PySide.QtGui import *


class simplePanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setLayout(QVBoxLayout())
        self.locationEdit = QCalendarWidget()
        self.layout().addWidget(self.locationEdit)

panels.registerWidgetAsPanel('simplePanel', 'Simple', "")

########################################################################################################################

import modulefinder
w = mod.simplePanel()
