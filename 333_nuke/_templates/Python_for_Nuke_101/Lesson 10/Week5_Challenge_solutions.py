"""
WEEK 05: CHALLENGE 01
Add the file_lister() function to the Utilities menu for easy access.
"""

utilitiesMenu.addCommand('File Lister', 'filepathLister.file_lister()')



"""
WEEK 05: CHALLENGE 02
Add the paste_selected() function to the Edit menu with a hotkey for easy access.
"""

# The following will simply overwrite the existing "Paste" menu item.
nuke.menu('Nuke').addCommand('Edit/Paste', 'paste_selected.paste_selected()', 'ctrl+v')

# Or you can create a new item if you prefer...
nuke.menu('Nuke').addCommand('Edit/Paste to Selected', 'paste_selected.paste_selected()', 'ctrl+shift+v')





"""
WEEK 05: CHALLENGE 03
Search the internet for a way to export the results of our filepathLister to a text file, as opposed to printing them in Nuke’s script editor.
"""

# To write to a file, you have to assign it to a variable and open it, like so:
script_name = os.path.basename(nuke.root()['name'].value())
output_file = open("C:\\Users\\Ben\\Documents\\"+script_name+"_file_lister_output.txt", "w+")

"""
- We're creating a new variable for the script_name since we want to use it as part of our file name
- The "w+" argument is saying "create the document if it doesn't exist, or overwrite if it does"

"""

# Replace any instance of 'print' with output_file.write("string_to_write_to_file") function to write text to file.
output_file.write("Nuke Script: "+script_name)
output_file.write("\n\nFILE & VERSION LIST:\n")

# ...and also at the end of our for loop
output_file.write("\nYou are using "+version_number+" of "+filename_no_version)


# See downloaded .nuke\python\filepathLister.py for finished script with solutions implemented.