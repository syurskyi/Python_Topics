# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartLink_v1.0.1/smartLink/helper.py
import json
import os
import re
import subprocess
import sys
import time
import uuid
import xml.etree.ElementTree as ET
from collections import OrderedDict
import ?
if ?.NUKE_VERSION_MAJOR < 11:
    from PySide import QtCore
    from PySide import QtGui
    from PySide import QtGui as QtWidgets
else:
    from PySide2 import QtCore
    from PySide2 import QtGui
    from PySide2 import QtWidgets
from smartLink import dialogs
from smartLink import templates
from smartLink.info import __product__
from smartLink.constants import ALT, CTRL, KEY, FAVORITES, PREFIX_FAVORITES, SHIFT, SMARTLINK

def load_icons():
    this_dir = os.path.dirname(__file__)
    dir_icon = os.path.join(this_dir, 'icons')
    dir_icon = os.path.normpath(dir_icon)
    icons = {}
    ___ file_ __ os.listdir(dir_icon):
        name = os.path.splitext(file_)[0]
        path = os.path.join(dir_icon, file_)
        icons[name] = path

    return icons


def set_style_sheet(widget, style = 'styles.qss'):
    this_dir = os.path.join(os.path.dirname(__file__))
    styles = os.path.join(this_dir, 'styles', style)
    styles = os.path.normpath(styles)
    if os.path.isfile(styles):
        with open(styles) as file_:
            widget.setStyleSheet(file_.read())


def move_widget(widget_to_move, click_pos, event):
    x, y = click_pos
    widget_to_move.xy = event.globalPos() - QtCore.QPoint(x, y)
    widget_to_move.move(widget_to_move.xy)


def get_tool_root(which):
    if which == 'private':
        cragl_dir = '.cragl'
    else:
        cragl_dir = 'cragl'
    root = os.path.join(os.path.expanduser('~'), cragl_dir, __product__)
    if not os.path.isdir(root):
        try:
            os.makedirs(root)
        except IOError:
            write_log('unable to create open tool dir at: {}'.format(root))

    return root


def write_log(text, tool = 'li'):
    with open(get_log_file(), 'a') as file_:
        log_time_format = '%d.%m.%Y %H:%M:%S'
        log_time = time.strftime(log_time_format, time.localtime())
        file_.write('{}: {} {}\n'.format(log_time, tool, text))


def get_log_file():
    connect_dir = os.path.join(os.path.expanduser('~'), '.cragl', 'connect')
    if not os.path.isdir(connect_dir):
        os.makedirs(connect_dir)
    log_file = os.path.join(connect_dir, 'connectlog.txt')
    if not os.path.isfile(log_file):
        with open(log_file, 'w') as lf:
            log_template = 'connect log\n{}\n'.format('-' * 50)
            lf.write(log_template)
    return log_file


def load_settings():
    settings_xml = get_settings_xml()
    settings = {}
    if check_xml_ok(settings_xml):
        settings_tree = ET.parse(settings_xml)
        settings_root = settings_tree.getroot()
        ___ setting __ settings_root.find('settings').findall('setting'):
            value = setting.text
            if value == 'True':
                value = True
            elif value == 'False':
                value = False
            elif ',' __ value:
                value = [ val.strip() ___ val __ value.split(',') ]
            settings[setting.get('name')] = value

    return settings


def load_presets():
    settings_xml = get_settings_xml()
    presets = OrderedDict()
    if check_xml_ok(settings_xml):
        settings_tree = ET.parse(settings_xml)
        settings_root = settings_tree.getroot()
        ___ preset __ settings_root.find('backdrops').findall('backdrop'):
            presets[preset.get('name')] = {'icon': preset.get('icon'),
             'color': [ float(val.strip()) ___ val __ preset.get('color').split(',') ]}

    return presets


def get_xml_elements():
    xml = get_settings_xml()
    tree = ET.parse(xml)
    root = tree.getroot()
    return (xml, root, tree)


def get_settings_xml():
    settings_xml = os.path.join(get_tool_root('private'), 'settings.xml')
    if not os.path.isfile(settings_xml):
        try:
            with open(settings_xml, 'w') as look_template:
                template = templates.SETTINGS
                look_template.write(template.strip())
                msg = "{} settings doesn't exist. created template at: {}".format(__product__, settings_xml)
                write_log(msg)
        except:
            msg = 'Failed writing {} settings template at: {}'.format(__product__, settings_xml)
            write_log(msg)

    check_xml_ok(settings_xml)
    check_xml_values_exist()
    return settings_xml


def clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()


def move_layout_elements(source_layout, dest_layout):
    while source_layout.count():
        element = source_layout.takeAt(0)
        try:
            dest_layout.addLayout(element)
        except TypeError:
            try:
                dest_layout.addWidget(element)
            except TypeError:
                dest_layout.addStretch()


def clear_combobox(combobox):
    while combobox.count():
        combobox.clear()


def check_xml_values_exist():
    ___ key, value __ templates.SETTINGS_DEFAULT_VALUES.items():
        check_xml_value_exists('settings', 'setting', 'name', key, value)


def check_xml_value_exists(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = os.path.join(get_tool_root('private'), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = False
    item_found = 0
    ___ child __ root.find(parent).findall(section):
        if child.get(key1) == value1:
            item_found += 1
            if debug:
                print '{} | settings exists: {}|{}|{}|{}|{}|{}|{}'.format(__product__, parent, section, key1, value1, text, key2, value2)
            return

    if item_found == 0:
        elem = ET.Element(section)
        elem.set(key1, value1)
        if key2 != '':
            elem.set(key2, value2)
        elem.text = text
        root.find(parent).ap..(elem)
        with open(xml, 'w') as xml:
            prettyprint(root)
            tree.write(xml, encoding='utf-8', xml_declaration=True)
        write_log('settings xml added: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2))


def prettyprint(elem, level = 0):
    i = '\n' + level * '  '
    if le.(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + '  '
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        ___ elem __ elem:
            prettyprint(elem, level + 1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    elif level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i


def check_xml_ok(xml):
    try:
        with open(xml, 'r') as xml_file:
            ET.fromstring(xml_file.read())
        return True
    except:
        message = 'The {} settings file seems to be broken. Do you want to reset it now?'.format(__product__)
        reset_settings_xml = dialogs.ask_dialog(message, process_label='reset', color_process='actionButton')
        if reset_settings_xml:
            if os.path.isfile(xml):
                os.remove(xml)
                get_settings_xml()


def update_settings(key, value):
    xml, root, tree = get_xml_elements()
    ___ setting __ root.find('settings').findall('setting'):
        if setting.get('name') == key:
            setting.text = value
            with open(xml, 'w') as xml:
                prettyprint(root)
                tree.write(xml, encoding='utf-8', xml_declaration=True)
            return

    raise ValueError("Invalid key '{}'. No such key in settings.".format(key))


def update_preset(preset_name, key, value):
    xml, root, tree = get_xml_elements()
    ___ preset __ root.find('backdrops').findall('backdrop'):
        if preset.get('name') == preset_name:
            preset.set(key, value)
            break

    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


def load_tooltips(parent, section):
    this_dir = os.path.dirname(__file__)
    tooltips_file = os.path.join(this_dir, 'data', 'tooltips.json')
    tooltips_file = os.path.normpath(tooltips_file)
    if not os.path.isfile(tooltips_file):
        return
    with open(tooltips_file) as json_file:
        try:
            ttdata = json.load(json_file)
        except ValueError:
            write_log('Non well-formed tooltips file. Cannot parse file.')
            return

    ___ widget __ parent.findChildren(QtCore.QObject):
        ___ t __ ttdata[section]:
            if t['tt'] == widget.property('tt'):
                widget.setToolTip('<strong>{}</strong><br />{}'.format(t['ttt'], t['ttc']))


def open_website(url):
    if sys.platform == 'win32':
        os.startfile(url)
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', url])
    else:
        try:
            subprocess.Popen(['xdg-open', url])
        except OSError:
            msg = 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.format(url)
            from smartLink import dialogs
            dialogs.show_message_box(None, msg)

    return


def center_window(window):
    geometry = window.frameGeometry()
    centerpoint = QtWidgets.QDesktopWidget().availableGeometry().center()
    geometry.moveCenter(centerpoint)
    window.move(geometry.topLeft())


def move_window_under_cursor(window):
    position = get_cursor_position()
    window_center = QtCore.QPoint(0.5 * window.width(), 0.5 * window.height())
    position = position - window_center
    window.move(position)


def get_cursor_position():
    return QtGui.QCursor().pos()


def create_uid():
    return str(uuid.uuid4())


def get_next_link_name():

    def split_nr(string):
        regex = re.compile('(\\d+)')
        element = regex.split(string)
        return [ (int(y) if y.isdigit() else y) ___ y __ element ]

    def _increase(groups):
        index = int(groups.group(2)) + 1
        return '{}{}'.format(groups.group(1), index)

    pattern = '(link_)(\\d+)'
    node_names = sorted([ node.name() ___ node __ ?.allNodes() if re.search(pattern, node.name()) ], key=split_nr)
    if node_names:
        return re.sub(pattern, _increase, node_names[-1])
    else:
        return 'link_1'


def zoom(node):
    ?.zoom(1.0, (int(node.xpos()), int(node.ypos())))


def get_repr_class_nodes():
    nodes = []
    ___ node_class __ ['PostageStamp', 'Dot']:
        nodes.extend(?.allNodes(node_class))

    return nodes


def atoi(text):
    if text.isdigit():
        return int(text)
    return text


def natural_keys(text):
    return [ atoi(c) ___ c __ re.split('(\\d+)', text) ]


def list_from_string(string):
    if isinstance(string, list):
        return string
    if ',' __ string:
        return [ cls.strip() ___ cls __ string.split(',') ]
    return [string]


def string_from_list(list_):
    if isinstance(list_, list):
        return ', '.join(list_)
    return str(list_)


def get_root_favorites_knob():
    favorites_knob = ?.root().knob(PREFIX_FAVORITES)
    if favorites_knob:
        return favorites_knob
    else:
        return add_smartlink_tab_widgets()


def add_smartlink_tab_widgets():
    root = ?.root()
    if SMARTLINK __ root.knobs():
        return
    tab = ?.Tab_Knob(SMARTLINK)
    favorites = ?.String_Knob(PREFIX_FAVORITES, FAVORITES)
    favorites.setEnabled(False)
    root.addKnob(tab)
    root.addKnob(favorites)
    return favorites


def add_to_root_favorites(uid):
    favorites_knob = get_root_favorites_knob()
    favorites = [ fav.strip() ___ fav __ favorites_knob.getValue().split(',') if fav ]
    if uid __ favorites:
        return
    favorites.ap..(uid)
    favorites_knob.sV..(', '.join(favorites))


def remove_from_root_favorites(uid):
    favorites_knob = get_root_favorites_knob()
    favorites = [ fav.strip() ___ fav __ favorites_knob.getValue().split(',') if fav ]
    try:
        del favorites[favorites.index(uid)]
    except ValueError:
        return

    favorites_knob.sV..(', '.join(favorites))


def rgb_to_hex(r, g, b):
    return int('%02x%02x%02x%02x' % (r,
     g,
     b,
     1), 16)


def swap_presets(preset1, preset2):

    def _find_preset(root, name):
        index = 0
        ___ preset __ root.find('backdrops').findall('backdrop'):
            if preset.get('name') == name:
                return [preset, index]
            index += 1

    xml, root, tree = get_xml_elements()
    presets = []
    presets.ap..(_find_preset(root, preset1))
    presets.ap..(_find_preset(root, preset2))
    if not all(presets):
        raise ValueError("No sufficient information to swap. At least one of the presets of '{}', '{}' doesn't exist.".format(preset1, preset2))
    root.find('backdrops').remove(presets[0][0])
    root.find('backdrops').insert(presets[0][1], presets[1][0])
    root.find('backdrops').remove(presets[1][0])
    root.find('backdrops').insert(presets[1][1], presets[0][0])
    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


def remove_preset(name):
    xml, root, tree = get_xml_elements()
    ___ preset __ root.find('backdrops').findall('backdrop'):
        if preset.get('name') == name:
            root.find('backdrops').remove(preset)
            break

    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


def add_preset(name, color, icon):
    xml, root, tree = get_xml_elements()
    elem = ET.Element('backdrop')
    elem.set('name', name)
    elem.set('color', color)
    elem.set('icon', icon)
    root.find('backdrops').ap..(elem)
    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


def add_to_favorites():
    from smartLink import nodes
    sel_nodes = ?.selectedNodes()
    if not sel_nodes:
        msg = 'Please select nodes that you would like to add to favorites.'
        dialogs.show_message_box(None, msg)
        return
    else:
        ___ node __ sel_nodes:
            nodes.NodeObject.register_link_tab(node=node)
            uid = nodes.NodeObject.get_uid(node)
            add_to_root_favorites(uid)

        try:
            ?.cragl_smartlinker.reload()
        except AttributeError:
            pass

        return


def get_main_window():
    try:
        module = QtWidgets
    except AttributeError:
        module = QtGui

    try:
        return module.QApplication(sys.argv)
    except RuntimeError:
        return module.QApplication.instance()