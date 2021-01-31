______ ?

?.m__('Nuke').aC..('Github/nuke-config/Node/Change Knob Values', 'edit_nodes.edit_knobs()', 'ctrl+e')
?.m__('Nuke').aC..('Github/nuke-config/Node/Paste Knob Value', 'edit_nodes.paste_knobs()', 'ctrl+alt+v')
?.m__('Nuke').aC..('Github/nuke-config/Node/Paste Selected Knob Values', 'edit_nodes.paste_knobs(checkboxes=True)', 'ctrl+alt+shift+v')

___ intersection(a, b):
    # calculate intersection between list a and list b
    r_ list(set(a)&set(b))

___ get_knobs(node):
    # Add suported knobs from node and return a list of knob names
    unsupported_classes _ [
        'LookupCurves_Knob', 
        'PythonKnob', 
        'Tab_Knob', 
        'Obsolete_Knob', 
        'ChannelMask_Knob', 
        'Font_Knob', 
        'ColorChip_Knob',
        'Text_Knob',
        ]
    unsupported_names _ [
        'xpos', 'ypos', 'selected', 'gl_color', 'rootNodeUpdated', 'onDestroy', 
        'onCreate', 'updateUI', 'indicators', 'knobChanged', 
        ]
    ignore_patterns _ ['_panelDropped']
    knobs _ list()
    default_knobs _ list()
    ___ k __ node.knobs
        knob _ node[k]
        __ knob.C..  no. __ unsupported_classes and knob.n..  no. __ unsupported_names:
            ___ pattern __ ignore_patterns:
                __ pattern no. __ k:
                    knobs.ap..(k)
    r_ knobs


___ edit_knobs
    # Display all knobs that are common between all selected nodes.
    # Allow user to set expression or value on one of the knobs
    n__ _ ?.sN..()
    # Find intersection of all knobs between all selected nodes
    knobs _ list()
    ___ i __ ra__(le.(n__)):
        __ i __ 0:
            knobs _ get_knobs(n__[i])
        ____
            knobs _ intersection(get_knobs(n__[i-1]), get_knobs(n__[i]))
        i +_ 1
    knobs.s..
    default_knob_names _ [
        'hide_input', 'note_font', 'note_font_size', 'icon', 'dope_sheet', 'invert_mask', 
        'enable_mix_luminance', 'process_mask', 'lifetimeStart', 'unpremult', 'autolabel', 
        'invert_unpremult', 'postage_stamp_frame', 'postage_stamp', 'disable', 'maskChannel', 
        'name', 'lifetimeEnd', 'fringe', 'inject', 'maskChannelInput', 'maskChannelMask', 'maskFromFlag'
        ]
    default_knobs _ list()
    node_knobs _ list()
    ___ knob __ knobs:
        __ knob __ default_knob_names:
            default_knobs.ap..(knob)
        ____
            node_knobs.ap..(knob)
    default_knobs.s..
    node_knobs.s..
    knobs _ node_knobs + default_knobs
    panel _ ?.Panel('Edit Knobs')
    panel.setWidth(250)
    panel.addEnumerationPulldown('knobs', ' '.j..(knobs))
    panel.addBooleanCheckBox('expression', 0)
    panel.addSingleLineInput('0', '')
    panel.addSingleLineInput('1', '')
    panel.addSingleLineInput('2', '')
    panel.addSingleLineInput('3', '')
    __ no. panel.show
        r_
    k _ panel.v.. ('knobs')
    set_expression _ panel.v.. ('expression')
    values _ list()
    ___ i __ ra__(4):
        val _ panel.v.. (st.(i))
        __ val __ '':
            values.ap.. F..
        ____
            ___
                values.ap..(fl..(val))
            ______ ValueError:
                values.ap..(st.(val))
    ___ node __ n__:
        knob _ node[k]
        ___
            array_size _ knob.arraySize()
        ______ AttributeError:
            array_size _ 1
        __ set_expression:
            ___ i __ ra__(array_size):
                __ values[i]:
                    __ knob.hasExpression(i):
                        knob.clearAnimated(i)
                    knob.sE..(st.(values[i]), channel_i)
        ____
            __ isinstance(knob, ?.Boolean_Knob):
                __ knob.hasExpression
                    knob.clearAnimated()
                __ no. values[0]:
                    knob.sV.. F..
                ____
                    knob.sV.. T..
            ____ isinstance(knob, (?.File_Knob)):
                knob.sV..(values[0])
            ____ isinstance(knob, (?.XYZ_Knob, ?.XY_Knob, ?.WH_Knob, ?.UV_Knob, ?.Array_Knob)):
                __ knob.singleValue
                    __ values[0] and no. values[1] and no. values[2] and no. values[3]:
                        # if only values[0] exists, set all in array_size to first value
                        knob.sV..(values[0])
                ___ i __ ra__(array_size):
                    __ knob.hasExpression(i):
                        knob.clearAnimated(i)
                    __ isinstance(values[i], fl..):
                        knob.sV..(values[i], i)
                    ____ isinstance(values[i], st.):
                        # Assume this was meant to be an expression
                        knob.sE..(st.(values[i]), channel_i)


___ paste_knobs(checkboxes_F..):
    # Override of the ctrl+alt+v shortcut which allows pasting of only specified knob values to selected nodes
    # Only a single source node is supported unlike the original
    # Based on nukescripts.misc.copy_knobs()
    # If not checkboxes, all knobs or a single knob can be chosen
    # If checkboxes, an arbitrary selection of knobs can be chosen
    grp _ ?.thisGroup()
    dst_nodes _ grp.sN..()
    copy_grp _ ?.n__.Group(name_'____tempcopyknobgroup__')
    with copy_grp:
        ?.nodePaste('%clipboard%')
    src_nodes _ copy_grp.n__()
    __ src_nodes:
        src_node _ src_nodes[-1]
    excluded_knobs _ ['name', 'xpos', 'ypos', 'selected']
    ___
        intersect_knobs _ dict()
        ___ dst_node __ dst_nodes:
            src_knobs _ src_node.knobs()
            dst_knobs _ dst_node.knobs()
            intersection _ dict(
                [(item, src_knobs[item]) ___ item __ src_knobs.k..  \
                __ item no. __ excluded_knobs and dst_knobs.has_key(item)]
                )
            intersect_knobs.update(intersection)
        knobs _ intersect_knobs.k..
        panel _ ?.Panel('Choose Knobs')
        panel.setWidth(250)
        __ checkboxes:
            # Checkboxes for each knob
            ___ k __ knobs:
                panel.addBooleanCheckBox(k, 0)
        ____
            panel.addEnumerationPulldown('knob', ' '.j..(knobs))
            panel.addBooleanCheckBox('paste all', 0)
        __ no. panel.show
            r_
        chosen_knobs _ list()
        __ checkboxes:
            ___ k __ knobs:
                __ panel.v.. (k):
                    chosen_knobs.ap..(k)
        ____
            paste_all _ panel.v.. ('paste all')
            print paste_all
            __ paste_all:
                chosen_knobs _ knobs
            ____
                chosen_knobs.ap..(panel.v.. ('knob'))
                print 'got single value: ', chosen_knobs
        ___ dst_node __ dst_nodes:
            dst_knobs _ dst_node.knobs()
            ___ knob __ chosen_knobs:
                print 'pasting src {0} to dst {1}'.f..(knob, dst_node.n..
                src _ src_knobs[knob]
                dst _ dst_knobs[knob]
                dst.fromScript(src.toScript())
    ______ E.. __ e:
        ?.delete(copy_grp)
        raise e
    ?.delete(copy_grp)