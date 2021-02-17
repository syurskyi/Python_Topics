create_node_options = {'Read': lambda: nuke.createNode('Read', inpanel=False),
                       'Grade': lambda: nuke.createNode('Grade', inpanel=False),
                       'Blur': lambda: nuke.createNode('Blur', inpanel=False),
                       }


def create_node(node):
    return create_node_options.get(node, 'not avaialable')


create_node('Blur')()


###### This is work
def operations(node):
    return {
        'Read': lambda: nuke.createNode('Read', inpanel=False),
        'Grade': lambda: nuke.createNode('Grade', inpanel=False),
        'Blur': lambda: nuke.createNode('Blur', inpanel=False),
        'Merge': lambda: nuke.createNode('Merge', inpanel=False),
    }.get(node, lambda: 'Not a valid operation')()

operations('Blur')

###### THis is work
create_node_options = {'Read': lambda: nuke.createNode('Read', inpanel=False),
                       'Grade': lambda: nuke.createNode('Grade', inpanel=False),
                       'Blur': lambda: nuke.createNode('Blur', inpanel=False),
                       }

print(create_node_options.keys())
create_node_options.get('Read', lambda: nuke.createNode('CheckerBoard', inpanel=False))()