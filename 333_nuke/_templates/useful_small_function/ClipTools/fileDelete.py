#!/usr/bin/env python
# Copyright (c) 2009 Howard Jones.  All Rights Reserved.
#
# deletes a list of clips or files from within Nuke
# version 1.1.2 added multiple clip delete

______ ___, __ ,?, re
______ __
______ ?
____ fileName ______ _



# deletes a list of files supplied from Nuke
#
___ deleteFiles(files):
    __ __.pa__.isf..(files[0]):
        do_it_nuke.a..('really delete "'+filestoDelete+'" ? (no undo available)')
        __ do_it:
            delete(files,F..)
    ____
        ?.m..('This is not a regular file - nothing deleted')
        r_ 1

# deletes a list of clips supplied from Nuke
#
___ deleteClips(files):
    do_it_nuke.a..('really delete "'+filestoDelete+'..." ?\n(no undo available)')
    __ do_it:
        ___ clips __ files:
            [filesList,name,padding, extension, rangeStart, rangeEnd]_createList(clips)
            __ do_it:
                deleteFiles_delete(filesList,T..)

        __ deleteFiles:
            ?.m..('some files failed to delete \ntry selecting individual files')


#deleter - function called from Nuke
#
# deletes files or clips supplied from nuke
#
___ deleter():
    g__ filestoDelete

    # asks nuke user for a clip name and checks for a '%'
    # if it finds a '%' or '#' it assumes a clip list from Nuke otherwise it assumes
    # a list of individual files from Nuke.

    files_nuke.getClipname('select files to delete',multiple_T..)

    w__ files:
        filestoDelete___.pa__.b_n_(files[0])  #sets name for message later
        __ '%' __ st.(files) or '#' __ st.(files):
            catchFail_deleteClips(files)
        ____
            catchFail_deleteFiles(files)

        __ no. catchFail:
            files_nuke.getClipname('select files to delete',multiple_T..)
        ____
            files_N..
    
