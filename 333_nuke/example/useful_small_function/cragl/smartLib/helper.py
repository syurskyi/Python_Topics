# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartLib_v4.0/smartLib/src/helper.py
import os
import sys
import errno
import shutil
import subprocess
import xml.etree.ElementTree as ET
import collections
import urllib
import time
import datetime
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
import osl
import templates
DIR_DOCS = '.docs'
IMAGE_EXT = ['exr',
 'cin',
 'dpx',
 'hdr',
 'jpeg',
 'pic',
 'png',
 'sgi',
 'targa',
 'tif',
 'xpm',
 'yuv',
 'jpg',
 'tiff']
VIDEO_EXT = ['mov',
 'avi',
 'mpg',
 'mpeg',
 'wmv',
 'flv',
 'm4v',
 'mp4']
IGNORE = ['.DS_Store', '.nk~', '.autosave']

def load_icons():
    this_dir = os.path.dirname(__file__)
    dir_icon = os.path.join(this_dir, '../', 'icons')
    dir_icon = os.path.normpath(dir_icon)
    join = os.path.join
    return {'icon_logo': join(dir_icon, 'logo.png'),
     'icon_folder': join(dir_icon, 'folder.png'),
     'icon_nuke': join(dir_icon, 'nuke.png'),
     'icon_img': join(dir_icon, 'img.jpg'),
     'icon_video': join(dir_icon, 'video.jpg'),
     'icon_copy': join(dir_icon, 'copy.png'),
     'icon_cut': join(dir_icon, 'cut.png'),
     'icon_paste': join(dir_icon, 'paste.png'),
     'icon_delete': join(dir_icon, 'delete.png'),
     'icon_reveal': join(dir_icon, 'reveal.jpg'),
     'icon_home': join(dir_icon, 'home.png'),
     'icon_dirup': join(dir_icon, 'dirup.png'),
     'icon_doc': join(dir_icon, 'doc.png'),
     'icon_system': join(dir_icon, 'system.png'),
     'icon_system_inactive': join(dir_icon, 'system_inactive.png'),
     'icon_shot': join(dir_icon, 'shot.png'),
     'icon_shot_inactive': join(dir_icon, 'shot_inactive.png'),
     'icon_preview_default': join(dir_icon, 'preview_default.png'),
     'icon_notes': join(dir_icon, 'notes.png'),
     'icon_notes_inactive': join(dir_icon, 'notes_inactive.png'),
     'icon_write': join(dir_icon, 'write.png'),
     'icon_search': join(dir_icon, 'search.png'),
     'icon_status_done': join(dir_icon, 'status_done.png'),
     'icon_status_progress': join(dir_icon, 'status_progress.png'),
     'icon_status_not_started': join(dir_icon, 'status_not_started.png'),
     'icon_insert': join(dir_icon, 'insert.png'),
     'icon_read': join(dir_icon, 'read.png'),
     'icon_pin_pinned': join(dir_icon, 'pin_unpinned.png'),
     'icon_pin_unpinned': join(dir_icon, 'pin_pinned.png'),
     'about': join(dir_icon, 'about.jpg')}


def check_web_connection():
    try:
        urllib.urlopen('http://www.cragl.com')
        return True
    except:
        return False


def show_message_box(window, message):
    QtWidgets.QMessageBox().information(window, 'information', message)


def message_confirm_overwrite(src, is_file = True):
    if is_file:
        item = 'File'
    else:
        item = 'Directory'
    message = "{} '{}' already exists.\nDo you want to overwrite it?".format(item, src)
    overwrite = ask_dialog(message=message, process_button_text='Overwrite', color_process='45,0,0', cancel_button_text='Cancel')
    return overwrite


def get_smartlib_private_dir():
    dir_ = os.path.join(os.path.expanduser('~'), '.cragl', 'smartLib')
    if not os.path.isdir(dir_):
        os.makedirs(dir_)
    return dir_


def get_smartlib_public_dir():
    dir_ = os.path.join(os.path.expanduser('~'), 'cragl', 'smartLib')
    if not os.path.isdir(dir_):
        os.makedirs(dir_)
    return dir_


def get_dir_templates():
    dir_ = os.path.join(get_smartlib_public_dir(), 'shot_templates')
    if not os.path.isdir(dir_):
        os.makedirs(dir_)
    return dir_


def set_item_icon(listwidget_item, name, is_dir, is_render_dir = False, is_footage_dir = False, icons = None):
    if is_dir:
        try:
            listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_folder']))
            if is_render_dir:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_write']))
            elif is_footage_dir:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_read']))
        except:
            listwidget_item.setIcon(QtGui.QIcon(icons['icon_folder']))
            if is_render_dir:
                listwidget_item.setIcon(QtGui.QIcon(icons['icon_write']))
            elif is_footage_dir:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_read']))

    if '.' in name:
        ext = name.split('.')[1]
        if ext == 'nk':
            try:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_nuke']))
            except:
                listwidget_item.setIcon(QtGui.QIcon(icons['icon_nuke']))

        elif ext.lower() in IMAGE_EXT:
            try:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_img']))
            except:
                listwidget_item.setIcon(QtGui.QIcon(icons['icon_img']))

        elif ext in VIDEO_EXT:
            try:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_video']))
            except:
                listwidget_item.setIcon(QtGui.QIcon(icons['icon_video']))

        else:
            try:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_doc']))
            except:
                listwidget_item.setIcon(QtGui.QIcon(icons['icon_doc']))


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


def get_smartLib_installed_root():
    this_dir = os.path.dirname(__file__)
    root = os.path.join(this_dir, '../', '../')
    return os.path.normpath(root)


def write_log(text, tool = 'sl'):
    with open(get_log_file(), 'a') as file_:
        log_time_format = '%d.%m.%Y %H:%M:%S'
        log_time = time.strftime(log_time_format, time.localtime())
        file_.write('{}: {} {}\n'.format(log_time, tool, text))


def _copy(src, dst):
    dst = os.path.join(dst, os.path.basename(src))
    if os.path.isdir(src):
        try:
            shutil.copytree(src, dst)
        except Exception as error:
            raise OSError(error)

    elif os.path.isfile(src):
        if not os.path.isdir(os.path.dirname(dst)):
            os.makedirs(os.path.dirname(dst))
        try:
            shutil.copy(src, dst)
        except Exception as error:
            raise OSError(error)


def remove(path):
    if os.path.isfile(path):
        try:
            os.remove(path)
            return True
        except:
            return False

    elif os.path.isdir(path):
        try:
            shutil.rmtree(path)
            return True
        except:
            return False


def set_style_sheet(widget):
    this_dir = os.path.dirname(__file__)
    styles = os.path.join(this_dir, '../', 'styles', 'nuke.qss')
    styles = os.path.normpath(styles)
    if os.path.isfile(styles):
        with open(styles) as file_:
            widget.setStyleSheet(file_.read())


def reveal_in_finder(path, open_file = False):
    path = os.path.normpath(path)
    try:
        if sys.platform == 'linux2':
            if open_file:
                nuke.scriptOpen(path)
                return
            if os.path.isfile(path):
                path = os.path.dirname(path)
            subprocess.Popen(['xdg-open', path])
        elif sys.platform == 'darwin':
            if open_file:
                subprocess.call(['open', '--', path])
            else:
                subprocess.call(['open', '-R', path])
        elif sys.platform == 'windows' or sys.platform == 'win32':
            if ':' in path:
                if ':{}'.format(os.path.sep) not in path:
                    path = path.replace(':', ':{}'.format(os.path.sep))
            if os.path.isfile(path):
                path = os.path.dirname(path)
            subprocess.call(['explorer', path])
    except:
        message('Failed opening: {}'.format(path))


def get_home_dir():
    return os.path.expanduser('~')


def load_bookmarks():
    bookmarklist = []
    bookmarklist.append('bookmarks')
    bookmarklist.append('add to bookmarks')
    bookmarklist.append('delete from bookmarks')
    bookmarklist.append('--------------------')
    settingsXML = get_settings_xml()
    settings_tree = ET.parse(settingsXML)
    settings_root = settings_tree.getroot()
    for child in settings_root.find('bookmarks').findall('bookmark'):
        bookmarklist.append(child.text)

    return bookmarklist


def get_settings_xml():
    settings_xml = os.path.join(get_smartlib_private_dir(), 'settings.xml')
    if not os.path.isfile(settings_xml):
        try:
            with open(settings_xml, 'w') as xml:
                template = templates.SETTINGS.format(user_home_dir=os.path.expanduser('~'))
                xml.write(template.strip())
        except Exception as error:
            write_log("Couldn't write settings xml template. {}".format(error))

    check_xml_values_exist()
    check_status_exists()
    check_xml_ok(settings_xml)
    return settings_xml


def check_xml_values_exist():
    settings = {'show_system': 'True',
     'show_shot': 'True',
     'show_notes': 'True',
     'hidden_files': 'False',
     'force_create_render_dir': 'True',
     'padding': '4',
     'ext': 'exr',
     'print_path': '',
     'padding_delimiter': '.',
     'collapse_image_sequences': 'True',
     'shot_enable_drag': 'False',
     'shot_thumb_gamma': '1.0',
     'nukescripts_ignore': 'backup, bckp, annotation',
     'pin': 'True',
     'default_w': '1920',
     'default_h': '1080',
     'default_fps': '24',
     'default_pixel_aspect': '1',
     'user': ' ',
     'tooltips': 'True'}
    for key, value in settings.items():
        check_xml_value_exists('settings', 'setting', 'name', key, value)

    navigations = {'system': '',
     'project': '',
     'shot': ''}
    for key, value in navigations.items():
        check_xml_value_exists('navigation', 'navi', 'name', key, value)

    check_xml_parent_val_exists('templateDefaults')


def check_xml_value_exists(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = os.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = False
    item_found = 0
    for child in root.find(parent).findall(section):
        if child.get(key1) == value1:
            item_found += 1
            if debug:
                print 'smartLib | settings exists: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2)
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


def check_xml_parent_val_exists(section):
    xml = os.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    if root.find(section) is None:
        elem = ET.Element(section)
        root.append(elem)
        with open(xml, 'w') as xml:
            prettyprint(root)
            tree.write(xml, encoding='utf-8', xml_declaration=True)
        write_log('settings xml added: {}'.format(section))
    return


def check_status_exists():
    status_found = 0
    xml = os.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    if len(root.find('statuslist')):
        for child in root.find('statuslist').findall('status'):
            status_found += 1

    if status_found == 0:
        default_status = templates.DEFAULT_STATUS
        if root.find('statuslist') is None:
            statuslist_elem = ET.Element('statuslist')
            root.append(statuslist_elem)
        for key in sorted(default_status):
            status_elem = ET.Element('status')
            status_elem.set('z-index', key)
            status_elem.set('color', default_status[key][0])
            status_elem.text = default_status[key][1]
            status_elem.set('default', default_status[key][2])
            root.find('statuslist').append(status_elem)

        with open(xml, 'w') as xml:
            prettyprint(root)
            tree.write(xml, encoding='utf-8', xml_declaration=True)
    return


def write_template_default(projectpath, template):
    xml = os.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    elem_exists = False
    for project in root.find('templateDefaults').findall('project'):
        if project.get('path') == projectpath:
            elem_exists = True
            project.text = template
            break

    if not elem_exists:
        projectelement = ET.Element('project')
        projectelement.set('path', projectpath)
        projectelement.text = template
        root.find('templateDefaults').append(projectelement)
    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


def load_template_default(project_path):
    xml = os.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    for project in root.find('templateDefaults').findall('project'):
        if project.get('path') == project_path:
            return project.text

    return ''


def load_status_list():
    xml = os.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    status_list = {}
    if len(root.find('statuslist')):
        for child in root.find('statuslist').findall('status'):
            data = [child.get('color'), child.text, child.get('default')]
            status_list[child.get('z-index')] = data

    return status_list


def load_default_status():
    settings_xml = get_settings_xml()
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    with open(settings_xml, 'r'):
        for child in settings_root.find('statuslist').findall('status'):
            if child.get('default') == '1':
                return [child.text, child.get('color')]


def ask_dialog(message = '', process_button_text = '', color_process = '', cancel_button_text = ''):
    msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, 'QMessageBox.warning()', message, QtWidgets.QMessageBox.NoButton, None)
    msg_box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg_box.setObjectName('msgBox')
    msg_box.raise_()
    process_button = msg_box.addButton(process_button_text, QtWidgets.QMessageBox.AcceptRole)
    if color_process != '':
        if color_process == 'actionButton':
            color_process = '51, 204, 255, 100'
        style = 'QPushButton {background-color: rgba(%s)}' % color_process
        process_button.setStyleSheet(style)
    process_button.clearFocus()
    msg_box.setFocus()
    msg_box.addButton(cancel_button_text, QtWidgets.QMessageBox.RejectRole)
    if msg_box.exec_() == QtWidgets.QMessageBox.AcceptRole:
        return True
    else:
        return False
        return


def check_xml_ok(xml):
    try:
        with open(xml, 'r') as xml_file:
            ET.fromstring(xml_file.read())
        return True
    except:
        if xml == get_settings_xml():
            message = 'The smartLib settings file seems to be broken. Do you want to reset it now?'
            write_log('smartLib settings file broken.')
        else:
            meta_xml = os.path.join(os.path.dirname(xml), '../')
            meta_xml = os.path.normpath(meta_xml)
            message = 'The meta xml for {} file seems to be broken. Do you want to reset it now?'.format(meta_xml)
            write_log('The meta xml for {} file broken.'.format(meta_xml))
        reset_xml = ask_dialog(message=message, process_button_text='reset', color_process='actionButton', cancel_button_text='Cancel')
        if reset_xml:
            if os.path.isfile(xml):
                os.remove(xml)
                get_settings_xml()
        return False


def load_settings():
    settings_xml = get_settings_xml()
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    settings = {}
    for setting in settings_root.find('settings').findall('setting'):
        if setting.text:
            settings[setting.get('name')] = setting.text
        else:
            settings[setting.get('name')] = ''

    for navi in settings_root.find('navigation').findall('navi'):
        if navi.text and os.path.isdir(navi.text):
            settings['current_{}'.format(navi.get('name'))] = navi.text
        else:
            settings['current_{}'.format(navi.get('name'))] = ''

    return settings


def center_window(window):
    qr = window.frameGeometry()
    cp = QtWidgets.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


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


def write_xml(xml, root, tree):
    prettyprint(root)
    tree.write(xml, encoding='utf-8', xml_declaration=True)
    return True


def collect_nuke_scripts_no_ignore(path):
    nuke_scripts = collections.OrderedDict()
    ignore_list = load_settings()['nukescripts_ignore']
    if ignore_list:
        ignore_list = ignore_list.split(',')
    else:
        ignore_list = []
    ignore_list.extend(['.nk~', '.autosave'])
    for root, dirs, files in os.walk(path):
        for name in files:
            file = os.path.join(root, name)
            if os.path.splitext(file)[1] == '.nk':
                ignore_count = 0
                for ignore in ignore_list:
                    if ignore.strip() in file:
                        ignore_count += 1

                if ignore_count == 0:
                    nuke_script = os.path.basename(file)
                    nuke_script_name = os.path.splitext(nuke_script)[0]
                    nuke_scripts[file] = nuke_script_name

    nuke_scripts = sorted(nuke_scripts.items(), key=lambda x: x[1])
    nuke_scripts.reverse()
    return nuke_scripts


def open_nukescript(name, nuke_scripts):
    for script in nuke_scripts:
        if script[1] == name:
            nuke.scriptOpen(script[0])


def write_location(location, value):
    settings_xml = get_settings_xml()
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    with open(settings_xml, 'r'):
        for child in settings_root.find('navigation').findall('navi'):
            if child.get('name') == location:
                child.text = value

    with open(settings_xml, 'w') as xml:
        prettyprint(settings_root)
        settings_tree.write(xml, encoding='utf-8', xml_declaration=True)


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


def set_preview_image(delete_nodes = True):
    if not osl.cl():
        return
    preview_image_width = 500
    try:
        sel = nuke.selectedNode()
    except:
        nuke.message('Please select a node to create a preview image.')
        return

    if sel.Class() == 'Viewer':
        return
    if get_script_name() == '' or get_script_name() == 'Root':
        nuke.message("Your nukescript hasn't been saved, yet. Please save your script first.")
        return
    root_dir_docs = get_dir_docs_current_nukescript()
    if root_dir_docs == '':
        return
    reformat = nuke.createNode('Reformat', inpanel=False)
    reformat.setInput(0, sel)
    reformat.setXYpos(sel.xpos(), sel.ypos() + 50)
    reformat['type'].setValue('to box')
    reformat['box_width'].setValue(preview_image_width)
    gamma = nuke.createNode('Gamma')
    gamma.setInput(0, reformat)
    gamma.setXYpos(sel.xpos(), reformat.ypos() + 50)
    gamma['value'].setValue(float(load_settings()['shot_thumb_gamma']))
    write = nuke.createNode('Write', inpanel=False)
    write.setInput(0, gamma)
    write.setXYpos(gamma.xpos(), gamma.ypos() + 50)
    write.knob('name').setValue('create preview')
    write.knob('use_limit').setValue(True)
    write.knob('first').setValue(nuke.frame())
    write.knob('last').setValue(nuke.frame())
    write.knob('file_type').setValue('jpg')
    preview_path = os.path.join(root_dir_docs, '__preview.jpg')
    preview_path = preview_path.replace(os.path.sep, '/')
    write.knob('file').setValue(preview_path)
    nuke.execute(write, nuke.frame(), nuke.frame())
    if delete_nodes:
        nuke.delete(reformat)
        nuke.delete(gamma)
        nuke.delete(write)


def get_dir_docs_current_nukescript():
    up_level = 7
    current_script_dir = os.path.dirname(nuke.root().name())
    if current_script_dir == 'Root' or current_script_dir == '':
        return ''
    root_dir_docs = ''
    dirs = []
    dirs.append(os.path.normpath(current_script_dir))
    for i in range(up_level - 1):
        dir = os.path.normpath(os.path.abspath(os.path.join(os.path.dirname(dirs[i - 1]))))
        dirs.append(dir)

    for i in range(up_level - 1):
        dir_content = os.listdir(dirs[i])
        if DIR_DOCS in dir_content:
            root_dir_docs = os.path.normpath(os.path.join(dirs[i], DIR_DOCS))
            return root_dir_docs

    if root_dir_docs == '':
        write_log("Wasn't able to find the _docs directory for the shot. Recursion depth for the shot is too high.")
        return


def get_meta_xml(path):
    if os.path.isdir(path):
        metaxml = os.path.join(path, DIR_DOCS, 'meta.xml')
        try:
            if not os.path.isdir(os.path.dirname(metaxml)):
                os.makedirs(os.path.dirname(metaxml))
        except:
            return

        if not os.path.isfile(metaxml):
            try:
                with open(metaxml, 'w') as file_:
                    template = templates.META
                    file_.write(template.strip())
            except:
                write_log("Couldn't write meta xml template at: {}".format(metaxml))

        check_meta_xml_values_exist(metaxml)
        return metaxml


def check_meta_xml_values_exist(metaxml):
    check_meta_xml_value_exists(metaxml, 'notes', 'note', 'name', 'footagepath', ' ', key2='loc', value2='local')
    check_meta_xml_value_exists(metaxml, 'notes', 'note', 'name', 'user', ' ')


def check_meta_xml_value_exists(metaxml_path, parent, section, key1, value1, text, key2 = '', value2 = ''):
    tree = ET.parse(metaxml_path)
    root = tree.getroot()
    debug = False
    item_found = 0
    for child in root.find(parent).findall(section):
        if child.get(key1) == value1:
            item_found += 1
            if debug:
                print 'smartLib | metaxml exists: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2)
            return

    if item_found == 0:
        elem = ET.Element(section)
        elem.set(key1, value1)
        if key2 != '':
            elem.set(key2, value2)
        elem.text = text
        root.find(parent).append(elem)
        with open(metaxml_path, 'w') as xml:
            prettyprint(root)
            tree.write(xml, encoding='utf-8', xml_declaration=True)
        write_log('settings metaxml added: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2))


def message(message):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg_box.setText(message)
    msg_box.raise_()
    msg_box.exec_()


def dialog_set_preview_image(smartlib):
    dialog = QtWidgets.QFileDialog()
    dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    dialog.setWindowIcon(QtGui.QIcon(load_icons()['icon_logo']))
    dialog.setWindowTitle('choose image file')
    dialog.setNameFilter('jpg files(*.jpg)')
    if dialog.exec_() == QtWidgets.QDialog.Accepted:
        input_image = dialog.selectedFiles()[0]
        dest = os.path.join(smartlib.current_shot_widget.path, DIR_DOCS, '__preview.jpg')
        if not os.path.isdir(os.path.dirname(dest)):
            os.makedirs(os.path.dirname(dest))
        save_image_scaled(input_image, dest)
        smartlib.current_shot_widget.refresh()
        current_project = load_settings()['current_project']
        smartlib.table_current_project.load_shots(current_project)


def save_image_scaled(src, dest):
    img = QtGui.QImage(src)
    try:
        pixmap = QtGui.QPixmap(img.scaledToWidth(500))
        pixmap.save(dest)
        return True
    except:
        write_log('Cannot create image scaled.')
        return False


def get_script_name():
    script = nuke.root().name()
    script_name = os.path.basename(script)
    return os.path.splitext(script_name)[0]


def setup_renderpath():
    dir_docs_current_nukescript = get_dir_docs_current_nukescript()
    if dir_docs_current_nukescript in (None, ''):
        return None
    else:
        project_root = os.path.dirname(dir_docs_current_nukescript)
        metaxml = os.path.join(dir_docs_current_nukescript, 'meta.xml')
        script_name = get_script_name()
        if os.path.isfile(metaxml) and script_name not in ('', 'Root'):
            meta_tree = ET.parse(metaxml)
            meta_root = meta_tree.getroot()
            for child in meta_root.find('notes').findall('note'):
                if child.get('name') == 'renderpath':
                    try:
                        if child.text.strip() != '':
                            if child.get('loc') == 'global':
                                render_dir = '{}'.format(child.text)
                            else:
                                render_dir = '{}{}'.format(project_root, child.text)
                            render_file = '{}{}%0{}d.{}'.format(script_name, load_settings()['padding_delimiter'], load_settings()['padding'], load_settings()['ext'])
                            render_full_path = os.path.join(render_dir, script_name, render_file)
                            render_dir = os.path.dirname(render_full_path)
                            if not os.path.isdir(render_dir):
                                os.makedirs(render_dir)
                            nuke.thisNode()['file'].setValue(render_full_path)
                            nuke.thisNode()['file_type'].setValue(load_settings()['ext'])
                    except:
                        pass

        return None


def load_templates():
    dir_templates = get_dir_templates()
    templates = []
    for item in os.listdir(dir_templates):
        element = os.path.join(dir_templates, item)
        if os.path.isdir(element) and item != DIR_DOCS:
            templates.append(item)

    return templates


def get_render_path(xml):
    if os.path.isfile(xml):
        try:
            meta_tree = ET.parse(xml)
            meta_root = meta_tree.getroot()
        except:
            write_log('Unable to parse metaxml.')
            return

        for child in meta_root.find('notes').findall('note'):
            if child.get('name') == 'renderpath':
                return child.text

    else:
        write_log("Metaxml doesn't exist in: {}".format(xml))


def rename_item(sender, path_orig, window):
    inp = QtWidgets.QInputDialog()
    inp.setObjectName('inp')
    if os.path.isfile(path_orig):
        item = 'file'
    else:
        item = 'directory'
    title = 'Enter new name'
    msg = 'Enter the new name for the {}:'.format(item)
    file_name = os.path.basename(path_orig)
    name, ok = inp.getText(window, title, msg, text=file_name)
    if ok:
        name = name.replace('/', '')
        new_name_full_path = os.path.join(os.path.dirname(path_orig), name)
        if os.path.isfile(path_orig):
            if '.' not in name:
                ext = os.path.splitext(os.path.basename(path_orig))[1]
                new_name_full_path = '{}{}'.format(new_name_full_path, ext)
        if sender == 'smartlibshotwindow':
            os.rename(path_orig, new_name_full_path)
            window.populate_tree()
        if sender == 'shot_templates':
            os.rename(path_orig, new_name_full_path)
            window.load_shot_template_in_tree()
        if sender == 'saved_projects':
            settingsXML = get_settings_xml()
            settingstree = ET.parse(settingsXML)
            settingsroot = settingstree.getroot()
            for child in settingsroot.find('projectslist').findall('project'):
                if child.text == path_orig:
                    child.set('name', name)

            write_xml(settingsXML, settingsroot, settingstree)
            window.populate_saved_projects()


def force_create_render_dir():
    filename = nuke.filename(nuke.thisNode())
    dirname = os.path.dirname(filename)
    osdir = nuke.callbacks.filenameFilter(dirname)
    try:
        os.makedirs(osdir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def get_finder_name():
    if sys.platform == 'darwin':
        return 'finder'
    else:
        return 'explorer'


def import_from_footage_directory():
    dir_docs = get_dir_docs_current_nukescript()
    try:
        if dir_docs == '':
            raise ValueError
        meta_xml = os.path.join(dir_docs, 'meta.xml')
        if not os.path.isfile(meta_xml):
            raise ValueError
        metatree = ET.parse(meta_xml)
        for note in metatree.find('notes').findall('note'):
            if note.get('name') == 'footagepath':
                shot_root = os.path.normpath(os.path.join(dir_docs, '../'))
                shot_root = shot_root.replace(os.path.sep, '/')
                if note.text is not None:
                    if note.get('loc') == 'global':
                        start_path = note.text
                    if note.get('loc') == 'local':
                        if note.text[0] == os.path.sep or note.text[0] == '/':
                            note.text = note.text[1:]
                        if note.text and note.text != '' and note.text != ' ':
                            start_path = os.path.join(shot_root, note.text)
                        else:
                            start_path = shot_root
                elif note.text is None or note.text == '' or note.text == ' ':
                    start_path = shot_root
                if start_path[-1:] != '/':
                    start_path += '/'
                start_path = start_path.replace(os.path.sep, '/')
                load_footage(path=start_path)

    except:
        pass

    return


def load_footage(defaulttype = 'Read', path = ''):
    sel_node = None
    default_dir = None
    try:
        sel_node = nuke.selectedNode()
    except:
        pass

    if sel_node:
        if 'file' in sel_node.knobs():
            default_dir = sel_node['file'].value()
        if not default_dir and 'proxy' in sel_node.knobs():
            default_dir = sel_node['proxy'].value()
    if default_dir == '':
        default_dir = None
    files = nuke.getClipname('import from footage directory', default=path, multiple=True)
    if files != None:
        max_files = nuke.numvalue('preferences.maxPanels')
        n = len(files)
        for f in files:
            is_abc = False
            stripped = nuke.stripFrameRange(f)
            nodeType = defaulttype
            if nukescripts.create.isAudioFilename(stripped):
                nodeType = 'AudioRead'
            if nukescripts.create.isGeoFilename(stripped):
                nodeType = 'ReadGeo2'
            if nukescripts.create.isAbcFilename(stripped):
                is_abc = True
            if nukescripts.create.isDeepFilename(stripped):
                nodeType = 'DeepRead'
            use_in_panel = True
            if max_files != 0 and n > max_files:
                use_in_panel = False
            n = n - 1
            if is_abc:
                nuke.createScenefileBrowser(f, '')
            else:
                try:
                    nuke.createNode(nodeType, 'file {' + f + '}', inpanel=use_in_panel)
                except RuntimeError as err:
                    nuke.message(err.args[0])

    return


def show_custom_directory_window(shot_root, which, sml = None):
    global crp
    try:
        crp.close()
        del crp
    except:
        pass

    crp = CustomPath(shot_root, sml, which)
    crp.raise_()
    crp.show()


def create_new_directory(widget, list_):
    inp = QtWidgets.QInputDialog()
    inp.setObjectName('inp')
    title = 'Enter name'
    msg = 'Enter the name of the new folder:'
    dir_name, ok = inp.getText(widget, title, msg)
    if ok:
        dest = list_.data(0, QtCore.Qt.UserRole)
        if os.path.isfile(dest):
            dest = os.path.dirname(dest)
        dest = dest.replace('\\', '/')

        def create_directory(dir_name):
            dir_path_full = os.path.join(dest, dir_name)
            if not os.path.isdir(dir_path_full):
                os.makedirs(dir_path_full)
                diritem = widget.build_tree_widget_item(widget.dirlist[dest], dir_name, dir_path_full, is_dir=True)
                widget.dirlist[dir_path_full] = diritem
                widget.allitems[dir_path_full] = diritem
            else:
                message("The directory '{}' already exists. The folder wasn't created".format(dir_name))

        dir_item_list = dir_name.split(',')
        for dir_item in dir_item_list:
            dir_item = dir_item.strip()
            create_directory(dir_item)


def error_loading(path, sml):
    message = 'Cannot find the bookmark:\n{}\n\n No such directory.Do you like to delete it from the bookmarks?'.format(path)
    remove_bookmark = ask_dialog(message=message, process_button_text='Delete from bookmarks', color_process='45,0,0', cancel_button_text='Cancel')
    if remove_bookmark:
        settingsXML = get_settings_xml()
        settingstree = ET.parse(settingsXML)
        settingsroot = settingstree.getroot()
        for child in settingsroot.find('bookmarks').findall('bookmark'):
            if child.text == path:
                settingsroot.find('bookmarks').remove(child)

        write_xml(settingsXML, settingsroot, settingstree)
        sml.combo_bookmarks.removeItem(sml.combo_bookmarks.findText(path))


def get_project_information(project_full_path):
    shot_information = {}
    for shot in os.listdir(project_full_path):
        shot_full_path = os.path.join(project_full_path, shot)
        if os.path.isdir(shot_full_path) and shot != '.docs':
            metaxml = os.path.join(shot_full_path, '.docs', 'meta.xml')
            if os.path.isfile(metaxml):
                with open(metaxml, 'r') as metaxml:
                    shot_info = []
                    tree = ET.parse(metaxml)
                    root = tree.getroot()
                    for child in root.find('notes').findall('note'):
                        if child.get('name') == 'status':
                            status = child.text
                            if status is None or status == '':
                                status = ''
                            shot_info.append(status)
                        if child.get('name') == 'shotnotes':
                            shot_info.append(child.text)

            thumbnail = os.path.join(shot_full_path, '.docs', '__preview.jpg')
            if os.path.isfile(thumbnail):
                shot_info.append('file:///{}'.format(thumbnail))
            else:
                default_image = load_icons()['icon_preview_default']
                default_image = os.path.normpath(default_image)
                shot_info.append('file:////{}'.format(default_image))
            shot_information[shot] = shot_info

    return shot_information


def build_html(html_path, project):
    shot_information = get_project_information(project)
    project_title = os.path.split(project)[-1]
    time_now = datetime.datetime.fromtimestamp(int(time.time())).strftime('%d/%m/%Y %H:%M:%S')
    shot_status_list = load_status_list().values()
    status_dict = {}
    for status in shot_status_list:
        status_dict[status[1]] = 0

    for shot in shot_information.values():
        if shot[0] in status_dict:
            status_dict[shot[0]] += 1
        else:
            default_status = load_default_status()[0]
            if default_status in status_dict:
                status_dict[default_status] += 1

    with open(html_path, 'w') as tmp_html:
        report_top = templates.REPORT_TOP.format(project_title=project_title, time_now=time_now, project_path=project, number_of_shots=len(shot_information))
        tmp_html.write(report_top)
    for key in sorted(status_dict):
        with open(html_path, 'a') as tmp_html:
            bg_color = '255,255,255'
            for status in shot_status_list:
                if key == status[1]:
                    bg_color = status[0]

            if status_dict[key] != 0:
                percent = 100.0 / len(shot_information) * status_dict[key]
                percent_graph = percent - 1
            else:
                percent = 0.0
                percent_graph = 0.0
            percent = '{0:.1f}'.format(percent)
            tmp_html.write("\n                <span style='background-color: rgb({color}); display: inline-block; width:{width}%;'>&nbsp;</span>\n            ".format(color=bg_color, width=percent_graph))

    for key in sorted(status_dict):
        with open(html_path, 'a') as tmp_html:
            bg_color = '255,255,255'
            for status in shot_status_list:
                if key == status[1]:
                    bg_color = status[0]

            if status_dict[key] != 0:
                percent = 100.0 / len(shot_information) * status_dict[key]
            else:
                percent = 0.0
            percent = '{0:.1f}'.format(percent)
            tmp_html.write("\n                <span style='background-color: rgb({color}); display: inline-block; width:20px; margin-top: 5px;'>&nbsp;</span> <span style='color: #aaaaaa; font-size: 8pt; margin-top: 5px;'>{status} {count}x ({percent}%)</span><br />\n            ".format(color=bg_color, status=key, count=status_dict[key], percent=percent))

    with open(html_path, 'a') as tmp_html:
        tmp_html.write("\n            </div>\n            <br />\n            <div class='line' style='border-top: 1px solid #cccccc;'></div>\n        ")
    with open(html_path, 'a') as tmp_html:
        for key in sorted(shot_information):
            shot_status = shot_information[key][0]
            if shot_information[key][1]:
                shot_notes = shot_information[key][1]
            else:
                shot_notes = ''
            shot_notes = shot_notes.replace('\n', '<br />')
            shot_thumbnail = shot_information[key][2]
            color = ''
            for status in shot_status_list:
                if shot_status == status[1]:
                    color = status[0]

            if color == '':
                color = load_default_status()[1]
                shot_status = load_default_status()[0]
            tmp_html.write('\n            <div class=\'shot\' style="display: block; height:auto; margin: 20px; border-bottom: 1px solid #cccccc; padding: 20px;">\n                <div class=\'shot_thumbnail\' style=\'display: inline-block; padding-right: 30px;\'>\n                    <img src=\'{thumb}\' alt=\'\' title=\'\' width=\'200\' />\n                </div>\n                <div class=\'shot_details\' style=\'display: inline-block; vertical-align: top;\'>\n                    <span style=\'display: inline-block; font-size: 14pt; font-weight:bold;\'>{shotname}</span> <span style=\'background-color: rgb({color}); padding: 2px 10px; position: relative; top: -2px;\'>{status}</span> <br />\n                    <span style=\'font-size: 8pt;\'>{notes}</span>\n                </div>\n            </div>\n            <div style=\'clear:both;\'></div>\n'.format(thumb=shot_thumbnail, shotname=key, color=color, status=shot_status, notes=shot_notes))

    with open(html_path, 'a') as tmp_html:
        tmp_html.write('\n        </div>\n    </div>\n</body>\n</html>\n')
        return html_path


def build_pdf(build_path, project, output_filename = '', parent = None):
    try:
        from PySide import QtWebKit
    except Exception:
        msg = "Error creating project report. The needed module 'QtWebKit' is not more supported in this Nuke version. Please use Nuke10 to create a project report."
        show_message_box(parent, msg)
        return

    debug = False
    try:
        tmp_html = build_html(os.path.join(get_smartlib_public_dir(), 'tmp.html'), project)
        if debug:
            print 'tmp_html: ', tmp_html
        web = QtWebKit.QWebView()
        web.load(QtCore.QUrl('file:///{}'.format(tmp_html)))
        printer = QtGui.QPrinter()
        printer.setPageSize(QtGui.QPrinter.A4)
        printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        printer.setOutputFileName(output_filename)
        if debug:
            print 'output pdf to: {}'.format(output_filename)

        def convertIt():
            web.print_(printer)

        QtCore.QObject.connect(web, QtCore.SIGNAL('loadFinished(bool)'), convertIt)
        if os.path.isfile(tmp_html):
            try:
                os.remove(tmp_html)
            except Exception:
                pass

        return 'created_pdf'
    except Exception as e:
        return e


def get_sequences_sets(dirpath):
    sequences = []
    sequences_set = []
    dir_content = os.listdir(dirpath)
    for file in dir_content:
        if file in IGNORE:
            continue
        if os.path.isdir(os.path.join(dirpath, file)):
            continue
        filename_noext, ext = os.path.splitext(file)
        ext = ext.replace('.', '')
        from string import digits
        if isinstance(file, bytes):
            digits = digits.encode()
        filename_nodigits = filename_noext.rstrip(digits)
        if ext not in IMAGE_EXT:
            sequence = os.path.normpath(os.path.join(dirpath, file))
            sequence = sequence.replace(os.path.sep, '/')
            sequences.append(sequence)
        else:
            if len(filename_nodigits) == len(filename_noext) and file not in IGNORE and file not in sequences:
                sequence = os.path.normpath(os.path.join(dirpath, file))
                sequence = sequence.replace(os.path.sep, '/')
                sequences.append(sequence)
                continue
            if filename_nodigits not in sequences_set and file not in IGNORE and file not in sequences:
                sequences_set.append(filename_nodigits)
                sequence = os.path.normpath(os.path.join(dirpath, file))
                sequence = sequence.replace(os.path.sep, '/')
                sequences.append(sequence)

    return sequences


def image_sequence_resolve_all(filepath):
    filepath = str(filepath.replace(os.path.sep, '/'))
    basedir, filename = os.path.split(filepath)
    filename_noext, ext = os.path.splitext(filename)
    from string import digits
    if isinstance(filepath, bytes):
        digits = digits.encode()
    filename_nodigits = filename_noext.rstrip(digits)
    if len(filename_nodigits) == len(filename_noext):
        return os.path.join(basedir, filename)
    files = os.listdir(basedir)
    image_sequence_list = [ os.path.join(f) for f in files if f.startswith(filename_nodigits) and f.endswith(ext) and f[len(filename_nodigits):-len(ext) if ext else -1].isdigit() ]
    seq_start = image_sequence_list[0]
    seq_start = seq_start.replace(filename_nodigits, '')
    seq_start = seq_start.replace(ext, '')
    seq_end = image_sequence_list[-1:][0]
    seq_end = seq_end.replace(filename_nodigits, '')
    seq_end = seq_end.replace(ext, '')
    seq_preview = '{}[{}-{}]{}'.format(filename_nodigits, seq_start, seq_end, ext)
    seq_full_path = os.path.join(basedir, seq_preview)
    seq_full_path = seq_full_path.replace(os.path.sep, '/')
    return seq_full_path


def collapse_sequences(dirpath):
    sequences_in_dir = []
    sequence_sets = []
    dirpath = dirpath.replace(os.path.sep, '/')
    for root, dirs, seq in os.walk(dirpath):
        sequence_sub_sets = get_sequences_sets(root)
        if os.path.basename(root) == DIR_DOCS:
            continue
        for sequence_item in sequence_sub_sets:
            sequence_item = os.path.normpath(sequence_item)
            sequence_item = sequence_item.replace(os.path.sep, '/')
            sequence_sets.append(sequence_item)

    for seq in sequence_sets:
        ext = os.path.splitext(seq)[1]
        ext = ext.replace('.', '')
        if ext not in IGNORE and os.path.basename(seq) not in IGNORE:
            if ext not in IMAGE_EXT:
                item = seq
                item = item.replace(os.path.sep, '/')
                sequences_in_dir.append(item)
            else:
                item = image_sequence_resolve_all(seq)
                item = os.path.normpath(item)
                item = item.replace(os.path.sep, '/')
                sequences_in_dir.append(item)

    return sequences_in_dir


def insert_shot_notes():
    shot_root = get_dir_docs_current_nukescript()
    if shot_root == '' or shot_root is None:
        return
    else:
        shot_root = shot_root.replace(DIR_DOCS, '')
        meta_xml = get_meta_xml(shot_root)
        if not os.path.isfile(meta_xml):
            return
        meta_tree = ET.parse(meta_xml)
        meta_root = meta_tree.getroot()
        shot_notes = ''
        for child in meta_root.find('notes').findall('note'):
            if child.get('name') == 'shotnotes':
                shot_notes = child.text

        if shot_notes != '':
            sticky = nuke.createNode('StickyNote')
            sticky['label'].setValue(shot_notes)
            sticky['note_font_size'].setValue(20)
        return


def show_edit_template_script(window, path):
    global ets
    script_values = get_script_values(path, window)
    set_default_format = False
    if 'format' in script_values:
        if script_values['format'] == '0':
            set_default_format = True
    else:
        set_default_format = True
    if set_default_format:
        settings = load_settings()
        w = settings['default_w']
        h = settings['default_h']
        pixel_aspect_ratio = settings['default_pixel_aspect']
        format_default = '{} {} 0 0 {} {} {} HD'.format(w, h, w, h, pixel_aspect_ratio)
        script_values['format'] = format_default
        script_values['fps'] = settings['default_fps']
    try:
        ets.close()
        del ets
    except:
        pass

    ets = osl.EditTemplateScript(path, script_values)
    ets.show()
    ets.raise_()
    return ets


def get_script_values(path, window):
    script_values = {}
    if not os.path.isfile(path):
        msg = "The file '{}' does not exist".format(path)
        show_message_box(window, msg)
        return {}
    if os.path.splitext(path)[1] != '.nk':
        msg = "The file '{}' is no nuke script.".format(path)
        show_message_box(window, msg)
        return {}
    this_dir = os.path.dirname(__file__)
    processor = os.path.join(this_dir, '../', 'trm', 'scripts.py')
    processor = os.path.normpath(processor)
    cmd = '"{nuke_exe}" -i -t "{scriptProcess}" get "{path}" " "'.format(nuke_exe=os.path.normpath(nuke.env['ExecutablePath']), scriptProcess=processor, path=path)
    process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.wait()
    for line in process.stdout:
        line = str(line.rstrip())
        if 'script@' in line:
            script_value = line.replace('script@', '')
            key = script_value.split(':')[0]
            val = str(script_value.split(':')[1])
            script_values[key] = val

    return script_values


def set_script_values(path, script_values, *args):
    debug = False
    script_vals = 'script_in:{}@script_out:{}@fps:{}@format:{}'
    script_vals = script_vals.format(script_values['script_in'], script_values['script_out'], script_values['fps'], script_values['format'].replace(' ', '_'))
    this_dir = os.path.dirname(__file__)
    processor = os.path.join(this_dir, '../', 'trm', 'scripts.py')
    processor = os.path.normpath(processor)
    cmd = '"{nuke_exe}" -i -t "{scriptProcess}" set "{path}" {vals}'.format(nuke_exe=os.path.normpath(nuke.env['ExecutablePath']), scriptProcess=processor, path=path, vals=script_vals)
    process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.wait()
    found_end = 0
    for line in process.stdout:
        line = str(line.rstrip())
        if debug:
            print line
        if '@script:set_end' in line:
            found_end += 1

    if found_end == 1:
        return True
    else:
        return False


def get_user(metaxml, *args):
    if not os.path.isfile(metaxml):
        return ''
    metatree = ET.parse(metaxml)
    metaroot = metatree.getroot()
    with open(metaxml, 'r') as xml:
        for child in metaroot.find('notes').findall('note'):
            if child.get('name') == 'user':
                return child.text


def set_user(user, dir_docs = ''):
    if dir_docs == '':
        dir_docs = get_dir_docs_current_nukescript()
    if dir_docs:
        meta_xml = os.path.join(dir_docs, 'meta.xml')
        if not os.path.isfile(meta_xml):
            return
        metatree = ET.parse(meta_xml)
        metaroot = metatree.getroot()
        with open(meta_xml, 'w') as xml:
            for child in metaroot.find('notes').findall('note'):
                if child.get('name') == 'user':
                    child.text = user

            prettyprint(metaroot)
            metatree.write(xml, encoding='utf-8', xml_declaration=True)


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


class CustomPath(QtWidgets.QWidget):

    def __init__(self, shot_root, sml, which):
        super(CustomPath, self).__init__()
        self.shot_root = shot_root
        self.sml = sml
        self.which = which
        self.setWindowTitle('Set custom {} path'.format(which))
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumWidth(600)
        self.build_ui()

    def build_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.create_signals()

    def create_widgets(self):
        info = 'Here you can set a custom {} path that can be outside of the shot'.format(self.which)
        self.label_info = QtWidgets.QLabel(info)
        self.label_path = QtWidgets.QLabel('path: ')
        self.input_path = QtWidgets.QLineEdit(self.load_custom_path(self.which))
        self.push_browse = QtWidgets.QPushButton()
        self.push_browse.setIcon(QtGui.QIcon(load_icons()['icon_folder']))
        self.push_browse.setObjectName('simple')
        self.push_save = QtWidgets.QPushButton('save')
        self.push_save.setObjectName('actionButtonBig')
        self.push_close = QtWidgets.QPushButton('close')

    def create_layouts(self):
        self.layout_top = QtWidgets.QHBoxLayout()
        self.layout_top.addWidget(self.label_path)
        self.layout_top.addWidget(self.input_path)
        self.layout_top.addWidget(self.push_browse)
        self.layout_push = QtWidgets.QHBoxLayout()
        self.layout_push.addWidget(self.push_save)
        self.layout_push.addWidget(self.push_close)
        self.layout_main = QtWidgets.QVBoxLayout()
        self.layout_main.addWidget(self.label_info)
        self.layout_main.addLayout(self.layout_top)
        self.layout_main.addLayout(self.layout_push)
        self.setLayout(self.layout_main)
        set_style_sheet(self)

    def create_signals(self):
        self.push_close.clicked.connect(self.close)
        self.push_save.clicked.connect(self.set_custom_path)
        self.push_browse.clicked.connect(self.browse)

    def browse(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.input_path.setText(dialog.selectedFiles()[0])

    def set_custom_path(self):
        try:
            if not os.path.isdir(self.input_path.text()):
                os.makedirs(self.input_path.text())
        except:
            if self.input_path.text() != '':
                msg = "Failed setting up the path '{}' as custom {} directory. Please choose a different path.".format(self.input_path.text(), self.which)
                show_message_box(self, msg)
                return

        meta_xml = get_meta_xml(self.shot_root)
        metatree = ET.parse(meta_xml)
        metaroot = metatree.getroot()
        with open(meta_xml, 'w') as xml:
            for child in metaroot.find('notes').findall('note'):
                if self.which == 'render':
                    if child.get('name') == 'renderpath':
                        child.text = self.input_path.text()
                        child.set('loc', 'global')
                        if self.input_path.text() == '':
                            child.set('loc', 'local')
                elif self.which == 'footage':
                    if child.get('name') == 'footagepath':
                        child.text = self.input_path.text()
                        child.set('loc', 'global')
                        if self.input_path.text() == '':
                            child.set('loc', 'local')

            prettyprint(metaroot)
            metatree.write(xml, encoding='utf-8', xml_declaration=True)
        if self.input_path.text() == '':
            msg = 'Successfully cleared the custom {} path'.format(self.which)
            show_message_box(self, msg)
        else:
            msg = "Successfully set up the custom {} path to: '{}'".format(self.which, self.input_path.text())
            show_message_box(self, msg)
        self.close()
        if self.sml is not None:
            try:
                if self.which == 'render':
                    self.sml.current_shot_widget.set_renderpath(self.input_path.text())
                elif self.which == 'footage':
                    self.sml.current_shot_widget.set_footagepath(self.input_path.text())
                self.sml.current_shot_widget.refresh()
            except Exception as e:
                pass

        return

    def load_custom_path(self, which):
        meta_xml = get_meta_xml(self.shot_root)
        metatree = ET.parse(meta_xml)
        metaroot = metatree.getroot()
        for child in metaroot.find('notes').findall('note'):
            if child.get('name') == '{}path'.format(which):
                if child.get('loc') and child.get('loc') == 'global':
                    return child.text
                else:
                    return ''

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()