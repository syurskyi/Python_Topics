import common
import sys
import backend
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MainMenu import MainMenu
		
app = QApplication(sys.argv)

class Login(QWidget):
	def __init__(self, parent=None):
		super(Login, self).__init__(parent)
		self.resize(250, 150)
		self.move(300, 300)
		grid = QGridLayout()
		self.setWindowTitle('Mongo Admin')
		self.setLayout(grid)


		loginBtn = QPushButton('Login')
		loginBtn.clicked.connect(self.login)

		userLabel = QLabel("User: ")
		self.userField = QLineEdit()
		passwordLabel = QLabel("Password: ")
		self.passwordField = QLineEdit()
		self.passwordField.setEchoMode(QLineEdit.Password)

		grid.addWidget(userLabel, 1, 1)
		grid.addWidget(self.userField, 1, 2)
		grid.addWidget(passwordLabel, 2, 1)
		grid.addWidget(self.passwordField, 2, 2)
		grid.addWidget(loginBtn, 3, 2)
	
	def login(self):
		result = backend.login(str(self.userField.text()), str(self.passwordField.text()))
		if result['code'] != 1 or len(result['message']) == 0:
			common.showError('Login', 'login failed')
		else:
			common.showMsg('Login', 'login Successful')
			newWindow = MainMenu(self)
			self.hide()
			newWindow.show()


main = Login()
main.show()
sys.exit(app.exec_())