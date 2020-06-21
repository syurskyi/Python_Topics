

from PyQt5 import QtCore, QtGui, QtWidgets
from manage_employees import EmployeeWindow
from charts import ChartsWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 360)
        MainWindow.setMinimumSize(QtCore.QSize(250, 300))
        MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(9, 9, -1, -1)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 78, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.manageEmployeesButton = QtWidgets.QPushButton(self.centralwidget)
        self.manageEmployeesButton.setMinimumSize(QtCore.QSize(200, 60))
        self.manageEmployeesButton.setObjectName("manageEmployeesButton")
        self.gridLayout.addWidget(self.manageEmployeesButton, 1, 0, 1, 1)
        self.viewChartsButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewChartsButton.setMinimumSize(QtCore.QSize(200, 60))
        self.viewChartsButton.setObjectName("viewChartsButton")
        self.gridLayout.addWidget(self.viewChartsButton, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 78, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.centralwidget.setStyleSheet("""
            QWidget {
                background-color: rgb(55,64,88);
            }

            QPushButton {
                border-radius: 10px;
                font-size: 9.5pt;
                font-family: Verdana;
                border: 2px solid rgb(45,52,71);
                color:white;
                background-color: rgb(94,109,148);
            }

            QPushButton:hover {
                background-color: rgb(112, 126, 164);
            }

            QPushButton:hover:pressed {
                background-color: rgb(129, 141, 175);
            }
            """)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Menu"))
        self.manageEmployeesButton.setText(_translate("MainWindow", "Manage Employees"))
        self.viewChartsButton.setText(_translate("MainWindow", "View charts"))


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.manageEmployeesButton.clicked.connect(self.manage_employees_button_clicked)
        self.ui.viewChartsButton.clicked.connect(self.view_charts_button_clicked)

    def manage_employees_button_clicked(self):
        self.hide()
        self.employeeWindow = EmployeeWindow(self)
        self.employeeWindow.show()

    def view_charts_button_clicked(self):
        self.hide()
        self.chartsWindow = ChartsWindow(self)
        self.chartsWindow.show()

