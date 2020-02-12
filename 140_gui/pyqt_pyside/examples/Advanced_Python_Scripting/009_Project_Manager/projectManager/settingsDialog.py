from PySide.QtCore import *
from PySide.QtGui import *
from widgets import settingsDialog_UIs as ui

import settings

from widgets import settingsDialog_UIs as ui

class settingsDialogClass(QDialog, ui.Ui_settingsDialog):
    def __init__(self, parent):
        super(settingsDialogClass, self).__init__(parent)
        self.setupUi(self)

        # ui

        self.table.setColumnCount(2)

        # start

        self.fillTable()

    def fillTable(self):
        data = settings.settingsClass().load()
        for key, value in data.items():
            self.addParm(key, value)

    def addParm(self, parm, value):
        self.table.insertRow(self.table.rowCount())
        item = QTableWidgetItem()
        item.setText(parm)
        self.table.setItem(self.table.rowCount()-1, 0, item)

        item = QTableWidgetItem()
        item.setText(value)
        self.table.setItem(self.table.rowCount() - 1, 1, item)

    def getTableOrder(self):
        data = dict()
        for i in range(self.table.rowCount()):
            parm = self.table.item(i, 0).text()
            value = self.table.item(i, 1).text()
            data[parm] = value
        return data
