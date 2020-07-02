#coding:utf8
from PySide2.QtWidgets import *
import os
import nuke

class NkLibrary(QWidget):
	def __init__(self):
		super(NkLibrary, self).__init__()
		#variable
		self.libpath = os.getenv("NUKE_PATH")+"/nk/"
		self.appname = "Nuke Library"
		self.version = "v0.1"

		#widget
		self.nklist = QListWidget()
		self.addNkList()
		self.ok = QPushButton('Ok')
		self.cancel = QPushButton('Cancel')

		#layout
		layout = QVBoxLayout()
		layout.addWidget(self.nklist)
		layout.addWidget(self.ok)
		layout.addWidget(self.cancel)
		self.setWindowTitle(self.appname + " " + self.version)
		self.setLayout(layout)

		#event
		self.ok.clicked.connect(self.pushOk)
		self.cancel.clicked.connect(self.close)
		self.nklist.itemChanged.connect(self.itemClick)

	def pushOK(self):
		nuke.nodePaste(self.libpath + self.currentItem)
		self.close()

	def itemClick(self, item):
		self.currentItem = item.text()

	def addNkList(self):
		if not os.path.exists(self.libpath):
			nuke.message(self.libpath + "The path does not exist.")
		for i in os.listdir(self.libpath):
			base, ext = os.path.splitext(i)
			if ext != ".nk":
				continue
			self.nklist.addItem(QListWidgetItem(i))

def main():
	global customApp
	try:
		customApp.close()
    except:
		pass

	customApp = NkLibrary()
	try:
		customApp.show()
    except:
		pass
