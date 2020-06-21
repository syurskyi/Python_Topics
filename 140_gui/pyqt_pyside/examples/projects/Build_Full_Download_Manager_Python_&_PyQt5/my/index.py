from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from os import path

from PyQt5.uic import loadUiType

# ui,_ = loadUiType('main.ui')
ui = loadUiType('main.ui')[0]

# ui,_ = loadUiType(path.join(path.dirname(__file__), "main.ui"))
# ui = loadUiType(path.join(path.dirname(__file__), "main.ui"))[0]

# explanation ui,_
# FROM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "car_Proj.ui")) has error
# loadUiType returns two objects: form_class and base_class. From your code, it seems you aren't
# interested in the base_class, so you name it _, which is a convention for "unimportant" variables.
# Alternatively, you could use:
#
# FROM_CLASS = loadUiType(path.join(path.dirname(__file__), "car_Proj.ui"))[0]

# It's actually pretty simple: when loadUiType returns two values but you want to store only one for later use,
# you can assign one to the dummy variable _. It also works with more than just two return values
# (_, my_var, _, _, _ = returns_five_values()).

class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.init_ui()
        self.handel_buttons()

    def init_ui(self):
        # contain all ui chages in loading
        pass

    def handel_buttons(self):
        # handle all buttons in the app
        self.pushButton.clicked.connect(self.download)

    def handel_progress(self):
        # calculate the progress
        pass

    def handel_browse(self):
        # enable browsing yo our os, pick save location
        pass

    def download(self):
        # download any file
        print("Starting Download")

    def save_browse(self):
        # save location in the line edit
        pass




def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()






