import common
import sys
import backend
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json
from bson.json_util import dumps
from Form import Form

class Data(QDialog):
	def __init__(self, parent=None):
		super(QDialog, self).__init__(parent)
		
		grid = QGridLayout()
		self.setLayout(grid)
		
		self.resize(400, 400)
		self.move(300, 300)
		self.setWindowTitle('Mongo Admin - Data')

		self.collectionDropdown = QComboBox()
		self.databaseDropdown = QComboBox()
		self.dbs = backend.getDbs()['message']
		self.databaseDropdown.currentIndexChanged.connect(self.loadCollections)
		for db in self.dbs:
			self.databaseDropdown.addItem(db)

		self.queryLineEdit = QLineEdit()
		self.queryLineEdit.setPlaceholderText('query')

		self.resultsArea = QTextEdit()

		deleteBtn = QPushButton("Delete")
		deleteBtn.clicked.connect(self.openDeleteDataDialog)
		findBtn = QPushButton("Find")
		findBtn.clicked.connect(self.openFindDataDialog)
		addBtn = QPushButton("Add")
		addBtn.clicked.connect(self.openAddDataDialog)

		grid.addWidget(self.databaseDropdown, 1, 1)
		grid.addWidget(self.collectionDropdown, 1, 2)
		# grid.addWidget(self.queryLineEdit, 2, 1)
		grid.addWidget(findBtn, 2, 1)
		grid.addWidget(deleteBtn, 2, 2)
		grid.addWidget(addBtn, 2, 3)
		grid.addWidget(self.resultsArea, 3, 1, 2, 3)

	def loadCollections(self):
		self.collectionDropdown.clear()
		db = self.dbs[self.databaseDropdown.currentIndex()]
		collections = backend.getCollections(db)['message']
		print(collections)
		for collection in collections:
			self.collectionDropdown.addItem(collection)

	def findData(self, query={}):
		db = str(self.dbs[self.databaseDropdown.currentIndex()])
		collection = str(self.collectionDropdown.currentText())
		result = backend.find(db, collection, query)
		formattedResult = ''
		for item in result['message']:
			formattedResult += dumps(item).replace('{', '{\n').replace('}', '}\n').replace(',', ',\n')
			formattedResult += '\n\n\n'

		self.resultsArea.setText(formattedResult)

	def addData(self, data):
		db = str(self.dbs[self.databaseDropdown.currentIndex()])
		collection = str(self.collectionDropdown.currentText())
		result = backend.insert(db, collection, data)
		self.findData()

	def openAddDataDialog(self):
		form = Form(self, self.addData)
		form.exec_()

	def openDeleteDataDialog(self):
		form = Form(self, self.deleteData)
		form.exec_()

	def openFindDataDialog(self):
		form = Form(self, self.findData)
		form.exec_()

	def deleteData(self, query):
		db = str(self.dbs[self.databaseDropdown.currentIndex()])
		collection = str(self.collectionDropdown.currentText())
		result = backend.delete(db, collection, query)
		self.findData()
