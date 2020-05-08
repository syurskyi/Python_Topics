from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

# Kogda prilozenie zapyskaetsja to ono vstraivaetsja v EventLoop, to est' cykl sobutij. Eto beskonechnuj cikl sobutij
# kotorue proishodjat y nas na kompjytere ili y nas v operacionnoj sisteme
# Kogda srabatuvaet signal on vuzuvaet slot.
# Slotov mozet but' neskol'ko na odnom signale a takze signal mozet vuzuvat' neskol'ko slotov.
# KOgda rabotaet prilozenie, postojanno generiryjytsja kakieto signalu, bydto sozdanue pol'zovatelem
# ili operacionoj sistemoj. Etim signalam sootvestvyjyt opredeljonue slotu, slotu eto fynkcii, kotorue bydyt
# vuzuvatsja kogda signal srabotaet

class myWidget(QWidget):
    def __init__(self):
        super(myWidget, self).__init__()
        layout = QVBoxLayout(self)
        button = QPushButton('Print')
        layout.addWidget(button)
        line = QLineEdit()
        layout.addWidget(line)
        line.textChanged.connect(self.text)
        # first version
        # button.clicked.connect(self.action)
        # second version
        # self.connect(button, SIGNAL('clicked()'), self, SLOT('action()'))
        # third version
        # Zapis cheres dekorator rabotaet tochno takze kak pervuj variant, potomyshto decorator eto funkcija,
        # kotoraja polychaet v vide argumenta drygyjy fynkcijy. V pervom variante mu peredajom  prosto funcijy,
        # na kotoryjy bydet zakonekchen eto signal a v slychae s dekoratorom ja mogy proizvesti
        # echjo kakie to dejstvija.
        #

        @button.clicked.connect
        def click():
            self.action()

    # @SLOT()
    def action(self):
        print('ACTION')

    def text(self, arg):
        print(arg)


app = QApplication([])
window = myWidget()
window.show()
app.exec_()