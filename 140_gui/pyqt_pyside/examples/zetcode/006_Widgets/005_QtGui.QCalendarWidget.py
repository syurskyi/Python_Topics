"""
ZetCode PyQt4 tutorial

This example shows a QtGui.QCalendarWidget widget.

author: Jan Bodnar
website: zetcode.com
last edited: September 2011
"""

import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        cal = QtGui.QCalendarWidget(self)
        cal.sGV..(True)
        cal.move(20, 20)
        cal.clicked[QtCore.QDate].connect(self.showDate)

        self.lbl = QtGui.QLabel(self)
        date = cal.sD..()
        self.lbl.setText(date.tS..())
        self.lbl.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):

        self.lbl.setText(date.tS..())

def start():
    #global form
    start.form = Example()
    start.form.show()

start()