# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4.QtCore import Qt, SIGNAL
import time

class MyWindow(QtGui.QPushButton):
    def __init__(self):
        QtGui.QPushButton.__init__(self)
        self.setText("Window Title")
        self.connect(self, SIGNAL("clicked()"), QtGui.qApp.quit)
    def load_data(self, sp):
        for i in range(1, 11):          # Имитируем процесс
            time.sleep(2)               # Что-то загружаем
            sp.showMessage("Загрузка данных... {0}%".format(i * 10),
                           Qt.AlignHCenter | Qt.AlignBottom, Qt.black)
            QtGui.qApp.processEvents()  # Запускаем оборот цикла

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    splash = QtGui.QSplashScreen(QtGui.QPixmap("img.png"))
    splash.showMessage("Загрузка данных... 0%",
                       Qt.AlignHCenter | Qt.AlignBottom, Qt.black)
    splash.show()                       # Отображаем заставку
    QtGui.qApp.processEvents()          # Запускаем оборот цикла
    window = MyWindow()
    window.setWindowTitle("Использование класса QSplashScreen")
    window.resize(300, 30)
    window.load_data(splash)            # Загружаем данные
    window.show()
    splash.finish(window)               # Скрываем заставку
    sys.exit(app.exec_())