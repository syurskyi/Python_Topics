import nuke
import os
import fnmatch
import shutil

def fixReadError():

    basePath = nuke.getFilename('Select Dir', " ", type='open')

    if basePath != None:
        path = os.path.join(basePath)
        for path, dirs, files in os.walk(path):
            subpath = path
        missingRead = ""
        for i in nuke.allNodes():
            if i.Class()=='Read':
                if i.error() == True:
                    oldpath = i['file'].value()
                    oldname = os.path.basename(oldpath)
                    fileExt = oldname[-3:]
                    fileName = oldname[:-4]

                    if fileName.find("%d") != -1:
                        newfindname = fileName.replace("%d", "*") and fileName.replace("%d", "*")
                    if fileName.find("%02d") != -1:
                        newfindname = fileName.replace("%d", "*") and fileName.replace("%02d", "*")
                    if fileName.find("%03d") != -1:
                        newfindname = fileName.replace("%d", "*") and fileName.replace("%03d", "*")
                    if fileName.find("%04d") != -1:
                        newfindname = fileName.replace("%d", "*") and fileName.replace("%04d", "*")
                    if fileName.find("%05d") != -1:
                        newfindname = fileName.replace("%d", "*") and fileName.replace("%05d", "*")
                    if fileName.find("%06d") != -1:
                        newfindname = fileName.replace("%d", "*") and fileName.replace("%06d", "*")
                    findFile = newfindname + "." + fileExt

                    path = os.path.join(basePath)
                    for path, dirs, files in os.walk(path):
                        subpath = path
                        for file in os.listdir(subpath):
                            if fnmatch.fnmatch(file, findFile):
                                reformatPath = subpath.replace("\\","/")
                                i['file'].setValue(reformatPath +'/'+ oldname)

                    if i.error() == False:
                        missingRead = i.name() + " - " + oldname + " - " + " Found Successfully!" + "\n" + missingRead
                    else:
                        missingRead = i.name() + " - " + oldname + " - " + " Not Fpund!" + "\n" + missingRead
                else:
                    if missingRead == "":
                        missingRead = "You don't have any readNode with error!."
    else:
        missingRead = "No folder was selected!"
    nuke.message(missingRead)

fixReadError()