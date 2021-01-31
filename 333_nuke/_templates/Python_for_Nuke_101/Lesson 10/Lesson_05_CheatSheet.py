# ----- CREATING LISTS & ADDING ITEMS TO THEM ---------------

# Creates a list named 'my_list'.
my_list = []

# Manually create a list with specified items.
car_list = ['Porsche', 'Ferrari', 'Ford', 'McLaren', 'Mercedes', 'Aston Martin', 'Lamborghini', 'Volkswagen', 'Audi']

# Automatically add selected nodes to a list.
node_list = []

___ i __ nuke.sN.. :
	node_list.append(i)

# Automatically add the node names of all Read nodes to a list.
node_list = []

___ i __ nuke.allNodes('Read'):
	node_list.append(i.name())

# Sort the items in your list alphabetically / numerically.
node_list.sort()



# --- Sort the items in your list by their y-position in the node graph. ---
node_list = nuke.sN..

# We have to define a function to use as a 'key' in the sort function...
def sort_ypos(node):
    return node['ypos'].value()

node_list.sort(key = sort_ypos)

print node_list



# Show all nodes currently in a list.
print node_list

# Show all nodes currently in a list, in a more human-readable way.
___ i __ node_list:
	print "- "+i





# ----- GETTING SPECIFIC ITEMS FROM A LIST ---------------

# First, define a list.
car_list = ['Porsche', 'Ferrari', 'Ford', 'McLaren', 'Mercedes', 'Aston Martin', 'Lamborghini', 'Volkswagen', 'Audi']

# Return the number of items in the list.
print len(car_list)

# Show a pop-up dialog box that displays a human-readable message.
nuke.message("There are "+str(len(car_list))+" cars in the list.")

# Return the 3rd item in the list. List index's start at 0, so the 3rd item will be index 2.
print car_list[2]

# Return the 3rd-last item in the list.
print car_list[-3]
 
# Return items 2 up until 5 from the list.
print car_list[2:5]

# Return every other item from 0 through 7 in the list.
print car_list[0:7:2] 

# Return every item in the list except the last 3.
print car_list[:-3]

# Return the last 5 items in the list.
print car_list[-5:]

# Return the last item in the list.
# We're finding the number of items in the list, and subtracting 1, since the index numbers start at 0.
print car_list[len(car_list)-1]

# Return the index of an item in the list.
print car_list.index('Volkswagen')





# ----- WORKING WITH STRINGS ---------------

# Shorten the word 'Compositor' to 'Comp'.
text = "Compositor"
print text[0:4]

# os module contains some handy functions.
import os

# Extract filename from full file path. Argument can be a filepath or a variable containing one.
print os.path.basename(your_filepath_here)

# Returns the directory of a file path.
print os.path.dirname(your_filepath_here)

# Returns the version number of a selected read node.
# Presumes format of a file is 'v0001.exr'.
path = nuke.sN.. ['file'].value()
print path[-9:-4]

# Find a character, or set of characters in a string (returns the index number).
my_string = "Python For Nuke 101"
nuke_index = my_string.find('Nuke')
print nuke_index

# This also works...
my_string = "Python For Nuke 101"
nuke_index = my_string.index('Nuke')
print nuke_index

# .find() only works on strings, whereas .index() works on lists.

# Print a goofy string
import nukescripts
print nukescripts.goofy_title()





# ----- NODES IN THE NODE GRAPH ---------------

# Select nodes in a list ('node_list' will have to be populated for this to work).
___ i __ node_list:
	i.setSelected(True)

# Deselect all nodes.
___ i __ nuke.allNodes()
	i.setSelected(F..)

# Copy / Paste nodes to the clipboard.
nuke.nodeCopy('%clipboard%')
nuke.nodePaste('%clipboard%')

# Delete selected nodes.
nuke.nodeDelete()

