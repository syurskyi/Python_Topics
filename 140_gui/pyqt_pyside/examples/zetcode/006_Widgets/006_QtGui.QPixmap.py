"""
ZetCode PyQt4 tutorial

In this example, we dispay an image
on the window.

author: Jan Bodnar
website: zetcode.com
last edited: September 2011
"""

import sys
from PySide import QtGui, QtCore
icon_path = 'C:/Users/serge/Dropbox/nuke/.nuke/example/Nuke_PyQt_PySide/examples/006_Widgets/NukeApp128.png'

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap(icon_path)

        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()

def start():
    #global form
    start.form = Example()
    start.form.show()

start()