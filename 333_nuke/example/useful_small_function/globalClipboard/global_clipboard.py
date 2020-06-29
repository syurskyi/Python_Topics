import os
import nuke

class global_clipboard():
    def __init__(self):
        if os.name == "nt":
            self.repo = "R:/Global_Clipboard/"
            self.user = os.environ.get("username")
        else:
            self.repo = "/Volumes/resources/Global_Clipboard/"
            self.user = os.environ.get("LOGNAME")

        self.saveName = "tempClipBoard"
        self.savePath = "{}{}_{}.nk".format(self.repo, self.saveName, self.user)

    def paste(self, getUser):
        loadPath = "{}{}_{}.nk".format(self.repo, self.saveName, getUser)
        if os.path.exists(loadPath):
            nuke.nodePaste(loadPath)
        else:
            nuke.message("{}\ndoesn't exists".format(loadPath))

    def copy(self):
        nuke.nodeCopy(self.savePath)
        print "Selected nodes saved to {}".format(self.savePath)

    def pasteName(self):
        name = nuke.getInput("First Initial + Last Name:")
        if name:
            name = str(name).strip().lower()
            self.paste(name)