import nuke

# Get all the nodes in the current script
all_nodes = nuke.allNodes()

# Create a dictionary where the keys are node names and values are node classes
node_info_dict = {node['name'].value(): node.Class() for node in all_nodes}

# Sort the dictionary by keys
sorted_dict = dict(sorted(node_info_dict.items()))

# Print the resulting dictionary
print(sorted_dict)

# ######################################################################################################################

read_nodes = {}
for node in nuke.allNodes('Read'):
    read_nodes[node.name()] = node['file'].value()

sorted_read_nodes = dict(sorted(read_nodes.items()))

print(sorted_read_nodes)


# ######################################################################################################################

read_nodes = {node.name(): (node.firstFrame(), node.lastFrame()) for node in nuke.allNodes('Read')}
sorted_nodes = dict(sorted(read_nodes.items()))

# ######################################################################################################################

node_dict = {node.name(): node.Class() for node in sorted(nuke.allNodes())}

for name, node_type in node_dict.items():
    print("{}: {}".format(name, node_type))

