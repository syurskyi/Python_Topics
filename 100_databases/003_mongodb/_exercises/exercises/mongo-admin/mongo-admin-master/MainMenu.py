import common
import sys
import backend
from users import Users
from Data import Data
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainMenu(QMainWindow):
	def __init__(self, parent=None):
		super(QMainWindow, self).__init__(parent)
		
		grid = QGridLayout()
		w = QWidget()
		w.setLayout(grid)
		
		self.resize(400, 400)
		self.move(300, 300)
		self.setWindowTitle('Mongo Admin')
		self.setCentralWidget(w)

		usersBtn = QPushButton('Users')
		usersBtn.clicked.connect(self.openUsersWindow)
		dataBtn = QPushButton('Data')
		dataBtn.clicked.connect(self.openDataWindow)

		grid.addWidget(usersBtn, 1, 1)
		grid.addWidget(dataBtn, 2, 1)

	def openUsersWindow(self):
		newWindow = Users(self)
		newWindow.exec_()

	def openDataWindow(self):
		newWindow = Data(self)
		newWindow.exec_()
