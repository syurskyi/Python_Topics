# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from database import Database
from ui_change_salary_dialog import SalaryDialog
from ui_change_position_dialog import PositionDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 465)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.salaryTopHorizontalLayout = QtWidgets.QHBoxLayout()
        self.salaryTopHorizontalLayout.setObjectName("salaryTopHorizontalLayout")
        self.salaryLogLineLeft = QtWidgets.QFrame(self.centralwidget)
        self.salaryLogLineLeft.setFrameShape(QtWidgets.QFrame.HLine)
        self.salaryLogLineLeft.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.salaryLogLineLeft.setObjectName("salaryLogLineLeft")
        self.salaryTopHorizontalLayout.addWidget(self.salaryLogLineLeft)
        self.salaryLogLabel = QtWidgets.QLabel(self.centralwidget)
        self.salaryLogLabel.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.salaryLogLabel.setFont(font)
        self.salaryLogLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.salaryLogLabel.setAutoFillBackground(False)
        self.salaryLogLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.salaryLogLabel.setObjectName("salaryLogLabel")
        self.salaryTopHorizontalLayout.addWidget(self.salaryLogLabel)
        self.salaryLogLineRight = QtWidgets.QFrame(self.centralwidget)
        self.salaryLogLineRight.setFrameShape(QtWidgets.QFrame.HLine)
        self.salaryLogLineRight.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.salaryLogLineRight.setObjectName("salaryLogLineRight")
        self.salaryTopHorizontalLayout.addWidget(self.salaryLogLineRight)
        self.gridLayout.addLayout(self.salaryTopHorizontalLayout, 0, 0, 1, 1)
        self.positionTopHorizontalLayout = QtWidgets.QHBoxLayout()
        self.positionTopHorizontalLayout.setObjectName("positionTopHorizontalLayout")
        self.positionLogLineLeft = QtWidgets.QFrame(self.centralwidget)
        self.positionLogLineLeft.setFrameShape(QtWidgets.QFrame.HLine)
        self.positionLogLineLeft.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.positionLogLineLeft.setObjectName("positionLogLineLeft")
        self.positionTopHorizontalLayout.addWidget(self.positionLogLineLeft)
        self.positionLogLabel = QtWidgets.QLabel(self.centralwidget)
        self.positionLogLabel.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.positionLogLabel.setFont(font)
        self.positionLogLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.positionLogLabel.setAutoFillBackground(False)
        self.positionLogLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.positionLogLabel.setObjectName("positionLogLabel")
        self.positionTopHorizontalLayout.addWidget(self.positionLogLabel)
        self.positionLogLineRight = QtWidgets.QFrame(self.centralwidget)
        self.positionLogLineRight.setFrameShape(QtWidgets.QFrame.HLine)
        self.positionLogLineRight.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.positionLogLineRight.setObjectName("positionLogLineRight")
        self.positionTopHorizontalLayout.addWidget(self.positionLogLineRight)
        self.gridLayout.addLayout(self.positionTopHorizontalLayout, 0, 1, 1, 1)
        self.salaryTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.salaryTableWidget.setObjectName("salaryTableWidget")
        self.salaryTableWidget.setColumnCount(0)
        self.salaryTableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.salaryTableWidget, 1, 0, 1, 1)
        self.positionTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.positionTableWidget.setObjectName("positionTableWidget")
        self.positionTableWidget.setColumnCount(0)
        self.positionTableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.positionTableWidget, 1, 1, 1, 1)
        self.salaryBottomHorizontalLayout = QtWidgets.QHBoxLayout()
        self.salaryBottomHorizontalLayout.setObjectName("salaryBottomHorizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.salaryBottomHorizontalLayout.addItem(spacerItem)
        self.changeSalaryButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeSalaryButton.setObjectName("changeSalaryButton")
        self.salaryBottomHorizontalLayout.addWidget(self.changeSalaryButton)
        spacerItem1 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.salaryBottomHorizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.salaryBottomHorizontalLayout, 2, 0, 1, 1)
        self.positionBottomHorizontalLayout = QtWidgets.QHBoxLayout()
        self.positionBottomHorizontalLayout.setObjectName("positionBottomHorizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.positionBottomHorizontalLayout.addItem(spacerItem2)
        self.changePositionButton = QtWidgets.QPushButton(self.centralwidget)
        self.changePositionButton.setObjectName("changePositionButton")
        self.positionBottomHorizontalLayout.addWidget(self.changePositionButton)
        spacerItem3 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.positionBottomHorizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.positionBottomHorizontalLayout, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.salaryLogLabel.setText(_translate("MainWindow", "Salary Log"))
        self.positionLogLabel.setText(_translate("MainWindow", "Position Log"))
        self.changeSalaryButton.setText(_translate("MainWindow", "Change Salary"))
        self.changePositionButton.setText(_translate("MainWindow", "Change Position"))


class EmployeeInfoWindow(QtWidgets.QMainWindow):

    def __init__(self, id):
        super(EmployeeInfoWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.id = id

        self.init_tables()

        self.ui.changeSalaryButton.clicked.connect(self.change_salary_button_clicked)
        self.ui.changePositionButton.clicked.connect(self.change_position_button_clicked)


        print(self.id)

    def init_tables(self):
        self.database = Database()

        result_salary = self.database.get_salary_log_for_employee(self.id)
        result_position = self.database.get_position_log_for_employee(self.id)

        self.init_table(self.ui.salaryTableWidget, result_salary[0], result_salary[1])
        self.init_table(self.ui.positionTableWidget, result_position[0], result_position[1])


    def init_table(self, tableWidget, header_list, values_list):

        no_rows = len(values_list)
        no_columns = len(header_list)

        tableWidget.clear()
        tableWidget.setRowCount(no_rows)
        tableWidget.setColumnCount(no_columns)

        tableWidget.setHorizontalHeaderLabels(tuple(header_list))
        tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for row in range(no_rows):
            for col in range(no_columns):
                # print(s)
                tableWidget.setItem(row, col, QTableWidgetItem(str(values_list[row][col])))

    def change_salary_button_clicked(self):
        last_row = self.ui.salaryTableWidget.rowCount() - 1
        self.salaryDialog = SalaryDialog(self.ui.salaryTableWidget.item(last_row, 0).text(),
                                         self.ui.salaryTableWidget.item(last_row, 1).text(),
                                         self.ui.salaryTableWidget.item(last_row, 3).text())

        result = self.salaryDialog.exec()

        if result == QtWidgets.QDialog.Accepted:
            self.database.insert_new_salary(self.id, self.salaryDialog.new_salary, self.salaryDialog.reason)
            
            self.init_tables()

    def change_position_button_clicked(self):

        last_row = self.ui.positionTableWidget.rowCount() - 1
        self.positionDialog = PositionDialog(self.ui.positionTableWidget.item(last_row, 0).text(),
                                         self.ui.positionTableWidget.item(last_row, 1).text(),
                                         self.ui.positionTableWidget.item(last_row, 3).text())

        result = self.positionDialog.exec()

        if result == QtWidgets.QDialog.Accepted:
            self.database.insert_new_position(self.id, self.positionDialog.new_position)

            self.init_tables()

