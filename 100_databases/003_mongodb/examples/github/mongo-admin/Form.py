import common
import sys
import backend
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json
from bson.json_util import dumps


class Form(QDialog):
	def __init__(self, parent=None, confirmCallback=None):
		super(QDialog, self).__init__(parent)
		self.confirmCallback = confirmCallback
		grid = QGridLayout()
		self.setLayout(grid)
		
		# self.resize(400, 400)
		# self.move(300, 300)
		self.setWindowTitle('Mongo Admin - Query')

		addRowBtn = QPushButton('Add Row')
		addRowBtn.clicked.connect(self.addRow)

		confirmBtn = QPushButton('Confirm')
		confirmBtn.clicked.connect(self.confirm)

		self.rowCount = 0
		self.resultsArea = QTextEdit()
		self.table = QTableWidget()
		self.table.setRowCount(self.rowCount)
		self.table.setColumnCount(2)
		self.table.setHorizontalHeaderLabels(QString("Key;Value;").split(";"))
		self.table.show()
		grid.addWidget(addRowBtn, 1, 1)
		grid.addWidget(confirmBtn, 1, 2)
		grid.addWidget(self.table, 2, 1)
	
	def confirm(self):
		data = {}
		for i in range(0, self.rowCount):
			key = self.table.item(i, 0)
			value = self.table.item(i, 1)
			if(key != None and value != None):
				key = str(key.text())
				value = str(value.text())
				data[key] = value
		self.confirmCallback(data)
		self.close()

	def addRow(self):
		self.rowCount += 1
		self.table.setRowCount(self.rowCount)