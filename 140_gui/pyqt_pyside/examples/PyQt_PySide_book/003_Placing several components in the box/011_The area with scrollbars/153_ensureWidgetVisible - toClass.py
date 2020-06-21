from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

scrollArea = QtGui.QScrollArea()
scrollArea.setWindowTitle("Класс QScrollArea")
scrollArea.resize(300, 200)
widget = QtGui.QWidget()
label1 = QtGui.QLabel("Содержимое компонента 1")
label2 = QtGui.QLabel("Содержимое компонента 2")
label1.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label2.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label1.setMinimumSize(350, 150)
label2.setMinimumHeight(80)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label1)
vbox.addWidget(label2)
widget.setLayout(vbox)
scrollArea.setWidget(widget)
scrollArea.show()
scrollArea.ensureWidgetVisible(label2, yMargin=50)
sys.exit(app.exec_())