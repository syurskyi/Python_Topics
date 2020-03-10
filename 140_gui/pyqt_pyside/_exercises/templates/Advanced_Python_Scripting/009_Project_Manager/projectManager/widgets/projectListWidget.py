____ __.__ ______ _
____ __.__ ______ _

______ settings

class projectListClass(QListWidget):
    def __init__(self):
        super(projectListClass, self).__init__()

    def updateProjectList(self):
        data = settings.settingsClass().load()
        if data.get('path'):
            return True
        else:
            return False
