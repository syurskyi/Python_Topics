from PySide.QtCore import *
from PySide.QtGui import *

import settings

class projectListClass(QListWidget):
    def __init__(self):
        super(projectListClass, self).__init__()

    def updateProjectList(self):
        data = settings.settingsClass().load()
        if data.get('path'):
            return True
        else:
            return False
