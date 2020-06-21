from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

try:
    from PyQt5.QtCore import QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = str

from pymongo import MongoClient
import json

class ServerInfoPage(QWidget):
    def __init__(self):
        super(ServerInfoPage,self).__init__()

        self.server='mongodb://localhost:27017'

        lbl_info=QLabel(self.tr('server info:'))
        self.txt_info=QTextEdit()
        
        vbox=QVBoxLayout()
        vbox.addWidget(lbl_info)
        vbox.addWidget(self.txt_info,1)

        self.setLayout(vbox)

    def set_server(self,server):
        self.server=server
        mongo=MongoClient(self.server)
        output=json.dumps(mongo.server_info(),indent=4)
        self.txt_info.setText(QString(output))
        mongo.close()
