# ----- DICTIONARY EXAMPLE --------------------

# Create Dictionary
dictionary = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

# Returns all keys and values.
print dictionary

# Returns all keys and values in a nicer format.
print dictionary.items()

# Returns the value for dictionary item "key2"
print dictionary['key2']

# Returns the key for dictionary item "value2"
print dictionary.keys()[dictionary.values().index('value2')]

# Returns the 3rd value in the list from the "KeyList" key.
dict = {'KeyList':('item1','item2','item3','item4','item5')}
print dict['KeyList'][2]

# Return a list of all keys
print dictionary.keys()

# Return a list of all values
print dictionary.values()





# ----- STORE ALL MERGE NODES AND THEIR CURRENT OPERATIONS ------------

# Create a list to hold our merge nodes, and a dictionary to hold keys (Merge Nodes) and values (operation knobs)
merge_nodes = []
dictionary = {}

# Find all Merge nodes in our script, and add them to the merge_nodes list
for node in nuke.allNodes('Merge2'):
    merge_nodes.append(node)

# Loop through the merge_nodes list, and add the name of the merge node to the dictionary as a key,
# and the value of it's operation knob as the value
for i in merge_nodes:
    dictionary[i.name()] = i.knob('operation').value()

# Then print our dictionary items to check the right thing is being done.
print dictionary.items()





# ----- VFX STUDIO LOCATOR EXAMPLE ------------

# The keys are the names of VFX studios, and the values are lists containing countries the studios have offices.
# The syntax reads {'key':('value in list 1', 'value in list 2', 'value in list 3')}
VFX_Studios_Countries = {'ILM': ('USA', 'Canada', 'England', 'Singapore'), 'DNEG': ('England', 'Canada', 'India'), 'Digital Domain':('USA', 'Canada', 'India'), 'Weta':('New Zealand', ""), 'Method':('Canada', 'USA', 'Australia', )}

# Let's set 'England' as the country to find, by default.
Country_Finder = 'England'

# First, we must loop through the dictionary itself.
for i in VFX_Studios_Countries:

	# Then, we loop through the values (x) of said keys (i)
    for x in VFX_Studios_Countries[i]:

    	# If any value (x) in our dictionary matches the value of our Country_Finder variable, then...
        if x == Country_Finder:

        	# Print the key (i) -- This will return the name of the studio
            print i






# ----- CREATING A DICTIONARY WHERE THE KEY IS A NODE, AND IT'S KNOBS ARE VALUES ------------
n = nuke.selectedNode()
knob_list = []

# Add selected node's knobs to a list
for i in n.knobs():
    knob_list.append(i)

# Create the dictionary, where our selected node is the key, and the list of knobs we just created in the value
node_knobs = {n:knob_list}


# Return the dictionary
print node_knobs

# Return the 14th value (don't forget, the index number of lists starts at 0)
print node_knobs[n][13]
