

def on_link_activated(link):
    print(link)

from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
window.setWindowTitle("Class QLabel")
window.resize(300, 150)
label = QtGui.QLabel()
label.setText("""<a href="http://google.ru/">Это гиперссылка 1</a>
<a href="http://bhv.ru/">Это гиперссылка 2</a>
""")
label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard)
label.linkActivated["const QString&"].connect(on_link_activated)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
