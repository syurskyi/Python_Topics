# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from ui_mainmenu import MainWindow
from database import Database


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

    # database = Database()
    # print(database.get_employee_full_info()[0])
    # print(database.get_employee_full_info()[1])

    # print(database.get_position_log_for_employee(5)[0])
    # print(database.get_position_log_for_employee(5)[1])
    # print(database.get_salary_log_for_employee(5)[0])
    # print(database.get_salary_log_for_employee(5)[1])

