# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartLook_v2.0/smartLook/src/helper.py
import time
import hashlib
import random
import os
import sys
import subprocess
import urllib
import xml.etree.ElementTree as ET
import collections
import platform
import struct
import imghdr
import json
import nuke
import nukescripts
if nuke.NUKE_VERSION_MAJOR < 11:
    from PySide import QtGui as QtWidgets
    from PySide import QtGui
    from PySide import QtCore
else:
    from PySide2 import QtWidgets
    from PySide2 import QtGui
    from PySide2 import QtCore
import templates

def load_icons(*args):
    this_dir = os.path.dirname(__file__)
    dir_icon = os.path.join(this_dir, '../', 'icons')
    dir_icon = os.path.normpath(dir_icon)
    join = os.path.join
    return {'about': join(dir_icon, 'about.jpg'),
     'icon_logo': join(dir_icon, 'logo.png'),
     'icon_logo_grey': join(dir_icon, 'logo_grey.png'),
     'icon_pool': join(dir_icon, 'pool.png'),
     'icon_star': join(dir_icon, 'look_star.png'),
     'icon_update': join(dir_icon, 'look_update.png'),
     'icon_delete': join(dir_icon, 'look_delete.png'),
     'icon_import': join(dir_icon, 'look_import.png'),
     'icon_export': join(dir_icon, 'look_export.png'),
     'icon_edit': join(dir_icon, 'edit.png'),
     'icon_page': join(dir_icon, 'page.png'),
     'icon_folder': join(dir_icon, 'folder.png'),
     'icon_folder_white': join(dir_icon, 'folder_white.png'),
     'icon_folder_grey': join(dir_icon, 'folder_grey.png'),
     'icon_explorer': join(dir_icon, 'explorer.png'),
     'icon_nuke': join(dir_icon, 'nuke.png'),
     'icon_nodes': join(dir_icon, 'nodes.png'),
     'icon_toolsets': join(dir_icon, 'toolsets.png'),
     'icon_insert': join(dir_icon, 'insert.png'),
     'icon_insert_nk': join(dir_icon, 'insert_nk.png'),
     'icon_insert_img': join(dir_icon, 'insert_img.jpg'),
     'icon_refresh': join(dir_icon, 'refresh.png'),
     'icon_snapshot': join(dir_icon, 'snapshot.png'),
     'icon_x': join(dir_icon, 'x.png'),
     'icon_settings': join(dir_icon, 'settings.png'),
     'icon_maximize': join(dir_icon, 'maximize.png'),
     'icon_half': join(dir_icon, 'half.png'),
     'icon_eye': join(dir_icon, 'eye.png'),
     'icon_delete_all': join(dir_icon, 'delete_all.png'),
     'icon_reveal': join(dir_icon, 'reveal.png'),
     'icon_flag': join(dir_icon, 'flag.png'),
     'icon_nocolor': join(dir_icon, 'nocolor.png'),
     'icon_comment': join(dir_icon, 'comment.png'),
     'icon_plus': join(dir_icon, 'plus.png'),
     'icon_minus': join(dir_icon, 'minus.png')}


def load_settings(*args):
    settings_xml = get_settings_xml()
    settings = {}
    if check_xml_ok(settings_xml):
        settingstree = ET.parse(settings_xml)
        settingsroot = settingstree.getroot()
        for setting in settingsroot.find('settings').findall('setting'):
            settings[setting.get('name')] = setting.text

        pools = collections.OrderedDict()
        for pool in settingsroot.find('pools').findall('pool'):
            pools[pool.get('name')] = pool.text
            if not os.path.isdir(pool.text):
                try:
                    os.makedirs(pool.text)
                    msg = 'created missing pools dir at {}'.format(pool.text)
                    write_log(msg)
                except Exception as error:
                    msg = 'Unable to create pools dir at {}; {}'.format(pool.text, error)
                    write_log(msg)

            pools_sorted = collections.OrderedDict(sorted(pools.items()))

        settings['pools'] = pools_sorted
        flags = []
        for flag in settingsroot.find('flags').findall('flag'):
            flags.append(flag.text)

        settings['flags'] = flags
    return settings


def load_hotkeys(*args):
    settings_xml = get_settings_xml()
    hotkeys = collections.OrderedDict()
    if check_xml_ok(settings_xml):
        settingstree = ET.parse(settings_xml)
        settingsroot = settingstree.getroot()
        for setting in settingsroot.find('hotkeys').findall('hotkey'):
            name = setting.get('name')
            hotkeys[name] = setting.text
            hotkeys['{}_ctrl'.format(name)] = setting.get('ctrl')
            hotkeys['{}_shift'.format(name)] = setting.get('shift')
            hotkeys['{}_alt'.format(name)] = setting.get('alt')

    return hotkeys


def get_settings_xml(*args):
    settings_xml = os.path.join(get_tool_private_root(), 'settings.xml')
    if not os.path.isfile(settings_xml):
        try:
            with open(settings_xml, 'w') as look_template:
                template = templates.SETTINGS.format(standard_pool=get_standard_preset_pool())
                look_template.write(template.strip())
                msg = "smartLook settings doesn't exist. created template at: {}".format(settings_xml)
                write_log(msg)
        except:
            msg = 'Failed writing smartLook settings template at: {}'.format(settings_xml)
            write_log(msg)

    check_xml_ok(settings_xml)
    check_xml_values_exist()
    return settings_xml


def check_xml_values_exist(*args):
    default_snapshotdir = os.path.join(get_default_snapshot_root_dir(), 'temp')
    settings = {'tooltips': 'True',
     'release_hotkey_closes_slider': 'True',
     'presetnodes_ignore': 'Viewer,Dot,BackdropNode,StickyNote',
     'hide_disabled_items': 'True',
     'look_icons': 'True',
     'icon_size': '17',
     'snapshotbrowser_root': get_default_snapshot_root_dir(),
     'current_pool': 'standard',
     'current_snapshot_dir': default_snapshotdir,
     'current_snapshot_preview': '',
     'snapshotbrowser_size_custom': '960,500',
     'snapshotbrowser_size_current': '960,500',
     'snapshotbrowser_thumbnail_scrollbar': 'True',
     'snapshot_selection': 'all nodes',
     'snapshot_render_width': '960'}
    for key, value in settings.items():
        check_xml_value_exists('settings', 'setting', 'name', key, value)


def get_default_snapshot_root_dir(*args):
    default_snapshots_root = os.path.join(get_tool_public_root(), 'snapshots')
    if not os.path.isdir(default_snapshots_root):
        try:
            os.makedirs(default_snapshots_root)
        except:
            msg = "Unable to create default snapshot root directory at: '{}'".format(default_snapshots_root)
            show_message_box(None, msg)

    return default_snapshots_root


def load_advanced_settings(*args):
    advanced_settings = os.path.join(get_tool_public_root(), 'advancedsettings.set')
    advanced_settings_default = templates.ADVANCED_SETTINGS_DEFAULT
    if not os.path.isfile(advanced_settings):
        try:
            with open(advanced_settings, 'w') as advset:
                advset.write(advanced_settings_default)
        except Exception as e:
            print e
            write_log('Error writing advanced settings file: {}'.format(e))

    try:
        with open(advanced_settings, 'r') as advset:
            content = advset.read()
    except Exception as e:
        return 'Unable to read advanced settings file. {}'.format(e)

    return content


def parse_advanced_settings(*args):
    advanced_settings_lines = []
    advanced_settings = {}
    vars_line = '-lk'
    advanced_settings_file = os.path.join(get_tool_public_root(), 'advancedsettings.set')
    try:
        with open(advanced_settings_file, 'r') as advset:
            advanced_settings_lines = [ line for line in advset.readlines() if line[:len(vars_line)] == vars_line ]
    except:
        pass

    for line in advanced_settings_lines:
        key = line.split('=')[0]
        key = key.replace(vars_line, '')
        key = key.strip()
        val = line.split('=')[1]
        val = val.strip()
        advanced_settings[key] = val

    return advanced_settings


def get_standard_preset_pool(*args):
    standardpool = os.path.join(get_tool_public_root(), 'standardpool')
    if not os.path.isdir(standardpool):
        os.makedirs(standardpool)
    return standardpool


def check_xml_ok(xml, *args):
    try:
        with open(xml, 'r') as xml_file:
            ET.fromstring(xml_file.read())
        return True
    except:
        message = 'The smartLook settings file seems to be broken. Do you want to reset it now?'
        reset_settings_xml = ask_dialog(message, process_label='reset', color_process='actionButton')
        if reset_settings_xml:
            if os.path.isfile(xml):
                os.remove(xml)
                get_settings_xml()


def show_message_box(window, message, *args):
    msg = QtWidgets.QMessageBox()
    msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg.information(window, 'information', message)


def open_website(url, *args):
    if sys.platform == 'win32':
        os.startfile(url)
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', url])
    else:
        try:
            subprocess.Popen(['xdg-open', url])
        except OSError:
            msg = 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.format(url)
            show_message_box(None, msg)

    return


def set_style_sheet(widget):
    this_dir = os.path.dirname(__file__)
    styles = os.path.join(this_dir, '../', 'styles', 'styles.qss')
    styles = os.path.normpath(styles)
    if os.path.isfile(styles):
        with open(styles) as file_:
            widget.setStyleSheet(file_.read())


def get_topleft_coordinates(*args):
    x = 0
    y = 0
    offset = 200
    for n in nuke.allNodes():
        if n.xpos() < x:
            x = n.xpos()
        if n.ypos() < y:
            y = n.ypos()

    return (x - offset, y - offset)


def create_uid(*args):
    val = '{}_{}'.format(time.time(), random.random())
    return hashlib.md5(val).hexdigest()


def find_looks_group(*args):
    try:
        return [ node for node in nuke.allNodes('Group') if node.knob('looks_group') ][0]
    except IndexError:
        show_message_box(None, "Cannot find 'looks' group in nodegraph.")

    return


def get_installed_root_dir(*args):
    root = os.path.join(os.path.dirname(__file__), '../', '../')
    return os.path.normpath(root)


def get_tool_public_root(*args):
    root = os.path.join(os.path.expanduser('~'), 'cragl', 'smartLook')
    if not os.path.isdir(root):
        try:
            os.makedirs(root)
        except:
            write_log('unable to create open dir')

    return root


def get_tool_private_root(*args):
    root = os.path.join(os.path.expanduser('~'), '.cragl', 'smartLook')
    if not os.path.isdir(root):
        try:
            os.makedirs(root)
        except:
            write_log('unable to create open dir')

    return root


def get_log_file(*args):
    connect_dir = os.path.join(os.path.expanduser('~'), '.cragl', 'connect')
    if not os.path.isdir(connect_dir):
        os.makedirs(connect_dir)
    log_file = os.path.join(connect_dir, 'connectlog.txt')
    if not os.path.isfile(log_file):
        with open(log_file, 'w') as lf:
            log_template = 'connect log\n{}\n'.format('-' * 50)
            lf.write(log_template)
    return log_file


def write_log(text, tool = 'lk', *args):
    with open(get_log_file(), 'a') as file_:
        log_time_format = '%d.%m.%Y %H:%M:%S'
        log_time = time.strftime(log_time_format, time.localtime())
        file_.write('{}: {} {}\n'.format(log_time, tool, text))


def check_web_connection(*args):
    try:
        urllib.urlopen('http://www.cragl.com')
        return True
    except:
        return False


def check_xml_value_exists(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = os.path.join(get_tool_private_root(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = False
    item_found = 0
    for child in root.find(parent).findall(section):
        if child.get(key1) == value1:
            item_found += 1
            if debug:
                print 'smartLook | settings exists: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2)
            return

    if item_found == 0:
        elem = ET.Element(section)
        elem.set(key1, value1)
        if key2 != '':
            elem.set(key2, value2)
        elem.text = text
        root.find(parent).append(elem)
        with open(xml, 'w') as xml:
            prettyprint(root)
            tree.write(xml, encoding='utf-8', xml_declaration=True)
        write_log('settings xml added: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2))


def prettyprint(elem, level = 0):
    i = '\n' + level * '  '
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + '  '
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            prettyprint(elem, level + 1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    elif level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i


def build_hotkeys(*args):
    hotkeys = load_hotkeys()
    hotkeys_build = {}
    settings_xml = get_settings_xml()
    settingstree = ET.parse(settings_xml)
    settingsroot = settingstree.getroot()
    elements = []
    for hotkey in settingsroot.find('hotkeys').findall('hotkey'):
        elements.append(hotkey.get('name'))

    for e in elements:
        hotkey = ''
        if hotkeys['{}_ctrl'.format(e)] == 'True':
            hotkey = 'ctrl+'
        if hotkeys['{}_shift'.format(e)] == 'True':
            hotkey += 'shift+'
        if hotkeys['{}_alt'.format(e)] == 'True':
            hotkey += 'alt+'
        if hotkeys[e] is None:
            hotkeys_build[e] = ''
        else:
            hotkey += hotkeys[e]
            hotkeys_build[e] = hotkey

    return hotkeys_build


def set_hotkeys(*args):
    hotkeys = build_hotkeys()
    hotkeys_dict = {'snapshot browser': 'snapshotbrowser',
     'take snapshot': 'snapshot',
     'looks slider': 'looks_slider',
     'import node | toolset': 'import',
     'export node | toolset': 'export',
     "delete selected node's looks": 'delete_look_knobs',
     'set looks': 'set_looks',
     'resolution slider': 'resolution_slider',
     'settings': 'looks_settings'}
    try:
        for command, hotkey in hotkeys_dict.items():
            command_item = nuke.menu('Nuke').findItem('cragl/smartLook/{}'.format(command))
            command_item.setShortcut(hotkeys[hotkey])

    except KeyError:
        pass


def get_explorer_name(*args):
    if sys.platform == 'darwin':
        return 'finder'
    else:
        return 'explorer'


def open_in_explorer(path, parent = None, *args):
    if not os.path.isdir(path):
        msg = "Unable to open directory '{}'. The path doesn't exist.".format(path)
        show_message_box(parent, msg)
        return
    if platform.system() == 'Windows':
        os.startfile(path)
    elif platform.system() == 'Darwin':
        subprocess.Popen(['open', path])
    else:
        subprocess.Popen(['xdg-open', path])


def build_tree_widget_item(parent, item_name, dirpath, disabled, selected, expanded = False, is_dir = False, enable_drag = False, icon = ''):
    diritem = QtWidgets.QTreeWidgetItem(parent, [item_name])
    diritem.setData(0, QtCore.Qt.UserRole, dirpath)
    if enable_drag == 'False':
        diritem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
    diritem.setExpanded(expanded)
    diritem.setSelected(selected)
    if disabled:
        diritem.setDisabled(True)
    dirpath = os.path.normpath(dirpath)
    if is_dir:
        if icon == '':
            icon = load_icons()['icon_folder_grey']
        diritem.setIcon(0, QtGui.QIcon(icon))
    else:
        diritem.setIcon(0, QtGui.QIcon(load_icons()['icon_nuke']))
    diritem.setData(0, QtCore.Qt.UserRole, dirpath)
    return diritem


def get_image_size(src, *args):
    with open(src, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return (1, 1)
        if imghdr.what(src) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 218765834:
                return (1, 1)
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(src) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(src) == 'jpeg':
            try:
                fhandle.seek(0)
                size = 2
                ftype = 0
                while not 192 <= ftype <= 207:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 255:
                        byte = fhandle.read(1)

                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2

                fhandle.seek(1, 1)
                height, width = struct.unpack('>HH', fhandle.read(4))
            except:
                return (1, 1)

        else:
            return
        return (width, height)


def update_xml(key, value, *args):
    settings_xml = get_settings_xml()
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    for setting in settings_root.find('settings').findall('setting'):
        if setting.get('name') == key:
            setting.text = value

    with open(settings_xml, 'w') as xml:
        prettyprint(settings_root)
        settings_tree.write(xml, encoding='utf-8', xml_declaration=True)


def center_window(window, *args):
    qr = window.frameGeometry()
    cp = QtWidgets.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


def get_connected_nodes(node, *args):
    connected_nodes = []
    ignore_list = ['Viewer']
    nukescripts.clear_selection_recursive()
    node.setSelected(True)
    connected_nodes.append(node)
    nuke.selectConnectedNodes()
    for node in nuke.selectedNodes():
        for dependency in node.dependencies():
            dependency.setSelected(True)

        for dependent in node.dependent():
            dependent.setSelected(True)

    for node in nuke.selectedNodes():
        if node.Class() not in ignore_list:
            connected_nodes.append(node)

    nukescripts.clear_selection_recursive()
    return list(set(connected_nodes))


def load_tooltips(parent, section, *args):
    this_dir = os.path.dirname(__file__)
    tooltips_file = os.path.join(this_dir, '../', 'data', 'tooltips.json')
    tooltips_file = os.path.normpath(tooltips_file)
    if not os.path.isfile(tooltips_file):
        return
    with open(tooltips_file) as json_file:
        ttdata = json.load(json_file)
    for widget in parent.findChildren(QtCore.QObject):
        for t in ttdata[section]:
            if t['tt'] == widget.property('tt'):
                widget.setToolTip('<strong>{}</strong><br />{}'.format(t['ttt'], t['ttc']))


def get_snapshot_dirs(*args):
    snapshot_root = load_settings()['snapshotbrowser_root']
    return [ d for d in os.listdir(snapshot_root) if os.path.isdir(os.path.join(snapshot_root, d)) ]


def set_flag(snapshotbowser, thumbnail_src, color, *args):
    metaxml = '{}.xml'.format(os.path.splitext(thumbnail_src)[0])
    if not os.path.isfile(metaxml):
        create_metaxml(metaxml)
    metatree = ET.parse(metaxml)
    metaroot = metatree.getroot()
    for meta in metaroot.find('metadata').findall('meta'):
        if meta.get('name') == 'flag':
            if color is None:
                meta.text = ''
            else:
                meta.text = '{},{},{}'.format(color[0], color[1], color[2])

    with open(metaxml, 'w') as xml:
        prettyprint(metaroot)
        metatree.write(xml, encoding='utf-8', xml_declaration=True)
    for thumb in snapshotbowser.get_thumbnails_list():
        thumb.set_meta_ui_elements()

    return


def create_metaxml(src, *args):
    with open(src, 'w') as f:
        f.write(templates.SNAPSHOT_META)


def load_metadata(src, *args):
    metadata = {'flag': '',
     'comment': ''}
    meta_xml = '{}.xml'.format(os.path.splitext(src)[0])
    if os.path.isfile(meta_xml):
        try:
            meta_tree = ET.parse(meta_xml)
            meta_root = meta_tree.getroot()
        except:
            msg = "corrupt metaxml, create new one for '{}'".format(meta_xml)
            write_log(msg)
            if os.path.isfile(meta_xml):
                os.remove(meta_xml)
                create_metaxml(meta_xml)
                meta_tree = ET.parse(meta_xml)
                meta_root = meta_tree.getroot()

        for meta in meta_root.find('metadata').findall('meta'):
            meta_val = meta.text
            if not meta_val:
                meta_val = ''
            metadata[meta.get('name')] = meta_val

    return metadata


def get_resolution(*args):
    if nuke.activeViewer():
        return nuke.activeViewer().node()['downrez'].getValue()


def ask_dialog(message, process_label = 'ok', color_process = 'actionButton', cancel_labek = 'cancel'):
    msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, 'QMessageBox.warning()', message, QtWidgets.QMessageBox.NoButton, None)
    msg_box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg_box.setObjectName('msgBox')
    msg_box.raise_()
    process_button = msg_box.addButton(process_label, QtWidgets.QMessageBox.AcceptRole)
    if color_process != '':
        if color_process == 'actionButton':
            color_process = '51, 204, 255, 100'
        style = 'QPushButton {background-color: rgba(%s)}' % color_process
        process_button.setStyleSheet(style)
    process_button.clearFocus()
    msg_box.setFocus()
    msg_box.addButton(cancel_labek, QtWidgets.QMessageBox.RejectRole)
    if msg_box.exec_() == QtWidgets.QMessageBox.AcceptRole:
        return True
    else:
        return False
        return