## Default Nuke pipelinefunctions

import nuke
import os


def nkPath():
    nkPath = os.path.dirname(nuke.root().name())
    nkPath = os.path.normpath(nkPath)
    return nkPath

    
def nkScriptName():
    nkScriptName = os.path.basename(nuke.root().name())
    return nkScriptName

    
def showPath():
    showPath = os.path.splitdrive(nukePath)[1]
    return showPath

    
def show():
    try:
        nkPath = os.path.dirname(nuke.root().name())
        nkPath = os.path.normpath(nkPath)
        showPath = os.path.splitdrive(nkPath)
        show = showPath[1]
        show = str.split(show, "\\")[1]
        return show
    except:
        print "Error: show not found in nkPath..."

        
def sequence():
    try:
        nkScriptName = os.path.basename(nuke.root().name())
        sequence = str.split(nkScriptName, "_")[0]
        return sequence
    except:
        print "Error: sequence not found in nk script name..."
        

def shot():
    try:
        nkScriptName = os.path.basename(nuke.root().name())
        shot = str.split(nkScriptName, "_")[1]
        return shot
    except:
        print "Error: shot not found in nk script name..."
        

def assetName():
    try:
        scriptInfo = os.path.basename(nuke.root().name())
        scriptInfo = str.split(scriptInfo,"_")
        assetName = scriptInfo[2]
        return assetName
    except:
        print "Error: couldn't find assetName in nk script name..."
        

def taskName():
    try:
        scriptInfo = os.path.basename(nuke.root().name())
        scriptInfo = str.split(scriptInfo,"_")
        taskName = scriptInfo[3]
        return taskName
    except:
        print "Error: taskName not found in nk script name..."
        

def nkScriptVersion():
    try:
        nkScriptVersion = nuke.root().name()
        nkScriptVersion = str.split(nkScriptVersion,"_")
        nkScriptVersion = nkScriptVersion[-1]
        nkScriptVersion = str.split(nkScriptVersion,".")
        nkScriptVersion = nkScriptVersion[0]
        return nkScriptVersion
    except:
        print "Error: nkScriptVersion not found in nk script name..."