from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import iconWidget_UIs as ui
from icons.icons import icons

import os
import random
import ctypes

from icons import icons_rcs  # potomy shto eto paket, nado importirovat' s pomochjy fom

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')

# vse pyti k ikonkam nahodjatsja v papke icons file icons

class iconWidgetClass(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(iconWidgetClass, self).__init__()
        self.setupUi(self)
        # ui
        self.setWindowIcon(QIcon(icons['create']))  # klass Icons imeet neskol'ko konstryktorov
        self.fill_btn.setText('')
        self.fill_btn.setFixedSize(QSize(40, 40))
        self.fill_btn.setIconSize(QSize(32, 32))
        self.fill_btn.setFlat(1)
        self.fill_btn.setIcon(QIcon(icons['create'])) # icons from icons.py
        self.fill_btn.setIcon(QIcon(':/create.png'))  # icons from resource file (icons_rcs)

        self.clear_btn.setText('')
        self.clear_btn.setFixedSize(QSize(40, 40))
        self.clear_btn.setIconSize(QSize(32, 32))
        self.clear_btn.setFlat(1)
        self.clear_btn.setIcon(QIcon(icons['clear']))

        self.fill_act.setIcon(QIcon(icons['create']))
        self.clear_act.setIcon(QIcon(icons['clear']))
        self.open_act.setIcon(QIcon(icons['open']))
        self.save_act.setIcon(QIcon(icons['save']))
        self.exit_act.setIcon(QIcon(icons['close']))

        pix = QPixmap(icons['sphere']).scaled(40, 40,
                                              Qt.KeepAspectRatio,
                                              Qt.SmoothTransformation)
        self.image_lb.setPixmap(pix)        # shto bu sozdat' Pixmap nado sozdat' exampljar klasa Pixmap i podat' tyda pyt'
                                            # eto prosto label s nej nikak nel'zja vzaimodejstvovat'

        self.list_lwd.setViewMode(QListView.IconMode)           # nastrojka kak otobrazajytsja kartinki
        self.list_lwd.setIconSize(QSize(64, 64))                # yvelichivaem razmer ikonok
        self.list_lwd.setResizeMode(QListWidget.ResizeMode.Adjust)  # kartinki izmenjayt razmer kogda izmenjaetsja razmer vidgeta
        self.list_lwd.setDragDropMode(QAbstractItemView.NoDragDrop) # otklychaet vozmoznost'  peremechat'  kartinki

        # connects
        self.fill_btn.clicked.connect(self.filList)
        self.clear_btn.clicked.connect(self.clearList)
        self.fill_act.triggered.connect(self.fillCombo)
        self.clear_act.triggered.connect(self.clearCombo)

    def filList(self):
        path = os.path.join(os.path.dirname(__file__), 'textures') # polychaem polnuj pyt' k papke
        self.clearList()
        for i in os.listdir(path):                                 # cherez list dir polychaem spisok fajlov
            item = QListWidgetItem(i)                              # sozdajotsja item i v teks k nemy kidaem imja faocherednogo fajla
            item.setIcon(QIcon(os.path.join(path, i)))
            self.list_lwd.addItem(item)

    def clearList(self):
        self.list_lwd.clear()

    def fillCombo(self):
        self.clearCombo()
        for i in range(10):
            item = QListWidgetItem('Item %s' % i)
            # item.setIcon(self.getRandomIcon())
            # item.setIcon((QIcon(icons['item1'])))
            self.combo_cbb.addItem('Item %s' % i)
            self.combo_cbb.setItemIcon(i, self.getRandomIcon())  # 1uj argyment eto index itema a 2oj ikonka
                                                                 # 1uj index mozno ykazuvat' tol'ko posle togo kak element s etim indexom bul sozdan

    def clearCombo(self):
        self.combo_cbb.clear()

    def getRandomIcon(self):
        return QIcon(icons[random.choice(['item1', 'item2', 'item3'])])
        # return QIcon(icons[random.choice(['item1', 'item2', 'item3'])])


if __name__ == '__main__':
    app = QApplication([])
    w = iconWidgetClass()
    w.show()
    app.exec_()