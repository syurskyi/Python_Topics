_____ ?
_____ __
_____ fnmatch
_____ shutil

___ fixReadError

    basePath _ ?.getFilename('Select Dir', " ", type_'open')

    __ basePath !_ N..:
        pa__ _ __.pa__.j..(basePath)
        ___ pa__, dirs, files __ __.walk(pa__):
            subpath _ pa__
        missingRead _ ""
        ___ i __ ?.aN..
            __ i.C.. __'Read':
                __ i.error() __ T..:
                    oldpath _ i['file'].value()
                    oldname _ __.pa__.b__(oldpath)
                    fileExt _ oldname[-3:]
                    fileName _ oldname[:-4]

                    __ fileName.find("%d") !_ -1:
                        newfindname _ fileName.replace("%d", "*") and fileName.replace("%d", "*")
                    __ fileName.find("%02d") !_ -1:
                        newfindname _ fileName.replace("%d", "*") and fileName.replace("%02d", "*")
                    __ fileName.find("%03d") !_ -1:
                        newfindname _ fileName.replace("%d", "*") and fileName.replace("%03d", "*")
                    __ fileName.find("%04d") !_ -1:
                        newfindname _ fileName.replace("%d", "*") and fileName.replace("%04d", "*")
                    __ fileName.find("%05d") !_ -1:
                        newfindname _ fileName.replace("%d", "*") and fileName.replace("%05d", "*")
                    __ fileName.find("%06d") !_ -1:
                        newfindname _ fileName.replace("%d", "*") and fileName.replace("%06d", "*")
                    findFile _ newfindname + "." + fileExt

                    pa__ _ __.pa__.j..(basePath)
                    ___ pa__, dirs, files __ __.walk(pa__):
                        subpath _ pa__
                        ___ file __ __.l_d_(subpath):
                            __ fnmatch.fnmatch(file, findFile):
                                reformatPath _ subpath.replace("\\","/")
                                i['file'].sV..(reformatPath +'/'+ oldname)

                    __ i.error() __ F..:
                        missingRead _ i.n.. + " - " + oldname + " - " + " Found Successfully!" + "\n" + missingRead
                    ____
                        missingRead _ i.n.. + " - " + oldname + " - " + " Not Fpund!" + "\n" + missingRead
                ____
                    __ missingRead __ "":
                        missingRead _ "You don't have any readNode with error!."
    ____
        missingRead _ "No folder was selected!"
    ?.m__(missingRead)

fixReadError()