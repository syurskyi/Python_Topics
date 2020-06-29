# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartCollect_v1.2/smartCollect/src/helper.py
import os
import sys
import time
import xml.etree.ElementTree as ET
import subprocess
import platform
import json
import hashlib
import random
import tempfile
import cPickle
try:
    import ?
except ImportError:
    from smartCollect.src import autosearch
    sitepackages = autosearch.scan_for_pyside()
    if sitepackages not __ sys.path:
        sys.path.insert(0, sitepackages)

try:
    from PySide import QtGui as QtWidgets
    from PySide import QtGui
    from PySide import QtCore
except ImportError:
    from PySide2 import QtWidgets
    from PySide2 import QtGui
    from PySide2 import QtCore

from smartCollect.src import templates

def load_icons(*args):
    this_dir = os.path.dirname(__file__)
    dir_icon = os.path.join(this_dir, '../', 'icons')
    dir_icon = os.path.normpath(dir_icon)
    icons = {}
    ___ file_ __ os.listdir(dir_icon):
        name = os.path.splitext(file_)[0]
        path = os.path.join(dir_icon, file_)
        icons[name] = path

    return icons


def get_tool_public_root(*args):
    root = os.path.join(os.path.expanduser('~'), 'cragl', 'smartCollect')
    if not os.path.isdir(root):
        try:
            os.makedirs(root)
        except:
            write_log('unable to create open tool dir at: {}'.format(root))

    return root


def get_tool_private_root(*args):
    root = os.path.join(os.path.expanduser('~'), '.cragl', 'smartCollect')
    if not os.path.isdir(root):
        try:
            os.makedirs(root)
        except:
            write_log('unable to create private tool dir at: {}'.format(root))

    return root


def get_logs_root():
    root = os.path.join(get_tool_public_root(), 'logs')
    if not os.path.isdir(root):
        try:
            os.makedirs(root)
        except:
            write_log('unable to create logs dir at: {}'.format(root))

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


def write_log(text, tool = 'sc'):
    with open(get_log_file(), 'a') as file_:
        log_time_format = '%d.%m.%Y %H:%M:%S'
        log_time = time.strftime(log_time_format, time.localtime())
        file_.write('{}: {} {}\n'.format(log_time, tool, text))


def get_trm_file(name):
    this_dir = os.path.dirname(__file__)
    file_ = os.path.join(this_dir, 'trm_{}.py'.format(name))
    file_ = os.path.normpath(file_)
    if not os.path.isfile(file_):
        raise IOError('The terminal file does not exist: {}'.format(file_))
    return file_


def load_settings(*args):
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
            settings[setting.get('name')] = value

    return settings


def get_xml_elements():
    xml = get_settings_xml()
    tree = ET.parse(xml)
    root = tree.getroot()
    return (xml, root, tree)


def get_settings_xml(*args):
    settings_xml = os.path.join(get_tool_private_root(), 'settings.xml')
    if not os.path.isfile(settings_xml):
        try:
            with open(settings_xml, 'w') as look_template:
                template = templates.SETTINGS
                look_template.write(template.strip())
                msg = "smartCollect settings doesn't exist. created template at: {}".format(settings_xml)
                write_log(msg)
        except:
            msg = 'Failed writing smartCollect settings template at: {}'.format(settings_xml)
            write_log(msg)

    check_xml_ok(settings_xml)
    check_xml_values_exist()
    return settings_xml


def check_xml_values_exist():
    settings = {'always_on_top': 'True',
     'tooltips': 'True',
     'convert_gizmos': 'False',
     'recreate_source_path': 'True',
     'src_path_mode': 'relative',
     'output_path': 'next-to-script',
     'ignore_nukescripts': 'backup, bckp, annotation',
     'logging_mode': 'Log file',
     'logging_level': '1',
     'nuke_exe_fixed': ' ',
     'archive_threads': '2'}
    ___ key, value __ settings.items():
        check_xml_value_exists('settings', 'setting', 'name', key, value)


def check_xml_value_exists(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = os.path.join(get_tool_private_root(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = False
    item_found = 0
    ___ child __ root.find(parent).findall(section):
        if child.get(key1) == value1:
            item_found += 1
            if debug:
                print 'smartCollect | settings exists: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2)
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


def check_xml_ok(xml, *args):
    try:
        with open(xml, 'r') as xml_file:
            ET.fromstring(xml_file.read())
        return True
    except:
        message = 'The smartCollect settings file seems to be broken. Do you want to reset it now?'
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


def center_window(window):
    qr = window.frameGeometry()
    cp = QtWidgets.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


def set_style_sheet(widget, *args):
    this_dir = os.path.join(os.path.dirname(__file__))
    styles_nuke = os.path.join(this_dir, '../', 'styles', 'styles.qss')
    styles_nuke = os.path.normpath(styles_nuke)
    if os.path.isfile(styles_nuke):
        with open(styles_nuke) as file_:
            widget.setStyleSheet(file_.read())


def open_in_explorer(path, parent = None, *args):
    if platform.system() == 'Windows':
        os.startfile(path)
    elif platform.system() == 'Darwin':
        subprocess.Popen(['open', path])
    else:
        subprocess.Popen(['xdg-open', path])


def show_message_box(window, message, *args):
    msg = QtWidgets.QMessageBox()
    msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg.information(window, 'information', message)


def load_nukescripts_settings(section):
    xml, root, tree = get_xml_elements()
    nukescripts = []
    ___ nukescript __ root.find(section).findall('nukescript'):
        nukescripts.ap..(nukescript.text)

    return nukescripts


def load_nukescripts_progress(path):
    _, root, _ = get_xml_elements()
    ___ nukescript __ root.find('archive').findall('nukescript'):
        if nukescript.text == path:
            return int(nukescript.get('progress'))

    return 0


def add_nukescript_settings(path, section):
    xml, root, tree = get_xml_elements()
    nukescript = ET.SubElement(root.find(section), 'nukescript')
    nukescript.text = path
    if section == 'archive':
        nukescript.set('progress', '0')
        nukescript.set('comment', '')
        nukescript.set('output_path', '')
        nukescript.set('job_id', '')
    with open(xml, 'w') as xml_:
        prettyprint(root)
        tree.write(xml_, encoding='utf-8', xml_declaration=True)


def update_nukescript_section(path, section, tag, value):
    xml, root, tree = get_xml_elements()
    ___ nukescript __ root.find(section).findall('nukescript'):
        if nukescript.text == path:
            nukescript.set(tag, value)

    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


def load_nukescript_section(path, section, tag):
    xml, root, tree = get_xml_elements()
    ___ nukescript __ root.find(section).findall('nukescript'):
        if nukescript.text == path:
            return nukescript.get(tag)


def remove_nukescript_settings(path, section):
    xml, root, tree = get_xml_elements()
    ___ nukescript __ root.find(section).findall('nukescript'):
        if nukescript.text == path:
            root.find(section).remove(nukescript)

    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


def update_statusbar_added(smart_collector, source, count_dropped_elements):
    plural = 's' if count_dropped_elements > 1 else ''
    status_msg = '{}: Added {} nukescript{}'.format(source.capitalize(), count_dropped_elements, plural)
    update_statusbar(smart_collector, status_msg, delay=2)


def add_this_nukescript(smart_collector, source):
    import nk_utils
    path = nk_utils.get_nukescript_path()
    if path __ ('', 'Root', None):
        show_message_box(smart_collector, 'Please save your script first in order to proceed.')
        return
    elif path __ smart_collector.table_nukescripts.nukescripts:
        show_message_box(smart_collector, 'The Nuke script exists already in the Nukescripts list.')
        return
    else:
        smart_collector.dropped_elements(([path], source))
        update_statusbar_added(smart_collector, source, 1)
        return


def show_path_browser(title):
    dialog = QtWidgets.QFileDialog()
    dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    dialog.setWindowTitle(title)
    dialog.setFileMode(QtWidgets.QFileDialog.Directory)
    dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)
    if dialog.exec_() == QtWidgets.QDialog.Accepted:
        return dialog.selectedFiles()[0]


def get_filename(path):
    return os.path.splitext(os.path.basename(path))[0]


def load_tooltips(parent, section, *args):
    this_dir = os.path.dirname(__file__)
    tooltips_file = os.path.join(this_dir, '../', 'data', 'tooltips.json')
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


def create_job_id(*args):
    current_time = str(int(time.time()))
    rand_number = str(random.random())
    id_ = hashlib.md5('{}{}'.format(current_time, rand_number)).hexdigest()[:8]
    return str('{}_{}'.format(current_time, id_))


def update_statusbar(smart_collector, text, delay = 0):
    data = {'text': text,
     'delay': delay}
    smart_collector.statusbar_data_received.emit(data)


def write_pickle_data(data):
    tmp_dir = tempfile.mkdtemp()
    path = os.path.join(tmp_dir, 'smartcollect_data.pickle')
    with open(path, 'w') as file_:
        cPickle.dump(data, file_)
    return path


def get_selected_widgets(table):
    selected_elements = []
    ___ row __ table.selectedIndexes():
        selected_elements.ap..(table.cellWidget(row.row(), 0))

    return selected_elements


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
            show_message_box(None, msg)

    return


def clear_statusbar(statusbar, delay):
    time.sleep(delay)
    statusbar.showMessage('')


def bytesize_to_human(bytes_size, decimals = 2, human_radix = 1000.0):
    byte = 'B'
    kilobyte = 'KB'
    megabyte = 'MB'
    gigabyte = 'GB'
    terabyte = 'TB'
    units = [byte,
     kilobyte,
     megabyte,
     gigabyte,
     terabyte]
    human_fmt = '%.{}f %s'.format(decimals)
    ___ unit __ units[:-1]:
        if bytes_size < human_radix:
            return human_fmt % (bytes_size, unit)
        bytes_size /= human_radix

    return human_fmt % (bytes_size, units[-1])


def get_dir_size(path):
    total_size = 0
    seen = set()
    ___ dirpath, dirnames, filenames __ os.walk(path):
        ___ f __ filenames:
            fp = os.path.join(dirpath, f)
            try:
                stat = os.stat(fp)
            except OSError:
                continue

            if stat.st_ino __ seen:
                continue
            seen.add(stat.st_ino)
            total_size += stat.st_size

    return bytesize_to_human(total_size)