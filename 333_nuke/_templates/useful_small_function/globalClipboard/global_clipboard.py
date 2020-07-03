______ __
______ ?

c_ global_clipboard():
    ___  -
        __ __.name __ "nt":
            repo = "R:/Global_Clipboard/"
            user = __.environ.get("username")
        ____
            repo = "/Volumes/resources/Global_Clipboard/"
            user = __.environ.get("LOGNAME")

        saveName = "tempClipBoard"
        savePath = "{}{}_{}.nk".f..(repo, saveName, user)

    ___ paste(self, getUser):
        loadPath = "{}{}_{}.nk".f..(repo, saveName, getUser)
        __ __.path.exists(loadPath):
            ?.nodePaste(loadPath)
        ____
            ?.m..("{}\ndoesn't exists".f..(loadPath))

    ___ copy
        ?.nodeCopy(savePath)
        print "Selected nodes saved to {}".f..(savePath)

    ___ pasteName
        name = ?.getInput("First Initial + Last Name:")
        __ name:
            name = str(name).strip().lower()
            paste(name)