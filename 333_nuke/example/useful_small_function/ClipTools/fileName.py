#!/usr/bin/env python
#
# written by Howard Jones (c) 2009
#
# os functions for deleteing and renaming a list of files passed in from outside
#

import sys
import os
import glob

def rename(files, pathToFile, search, replace, verbose):
    count=0
    try:
        for f in files:
            pf = pathToFile+'/'+f                                # add path to source file
            r = f.replace(search, replace)                  # sets up the replace list for the files only
            pr = pathToFile+'/'+r                              # add path or replace file
            if (verbose):
                print ( "Renaming "+str(pf)+" to "+str(pr))          # return a debug output - command line
            os.rename(pf, pr) 
            count += 1
    except OSError:
        return 0
    if (verbose):
        print str(count)+' files renamed'


def delete(files, verbose):
    count=0
    try:
        for f in files:
            if (verbose):
                print "deleting "+f                             #return a useful output - command line
            os.remove(f)  
            count += 1
    except:
        return 1





#For calling this from command line
# 
'''def main():
    os.chdir(raw_input('directory path: '))
    files = []
    #l = len(files) #if possible its better to call functions before a loop to stop unnecessary function calls that slow down the system
    #so the next kine would be replaced with "while (0==l)):"
    while (0==len(files)): # assign this way to force compiler error if accidentally write 0= rather than 0==
        search=raw_input('search text: ')
        files=glob.glob('*'+search+'*')
        if (0==len(files)):
            print "Error: No files found with '"+search+"' in their name"

    replace=raw_input('replacement text: ')

    #now do it. By making the 
    #rename(files, search, replace, True)
    delete(files, search, replace, True)

'''
