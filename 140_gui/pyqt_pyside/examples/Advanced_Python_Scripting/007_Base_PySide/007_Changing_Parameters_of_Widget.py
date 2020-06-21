from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class simpleWindowClass(QWidget):
    def __init__(self):
        super(simpleWindowClass, self).__init__()
        layout = QVBoxLayout(self)   # zdes' sozdan LAyout no on ni kak neoboznachen kak layout nashego widgeta. Na samom
        # self.setLayout(layout)     # dele zdes' ykazan v kachestve argymenta self. To est' parenta. I dlja layout eto
                                     # avtomaticheski oboznachaet vstroitsja k nemy kak osnovnoj layout, esli tam yze
                                     #  ne sychestvyet kakogoto layouta. To est' ne prishlos' dal'she pisat'
                                     # Layout i Button mu ne kladjom v atribyt klassa, potomy shto nam ne prijdjotsja v
                                     # v dal'nejshem k nemy obrachatsja i s nim rabotat'. Eti peremenue javljajytsja
                                     # lokalnumi dlja konstryktora i v dal'nejshem bydyt ne dostypnu.
                                     # S imenem layout nyzno but' ostoroznum. Delo v tom shto y klassa widgeta yze est'
                                     # metod s takim ze imenem layout, kotoruj vozvrachaet ego central'nuj layout.
                                     # I esli v dannom primere mu napishem self.layout mu perezapishem etot metod.
                                     # Lychshe kak to ego pereimenovat'  esli mu hotim pomestit' ego v atribyt klassa.

        self.label = QLabel('Text')  # nadpis label = QLabel objavljaetsja kak lokalnyjy peremenyjy. I mu ne polychaem
                                     # prjmogo dostypa k etomy vidzety. Shto bu imet'  vozmoznost'  obratitsja k nemy
                                     # s lybogo metoda, ego nado pomechat' v atribyt klassa - self.label
        layout.addWidget(self.label)
        self.button = QPushButton('Press')
        layout.addWidget(self.button)
        self.button.clicked.connect(self.action)    # Posle pervogo nazatija knopki, connect izmenitsja na zakrutie okna.
                                                    # To est' mozno menjat' ne tol'ko tekst no i connectu i signalu,
                                                    # to est' lybue svojstva

    def action(self):
        self.label.setText('New Text')
        self.button.setText('Presseed')
        self.button.clicked.connect(self.close)

if __name__ == '__main__':
    app = QApplication([])
    w = simpleWindowClass()
    w.show()
    app.exec_()
