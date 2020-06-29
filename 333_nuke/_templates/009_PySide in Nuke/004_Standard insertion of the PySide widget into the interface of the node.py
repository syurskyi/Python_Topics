from PySide.QtGui ______ *
from PySide.QtCore ______ *


# put to main namespase
class myWidget(QPushButton):
    ___ __init__(self, text='NewButton'):
        super(myWidget, self).__init__(text)

    ___ makeUI(self):
        return self

    ___ updateValue(self):
        pass


# ====================

n = ?.sN__
k = ?.PyCustom_Knob('btn', '', 'myWidget("Button")')
k = ?.PyCustom_Knob('btn', '', 'myWidget()')
n.addKnob(k)
k.setFlag(?.STARTLINE)