______ ?
______ ___
______ __
______ webbrowser
______ subprocess

___ openFileReturnArr(file):
    '''
    open set file, read in all lines and
    return an array with all the lines
    '''
    arr_# list
    fobj _ o..("@"%file, "r")
    #load in all lines
    ___ line __ fobj:
        #delete word wrap at the end of each line
        line_line.r__("\n", "")
        arr.ap..(line)
    fobj.c__
    r_ arr

___ getBackupSettings(val, pa__):
    '''
    getValues by finding pattern in array.
    for getting the values out of the array which
    comes from the settings file
    '''
    pa__ _ pa__
    arr _ openFileReturnArr(pa__)
    i_0
    ___ line __ arr:
        findVal_arr[i].find("@"%val)
        #if pattern found
        __ findVal!_-1:
            val_arr[i]
            valArr_val.s..("=")
            ___
                val_valArr[1] #value
                __ val__"":
                    val_" "
                ____ val__"NONE":
                    val_" "
            ______
                val_"---"
        i+_1
    r_ val

___ openFolder(pa__):
    __ ___.pl.. __ 'darwin':
        subprocess.check_call(['open', '--', pa__])
    ____ ___.pl.. __ 'linux2':
        subprocess.check_call(['gnome-open', '--', pa__])
    ____ ___.pl.. __ 'windows':
        subprocess.check_call(['explorer', pa__])

___ help
    '''
    goto web
    '''
    url _ 'http://www.leafpictures.de/blackbox'
    webbrowser.open_new(url)