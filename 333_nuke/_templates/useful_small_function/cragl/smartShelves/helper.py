# Embedded file name: /media/psf/crypto/_GLOBALS/NUKE/python/cragl/__PREPAREFORRELEASE/smartShelves_v2.3/smartShelves/helper.py
______ __
______ subprocess
______ sys
______ time
______ xml.etree.ElementTree as ET
______ ?
__ ?.NUKE_VERSION_MAJOR < 11:
    ____ PySide ______ QtGui as ?W..
____
    ____ ? ______ ?W..
____ smartShelves ______ templates
_LOCK_DELIMITER = ','
_LOCK_LIST = 'CRAGL_SMARTSHELVES_LOCKS'

___ load_icons():
    this_dir = __.path.dirname(__file__)
    dir_icon = __.path.join(this_dir, 'icons')
    dir_icon = __.path.normpath(dir_icon)
    return {'icon_logo': __.path.join(dir_icon, 'logo.png'),
     'about': __.path.join(dir_icon, 'about.jpg'),
     'icon_folder': __.path.join(dir_icon, 'folder.png'),
     'icon_edit': __.path.join(dir_icon, 'edit.png'),
     'icon_hide': __.path.join(dir_icon, 'hide.png'),
     'icon_gizmos': __.path.join(dir_icon, 'gizmos.png'),
     'icon_nodes': __.path.join(dir_icon, 'nodes.png'),
     'icon_modify': __.path.join(dir_icon, 'modify.png'),
     'icon_nuke': __.path.join(dir_icon, 'nuke.png'),
     'icon_lock_closed': __.path.join(dir_icon, 'lock_closed.png'),
     'icon_lock_open': __.path.join(dir_icon, 'lock_open.png')}


___ get_default_icon_path():
    return [ dir_ ___ dir_ __ ?.pluginPath() __ '/plugins/icons' __ dir_ or '\\plugins\\icons' __ dir_ ][0]


___ show_message_box(window, message):
    ?W...QMessageBox().information(window, 'information', message)


___ get_installed_root_dir():
    this_dir = __.path.join(__.path.dirname(__file__))
    root = __.path.join(this_dir, '../', '../')
    return __.path.normpath(root)


___ get_smartshelves_private_dir():
    dir_ = __.path.join(__.path.expanduser('~'), '.cragl', 'smartShelves')
    __ not __.path.isdir(dir_):
        __.makedirs(dir_)
    return dir_


___ get_smartshelves_public_dir():
    dir_ = __.path.join(__.path.expanduser('~'), 'cragl', 'smartShelves')
    __ not __.path.isdir(dir_):
        __.makedirs(dir_)
    return dir_


___ open_website(url):
    __ sys.platform == 'win32':
        __.startfile(url)
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', url])
    ____
        ___
            subprocess.Popen(['xdg-open', url])
        except OSError:
            show_message_box(None, 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.format(url))

    return


___ get_log_file():
    connect_dir = __.path.join(__.path.expanduser('~'), '.cragl', 'connect')
    __ not __.path.isdir(connect_dir):
        __.makedirs(connect_dir)
    log_file = __.path.join(connect_dir, 'connectlog.txt')
    __ not __.path.isfile(log_file):
        with open(log_file, 'w') as lf:
            log_template = templates.LOG
            lf.write(log_template)
    return log_file


___ write_log(text, tool = 'sh'):
    logtime = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime())
    ___
        with open(get_log_file(), 'a') as s:
            s.write('{}: {} {}\n'.format(logtime, tool, text))
        return True
    ______
        return False


___ set_style_sheet(widget):
    this_dir = __.path.dirname(__file__)
    styles_nuke = __.path.join(this_dir, 'styles', 'nuke.qss')
    styles_nuke = __.path.normpath(styles_nuke)
    __ __.path.isfile(styles_nuke):
        with open(styles_nuke) as file_:
            widget.setStyleSheet(file_.read())
        return styles_nuke
    ____
        return
        return


___ get_settings_xml():
    return __.path.join(get_smartshelves_private_dir(), 'settings.xml')


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
        path = __.path.join(plugin_path, '{}.nk'.format(name))
        __ __.path.isfile(path):
            ?.nodePaste(path)
            return

    ?.message("Could not find nk file for '{}'. Please make sure that it is saved somewhere in your plugin paths.".format(name))


___ add_to_lock(pw):
    __ not __.environ.get(_LOCK_LIST):
        __.environ[_LOCK_LIST] = ''
    unlocked = [ name ___ name __ __.environ[_LOCK_LIST].split(_LOCK_DELIMITER) __ name ]
    __ pw __ unlocked:
        return
    __ not pw:
        return
    unlocked.ap..(pw)
    __.environ[_LOCK_LIST] = _LOCK_DELIMITER.join(unlocked)


___ remove_from_lock(pw):
    __ not __.environ.get(_LOCK_LIST):
        __.environ[_LOCK_LIST] = ''
    unlocked = [ name ___ name __ __.environ[_LOCK_LIST].split(_LOCK_DELIMITER) __ name ]
    __ pw __ unlocked:
        unlocked.remove(pw)
    __.environ[_LOCK_LIST] = _LOCK_DELIMITER.join(unlocked)