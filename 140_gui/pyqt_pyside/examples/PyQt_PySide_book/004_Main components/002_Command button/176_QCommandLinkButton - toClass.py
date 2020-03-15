

def on_clicked():
    print("Кнопка нажата")

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

window.setWindowTitle("Class QCommandLinkButton")
window.resize(300, 70)
button = QtGui.QCommandLinkButton("The text on the button")
button.setDescription("Additional text")
button.clicked.connect(on_clicked)
hbox = QtGui.QHBoxLayout()
hbox.addWidget(button)
window.setLayout(hbox)
window.show()
sys.exit(app.exec_())