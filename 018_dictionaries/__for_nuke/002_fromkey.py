import nuke

# Get a list of all the nodes in the current script
all_nodes = nuke.allNodes()

# Create a dictionary with default values of 0 for each node class
class_counts = dict.fromkeys(nuke.allNodeClasses(), 0)

# Count the number of nodes in each class
for node in all_nodes:
    class_counts[node.Class()] += 1

# Print the resulting dictionary
print(class_counts)


# In this script, we first use nuke.allNodes() to get a list of all the nodes in the Nuke script. We then use
# the fromkeys method to create a dictionary with keys that are the names of all the node classes in the script,
# and default values of 0 for each key.
#
# We then loop over all the nodes in the script and increment the value of the corresponding key in
# the class_counts dictionary by 1 for each node we encounter. This gives us a count of the number of nodes
# in each class.
#
# Finally, we print out the resulting dictionary, which shows the number of nodes in each class.

import nuke

# Get all the nodes in the current script
all_nodes = nuke.allNodes()

# Extract the names of all the nodes
node_names = [node.name() for node in all_nodes]

# Create a dictionary with keys from node_names list and values initialized to None using fromkeys()
node_dict = dict.fromkeys(node_names, None)

# Print the resulting dictionary
print(node_dict)


# #####################################################################################################################

import nuke

# Get all Read nodes in the current script
read_nodes = nuke.allNodes('Read')

# Create a dictionary with keys based on the names of the Read nodes, and values set to None
read_dict = dict.fromkeys([node['name'].value() for node in read_nodes], None)

# Print the resulting dictionary
print(read_dict)

# #####################################################################################################################

import nuke

# Get all the nodes in the current script
all_nodes = nuke.allNodes()

# Use the fromkeys method to create a dictionary with default value of 0 for each node name
node_count_dict = dict.fromkeys([node['name'].value() for node in all_nodes], 0)

# Iterate over all the nodes and increment the count for each node name
for node in all_nodes:
    node_name = node['name'].value()
    node_count_dict[node_name] += 1

# Print the resulting dictionary
print(node_count_dict)
