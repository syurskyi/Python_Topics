from PySide.QtGui import *
from PySide.QtCore import *


# put to main namespase
class myWidget(QPushButton):
    def __init__(self, text='NewButton'):
        super(myWidget, self).__init__(text)

    def makeUI(self):
        return self

    def updateValue(self):
        pass


# ====================

n = ?.sN__
k = ?.PyCustom_Knob('btn', '', 'myWidget("Button")')
k = ?.PyCustom_Knob('btn', '', 'myWidget()')
n.addKnob(k)
k.setFlag(?.STARTLINE)