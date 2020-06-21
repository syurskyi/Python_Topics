# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtWidgets, QtCore
from mainmenu import MainWindow
from database import Database


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
#    database = Database()
#    print(database.get_position_log_for_employee(2)[0])
#    print(database.get_position_log_for_employee(2)[1])
#    print(database.get_salary_log_for_employee(2)[0])
#    print(database.get_salary_log_for_employee(2)[1])
