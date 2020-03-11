import nuke
import nukescripts
import json
import os
import colorsys

path = os.path.expanduser("C:/Users/nuke/Dropbox/nuke/.nuke/PYTHON/NODEGRAPH/node_color_presets/nodeColorPresets.json")
pathToNames = "C:/Users/nuke/Dropbox/nuke/.nuke/PYTHON/NODEGRAPH/node_color_presets/colorsYIQ.json"
targetMenu = nuke.toolbar("Nodes")


class ColorPresetPanel(nukescripts.PythonPanel):
    def __init__(self, colors):
        nukescripts.PythonPanel.__init__(self, 'Manage Color Presets')
        self.list = []
        for color in sorted(colors):
            knob_dict = {"name": nuke.String_Knob("name_%s" % color, '', color),
                        "value": nuke.ColorChip_Knob('value_%s' % color, ''),
                        "delete": nuke.Boolean_Knob("delete_%s" % color, 'delete')}
            knob_dict["value"].setValue(colors[color])
            knob_dict["value"].clearFlag(nuke.STARTLINE)
            knob_dict["delete"].clearFlag(nuke.STARTLINE)
            self.list.append(knob_dict)
        for i in self.list:
            for k in i:
                self.addKnob(i[k])


def name_color(r, g, b):
    yiq = colorsys.rgb_to_yiq(r, g, b)
    x, y, z = yiq[0], yiq[1], yiq[2]
    vector_a = nuke.math.Vector3(x, y, z)
    name = ''
    min_dist = None
    try:
        file = open(pathToNames)
        data = json.load(file)
        file.close()
    except:
        print "Error loading Color labels"
        return "Unknown Color"

    for color in data:
        vector_b = nuke.math.Vector3(color['x'], color['y'], color['z'])
        dist = vector_a.distanceBetween(vector_b)
        if min_dist == None or dist < min_dist:
            min_dist = dist
            name = color['label']
    return name


def nuke_hex_to_rgb(nuke_hex):
    try:
        real_hex = '%08x' % nuke_hex
        r = int(real_hex[0:2], 16) / 255.0
        g = int(real_hex[2:4], 16) / 255.0
        b = int(real_hex[4:6], 16) / 255.0
    except:
        return None, None, None
    return r, g, b


def read_color_presets(path):
    if not os.path.isfile(path):
        print "No Color preset found "
        return {}
    else:
        try:
            f = open(path)
            colors = json.load(f)
            f.close()
            if type(colors) is dict:
                return colors
            else:
                print "The preset file doesn't contain a valid dictionary"
                return {}
        except:
            print "Error reading color preset file"
            return {}


def write_color_presets(path, colors):
    try:
        f = open(path, "w")
        json.dump(colors, f)
        f.close()
        return True
    except:
        return False


def set_tile_color(value=None):
    if value == None:
        value = nuke.getColor()
    for node in nuke.selectedNodes():
        node.knob('tile_color').setValue(value)


def create_tile_color_menu():
    colors = read_color_presets(path)
    color_menu = targetMenu.addMenu('Color Nodes', icon="color_node.png")
    for color in sorted(colors):
        color_menu.addCommand(color, 'setTileColor(%s)' % colors[color])

    color_menu.addCommand("Custom Color", lambda: set_tile_color())
    color_menu.addCommand("-", "", "")
    color_menu.addCommand("Add New Preset", lambda: add_new_color())
    color_menu.addCommand("Manage Presets", lambda: manage_color_presets())


def add_new_color():
    color = nuke.getColor()
    if color:
        colors = read_color_presets(path)
        valid_name = False
        r, g, b = nuke_hex_to_rgb(color)
        while not valid_name:
            name = nuke.getInput("Give a name to your color", name_color(r, g, b))
            if name:
                if not name in colors.keys():
                    valid_name = True
                    colors[name] = color
                    success = write_color_presets(path, colors)
                    if success:
                        targetMenu.findItem("Color Nodes").clearMenu()
                        create_tile_color_menu()
                    else:
                        print "Error writing file %s" % path
                else:
                    nuke.message("The name already exists")


def manage_color_presets():
    colors = read_color_presets(path)
    p = ColorPresetPanel(colors)
    if p.showModalDialog():
        new_colors = {}
        for preset in p.list:
            if not preset['delete'].value():
                new_colors[preset['name'].value()] = preset['value'].value()
        success = write_color_presets(path, new_colors)
        if success:
            targetMenu.findItem("Color Nodes").clearMenu()
            create_tile_color_menu()
        else:
            print "Error writing file %s" % path


create_tile_color_menu()
