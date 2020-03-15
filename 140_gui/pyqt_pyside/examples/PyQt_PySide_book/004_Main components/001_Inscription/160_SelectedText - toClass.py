

def on_clicked():
    print(label.hasSelectedText())
    label.setSelection(3, 10)
    print(label.hasSelectedText())
    print(label.selectedText())
    print(label.selectionStart())
    label.setFocus()

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

window.setWindowTitle("Class QLabel")
window.resize(300, 150)
button = QtGui.QPushButton("Select text")
button.clicked.connect(on_clicked)
label = QtGui.QLabel()
label.setText("This text possible to select")
label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label.setFocusPolicy(QtCore.Qt.StrongFocus)
label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())