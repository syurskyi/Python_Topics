______ ?

?.menu('Nuke').addCommand('Github/nuke-config/Node/Change Knob Values', 'edit_nodes.edit_knobs()', 'ctrl+e')
?.menu('Nuke').addCommand('Github/nuke-config/Node/Paste Knob Value', 'edit_nodes.paste_knobs()', 'ctrl+alt+v')
?.menu('Nuke').addCommand('Github/nuke-config/Node/Paste Selected Knob Values', 'edit_nodes.paste_knobs(checkboxes=True)', 'ctrl+alt+shift+v')

___ intersection(a, b):
    # calculate intersection between list a and list b
    r_ list(set(a)&set(b))

___ get_knobs(node):
    # Add suported knobs from node and return a list of knob names
    unsupported_classes = [
        'LookupCurves_Knob', 
        'PythonKnob', 
        'Tab_Knob', 
        'Obsolete_Knob', 
        'ChannelMask_Knob', 
        'Font_Knob', 
        'ColorChip_Knob',
        'Text_Knob',
        ]
    unsupported_names = [
        'xpos', 'ypos', 'selected', 'gl_color', 'rootNodeUpdated', 'onDestroy', 
        'onCreate', 'updateUI', 'indicators', 'knobChanged', 
        ]
    ignore_patterns = ['_panelDropped']
    knobs = list()
    default_knobs = list()
    ___ k in node.knobs():
        knob = node[k]
        __ knob.Class() not in unsupported_classes and knob.name() not in unsupported_names:
            ___ pattern in ignore_patterns:
                __ pattern not in k:
                    knobs.append(k)
    r_ knobs


___ edit_knobs():
    # Display all knobs that are common between all selected nodes.
    # Allow user to set expression or value on one of the knobs
    nodes = ?.sN..()
    # Find intersection of all knobs between all selected nodes
    knobs = list()
    ___ i in ra__(le.(nodes)):
        __ i __ 0:
            knobs = get_knobs(nodes[i])
        ____
            knobs = intersection(get_knobs(nodes[i-1]), get_knobs(nodes[i]))
        i += 1
    knobs.sort()
    default_knob_names = [
        'hide_input', 'note_font', 'note_font_size', 'icon', 'dope_sheet', 'invert_mask', 
        'enable_mix_luminance', 'process_mask', 'lifetimeStart', 'unpremult', 'autolabel', 
        'invert_unpremult', 'postage_stamp_frame', 'postage_stamp', 'disable', 'maskChannel', 
        'name', 'lifetimeEnd', 'fringe', 'inject', 'maskChannelInput', 'maskChannelMask', 'maskFromFlag'
        ]
    default_knobs = list()
    node_knobs = list()
    ___ knob in knobs:
        __ knob in default_knob_names:
            default_knobs.append(knob)
        ____
            node_knobs.append(knob)
    default_knobs.sort()
    node_knobs.sort()
    knobs = node_knobs + default_knobs
    panel = ?.Panel('Edit Knobs')
    panel.setWidth(250)
    panel.addEnumerationPulldown('knobs', ' '.j..(knobs))
    panel.addBooleanCheckBox('expression', 0)
    panel.addSingleLineInput('0', '')
    panel.addSingleLineInput('1', '')
    panel.addSingleLineInput('2', '')
    panel.addSingleLineInput('3', '')
    __ not panel.show():
        r_
    k = panel.value('knobs')
    set_expression = panel.value('expression')
    values = list()
    ___ i in ra__(4):
        val = panel.value(st.(i))
        __ val __ '':
            values.append(False)
        ____
            ___
                values.append(float(val))
            ______ ValueError:
                values.append(st.(val))
    ___ node in nodes:
        knob = node[k]
        ___
            array_size = knob.arraySize()
        ______ AttributeError:
            array_size = 1
        __ set_expression:
            ___ i in ra__(array_size):
                __ values[i]:
                    __ knob.hasExpression(i):
                        knob.clearAnimated(i)
                    knob.setExpression(st.(values[i]), channel=i)
        ____
            __ isinstance(knob, ?.Boolean_Knob):
                __ knob.hasExpression():
                    knob.clearAnimated()
                __ not values[0]:
                    knob.setValue(False)
                ____
                    knob.setValue(True)
            ____ isinstance(knob, (?.File_Knob)):
                knob.setValue(values[0])
            ____ isinstance(knob, (?.XYZ_Knob, ?.XY_Knob, ?.WH_Knob, ?.UV_Knob, ?.Array_Knob)):
                __ knob.singleValue():
                    __ values[0] and not values[1] and not values[2] and not values[3]:
                        # if only values[0] exists, set all in array_size to first value
                        knob.setValue(values[0])
                ___ i in ra__(array_size):
                    __ knob.hasExpression(i):
                        knob.clearAnimated(i)
                    __ isinstance(values[i], float):
                        knob.setValue(values[i], i)
                    ____ isinstance(values[i], st.):
                        # Assume this was meant to be an expression
                        knob.setExpression(st.(values[i]), channel=i)


___ paste_knobs(checkboxes=False):
    # Override of the ctrl+alt+v shortcut which allows pasting of only specified knob values to selected nodes
    # Only a single source node is supported unlike the original
    # Based on nukescripts.misc.copy_knobs()
    # If not checkboxes, all knobs or a single knob can be chosen
    # If checkboxes, an arbitrary selection of knobs can be chosen
    grp = ?.thisGroup()
    dst_nodes = grp.sN..()
    copy_grp = ?.nodes.Group(name='____tempcopyknobgroup__')
    with copy_grp:
        ?.nodePaste('%clipboard%')
    src_nodes = copy_grp.nodes()
    __ src_nodes:
        src_node = src_nodes[-1]
    excluded_knobs = ['name', 'xpos', 'ypos', 'selected']
    ___
        intersect_knobs = dict()
        ___ dst_node in dst_nodes:
            src_knobs = src_node.knobs()
            dst_knobs = dst_node.knobs()
            intersection = dict(
                [(item, src_knobs[item]) ___ item in src_knobs.keys() \
                __ item not in excluded_knobs and dst_knobs.has_key(item)]
                )
            intersect_knobs.update(intersection)
        knobs = intersect_knobs.keys()
        panel = ?.Panel('Choose Knobs')
        panel.setWidth(250)
        __ checkboxes:
            # Checkboxes for each knob
            ___ k in knobs:
                panel.addBooleanCheckBox(k, 0)
        ____
            panel.addEnumerationPulldown('knob', ' '.j..(knobs))
            panel.addBooleanCheckBox('paste all', 0)
        __ not panel.show():
            r_
        chosen_knobs = list()
        __ checkboxes:
            ___ k in knobs:
                __ panel.value(k):
                    chosen_knobs.append(k)
        ____
            paste_all = panel.value('paste all')
            print paste_all
            __ paste_all:
                chosen_knobs = knobs
            ____
                chosen_knobs.append(panel.value('knob'))
                print 'got single value: ', chosen_knobs
        ___ dst_node in dst_nodes:
            dst_knobs = dst_node.knobs()
            ___ knob in chosen_knobs:
                print 'pasting src {0} to dst {1}'.format(knob, dst_node.name())
                src = src_knobs[knob]
                dst = dst_knobs[knob]
                dst.fromScript(src.toScript())
    ______ E.. __ e:
        ?.delete(copy_grp)
        raise e
    ?.delete(copy_grp)