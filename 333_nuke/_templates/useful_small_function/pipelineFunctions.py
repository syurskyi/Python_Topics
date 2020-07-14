## Default Nuke pipelinefunctions

______ ?
______ os


___ nkPath():
    nkPath = os.pa__.d_n_(?.root().name())
    nkPath = os.pa__.normpath(nkPath)
    r_ nkPath

    
___ nkScriptName():
    nkScriptName = os.pa__.b_n_(?.root().name())
    r_ nkScriptName

    
___ showPath():
    showPath = os.pa__.splitdrive(nukePath)[1]
    r_ showPath

    
___ show():
    ___
        nkPath = os.pa__.d_n_(?.root().name())
        nkPath = os.pa__.normpath(nkPath)
        showPath = os.pa__.splitdrive(nkPath)
        show = showPath[1]
        show = st..split(show, "\\")[1]
        r_ show
    ______:
        print "Error: show not found in nkPath..."

        
___ sequence():
    ___
        nkScriptName = os.pa__.b_n_(?.root().name())
        sequence = st..split(nkScriptName, "_")[0]
        r_ sequence
    ______:
        print "Error: sequence not found in nk script name..."
        

___ shot():
    ___
        nkScriptName = os.pa__.b_n_(?.root().name())
        shot = st..split(nkScriptName, "_")[1]
        r_ shot
    ______:
        print "Error: shot not found in nk script name..."
        

___ assetName():
    ___
        scriptInfo = os.pa__.b_n_(?.root().name())
        scriptInfo = st..split(scriptInfo,"_")
        assetName = scriptInfo[2]
        r_ assetName
    ______:
        print "Error: couldn't find assetName in nk script name..."
        

___ taskName():
    ___
        scriptInfo = os.pa__.b_n_(?.root().name())
        scriptInfo = st..split(scriptInfo,"_")
        taskName = scriptInfo[3]
        r_ taskName
    ______:
        print "Error: taskName not found in nk script name..."
        

___ nkScriptVersion():
    ___
        nkScriptVersion = ?.root().name()
        nkScriptVersion = st..split(nkScriptVersion,"_")
        nkScriptVersion = nkScriptVersion[-1]
        nkScriptVersion = st..split(nkScriptVersion,".")
        nkScriptVersion = nkScriptVersion[0]
        r_ nkScriptVersion
    ______:
        print "Error: nkScriptVersion not found in nk script name..."