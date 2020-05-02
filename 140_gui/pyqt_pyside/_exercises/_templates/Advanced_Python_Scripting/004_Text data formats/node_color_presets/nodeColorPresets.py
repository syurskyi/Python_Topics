_____ nuke
_____ nukescripts
_____ json
_____ os
_____ colorsys

path _ os.path.expanduser("C:/Users/nuke/Dropbox/nuke/.nuke/PYTHON/NODEGRAPH/node_color_presets/nodeColorPresets.json")
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
            knob_dict["value"].setValue(colors[color])
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
    min_dist _ None
    try:
        file _ open(pathToNames)
        data _ json.load(file)
        file.close()
    except:
        print "Error loading Color labels"
        return "Unknown Color"

    ___ color in data:
        vector_b _ nuke.math.Vector3(color['x'], color['y'], color['z'])
        dist _ vector_a.distanceBetween(vector_b)
        __ min_dist __ None or dist < min_dist:
            min_dist _ dist
            name _ color['label']
    return name


___ nuke_hex_to_rgb(nuke_hex
    try:
        real_hex _ '%08x' % nuke_hex
        r _ int(real_hex[0:2], 16) / 255.0
        g _ int(real_hex[2:4], 16) / 255.0
        b _ int(real_hex[4:6], 16) / 255.0
    except:
        return None, None, None
    return r, g, b


___ read_color_presets(path
    __ not os.path.isfile(path
        print "No Color preset found "
        return {}
    ____
        try:
            f _ open(path)
            colors _ json.load(f)
            f.close()
            __ type(colors) is dict:
                return colors
            ____
                print "The preset file doesn't contain a valid dictionary"
                return {}
        except:
            print "Error reading color preset file"
            return {}


___ write_color_presets(path, colors
    try:
        f _ open(path, "w")
        json.dump(colors, f)
        f.close()
        return T..
    except:
        return False


___ set_tile_color(value_None
    __ value __ None:
        value _ nuke.getColor()
    ___ node in nuke.selectedNodes(
        node.knob('tile_color').setValue(value)


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
    color _ nuke.getColor()
    __ color:
        colors _ read_color_presets(path)
        valid_name _ False
        r, g, b _ nuke_hex_to_rgb(color)
        while not valid_name:
            name _ nuke.getInput("Give a name to your color", name_color(r, g, b))
            __ name:
                __ not name in colors.keys(
                    valid_name _ T..
                    colors[name] _ color
                    success _ write_color_presets(path, colors)
                    __ success:
                        targetMenu.findItem("Color Nodes").clearMenu()
                        create_tile_color_menu()
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
            __ not preset['delete'].value(
                new_colors[preset['name'].value()] _ preset['value'].value()
        success _ write_color_presets(path, new_colors)
        __ success:
            targetMenu.findItem("Color Nodes").clearMenu()
            create_tile_color_menu()
        ____
            print "Error writing file %s" % path


create_tile_color_menu()
