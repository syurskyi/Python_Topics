______ os
______ ?

c_ global_clipboard():
    ___  - (self):
        __ os.name == "nt":
            self.repo = "R:/Global_Clipboard/"
            self.user = os.environ.get("username")
        ____
            self.repo = "/Volumes/resources/Global_Clipboard/"
            self.user = os.environ.get("LOGNAME")

        self.saveName = "tempClipBoard"
        self.savePath = "{}{}_{}.nk".format(self.repo, self.saveName, self.user)

    ___ paste(self, getUser):
        loadPath = "{}{}_{}.nk".format(self.repo, self.saveName, getUser)
        __ os.path.exists(loadPath):
            ?.nodePaste(loadPath)
        ____
            ?.message("{}\ndoesn't exists".format(loadPath))

    ___ copy(self):
        ?.nodeCopy(self.savePath)
        print "Selected nodes saved to {}".format(self.savePath)

    ___ pasteName(self):
        name = ?.getInput("First Initial + Last Name:")
        __ name:
            name = str(name).strip().lower()
            self.paste(name)