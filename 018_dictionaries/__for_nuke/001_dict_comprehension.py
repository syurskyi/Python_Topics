# create a list of nodes in the current Nuke script
nodes = nuke.allNodes()

# create a dictionary comprehension that maps node names to their class name
node_classes = {node.name(): node.Class() for node in nodes}

# print the resulting dictionary
print(node_classes)



# ######################################################################################################################

# Get all read nodes in the current Nuke script
read_nodes = nuke.allNodes('Read')

# Create a dictionary comprehension to map read node names to their file paths
read_paths = {node.name(): node['file'].value() for node in read_nodes}

# ######################################################################################################################

# Create a dictionary of all read nodes in the Nuke script, with their file paths as values
read_nodes = {node.name(): node['file'].getValue() for node in nuke.allNodes('Read')}

# ######################################################################################################################

import nuke

# Get all the nodes in the current script
nodes = nuke.allNodes()

# Create a dictionary that maps the node name to its Class knob value
node_dict = {node['name'].value(): node['Class'].value() for node in nodes}

# Create a dictionary that maps the node Class to the number of nodes with that Class
class_count_dict = {node_class: count for node_class, count in zip(set(node_dict.values()), [list(node_dict.values()).count(node_class) for node_class in set(node_dict.values())])}

# Print the resulting dictionary
print(class_count_dict)

# ######################################################################################################################

import nuke

node = nuke.selectedNode()

# get all the knob names and their values
knob_dict = {k: v.value() for k, v in zip(node.knobs().keys(), node.knobs().values())}

print(knob_dict)

# ######################################################################################################################

# Get all the selected nodes in the current script
selected_nodes = nuke.selectedNodes()

# Create a dictionary that maps node names to their selected status
node_status = {node['name'].value(): node in selected_nodes for node in nuke.allNodes()}

# Create a dictionary that maps node names to their node class
node_classes = {node['name'].value(): node.Class() for node in nuke.allNodes()}

# Create a dictionary that combines the two dictionaries using zip()
node_info = {name: {'selected': node_status[name], 'class': node_classes[name]} for name in node_status}

# Print the resulting dictionary
print(node_info)



