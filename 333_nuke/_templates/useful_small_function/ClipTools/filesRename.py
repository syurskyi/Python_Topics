# Copyright (c) 2009 Howard Jones.  All Rights Reserved.
#
# renames or renumbers a list of clips from within Nuke
# version 1.0.2 (few bug fixes) 10th feb 09

______ fileName
______ re
#______ string - shouldn't be needed

# creates a list of files based on the shorthand from the selection supplied from Nuke
#
___ createList(files):
    g__ pathToFile
    g__ clipname
    g__ name
    g__ padding
    g__ extension
    g__ rangeStart
    g__ rangeEnd
    g__ filesList

    # parses the Nuke shorthand and splits into several components
    ___
        pathToFile___.pa__.d_n_(files[0])
        clipname___.pa__.b_n_(files[0]).s..('(')[0]
        name_clipname.s..('.')[0]
        padding_(clipname.s..('.')[1])[1:3]
        extension_clipname.s..(' ')[0].s..('.')[2]
        rangeStart_clipname.s..(' ')[1].s..('-')[0]
        rangeEnd_clipname.s..(' ')[1].s..('-')[1]

        # creates a list of files from above
        filesList_ # list
        rangeCount_int(rangeStart)
        w__ __.(rangeCount)<_ __.(rangeEnd):
            paddedNum_str('%'+padding+'d') % __.(rangeCount)
            #filesList.append(pathToFile+'/'+name+'.'+paddedNum+'.'+extension)
            filesList.ap..(name+'.'+paddedNum+'.'+extension)
            rangeCount+_1
        r_ [filesList, pathToFile]
    ______
        r_ [1,1]

# function that asks the nuke user for the 'replace' name and removes illegal characters from user input
# illegal characters set in renamer below.
#
___ getRename(files,name):
    g__ search
    g__ r..
    
    panel _ ?.Panel ( "Rename Files",400)
    panel.addSingleLineInput("text to replace:",name)
    panel.addSingleLineInput("replace with:", '')
    result_panel.s__

    __ result:
        search _ panel.v.. ("text to replace:")
        r.. _ panel.v.. ("replace with:")
        __ replace__'':
            replace_search                          # stops files being renamed with nothing
        __ r..[0] __'.':
            ?.m..('Starting with "." is unsupported')
            r_ 1
        # define the illegal characters and replace with '_'
        pattern _ re.compile('[^a-zA-Z0-9.]')
        r.. _ pattern.sub('_', r..)
        r_ [search,r..]
    ____
        r_ 1

# renames the clips passed from Nuke using shorthand (parsed in createList)
#
___ renameClips(files):
    (filesList, pathToFile)_createList(files)
    __ filesList __ no. 1:
        (search,r..)_getRename(files,name)
        renamed_fileName.rename(filesList, pathToFile, search, r.., F..)
        __ 0__renamed:
            ?.m..('failed - try selecting individual files')
    ____
        ?.m..('failed - try selecting individual files')
         

# renames the individual files passed from Nuke
#
___ renameFiles(files):
    pathToFile___.pa__.d_n_(files[0])
    name___.pa__.b_n_(files[0]).s..('.')[0]
    (search,r..)_getRename(files,name)
    filesList_# list
    ___ f __ files:
        clipname___.pa__.b_n_(f)
        filesList.ap..(clipname)
        

    renamed_fileName.rename(filesList, pathToFile, search, r.., F..)
    __ 0__renamed:
        ?.m..('failed, maybe permissions?')
      




# renamer - function called from Nuke
#
# renames files on disc from inside Nuke
#
___ renamer


    # asks nuke user for a clip name and checks for a '%'
    # if it finds a '%' it assumes a clip list from Nuke otherwise it assumes
    # a list of individual files from Nuke.
    
    files_nuke.getClipname('select files to rename',multiple_T..)
    
    w__ files:
        __ '%' __ st.(files):
            renameClips(files)
        ____
            renameFiles(files)
        files_N..   # stops renamer renaming files a 2nd time around the loop by mistake
        files_nuke.getClipname('select files to rename',multiple_T..)



# renumber - function called from Nuke
#
# renumbers and/or repads image sequences on disc from within Nuke
___ renumber
    
    files_nuke.getClipname('select clip to renumber',multiple_T..)
    #nuke.message('files selected = '+str(files))
    
    
    w__ files:

        __ '%' __ st.(files):
            createList(files)
            panel _ ?.Panel ( "Renumber Files",60)
            panel.addSingleLineInput("change padding to:", padding)
            panel.addSingleLineInput("frameStart:", rangeStart)
            result_panel.s__

            __ result:
                newPad _ panel.v.. ("change padding to:")
                frameStart_ panel.v.. ("frameStart:")


                tempFilesList_ # list
                rangeCount_int(rangeStart)
                newRangeCount_int(frameStart)

                w__ __.(rangeCount)<_ __.(rangeEnd):
                    paddedNum_str('%'+padding+'d') % __.(rangeCount)
                    newPaddedNum_str('%'+newPad+'d') % __.(newRangeCount)

                    searchPad_(pathToFile+'/'+name+'.'+paddedNum+'.'+extension)
                    tempPad_(pathToFile+'/'+name+'.'+newPaddedNum+'.'+extension+'.tmp')

                    # if there is no padding nuke lists '%d' this catches that and fails
                    ___
                        __.rename(searchPad, tempPad)
                    ______
                        ?.m..('Failed - try "renameClips" instead')
                        r_
                    #---------------------#
                    
                    tempFilesList.ap..(tempPad)
                    rangeCount+_1
                    newRangeCount+_1

                ___ f __ tempFilesList:
                    __.rename(f, f[:-4])

        ____
            ?.m..('This only works with clip ranges')
            
        files_nuke.getClipname('select more clips to renumber',multiple_T..)



# removeExtension - function called from Nuke
#
# removes last 4 characters from a list of files
# often this would be used to move tmp files created by Nuke on render failiure
# or overwrite a locked file (after unlocked) when render successful
#
___ removeExtension
    files_nuke.getFilename('select files to remove extension',multiple_T..)
    w__ files:
        __ '%' __ st.(files):
            ?.m..('This only works on individually selected files')
        ____
            result_nuke.a..('Remove extension "'+__.pa__.b_n_(files[0])[-4:]+'" ? \nthis can overwrite existing files')
            __ result:
                ___ f __ files:
                    __.rename(f, f[:-4])
        files_nuke.getFilename('select more files to remove extension',multiple_T..)


# removeTemps - function called from Nuke
# written by Diogo Girondi - modified by Howard Jones
#
# searches write nodes in Nuke and remves automatically any files ending with '.tmp' to help clean up files left after render failiure
#
___ removeTemps
     
    do_it_nuke.a..('This removes all .tmp files from the write nodes in this script. Are you sure you want to do this?')
    __ do_it:
        aw _ ?.aN..('Write')
        
        paths _ # list
        
        ___ w __ aw:
            f _ w['file'].v..
            p _ w['proxy'].v..
            
            __ f:
                f_path _ __.pa__.d_n_(f)
                paths.ap..(f_path)
            __ p:
                p_path _ __.pa__.d_n_(p)
                paths.ap..(p_path)
                
        ___ pa__ __ list(set(paths)):
            files _ __.l_d_(pa__)
            count_0
            ___ f __ files:
                filename _ f.s..('.')
                ext _ filename[-1]
                __ ext __ 'tmp':
                    ___
                        __.r__(pa__+'/'+f)
                        count+_1
                    ______
                        ?.tprint('Unable to delete file: @' % f)
        ?.m..('removed '+st.(count)+' files')


