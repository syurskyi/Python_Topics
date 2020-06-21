import sys
#from PyQt4 import QtGui
from PyQt5 import QtGui, QtWidgets


class QCustomQWidget (QtWidgets.QWidget):                       # QtWidgets
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()          # QtWidgets
        self.textUpQLabel    = QtWidgets.QLabel()               # QtWidgets
        self.textDownQLabel  = QtWidgets.QLabel()               # QtWidgets
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout  = QtWidgets.QHBoxLayout()          # QtWidgets
        self.iconQLabel      = QtWidgets.QLabel()               # QtWidgets
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        self.iconQLabel.setPixmap(QtGui.QPixmap(imagePath).scaled(60, 60))   # + .scaled(60, 60

class exampleQMainWindow (QtWidgets.QMainWindow):                            # QtWidgets
    def __init__ (self):
        super(exampleQMainWindow, self).__init__()
        # Create QListWidget
        self.list = QtWidgets.QListWidget(self)                     
        for index, name, icon in [
            ('No.1', 'Meyoko',  'lena-2.png'),
            ('No.2', 'Nyaruko', 'im.png'),
            ('No.3', 'Louise',  'Ok.png')]:
            # Create QCustomQWidget
            customWidget = QCustomQWidget()
            customWidget.setTextUp(index)
            customWidget.setTextDown(name)
            customWidget.setIcon(icon)
            # Create QListWidgetItem
            item = QtWidgets.QListWidgetItem()  
            # Set size hint
            item.setSizeHint(customWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.list.addItem(item)
            self.list.setItemWidget(item, customWidget)
        self.setCentralWidget(self.list)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])                                           # QtWidgets
    window = exampleQMainWindow()
    window.show()
    sys.exit(app.exec_())