#!/usr/bin/env python
# Copyright (c) 2009 Howard Jones.  All Rights Reserved.
#
# deletes a list of clips or files from within Nuke
# version 1.1.2 added multiple clip delete

______ ___, __ ,nuke, re
______ __
______ nuke
____ fileName ______ *



# deletes a list of files supplied from Nuke
#
___ deleteFiles(files):
    __ __.path.isfile(files[0]):
        do_it=nuke.ask('really delete "'+filestoDelete+'" ? (no undo available)')
        __ do_it:
            delete(files,False)
    else:
        nuke.m..('This is not a regular file - nothing deleted')
        r_ 1

# deletes a list of clips supplied from Nuke
#
___ deleteClips(files):
    do_it=nuke.ask('really delete "'+filestoDelete+'..." ?\n(no undo available)')
    __ do_it:
        ___ clips __ files:
            [filesList,name,padding, extension, rangeStart, rangeEnd]=createList(clips)
            __ do_it:
                deleteFiles=delete(filesList,True)

        __ deleteFiles:
            nuke.m..('some files failed to delete \ntry selecting individual files')


#deleter - function called from Nuke
#
# deletes files or clips supplied from nuke
#
___ deleter():
    g__ filestoDelete

    # asks nuke user for a clip name and checks for a '%'
    # if it finds a '%' or '#' it assumes a clip list from Nuke otherwise it assumes
    # a list of individual files from Nuke.

    files=nuke.getClipname('select files to delete',multiple=True)

    while files:
        filestoDelete=__.path.basename(files[0])  #sets name for message later
        __ '%' __ str(files) or '#' __ str(files):
            catchFail=deleteClips(files)
        else:
            catchFail=deleteFiles(files)

        __ no. catchFail:
            files=nuke.getClipname('select files to delete',multiple=True)
        else:
            files=None
    
