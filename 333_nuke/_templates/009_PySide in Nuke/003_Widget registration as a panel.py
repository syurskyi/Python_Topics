______ ?
______ nukescripts
from nukescripts ______ panels

from PySide.QtCore ______ *
from PySide.QtGui ______ *


class simplePanel(QWidget):
    ___ __init__(self):
        QWidget.__init__(self)
        self.setLayout(QVBoxLayout())
        self.locationEdit = QCalendarWidget()
        self.layout().addWidget(self.locationEdit)

panels.registerWidgetAsPanel('simplePanel', 'Simple', "")

########################################################################################################################

______ modulefinder
w = mod.simplePanel()
