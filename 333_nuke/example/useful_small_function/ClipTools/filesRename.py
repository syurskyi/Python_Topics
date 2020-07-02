# Copyright (c) 2009 Howard Jones.  All Rights Reserved.
#
# renames or renumbers a list of clips from within Nuke
# version 1.0.2 (few bug fixes) 10th feb 09

import fileName
import re
#import string - shouldn't be needed

# creates a list of files based on the shorthand from the selection supplied from Nuke
#
def createList(files):
    global pathToFile
    global clipname
    global name
    global padding
    global extension
    global rangeStart
    global rangeEnd
    global filesList

    # parses the Nuke shorthand and splits into several components
    try:
        pathToFile=os.path.dirname(files[0])
        clipname=os.path.basename(files[0]).split('(')[0]
        name=clipname.split('.')[0]
        padding=(clipname.split('.')[1])[1:3]
        extension=clipname.split(' ')[0].split('.')[2]
        rangeStart=clipname.split(' ')[1].split('-')[0]
        rangeEnd=clipname.split(' ')[1].split('-')[1]

        # creates a list of files from above
        filesList= []
        rangeCount=int(rangeStart)
        while int(rangeCount)<= int(rangeEnd):
            paddedNum=str('%'+padding+'d') % int(rangeCount)
            #filesList.append(pathToFile+'/'+name+'.'+paddedNum+'.'+extension)
            filesList.append(name+'.'+paddedNum+'.'+extension)
            rangeCount+=1
        return [filesList, pathToFile]
    except:
        return [1,1]

# function that asks the nuke user for the 'replace' name and removes illegal characters from user input
# illegal characters set in renamer below.
#
def getRename(files,name):
    global search
    global replace
    
    panel = nuke.Panel ( "Rename Files",400)     
    panel.addSingleLineInput("text to replace:",name)
    panel.addSingleLineInput("replace with:", '')
    result=panel.show() 

    if result:
        search = panel.value("text to replace:")
        replace = panel.value("replace with:")
        if replace=='':
            replace=search                          # stops files being renamed with nothing
        if replace[0] =='.':
            nuke.message('Starting with "." is unsupported')
            return 1
        # define the illegal characters and replace with '_'
        pattern = re.compile('[^a-zA-Z0-9.]')
        replace = pattern.sub('_', replace)
        return [search,replace]
    else:
        return 1

# renames the clips passed from Nuke using shorthand (parsed in createList)
#
def renameClips(files):
    (filesList, pathToFile)=createList(files)
    if filesList is not 1:
        (search,replace)=getRename(files,name)
        renamed=fileName.rename(filesList, pathToFile, search, replace, False)
        if 0==renamed:
            nuke.message('failed - try selecting individual files')
    else:
        nuke.message('failed - try selecting individual files')
         

# renames the individual files passed from Nuke
#
def renameFiles(files):
    pathToFile=os.path.dirname(files[0])
    name=os.path.basename(files[0]).split('.')[0]
    (search,replace)=getRename(files,name)
    filesList=[]
    for f in files:
        clipname=os.path.basename(f)
        filesList.append(clipname)
        

    renamed=fileName.rename(filesList, pathToFile, search, replace, False)
    if 0==renamed:
        nuke.message('failed, maybe permissions?')
      




# renamer - function called from Nuke
#
# renames files on disc from inside Nuke
#
def renamer():


    # asks nuke user for a clip name and checks for a '%'
    # if it finds a '%' it assumes a clip list from Nuke otherwise it assumes
    # a list of individual files from Nuke.
    
    files=nuke.getClipname('select files to rename',multiple=True)
    
    while files:
        if '%' in str(files):
            renameClips(files)
        else:
            renameFiles(files)
        files=None   # stops renamer renaming files a 2nd time around the loop by mistake
        files=nuke.getClipname('select files to rename',multiple=True)



# renumber - function called from Nuke
#
# renumbers and/or repads image sequences on disc from within Nuke
def renumber():
    
    files=nuke.getClipname('select clip to renumber',multiple=True)
    #nuke.message('files selected = '+str(files))
    
    
    while files:

        if '%' in str(files):
            createList(files)
            panel = nuke.Panel ( "Renumber Files",60)     
            panel.addSingleLineInput("change padding to:", padding)
            panel.addSingleLineInput("frameStart:", rangeStart)
            result=panel.show() 

            if result:
                newPad = panel.value("change padding to:")
                frameStart= panel.value("frameStart:")


                tempFilesList= []
                rangeCount=int(rangeStart)
                newRangeCount=int(frameStart)

                while int(rangeCount)<= int(rangeEnd):
                    paddedNum=str('%'+padding+'d') % int(rangeCount)
                    newPaddedNum=str('%'+newPad+'d') % int(newRangeCount)

                    searchPad=(pathToFile+'/'+name+'.'+paddedNum+'.'+extension)
                    tempPad=(pathToFile+'/'+name+'.'+newPaddedNum+'.'+extension+'.tmp')

                    # if there is no padding nuke lists '%d' this catches that and fails
                    try:
                        os.rename(searchPad, tempPad)
                    except:
                        nuke.message('Failed - try "renameClips" instead')
                        return
                    #---------------------#
                    
                    tempFilesList.append(tempPad)
                    rangeCount+=1
                    newRangeCount+=1

                for f in tempFilesList:
                    os.rename(f, f[:-4])

        else:
            nuke.message('This only works with clip ranges')
            
        files=nuke.getClipname('select more clips to renumber',multiple=True)



# removeExtension - function called from Nuke
#
# removes last 4 characters from a list of files
# often this would be used to move tmp files created by Nuke on render failiure
# or overwrite a locked file (after unlocked) when render successful
#
def removeExtension():
    files=nuke.getFilename('select files to remove extension',multiple=True)
    while files:
        if '%' in str(files):
            nuke.message('This only works on individually selected files')
        else:
            result=nuke.ask('Remove extension "'+os.path.basename(files[0])[-4:]+'" ? \nthis can overwrite existing files')
            if result:
                for f in files:
                    os.rename(f, f[:-4])
        files=nuke.getFilename('select more files to remove extension',multiple=True)


# removeTemps - function called from Nuke
# written by Diogo Girondi - modified by Howard Jones
#
# searches write nodes in Nuke and remves automatically any files ending with '.tmp' to help clean up files left after render failiure
#
def removeTemps():
     
    do_it=nuke.ask('This removes all .tmp files from the write nodes in this script. Are you sure you want to do this?')
    if do_it:
        aw = nuke.allNodes('Write')
        
        paths = []
        
        for w in aw:
            f = w['file'].value()
            p = w['proxy'].value()
            
            if f:
                f_path = os.path.dirname(f)
                paths.append(f_path)
            if p:
                p_path = os.path.dirname(p)
                paths.append(p_path)
                
        for path in list(set(paths)):
            files = os.listdir(path)
            count=0
            for f in files:
                filename = f.split('.')
                ext = filename[-1]
                if ext == 'tmp':
                    try:
                        os.remove(path+'/'+f)
                        count+=1
                    except:
                        nuke.tprint('Unable to delete file: %s' % f)
        nuke.message('removed '+str(count)+' files')


