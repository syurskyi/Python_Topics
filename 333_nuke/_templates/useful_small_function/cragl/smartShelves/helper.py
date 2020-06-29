# Embedded file name: /media/psf/crypto/_GLOBALS/NUKE/python/cragl/__PREPAREFORRELEASE/smartShelves_v2.3/smartShelves/helper.py
______ os
______ subprocess
______ sys
______ time
______ xml.etree.ElementTree as ET
______ ?
__ ?.NUKE_VERSION_MAJOR < 11:
    from PySide ______ QtGui as QtWidgets
____
    from PySide2 ______ QtWidgets
from smartShelves ______ templates
_LOCK_DELIMITER = ','
_LOCK_LIST = 'CRAGL_SMARTSHELVES_LOCKS'

___ load_icons():
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


___ get_default_icon_path():
    return [ dir_ ___ dir_ __ ?.pluginPath() __ '/plugins/icons' __ dir_ or '\\plugins\\icons' __ dir_ ][0]


___ show_message_box(window, message):
    QtWidgets.QMessageBox().information(window, 'information', message)


___ get_installed_root_dir():
    this_dir = os.path.join(os.path.dirname(__file__))
    root = os.path.join(this_dir, '../', '../')
    return os.path.normpath(root)


___ get_smartshelves_private_dir():
    dir_ = os.path.join(os.path.expanduser('~'), '.cragl', 'smartShelves')
    __ not os.path.isdir(dir_):
        os.makedirs(dir_)
    return dir_


___ get_smartshelves_public_dir():
    dir_ = os.path.join(os.path.expanduser('~'), 'cragl', 'smartShelves')
    __ not os.path.isdir(dir_):
        os.makedirs(dir_)
    return dir_


___ open_website(url):
    __ sys.platform == 'win32':
        os.startfile(url)
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', url])
    ____
        try:
            subprocess.Popen(['xdg-open', url])
        except OSError:
            show_message_box(None, 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.format(url))

    return


___ get_log_file():
    connect_dir = os.path.join(os.path.expanduser('~'), '.cragl', 'connect')
    __ not os.path.isdir(connect_dir):
        os.makedirs(connect_dir)
    log_file = os.path.join(connect_dir, 'connectlog.txt')
    __ not os.path.isfile(log_file):
        with open(log_file, 'w') as lf:
            log_template = templates.LOG
            lf.write(log_template)
    return log_file


___ write_log(text, tool = 'sh'):
    logtime = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime())
    try:
        with open(get_log_file(), 'a') as s:
            s.write('{}: {} {}\n'.format(logtime, tool, text))
        return True
    except:
        return False


___ set_style_sheet(widget):
    this_dir = os.path.dirname(__file__)
    styles_nuke = os.path.join(this_dir, 'styles', 'nuke.qss')
    styles_nuke = os.path.normpath(styles_nuke)
    __ os.path.isfile(styles_nuke):
        with open(styles_nuke) as file_:
            widget.setStyleSheet(file_.read())
        return styles_nuke
    ____
        return
        return


___ get_settings_xml():
    return os.path.join(get_smartshelves_private_dir(), 'settings.xml')


___ load_settings():
    xml = get_settings_xml()
    tree = ET.parse(xml)
    root = tree.getroot()
    settings = {}
    ___ setting __ root.find('settings').findall('setting'):
        settings[setting.get('name')] = setting.text

    return settings


___ paste_script(name):
    ___ plugin_path __ ?.pluginPath():
        path = os.path.join(plugin_path, '{}.nk'.format(name))
        __ os.path.isfile(path):
            ?.nodePaste(path)
            return

    ?.message("Could not find nk file for '{}'. Please make sure that it is saved somewhere in your plugin paths.".format(name))


___ add_to_lock(pw):
    __ not os.environ.get(_LOCK_LIST):
        os.environ[_LOCK_LIST] = ''
    unlocked = [ name ___ name __ os.environ[_LOCK_LIST].split(_LOCK_DELIMITER) __ name ]
    __ pw __ unlocked:
        return
    __ not pw:
        return
    unlocked.ap..(pw)
    os.environ[_LOCK_LIST] = _LOCK_DELIMITER.join(unlocked)


___ remove_from_lock(pw):
    __ not os.environ.get(_LOCK_LIST):
        os.environ[_LOCK_LIST] = ''
    unlocked = [ name ___ name __ os.environ[_LOCK_LIST].split(_LOCK_DELIMITER) __ name ]
    __ pw __ unlocked:
        unlocked.remove(pw)
    os.environ[_LOCK_LIST] = _LOCK_DELIMITER.join(unlocked)