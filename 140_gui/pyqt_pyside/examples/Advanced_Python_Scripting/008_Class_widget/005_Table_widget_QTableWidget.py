from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import os
path = os.path.dirname(__file__)

class simpleWindow(QWidget):
    path = os.path.dirname(__file__)

    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QHBoxLayout()
        self.setLayout(ly)
        self.table = QTableWidget()
        ly.addWidget(self.table)
        self.table.verticalHeader().hide()                           # shto bu sprjat' vertikalnue zagolovki mozno ispol'zovat' Headers
        print(self.table.verticalHeader())                                                          # fynkcija verticalHEader vozvrachaet klass QHeaderView
        # self.table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        # start
        self.resize(500, 400)
        self.fillTable()

    def fillTable(self):
        files = os.listdir(path)
        self.table.setColumnCount(2)                                   # pered tem kak sozdat' tablicy nyzno ykazat' skol'ko v nej kolonok i strok
        self.table.setRowCount(len(files))
        self.table.setHorizontalHeaderLabels(['Name', 'Size'])         # kogda tablica y nas pystaja, to est' net niodnoj jachejki to i Headera y nas net
                                                                       # Header sozdajytsja tol'ko togda kogda sozdajytsja eti jachejki, to est' gynkcijy setHorisontalHeaderLabels
                                                                       # nado vuzvat' posle togo kak mu sozdali kolichestvo jacheek
        for i, f in enumerate(files):
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)      # y itemov est' specialnoe ponjatie flagi. Method setFlags objavljaet razlichnue
                                                                       # flagi kotorue govorjat mozet li item but' vudeljaemum ili modificirovanum
            item.setText(f)
            self.table.setItem(i, 0, item)
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.setText(str(os.stat(os.path.join(path, f)).st_size) + ' bytes')
            self.table.setItem(i, 1, item)


if __name__ == '__main__':
    app = QApplication([])
    w = simpleWindow()
    w.show()
    app.exec_()