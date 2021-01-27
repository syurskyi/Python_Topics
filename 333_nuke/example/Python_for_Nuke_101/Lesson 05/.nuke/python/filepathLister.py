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


	# Print the name of the current nuke script
    print "\n\nNuke Script: "+os.path.basename(nuke.root()['name'].value())

	# Print a heading for the list of file names & version numbers that will follow
    print "\nFILE & VERSION LIST:"

    # Create a list of node Classes to filter through
    node_classes = ['Read', 'ReadGeo', 'Camera']
    node_list = []

    # Search the Nuke script for all nodes that match the classname from our node_classes list, and add them to a new list node_list
    for i in nuke.allNodes():
        for x in node_classes:
            if i.knob('file') and i.Class() == x:
                node_list.append(i)

    # Loop through the nodes in our node_list list and get the filename in the 'file' knob
    for node in node_list:
        filepath = node['file'].value()
        filename = os.path.basename(filepath)
        
        # Separate the file name and version number
        filename_no_version = filename[0:filename.find('_v')]
        version_number = filename[filename.find('_v')+1:filename.find('_v')+6]

    	# Print the file name and version number of every node in the list.
        print ("You are using "+version_number+" of "+filename_no_version)

