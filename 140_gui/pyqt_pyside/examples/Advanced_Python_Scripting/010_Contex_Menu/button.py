from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

textArray = 'Click', 'Press', 'Enter'

class MyButtonClass(QPushButton):
    def __init__(self, text):
        super(MyButtonClass, self).__init__(text)

    # nam nyzno pereopredelit' dejstvija na opredeljomij event.
    # eventu eto sobutija, kotorue postojanno generjatsja v programme, v zavisimosti ot kakih to dejstvij
    #
    # Protected functions eto te fynkcii kotorue mu mozem pereopredeljat'
    #
    # Mu pereopredelili vse signalu dlja button, i kogda mu zmjom levoj knopkoj mushi nichego ne proishodit
    # NEt daze animacii nazatija na knopky, potomy shto mu perezapisali eto dejstvie i esli na ety
    # knopky zakonektchen kakoj to signal po kliky, to on ne srabotaet, potomy shto prosto signal ne generitsja
    # Eto mozno ispravit' vuzvav default MousePressEvent iz roditel'skogo klassa. To est' cherez syper

    def mousePressEvent(self, event):
        print(event.button())
        if event.button() == Qt.MouseButton.LeftButton:        # v evente nahoditsja informacija kakaja knopka bula nazata
            super(MyButtonClass, self).mousePressEvent(event)
        elif event.button() == Qt.MouseButton.RightButton:

            pos = event.globalPos()   # pozicija berjotsja iz eventa.Tam yze est' takaja peremenaja
            menu = QMenu()
            for i in textArray:
                menu.addAction(QAction(i, self))
            a = menu.exec_(QCursor().pos())
            if a:
                self.setText(a.text())
        elif event.button() == Qt.MouseButton.MiddleButton:
            pass
