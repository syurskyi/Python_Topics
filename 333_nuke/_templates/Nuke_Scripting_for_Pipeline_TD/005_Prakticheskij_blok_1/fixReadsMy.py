_____ ?
_____ __
_____ fnmatch
_____ shutil

___ fixReadError

    basePath = ?.getFilename('Select Dir', " ", type='open')

    __ basePath != N..:
        pa__ = __.pa__.j..(basePath)
        ___ pa__, dirs, files __ __.walk(pa__):
            subpath = pa__
        missingRead = ""
        ___ i __ ?.aN..
            __ i.C.. __'Read':
                __ i.error() __ T..:
                    oldpath = i['file'].value()
                    oldname = __.pa__.b__(oldpath)
                    fileExt = oldname[-3:]
                    fileName = oldname[:-4]

                    __ fileName.find("%d") != -1:
                        newfindname = fileName.replace("%d", "*") and fileName.replace("%d", "*")
                    __ fileName.find("%02d") != -1:
                        newfindname = fileName.replace("%d", "*") and fileName.replace("%02d", "*")
                    __ fileName.find("%03d") != -1:
                        newfindname = fileName.replace("%d", "*") and fileName.replace("%03d", "*")
                    __ fileName.find("%04d") != -1:
                        newfindname = fileName.replace("%d", "*") and fileName.replace("%04d", "*")
                    __ fileName.find("%05d") != -1:
                        newfindname = fileName.replace("%d", "*") and fileName.replace("%05d", "*")
                    __ fileName.find("%06d") != -1:
                        newfindname = fileName.replace("%d", "*") and fileName.replace("%06d", "*")
                    findFile = newfindname + "." + fileExt

                    pa__ = __.pa__.j..(basePath)
                    ___ pa__, dirs, files __ __.walk(pa__):
                        subpath = pa__
                        ___ file __ __.l_d_(subpath):
                            __ fnmatch.fnmatch(file, findFile):
                                reformatPath = subpath.replace("\\","/")
                                i['file'].sV..(reformatPath +'/'+ oldname)

                    __ i.error() __ False:
                        missingRead = i.n.. + " - " + oldname + " - " + " Found Successfully!" + "\n" + missingRead
                    ____
                        missingRead = i.n.. + " - " + oldname + " - " + " Not Fpund!" + "\n" + missingRead
                ____
                    __ missingRead __ "":
                        missingRead = "You don't have any readNode with error!."
    ____
        missingRead = "No folder was selected!"
    ?.m__(missingRead)

fixReadError()