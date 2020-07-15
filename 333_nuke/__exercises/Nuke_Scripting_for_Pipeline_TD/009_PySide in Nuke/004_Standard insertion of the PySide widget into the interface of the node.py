from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


# put to main namespase
class myWidget(QPushButton):
    def __init__(self, text='NewButton'):
        super(myWidget, self).__init__(text)

    def makeUI(self):
        return

    def updateValue(self):
        pass


# ====================

n = nuke.selectNode()
k = nuke.PyCustom_Knob('btn', '', 'myWidget("Button")')
k _ nuke.PyCustom_Knob('btn', '', 'myWidget()')
n.addKnob(k)
k.setFlag(nuke.STARTLINE)