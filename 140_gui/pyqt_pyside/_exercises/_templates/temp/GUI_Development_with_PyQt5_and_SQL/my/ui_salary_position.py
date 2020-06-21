# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from database import Database
from ui_change_salary_dialog import SalaryDialog
from ui_change_position_dialog import PositionDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 0, 1, 2)
        self.salaryLogLabel = QtWidgets.QLabel(self.centralwidget)
        self.salaryLogLabel.setObjectName("salaryLogLabel")
        self.gridLayout.addWidget(self.salaryLogLabel, 0, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 3, 1, 2)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 0, 5, 1, 2)
        self.positionLogLabel = QtWidgets.QLabel(self.centralwidget)
        self.positionLogLabel.setObjectName("positionLogLabel")
        self.gridLayout.addWidget(self.positionLogLabel, 0, 7, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 0, 8, 1, 1)
        self.salaryTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.salaryTableWidget.setObjectName("salaryTableWidget")
        self.salaryTableWidget.setColumnCount(0)
        self.salaryTableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.salaryTableWidget, 1, 0, 1, 5)
        self.positionTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.positionTableWidget.setObjectName("positionTableWidget")
        self.positionTableWidget.setColumnCount(0)
        self.positionTableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.positionTableWidget, 1, 5, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.changeSalaryButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeSalaryButton.setObjectName("changeSalaryButton")
        self.gridLayout.addWidget(self.changeSalaryButton, 2, 1, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 5, 1, 1)
        self.changePositionButton = QtWidgets.QPushButton(self.centralwidget)
        self.changePositionButton.setObjectName("changePositionButton")
        self.gridLayout.addWidget(self.changePositionButton, 2, 6, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 8, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.centralwidget.setStyleSheet("""
            QWidget#centralwidget {
                background-color: rgb(55,64,88);
            }

            QLabel {
                color: white;
                font-size: 8pt;
                font-family: Verdana;
            }

            QPushButton {
                border-radius: 5px;
                padding-left: 10px;
                padding-right: 10px;
                padding-top:4px;
                padding-bottom:4px;
                font-size: 8pt;
                font-family: Verdana;
                border: 1px solid rgb(45,52,71);
                color:white;
                background-color: rgb(94,109,148);
            }

            QPushButton:hover {
                background-color: rgb(112, 126, 164);
            }

            QPushButton:hover:pressed {
                background-color: rgb(129, 141, 175);
            }

            QTableWidget {
                background-color: #ced3e0;
            }

            QToolButton {
                color: white;
            }

            QHeaderView::section {
                background-color: #abb3ca;
            }
            """)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Salary and Position Log"))
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
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        tableWidget.verticalHeader().hide()

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
