______ __
______ ?

c_ global_clipboard
    ___  -
        __ __.name __ "nt":
            repo _ "R:/Global_Clipboard/"
            user _ __.en__.get("username")
        ____
            repo _ "/Volumes/resources/Global_Clipboard/"
            user _ __.en__.get("LOGNAME")

        saveName _ "tempClipBoard"
        savePath _ "{}{}_{}.nk".f..(repo, saveName, user)

    ___ paste(, getUser):
        loadPath _ "{}{}_{}.nk".f..(repo, saveName, getUser)
        __ __.pa__.e..(loadPath):
            ?.nodePaste(loadPath)
        ____
            ?.m..("{}\ndoesn't exists".f..(loadPath))

    ___ copy
        ?.nodeCopy(savePath)
        print "Selected nodes saved to {}".f..(savePath)

    ___ pasteName
        name _ ?.getInput("First Initial + Last Name:")
        __ name:
            name _ st.(name).strip().lower()
            paste(name)