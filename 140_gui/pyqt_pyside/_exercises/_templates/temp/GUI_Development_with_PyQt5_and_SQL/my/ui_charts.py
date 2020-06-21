# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtChart import *
from PyQt5.QtWidgets import *
from database import Database


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(818, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.gridLayout_2.setRowStretch(0, 20)
        self.gridLayout_2.setRowStretch(1, 1)

        self.centralwidget.setStyleSheet("""
            QWidget {
                background-color: rgb(55,64,88);
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
            """)

        self.firstLayout = QGridLayout(self.widget)
        self.secondLayout = QGridLayout(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Charts"))
        self.backButton.setText(_translate("MainWindow", "← Back"))

class ChartsWindow(QtWidgets.QMainWindow):

    def __init__(self, mainMenu):
        super(ChartsWindow, self).__init__()
        self.mainMenu = mainMenu

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.database = Database()

        self.firstChart = QChart()
        self.secondChart = QChart()
        self.firstSeries = QBarSeries()
        self.secondSeries = QPieSeries()

        # self.firstChart.legend().hide()
        #self.secondChart.legend().hide()

        self.load_first_series()
        self.load_second_series()

        self.firstChart.addSeries(self.firstSeries)
        self.firstChart.setTitle("Salary Statistics")

        self.secondChart.addSeries(self.secondSeries)
        self.secondChart.setTitle("Total salaries per department")

        self.firstChartView = QChartView(self.firstChart)
        self.firstChartView.setRenderHint(QPainter.Antialiasing)

        self.secondChartView = QChartView(self.secondChart)
        self.secondChartView.setRenderHint(QPainter.Antialiasing)

        self.ui.firstLayout.addWidget(self.firstChartView)
        self.ui.secondLayout.addWidget(self.secondChartView)

        self.ui.backButton.clicked.connect(self.back_button_clicked)

    def load_first_series(self):
        resultList = self.database.get_salary_statistics()

        minBarSet = QBarSet("Min. salary")
        avgBarSet = QBarSet("Avg. salary")
        maxBarSet = QBarSet("Max. salary")

        minBarSet << resultList[0]
        avgBarSet << resultList[1]
        maxBarSet << resultList[2]

        self.firstSeries.append(minBarSet)
        self.firstSeries.append(avgBarSet)
        self.firstSeries.append(maxBarSet)

    def load_second_series(self):
        result_list = self.database.get_total_department_salaries()

        for entry in result_list:
            self.secondSeries.append(entry[0], entry[1])

    def back_button_clicked(self):
        self.hide()
        self.mainMenu.show()
