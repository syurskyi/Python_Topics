______ ?
______ ?
from ? ______ panels

from PySide.QtCore ______ *
from PySide.QtGui ______ *


c_ simplePanel(QWidget):
    ___  - (self):
        QWidget. - (self)
        self.setLayout(QVBoxLayout())
        self.locationEdit = QCalendarWidget()
        self.layout().addWidget(self.locationEdit)

panels.registerWidgetAsPanel('simplePanel', 'Simple', "")

########################################################################################################################

______ modulefinder
w = mod.simplePanel()
