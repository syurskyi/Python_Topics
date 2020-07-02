______ nuke
______ ___
______ __
______ webbrowser
______ subprocess

___ openFileReturnArr(file):
    '''
    open set file, read in all lines and
    return an array with all the lines
    '''
    arr=[]
    fobj = open("%s"%file, "r")
    #load in all lines
    ___ line __ fobj:
        #delete word wrap at the end of each line
        line=line.r__("\n", "")
        arr.append(line)
    fobj.c__
    r_ arr

___ getBackupSettings(val, path):
    '''
    getValues by finding pattern in array.
    for getting the values out of the array which
    comes from the settings file
    '''
    path = path
    arr = openFileReturnArr(path)
    i=0
    ___ line __ arr:
        findVal=arr[i].find("%s"%val)
        #if pattern found
        __ findVal!=-1:
            val=arr[i]
            valArr=val.split("=")
            ___
                val=valArr[1] #value
                __ val__"":
                    val=" "
                ____ val__"NONE":
                    val=" "
            ______
                val="---"
        i+=1
    r_ val

___ openFolder(path):
    __ ___.pl.. __ 'darwin':
        subprocess.check_call(['open', '--', path])
    ____ ___.pl.. __ 'linux2':
        subprocess.check_call(['gnome-open', '--', path])
    ____ ___.pl.. __ 'windows':
        subprocess.check_call(['explorer', path])

___ help():
    '''
    goto web
    '''
    url = 'http://www.leafpictures.de/blackbox'
    webbrowser.open_new(url)