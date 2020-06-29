# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartCommand_v1.0.0/smartCommand/helper.py
import json
import os
import time
import platform
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
import nuke
if nuke.NUKE_VERSION_MAJOR < 11:
    from PySide import QtGui as QtWidgets
    from PySide import QtGui
    from PySide import QtCore
else:
    from PySide2 import QtWidgets
    from PySide2 import QtCore
    from PySide2 import QtGui
from smartCommand import templates
from smartCommand.info import __product__

def load_icons():
    this_dir = os.path.dirname(__file__)
    dir_icon = os.path.join(this_dir, 'icons')
    dir_icon = os.path.normpath(dir_icon)
    icons = {}
    for file_ in os.listdir(dir_icon):
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


def write_log(text, tool = 'sc'):
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
        for setting in settings_root.find('settings').findall('setting'):
            value = setting.text
            if value == 'True':
                value = True
            elif value == 'False':
                value = False
            settings[setting.get('name')] = value

    return settings


def get_collection_root():
    collection_root = load_settings()['collection_root']
    if not os.path.isdir(collection_root):
        try:
            os.makedirs(collection_root)
        except OSError:
            msg = "Cannot create menu direcory in '{}'. Please set a different path.".format(collection_root)
            nuke.message(msg)

    return collection_root


def get_scriptlets_root():
    scriptlet_root = load_settings()['scriptlets']
    if not os.path.isdir(scriptlet_root):
        try:
            os.makedirs(scriptlet_root)
        except OSError:
            msg = "Cannot create scriptlet direcory in '{}'. Please set a different path.".format(scriptlet_root)
            nuke.message(msg)

    return scriptlet_root


def default_collection_root():
    root = os.path.join(get_tool_root('public'), 'collections')
    if not os.path.isdir(root):
        os.makedirs(root)
    return root


def default_scriptlets_root():
    root = os.path.join(get_tool_root('public'), 'scriptlets')
    if not os.path.isdir(root):
        os.makedirs(root)
    return root


def create_default_data_roots():
    default_collection_root()
    default_scriptlets_root()


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


def check_xml_values_exist():
    for key, value in templates.SETTINGS_DEFAULT_VALUES.items():
        check_xml_value_exists('settings', 'setting', 'name', key, value)


def check_xml_value_exists(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = os.path.join(get_tool_root('private'), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = False
    item_found = 0
    for child in root.find(parent).findall(section):
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


def check_xml_ok(xml):
    try:
        with open(xml, 'r') as xml_file:
            ET.fromstring(xml_file.read())
        return True
    except:
        message = 'The {} settings file seems to be broken. Do you want to reset it now?'.format(__product__)
        reset_settings_xml = ask_dialog(message, process_label='reset', color_process='actionButton')
        if reset_settings_xml:
            if os.path.isfile(xml):
                os.remove(xml)
                get_settings_xml()


def ask_dialog(message, process_label = 'ok', color_process = 'actionButton', cancel_label = 'cancel'):
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
    msg_box.addButton(cancel_label, QtWidgets.QMessageBox.RejectRole)
    if msg_box.exec_() == QtWidgets.QMessageBox.AcceptRole:
        return True
    else:
        return False
        return


def show_path_browser(title):
    dialog = QtWidgets.QFileDialog()
    dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    dialog.setWindowTitle(title)
    dialog.setFileMode(QtWidgets.QFileDialog.Directory)
    dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)
    if dialog.exec_() == QtWidgets.QDialog.Accepted:
        return dialog.selectedFiles()[0]


def update_settings(key, value):
    xml, root, tree = get_xml_elements()
    for setting in root.find('settings').findall('setting'):
        if setting.get('name') == key:
            setting.text = value

    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


def get_menus(all_incl = True, exclude_prefix = '_'):
    menus = []
    if all_incl:
        menus.append('all')
    menu_root = get_collection_root()
    for file_ in os.listdir(menu_root):
        if file_.startswith(exclude_prefix):
            continue
        if file_.endswith('.xml'):
            try:
                xml_path = os.path.join(menu_root, file_)
                xml_name = os.path.splitext(file_)[0]
                with open(xml_path, 'r') as xml_file:
                    ET.fromstring(xml_file.read())
                menus.append(xml_name)
            except ET.ParseError:
                write_log('Skip non well formed menu collection: {}'.format(xml_path))

    return menus


def add_command(collection_name, command_path, color = None, hotkey = None):
    xml = create_collection(collection_name)
    tree = ET.parse(xml)
    root = tree.getroot()
    collection = root.find('collection')
    remove_command_duplicates(collection, command_path)
    command_item = ET.Element('command')
    command_item.text = command_path
    if color:
        command_item.set('color', str(color))
    if hotkey:
        command_item.set('hotkey', sanitize(hotkey))
    collection.insert(0, command_item)
    with open(xml, 'w') as file_:
        prettyprint(root)
        tree.write(file_, encoding='utf-8', xml_declaration=True)


def sanitize(string):
    return re.sub('[^a-zA-Z0-9+]', '', string)


def get_history_xml():
    from smartCommand.constants import HISTORY
    return os.path.join(get_tool_root('private'), '{}.xml'.format(HISTORY))


def swap_commands(xml, path_1, path_2):
    tree = ET.parse(xml)
    root = tree.getroot()
    command_1 = None
    command_2 = None
    index_1 = 0
    index_2 = 0
    index = 0
    for command in root.find('collection').findall('command'):
        if command.text == path_1:
            command_1 = command
            index_1 = index
        elif command.text == path_2:
            command_2 = command
            index_2 = index
        index += 1

    if not all((command is not None for command in [command_1, command_2])):
        raise ValueError('No such sufficient data to swap.')
    root.find('collection').remove(command_2)
    root.find('collection').insert(index_1, command_2)
    root.find('collection').remove(command_1)
    root.find('collection').insert(index_2, command_1)
    with open(xml, 'w') as file_:
        prettyprint(root)
        tree.write(file_, encoding='utf-8', xml_declaration=True)
    return


def get_collection_xml(name):
    collection_root = get_collection_root()
    xml = os.path.join(collection_root, '{}.xml'.format(name))
    if not os.path.isfile(xml):
        raise IOError('No such collection xml: {}'.format(xml))
    return xml


def remove_history_commands(xml, history_max):
    tree = ET.parse(xml)
    root = tree.getroot()
    index = 1
    for command in root.find('collection').findall('command'):
        if index > history_max:
            root.find('collection').remove(command)
        index += 1

    with open(xml, 'w') as file_:
        prettyprint(root)
        tree.write(file_, encoding='utf-8', xml_declaration=True)


def create_collection(collection_name):
    if collection_name == 'history':
        collection_root = get_tool_root('private')
    else:
        collection_root = load_settings()['collection_root']
    xml = os.path.join(collection_root, '{}.xml'.format(collection_name))
    if not os.path.isfile(xml):
        write_log("Create new collection '{}.xml'".format(collection_name))
        with open(xml, 'w') as file_:
            file_.write(templates.COLLECTION.format(collection_name=collection_name))
    return xml


def remove_command_duplicates(menu, command_path):
    equals = [ command_elem for command_elem in menu.findall('command') if command_elem.text == command_path ]
    for element in equals:
        menu.remove(element)

    return menu


def get_command_object(path):
    command = nuke.menu('Nuke').findItem(path)
    if not command:
        return None
    else:
        return command


def get_next_element(list_, current):
    try:
        return list_[list_.index(current) + 1]
    except IndexError:
        return list_[0]


def get_previous_element(list_, current):
    try:
        return list_[list_.index(current) - 1]
    except IndexError:
        return list_[len(list_)]


def update_command(xml, path, key, value):
    if not os.path.isfile(xml):
        raise IOError('No such collection file: {}'.format(xml))
    tree = ET.parse(xml)
    root = tree.getroot()
    for command in root.find('collection').findall('command'):
        if command.text == path:
            command.set(key, value)
            with open(xml, 'w') as xml:
                prettyprint(root)
                tree.write(xml, encoding='utf-8', xml_declaration=True)
            break
    else:
        raise ValueError('No such command path: {}'.format(path))


def remove_command(xml, path):
    if not os.path.isfile(xml):
        raise IOError('No such collection xml: {}'.format(xml))
    tree = ET.parse(xml)
    root = tree.getroot()
    for command in root.find('collection').findall('command'):
        if command.text == path:
            root.find('collection').remove(command)
            with open(xml, 'w') as xml:
                prettyprint(root)
                tree.write(xml, encoding='utf-8', xml_declaration=True)
            break
    else:
        raise ValueError('No such command path: {}'.format(path))


def get_basename(path):
    out = path
    sep = '/'
    if sep in path:
        out = path.split(sep)[-1]
    return out


def get_all_hotkeys():
    hotkey_commands = {}
    collection_root = get_collection_root()
    for collection in get_menus(all_incl=False):
        xml = '{}.xml'.format(collection)
        tree = ET.parse(os.path.join(collection_root, xml))
        root = tree.getroot()
        for command in root.find('collection').findall('command'):
            if command.get('hotkey'):
                hotkey_commands[command.get('hotkey')] = [command.text, xml]

    return hotkey_commands


def initialize_hotkeys():
    hotkey_commands = get_all_hotkeys()
    for hotkey, command in hotkey_commands.items():
        path = command[0]
        command_item = nuke.menu('Nuke').findItem(path)
        if command_item:
            command_item.setShortcut(hotkey)


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

    for widget in parent.findChildren(QtCore.QObject):
        for t in ttdata[section]:
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
            from smartCommand import dialogs
            dialogs.show_message_box(None, msg)

    return


def get_basename(path, extension = False):
    basename = os.path.basename(path)
    if extension:
        return basename
    return os.path.splitext(basename)[0]


def get_module_docstring(path):
    compile_ = compile(open(path).read(), path, 'exec')
    if compile_.co_consts and isinstance(compile_.co_consts[0], basestring):
        docstring = compile_.co_consts[0]
    else:
        docstring = None
    return docstring


def center_window(window):
    geometry = window.frameGeometry()
    centerpoint = QtWidgets.QDesktopWidget().availableGeometry().center()
    geometry.moveCenter(centerpoint)
    window.move(geometry.topLeft())


def get_cursor_position():
    return QtGui.QCursor().pos()