from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class simpleWindow(QWidget):
    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QVBoxLayout(self)
        self.btn = QPushButton('Open')
        ly.addWidget(self.btn)
        self.resize(300, 200)
        self.btn.clicked.connect(self.showMessage)

    def showMessage2(self):
        i = QInputDialog.getItem(self, 'Enter text', 'Name:',  # Tak kak eto staticheskij metod, mu mozem vuzvat' ne sozdavaja ekzempljar klassa
                                                               # getItem eto staticheskaja fynkcija, mu mozem vuzvat' ne sozdavaja ekzempljar klassa
                                                               # Esli smotret' na Qt documentation to mozno videt
                                                               # QWidget *parent, const QString &title, const QString &label, const QStringList &items
                                                               # self,            title,                   label,               elementu iz kotoruh mozno vuberat' i eto objazatel'no dolznu but' stroki
                                 [str(x) for x in range(10)])
        print(i)

    def showMessage(self):
        msgBox = QMessageBox()      # sozdali ekzempljar klassa
        print(msgBox, type(msgBox))
        msgBox.setText("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        msgBox.setDetailedText('Detail text')
        ret = msgBox.exec_()                    # Kogda mu vuzuvaem exec_, eta fynkcija dolzna nam vernyt' kakoe to
                                                # znachenie, a kakoe znachenie zavisit ot togo kakyjy knopky mu nazmjom
                                                # Posle togo kak mu sdelali vuzov nashego Message boxa nam nado
                                                # proverit', shto ypalo nam v peremenyjy i potom vzavisimosti ot etogo
                                                # prodolzat'  kakie to dejstvija
        print(ret)
        print(ret == QMessageBox.Save)

if __name__ == '__main__':
    app = QApplication([])
    w = simpleWindow()
    w.show()
    app.exec_()