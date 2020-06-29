# Embedded file name: /media/psf/crypto/_GLOBALS/NUKE/python/cragl/__PREPAREFORRELEASE/smartShelves_v2.3/smartShelves/helper.py
import os
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
import nuke
if nuke.NUKE_VERSION_MAJOR < 11:
    from PySide import QtGui as QtWidgets
else:
    from PySide2 import QtWidgets
from smartShelves import templates
_LOCK_DELIMITER = ','
_LOCK_LIST = 'CRAGL_SMARTSHELVES_LOCKS'

def load_icons():
    this_dir = os.path.dirname(__file__)
    dir_icon = os.path.join(this_dir, 'icons')
    dir_icon = os.path.normpath(dir_icon)
    return {'icon_logo': os.path.join(dir_icon, 'logo.png'),
     'about': os.path.join(dir_icon, 'about.jpg'),
     'icon_folder': os.path.join(dir_icon, 'folder.png'),
     'icon_edit': os.path.join(dir_icon, 'edit.png'),
     'icon_hide': os.path.join(dir_icon, 'hide.png'),
     'icon_gizmos': os.path.join(dir_icon, 'gizmos.png'),
     'icon_nodes': os.path.join(dir_icon, 'nodes.png'),
     'icon_modify': os.path.join(dir_icon, 'modify.png'),
     'icon_nuke': os.path.join(dir_icon, 'nuke.png'),
     'icon_lock_closed': os.path.join(dir_icon, 'lock_closed.png'),
     'icon_lock_open': os.path.join(dir_icon, 'lock_open.png')}


def get_default_icon_path():
    return [ dir_ for dir_ in nuke.pluginPath() if '/plugins/icons' in dir_ or '\\plugins\\icons' in dir_ ][0]


def show_message_box(window, message):
    QtWidgets.QMessageBox().information(window, 'information', message)


def get_installed_root_dir():
    this_dir = os.path.join(os.path.dirname(__file__))
    root = os.path.join(this_dir, '../', '../')
    return os.path.normpath(root)


def get_smartshelves_private_dir():
    dir_ = os.path.join(os.path.expanduser('~'), '.cragl', 'smartShelves')
    if not os.path.isdir(dir_):
        os.makedirs(dir_)
    return dir_


def get_smartshelves_public_dir():
    dir_ = os.path.join(os.path.expanduser('~'), 'cragl', 'smartShelves')
    if not os.path.isdir(dir_):
        os.makedirs(dir_)
    return dir_


def open_website(url):
    if sys.platform == 'win32':
        os.startfile(url)
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', url])
    else:
        try:
            subprocess.Popen(['xdg-open', url])
        except OSError:
            show_message_box(None, 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.format(url))

    return


def get_log_file():
    connect_dir = os.path.join(os.path.expanduser('~'), '.cragl', 'connect')
    if not os.path.isdir(connect_dir):
        os.makedirs(connect_dir)
    log_file = os.path.join(connect_dir, 'connectlog.txt')
    if not os.path.isfile(log_file):
        with open(log_file, 'w') as lf:
            log_template = templates.LOG
            lf.write(log_template)
    return log_file


def write_log(text, tool = 'sh'):
    logtime = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime())
    try:
        with open(get_log_file(), 'a') as s:
            s.write('{}: {} {}\n'.format(logtime, tool, text))
        return True
    except:
        return False


def set_style_sheet(widget):
    this_dir = os.path.dirname(__file__)
    styles_nuke = os.path.join(this_dir, 'styles', 'nuke.qss')
    styles_nuke = os.path.normpath(styles_nuke)
    if os.path.isfile(styles_nuke):
        with open(styles_nuke) as file_:
            widget.setStyleSheet(file_.read())
        return styles_nuke
    else:
        return
        return


def get_settings_xml():
    return os.path.join(get_smartshelves_private_dir(), 'settings.xml')


def load_settings():
    xml = get_settings_xml()
    tree = ET.parse(xml)
    root = tree.getroot()
    settings = {}
    for setting in root.find('settings').findall('setting'):
        settings[setting.get('name')] = setting.text

    return settings


def paste_script(name):
    for plugin_path in nuke.pluginPath():
        path = os.path.join(plugin_path, '{}.nk'.format(name))
        if os.path.isfile(path):
            nuke.nodePaste(path)
            return

    nuke.message("Could not find nk file for '{}'. Please make sure that it is saved somewhere in your plugin paths.".format(name))


def add_to_lock(pw):
    if not os.environ.get(_LOCK_LIST):
        os.environ[_LOCK_LIST] = ''
    unlocked = [ name for name in os.environ[_LOCK_LIST].split(_LOCK_DELIMITER) if name ]
    if pw in unlocked:
        return
    if not pw:
        return
    unlocked.append(pw)
    os.environ[_LOCK_LIST] = _LOCK_DELIMITER.join(unlocked)


def remove_from_lock(pw):
    if not os.environ.get(_LOCK_LIST):
        os.environ[_LOCK_LIST] = ''
    unlocked = [ name for name in os.environ[_LOCK_LIST].split(_LOCK_DELIMITER) if name ]
    if pw in unlocked:
        unlocked.remove(pw)
    os.environ[_LOCK_LIST] = _LOCK_DELIMITER.join(unlocked)