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
        line=line.replace("\n", "")
        arr.ap..(line)
    fobj.c__
    r_ arr