_____ nuke
_____ nukescripts
_____ json
_____ __
_____ colorsys

path _ __.path.expanduser("C:/Users/nuke/Dropbox/nuke/.nuke/PYTHON/NODEGRAPH/node_color_presets/nodeColorPresets.json")
pathToNames _ "C:/Users/nuke/Dropbox/nuke/.nuke/PYTHON/NODEGRAPH/node_color_presets/colorsYIQ.json"
targetMenu _ nuke.toolbar("Nodes")


c_ ColorPresetPanel(nukescripts.PythonPanel
    ___  -  , colors
        nukescripts.PythonPanel. -  , 'Manage Color Presets')
        list _ []
        ___ color in sorted(colors
            knob_dict _ {"name": nuke.String_Knob("name_%s" % color, '', color),
                        "value": nuke.ColorChip_Knob('value_%s' % color, ''),
                        "delete": nuke.Boolean_Knob("delete_%s" % color, 'delete')}
            knob_dict["value"].sV..(colors[color])
            knob_dict["value"].clearFlag(nuke.STARTLINE)
            knob_dict["delete"].clearFlag(nuke.STARTLINE)
            list.ap..(knob_dict)
        ___ i in list:
            ___ k in i:
                addKnob(i[k])


___ name_color(r, g, b
    yiq _ colorsys.rgb_to_yiq(r, g, b)
    x, y, z _ yiq[0], yiq[1], yiq[2]
    vector_a _ nuke.math.Vector3(x, y, z)
    name _ ''
    min_dist _ N..
    ___
        file _ o..(pathToNames)
        data _ json.l..(file)
        file.c..
    _____:
        print "Error loading Color labels"
        r_ "Unknown Color"

    ___ color in data:
        vector_b _ nuke.math.Vector3(color['x'], color['y'], color['z'])
        dist _ vector_a.distanceBetween(vector_b)
        __ min_dist __ N.. or dist < min_dist:
            min_dist _ dist
            name _ color['label']
    r_ name


___ nuke_hex_to_rgb(nuke_hex
    ___
        real_hex _ '%08x' % nuke_hex
        r _ int(real_hex[0:2], 16) / 255.0
        g _ int(real_hex[2:4], 16) / 255.0
        b _ int(real_hex[4:6], 16) / 255.0
    _____:
        r_ N.., N.., N..
    r_ r, g, b


___ read_color_presets(path
    __ no. __.path.isfile(path
        print "No Color preset found "
        r_ {}
    ____
        ___
            f _ o..(path)
            colors _ json.l..(f)
            f.c..
            __ ty..(colors) __ dict:
                r_ colors
            ____
                print "The preset file doesn't contain a valid dictionary"
                r_ {}
        _____:
            print "Error reading color preset file"
            r_ {}


___ write_color_presets(path, colors
    ___
        f _ o..(path, "w")
        json.dump(colors, f)
        f.c..
        r_ T..
    _____:
        r_ F..


___ set_tile_color(value_None
    __ value __ N..:
        value _ nuke.gC..
    ___ node in nuke.selectedNodes(
        node.knob('tile_color').sV..(value)


___ create_tile_color_menu(
    colors _ read_color_presets(path)
    color_menu _ targetMenu.addMenu('Color Nodes', icon_"color_node.png")
    ___ color in sorted(colors
        color_menu.addCommand(color, 'setTileColor(%s)' % colors[color])

    color_menu.addCommand("Custom Color", lambda: set_tile_color())
    color_menu.addCommand("-", "", "")
    color_menu.addCommand("Add New Preset", lambda: add_new_color())
    color_menu.addCommand("Manage Presets", lambda: manage_color_presets())


___ add_new_color(
    color _ nuke.gC..
    __ color:
        colors _ read_color_presets(path)
        valid_name _ F..
        r, g, b _ nuke_hex_to_rgb(color)
        w__ no. valid_name:
            name _ nuke.getInput("Give a name to your color", name_color(r, g, b))
            __ name:
                __ no. name in colors.keys(
                    valid_name _ T..
                    colors[name] _ color
                    success _ write_color_presets(path, colors)
                    __ success:
                        targetMenu.findItem("Color Nodes").clearMenu
                        create_tile_color_menu
                    ____
                        print "Error writing file %s" % path
                ____
                    nuke.message("The name already exists")


___ manage_color_presets(
    colors _ read_color_presets(path)
    p _ ColorPresetPanel(colors)
    __ p.showModalDialog(
        new_colors _ {}
        ___ preset in p.list:
            __ no. preset['delete'].value(
                new_colors[preset['name'].v..] _ preset['value'].v..
        success _ write_color_presets(path, new_colors)
        __ success:
            targetMenu.findItem("Color Nodes").clearMenu
            create_tile_color_menu
        ____
            print "Error writing file %s" % path


create_tile_color_menu
