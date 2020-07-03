#noViewer at nuke startUp
def killViewers():
    for v in nuke.allNodes("Viewer"):
        nuke.delete(v)
nuke.addOnScriptLoad(killViewers)


##font Size increase
def font_increase():
    for i in nuke.selectedNodes():
        size = i['note_font_size'].getValue() + 10
        i['note_font_size'].setValue(size)

nuke.menu('Nuke').addCommand( 'Edit/font_size_increase', font_increase, "ctrl+]")

##font Size decrease
def font_decrease():
    for i in nuke.selectedNodes():
        size = i['note_font_size'].getValue() - 10
        i['note_font_size'].setValue(size)
nuke.menu('Nuke').addCommand( 'Edit/font_size_decrease', font_decrease, "ctrl+[")


##size_increase
def size_increase():
    for i in nuke.selectedNodes():
        newsize = i['size'].getValue() + 1
        i['size'].setValue(newsize)

nuke.menu('Nuke').addCommand( 'Edit/size_increase', size_increase, "alt+]")


##size_increase
def size_decrease():
    for i in nuke.selectedNodes():
        newsize = i['size'].getValue() - 1
        i['size'].setValue(newsize)

nuke.menu('Nuke').addCommand( 'Edit/size_decrease', size_decrease, "alt+[")


##Toggle between opposite operation in transform and Merge
def operationSwitcher():
    node = nuke.selectedNode()
    merge_ops = {'stencil': 'mask', 'over': 'under', 'from': 'plus', 'out': 'in', 'multiply': 'divide'}
    if node.Class() == "Merge2":
        current_op = node['operation'].value()
        if current_op in merge_ops.keys():
            node['operation'].setValue(merge_ops[node['operation'].value()])
        elif current_op in merge_ops.values():
            node['operation'].setValue(merge_ops.keys()[merge_ops.values().index(current_op)])

    if node.Class() == "Transform":
        if node.knob('invert_matrix').value() == 1:
           node.knob('invert_matrix').setValue(0)
        else :
           node.knob('invert_matrix').setValue(1)

    if node.Class() == "Log2Lin":
        if node.knob('operation').value() == 'lin2log':
           node.knob('operation').setValue('log2lin')
        else :
           node.knob('operation').setValue('lin2log')


    if node.Class() == "CornerPin2D":
        if node.knob('invert').value() == 1:
           node.knob('invert').setValue(0)
        else :
           node.knob('invert').setValue(1)

