# Embedded file name: /media/psf/crypto/_GLOBALS/NUKE/python/cragl/__PREPAREFORRELEASE/smartShelves_v2.3/smartShelves/helper.py
______ __
______ subprocess
______ ___
______ ti__
______ xml.etree.ElementTree __ ET
______ ?
__ ?.NUKE_VERSION_MAJOR < 11:
    ____ ? ______ ?G.. __ ?W..
____
    ____ ? ______ ?W..
____ smartShelves ______ templates
_LOCK_DELIMITER _ ','
_LOCK_LIST _ 'CRAGL_SMARTSHELVES_LOCKS'

___ load_icons():
    this_dir _ __.path.dirname( -f)
    dir_icon _ __.path.join(this_dir, 'icons')
    dir_icon _ __.path.n_p_(dir_icon)
    r_ {'icon_logo': __.path.join(dir_icon, 'logo.png'),
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
    r_ [ dir_ ___ dir_ __ ?.pluginPath() __ '/plugins/icons' __ dir_ or '\\plugins\\icons' __ dir_ ][0]


___ show_message_box(window, m..):
    ?W...QMessageBox().information(window, 'information', m..)


___ get_installed_root_dir():
    this_dir _ __.path.join(__.path.dirname( -f))
    root _ __.path.join(this_dir, '../', '../')
    r_ __.path.n_p_(root)


___ get_smartshelves_private_dir():
    dir_ _ __.path.join(__.path.expanduser('~'), '.cragl', 'smartShelves')
    __ no. __.path.isdir(dir_):
        __.makedirs(dir_)
    r_ dir_


___ get_smartshelves_public_dir():
    dir_ _ __.path.join(__.path.expanduser('~'), 'cragl', 'smartShelves')
    __ no. __.path.isdir(dir_):
        __.makedirs(dir_)
    r_ dir_


___ open_website(url):
    __ ___.pl.. __ 'win32':
        __.startfile(url)
    ____ ___.pl.. __ 'darwin':
        subprocess.P..(['open', url])
    ____
        ___
            subprocess.P..(['xdg-open', url])
        except OSError:
            show_message_box(N.., 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.f..(url))

    r_


___ get_log_file():
    connect_dir _ __.path.join(__.path.expanduser('~'), '.cragl', 'connect')
    __ no. __.path.isdir(connect_dir):
        __.makedirs(connect_dir)
    log_file _ __.path.join(connect_dir, 'connectlog.txt')
    __ no. __.path.isfile(log_file):
        w__ o..(log_file, 'w') __ lf:
            log_template _ templates.LOG
            lf.write(log_template)
    r_ log_file


___ write_log(text, tool _ 'sh'):
    logtime _ ti__.strftime('%d.%m.%Y %H:%M:%S', ti__.localtime())
    ___
        w__ o..(get_log_file(), 'a') __ s:
            s.write('{}: {} {}\n'.f..(logtime, tool, text))
        r_ T..
    ______
        r_ F..


___ set_style_sheet(widget):
    this_dir _ __.path.dirname( -f)
    styles_nuke _ __.path.join(this_dir, 'styles', 'nuke.qss')
    styles_nuke _ __.path.n_p_(styles_nuke)
    __ __.path.isfile(styles_nuke):
        w__ o..(styles_nuke) __ file_:
            widget.setStyleSheet(file_.read())
        r_ styles_nuke
    ____
        r_
        r_


___ get_settings_xml():
    r_ __.path.join(get_smartshelves_private_dir(), 'settings.xml')


___ load_settings():
    xml _ get_settings_xml()
    tree _ ET.parse(xml)
    root _ tree.getroot()
    settings _ {}
    ___ setting __ root.find('settings').f_a_('setting'):
        settings[setting.get('name')] _ setting.text

    r_ settings


___ paste_script(name):
    ___ plugin_path __ ?.pluginPath():
        path _ __.path.join(plugin_path, '{}.nk'.f..(name))
        __ __.path.isfile(path):
            ?.nodePaste(path)
            r_

    ?.m..("Could not find nk file for '{}'. Please make sure that it is saved somewhere in your plugin paths.".f..(name))


___ add_to_lock(pw):
    __ no. __.en__.get(_LOCK_LIST):
        __.en__[_LOCK_LIST] _ ''
    unlocked _ [ name ___ name __ __.en__[_LOCK_LIST].split(_LOCK_DELIMITER) __ name ]
    __ pw __ unlocked:
        r_
    __ no. pw:
        r_
    unlocked.ap..(pw)
    __.en__[_LOCK_LIST] _ _LOCK_DELIMITER.join(unlocked)


___ remove_from_lock(pw):
    __ no. __.en__.get(_LOCK_LIST):
        __.en__[_LOCK_LIST] _ ''
    unlocked _ [ name ___ name __ __.en__[_LOCK_LIST].split(_LOCK_DELIMITER) __ name ]
    __ pw __ unlocked:
        unlocked.remove(pw)
    __.en__[_LOCK_LIST] _ _LOCK_DELIMITER.join(unlocked)