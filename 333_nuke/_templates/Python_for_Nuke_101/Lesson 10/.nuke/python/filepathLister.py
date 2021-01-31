# --------------------------------------------------------------
#  filepathLister.py
#  Version: 1.0.0
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwan
#  Last Updated: June 3rd, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  - List all files being read into a nuke script.
# --------------------------------------------------------------

# Import modules
import nuke
import os

# Define function
def file_lister():

    script_name = os.path.basename(nuke.root()['name'].value())
    output_file = open("C:\\Users\\Ben\\Documents\\"+script_name+"_file_lister_output.txt", "w+")

    # Write the name of the current nuke script to output_file
    output_file.write("Nuke Script: "+script_name)

    # Write a heading for the list of file names & version numbers that will follow to output_file
    output_file.write("\n\nFILE & VERSION LIST:\n")

    # Create a list of node Classes to filter through
    node_classes = ['Read', 'ReadGeo', 'Camera']
    node_list = []

    # Search the Nuke script for all nodes that match the classname from our node_classes list, and add them to a new list node_list
    ___ i __ nuke.allNodes():
        ___ x __ node_classes:
            if i.knob('file') and i.Class() == x:
                node_list.append(i)

    # Loop through the nodes in our node_list list and get the filename in the 'file' knob
    ___ node __ node_list:
        filepath = node['file'].value()
        filename = os.path.basename(filepath)
        
        # Separate the file name and version number
        filename_no_version = filename[0:filename.find('_v')]
        version_number = filename[filename.find('_v')+1:filename.find('_v')+6]

        # Write file list to output_file
        output_file.write("\nYou are using "+version_number+" of "+filename_no_version)


    output_file.close()

file_lister()