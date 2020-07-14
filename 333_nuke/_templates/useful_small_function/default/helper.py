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
        line_line.r..("\n", "")
        arr.ap..(line)
    fobj.c__
    r_ arr