from PySide.QtGui import *
from PySide.QtCore import *

import window_UIs

# v perekompilirovanom fajle window_Uis y nas est' fynkcija setupUi, kotoraj polychaet v vide argymenta nekij objekt,
# v dannom slychae 'example' i potom k nemy prikleivaet vse nashi widgetu ili otpravljet ego kak parent
# example.setObjectName("example")
# self.verticalLayout_2 = QtGui.QVBoxLayout(example) - otpravljet kak parent
# eto znachit nam nado vuzvat' fynkcijy setupUi i peredat' nyznuj widget v kachestve argymenta.
# potomy shto mu nasledyemsja ot klas Ui_example i teper' vse metodu etogo klassa javljaytsja metodami etogo klassa.
# ochen' vazno connektit' knopky posle vuzova fynkcii setupUi, potomyshto do etogo etoj knopki ne sychestvyet

class exampleWindowClass(QWidget, window_UIs.Ui_example):
    def __init__(self):
        super(exampleWindowClass, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('ITEM LIST')
        self.count = 1                                 # shobu dobavit nymeracijy. Zavodim atribyt klassa
        self.additem_btn.clicked.connect(self.addItem)
        self.name_le.returnPressed.connect(self.addItem) # signal vuzuvaetsja kogda nazimaetsja Enter

    def addItem(self):
        text = self.name_le.text()    # vo pervuh nado polychit test s lineedit. On vozvrachaet nam tekst s lineedit
        # print text, type(text)
        if text:                                   # esli teks est' on ne pystoj,
            # lb = QLabel(text)
            lb = QLabel('%s: %s' %(self.count, text))  # mu sozdajom novuj label
            self.items_ly.addWidget(lb)                # dobavljaem v svoj layout novuj vidget
            self.count += 1

if __name__ == '__main__':
    app = QApplication([])
    w = exampleWindowClass()
    w.show()
    app.exec_()