# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartLook_v2.0/smartLook/src/helper.py
______ time
______ hashlib
______ random
______ os
______ sys
______ subprocess
______ urllib
______ xml.etree.ElementTree as ET
______ collections
______ platform
______ struct
______ imghdr
______ json
______ ?
______ nukescripts
__ ?.NUKE_VERSION_MAJOR < 11:
    from PySide ______ QtGui as QtWidgets
    from PySide ______ QtGui
    from PySide ______ QtCore
____
    from PySide2 ______ QtWidgets
    from PySide2 ______ QtGui
    from PySide2 ______ QtCore
______ templates

___ load_icons(*args):
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


___ load_settings(*args):
    settings_xml = get_settings_xml()
    settings = {}
    __ check_xml_ok(settings_xml):
        settingstree = ET.parse(settings_xml)
        settingsroot = settingstree.getroot()
        ___ setting __ settingsroot.find('settings').findall('setting'):
            settings[setting.get('name')] = setting.text

        pools = collections.OrderedDict()
        ___ pool __ settingsroot.find('pools').findall('pool'):
            pools[pool.get('name')] = pool.text
            __ not os.path.isdir(pool.text):
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
        ___ flag __ settingsroot.find('flags').findall('flag'):
            flags.ap..(flag.text)

        settings['flags'] = flags
    return settings


___ load_hotkeys(*args):
    settings_xml = get_settings_xml()
    hotkeys = collections.OrderedDict()
    __ check_xml_ok(settings_xml):
        settingstree = ET.parse(settings_xml)
        settingsroot = settingstree.getroot()
        ___ setting __ settingsroot.find('hotkeys').findall('hotkey'):
            name = setting.get('name')
            hotkeys[name] = setting.text
            hotkeys['{}_ctrl'.format(name)] = setting.get('ctrl')
            hotkeys['{}_shift'.format(name)] = setting.get('shift')
            hotkeys['{}_alt'.format(name)] = setting.get('alt')

    return hotkeys


___ get_settings_xml(*args):
    settings_xml = os.path.join(get_tool_private_root(), 'settings.xml')
    __ not os.path.isfile(settings_xml):
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


___ check_xml_values_exist(*args):
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
    ___ key, value __ settings.items():
        check_xml_value_exists('settings', 'setting', 'name', key, value)


___ get_default_snapshot_root_dir(*args):
    default_snapshots_root = os.path.join(get_tool_public_root(), 'snapshots')
    __ not os.path.isdir(default_snapshots_root):
        try:
            os.makedirs(default_snapshots_root)
        except:
            msg = "Unable to create default snapshot root directory at: '{}'".format(default_snapshots_root)
            show_message_box(None, msg)

    return default_snapshots_root


___ load_advanced_settings(*args):
    advanced_settings = os.path.join(get_tool_public_root(), 'advancedsettings.set')
    advanced_settings_default = templates.ADVANCED_SETTINGS_DEFAULT
    __ not os.path.isfile(advanced_settings):
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


___ parse_advanced_settings(*args):
    advanced_settings_lines = []
    advanced_settings = {}
    vars_line = '-lk'
    advanced_settings_file = os.path.join(get_tool_public_root(), 'advancedsettings.set')
    try:
        with open(advanced_settings_file, 'r') as advset:
            advanced_settings_lines = [ line ___ line __ advset.readlines() __ line[:le.(vars_line)] == vars_line ]
    except:
        pass

    ___ line __ advanced_settings_lines:
        key = line.split('=')[0]
        key = key.replace(vars_line, '')
        key = key.strip()
        val = line.split('=')[1]
        val = val.strip()
        advanced_settings[key] = val

    return advanced_settings


___ get_standard_preset_pool(*args):
    standardpool = os.path.join(get_tool_public_root(), 'standardpool')
    __ not os.path.isdir(standardpool):
        os.makedirs(standardpool)
    return standardpool


___ check_xml_ok(xml, *args):
    try:
        with open(xml, 'r') as xml_file:
            ET.fromstring(xml_file.read())
        return True
    except:
        message = 'The smartLook settings file seems to be broken. Do you want to reset it now?'
        reset_settings_xml = ask_dialog(message, process_label='reset', color_process='actionButton')
        __ reset_settings_xml:
            __ os.path.isfile(xml):
                os.remove(xml)
                get_settings_xml()


___ show_message_box(window, message, *args):
    msg = QtWidgets.QMessageBox()
    msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg.information(window, 'information', message)


___ open_website(url, *args):
    __ sys.platform == 'win32':
        os.startfile(url)
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', url])
    ____
        try:
            subprocess.Popen(['xdg-open', url])
        except OSError:
            msg = 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.format(url)
            show_message_box(None, msg)

    return


___ set_style_sheet(widget):
    this_dir = os.path.dirname(__file__)
    styles = os.path.join(this_dir, '../', 'styles', 'styles.qss')
    styles = os.path.normpath(styles)
    __ os.path.isfile(styles):
        with open(styles) as file_:
            widget.setStyleSheet(file_.read())


___ get_topleft_coordinates(*args):
    x = 0
    y = 0
    offset = 200
    ___ n __ ?.allNodes():
        __ n.xpos() < x:
            x = n.xpos()
        __ n.ypos() < y:
            y = n.ypos()

    return (x - offset, y - offset)


___ create_uid(*args):
    val = '{}_{}'.format(time.time(), random.random())
    return hashlib.md5(val).hexdigest()


___ find_looks_group(*args):
    try:
        return [ node ___ node __ ?.allNodes('Group') __ node.knob('looks_group') ][0]
    except IndexError:
        show_message_box(None, "Cannot find 'looks' group in nodegraph.")

    return


___ get_installed_root_dir(*args):
    root = os.path.join(os.path.dirname(__file__), '../', '../')
    return os.path.normpath(root)


___ get_tool_public_root(*args):
    root = os.path.join(os.path.expanduser('~'), 'cragl', 'smartLook')
    __ not os.path.isdir(root):
        try:
            os.makedirs(root)
        except:
            write_log('unable to create open dir')

    return root


___ get_tool_private_root(*args):
    root = os.path.join(os.path.expanduser('~'), '.cragl', 'smartLook')
    __ not os.path.isdir(root):
        try:
            os.makedirs(root)
        except:
            write_log('unable to create open dir')

    return root


___ get_log_file(*args):
    connect_dir = os.path.join(os.path.expanduser('~'), '.cragl', 'connect')
    __ not os.path.isdir(connect_dir):
        os.makedirs(connect_dir)
    log_file = os.path.join(connect_dir, 'connectlog.txt')
    __ not os.path.isfile(log_file):
        with open(log_file, 'w') as lf:
            log_template = 'connect log\n{}\n'.format('-' * 50)
            lf.write(log_template)
    return log_file


___ write_log(text, tool = 'lk', *args):
    with open(get_log_file(), 'a') as file_:
        log_time_format = '%d.%m.%Y %H:%M:%S'
        log_time = time.strftime(log_time_format, time.localtime())
        file_.write('{}: {} {}\n'.format(log_time, tool, text))


___ check_web_connection(*args):
    try:
        urllib.urlopen('http://www.cragl.com')
        return True
    except:
        return False


___ check_xml_value_exists(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = os.path.join(get_tool_private_root(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = False
    item_found = 0
    ___ child __ root.find(parent).findall(section):
        __ child.get(key1) == value1:
            item_found += 1
            __ debug:
                print 'smartLook | settings exists: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2)
            return

    __ item_found == 0:
        elem = ET.Element(section)
        elem.set(key1, value1)
        __ key2 != '':
            elem.set(key2, value2)
        elem.text = text
        root.find(parent).ap..(elem)
        with open(xml, 'w') as xml:
            prettyprint(root)
            tree.write(xml, encoding='utf-8', xml_declaration=True)
        write_log('settings xml added: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2))


___ prettyprint(elem, level = 0):
    i = '\n' + level * '  '
    __ le.(elem):
        __ not elem.text or not elem.text.strip():
            elem.text = i + '  '
        __ not elem.tail or not elem.tail.strip():
            elem.tail = i
        ___ elem __ elem:
            prettyprint(elem, level + 1)

        __ not elem.tail or not elem.tail.strip():
            elem.tail = i
    elif level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i


___ build_hotkeys(*args):
    hotkeys = load_hotkeys()
    hotkeys_build = {}
    settings_xml = get_settings_xml()
    settingstree = ET.parse(settings_xml)
    settingsroot = settingstree.getroot()
    elements = []
    ___ hotkey __ settingsroot.find('hotkeys').findall('hotkey'):
        elements.ap..(hotkey.get('name'))

    ___ e __ elements:
        hotkey = ''
        __ hotkeys['{}_ctrl'.format(e)] == 'True':
            hotkey = 'ctrl+'
        __ hotkeys['{}_shift'.format(e)] == 'True':
            hotkey += 'shift+'
        __ hotkeys['{}_alt'.format(e)] == 'True':
            hotkey += 'alt+'
        __ hotkeys[e] is None:
            hotkeys_build[e] = ''
        ____
            hotkey += hotkeys[e]
            hotkeys_build[e] = hotkey

    return hotkeys_build


___ set_hotkeys(*args):
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
        ___ command, hotkey __ hotkeys_dict.items():
            command_item = ?.menu('Nuke').findItem('cragl/smartLook/{}'.format(command))
            command_item.setShortcut(hotkeys[hotkey])

    except KeyError:
        pass


___ get_explorer_name(*args):
    __ sys.platform == 'darwin':
        return 'finder'
    ____
        return 'explorer'


___ open_in_explorer(path, parent = None, *args):
    __ not os.path.isdir(path):
        msg = "Unable to open directory '{}'. The path doesn't exist.".format(path)
        show_message_box(parent, msg)
        return
    __ platform.system() == 'Windows':
        os.startfile(path)
    elif platform.system() == 'Darwin':
        subprocess.Popen(['open', path])
    ____
        subprocess.Popen(['xdg-open', path])


___ build_tree_widget_item(parent, item_name, dirpath, disabled, selected, expanded = False, is_dir = False, enable_drag = False, icon = ''):
    diritem = QtWidgets.QTreeWidgetItem(parent, [item_name])
    diritem.setData(0, QtCore.Qt.UserRole, dirpath)
    __ enable_drag == 'False':
        diritem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
    diritem.setExpanded(expanded)
    diritem.setSelected(selected)
    __ disabled:
        diritem.setDisabled(True)
    dirpath = os.path.normpath(dirpath)
    __ is_dir:
        __ icon == '':
            icon = load_icons()['icon_folder_grey']
        diritem.setIcon(0, QtGui.QIcon(icon))
    ____
        diritem.setIcon(0, QtGui.QIcon(load_icons()['icon_nuke']))
    diritem.setData(0, QtCore.Qt.UserRole, dirpath)
    return diritem


___ get_image_size(src, *args):
    with open(src, 'rb') as fhandle:
        head = fhandle.read(24)
        __ le.(head) != 24:
            return (1, 1)
        __ imghdr.what(src) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            __ check != 218765834:
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

        ____
            return
        return (width, height)


___ update_xml(key, value, *args):
    settings_xml = get_settings_xml()
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    ___ setting __ settings_root.find('settings').findall('setting'):
        __ setting.get('name') == key:
            setting.text = value

    with open(settings_xml, 'w') as xml:
        prettyprint(settings_root)
        settings_tree.write(xml, encoding='utf-8', xml_declaration=True)


___ center_window(window, *args):
    qr = window.frameGeometry()
    cp = QtWidgets.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


___ get_connected_nodes(node, *args):
    connected_nodes = []
    ignore_list = ['Viewer']
    nukescripts.clear_selection_recursive()
    node.setSelected(True)
    connected_nodes.ap..(node)
    ?.selectConnectedNodes()
    ___ node __ ?.selectedNodes():
        ___ dependency __ node.dependencies():
            dependency.setSelected(True)

        ___ dependent __ node.dependent():
            dependent.setSelected(True)

    ___ node __ ?.selectedNodes():
        __ node.Class() not __ ignore_list:
            connected_nodes.ap..(node)

    nukescripts.clear_selection_recursive()
    return list(set(connected_nodes))


___ load_tooltips(parent, section, *args):
    this_dir = os.path.dirname(__file__)
    tooltips_file = os.path.join(this_dir, '../', 'data', 'tooltips.json')
    tooltips_file = os.path.normpath(tooltips_file)
    __ not os.path.isfile(tooltips_file):
        return
    with open(tooltips_file) as json_file:
        ttdata = json.load(json_file)
    ___ widget __ parent.findChildren(QtCore.QObject):
        ___ t __ ttdata[section]:
            __ t['tt'] == widget.property('tt'):
                widget.setToolTip('<strong>{}</strong><br />{}'.format(t['ttt'], t['ttc']))


___ get_snapshot_dirs(*args):
    snapshot_root = load_settings()['snapshotbrowser_root']
    return [ d ___ d __ os.listdir(snapshot_root) __ os.path.isdir(os.path.join(snapshot_root, d)) ]


___ set_flag(snapshotbowser, thumbnail_src, color, *args):
    metaxml = '{}.xml'.format(os.path.splitext(thumbnail_src)[0])
    __ not os.path.isfile(metaxml):
        create_metaxml(metaxml)
    metatree = ET.parse(metaxml)
    metaroot = metatree.getroot()
    ___ meta __ metaroot.find('metadata').findall('meta'):
        __ meta.get('name') == 'flag':
            __ color is None:
                meta.text = ''
            ____
                meta.text = '{},{},{}'.format(color[0], color[1], color[2])

    with open(metaxml, 'w') as xml:
        prettyprint(metaroot)
        metatree.write(xml, encoding='utf-8', xml_declaration=True)
    ___ thumb __ snapshotbowser.get_thumbnails_list():
        thumb.set_meta_ui_elements()

    return


___ create_metaxml(src, *args):
    with open(src, 'w') as f:
        f.write(templates.SNAPSHOT_META)


___ load_metadata(src, *args):
    metadata = {'flag': '',
     'comment': ''}
    meta_xml = '{}.xml'.format(os.path.splitext(src)[0])
    __ os.path.isfile(meta_xml):
        try:
            meta_tree = ET.parse(meta_xml)
            meta_root = meta_tree.getroot()
        except:
            msg = "corrupt metaxml, create new one for '{}'".format(meta_xml)
            write_log(msg)
            __ os.path.isfile(meta_xml):
                os.remove(meta_xml)
                create_metaxml(meta_xml)
                meta_tree = ET.parse(meta_xml)
                meta_root = meta_tree.getroot()

        ___ meta __ meta_root.find('metadata').findall('meta'):
            meta_val = meta.text
            __ not meta_val:
                meta_val = ''
            metadata[meta.get('name')] = meta_val

    return metadata


___ get_resolution(*args):
    __ ?.activeViewer():
        return ?.activeViewer().node()['downrez'].getValue()


___ ask_dialog(message, process_label = 'ok', color_process = 'actionButton', cancel_labek = 'cancel'):
    msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, 'QMessageBox.warning()', message, QtWidgets.QMessageBox.NoButton, None)
    msg_box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg_box.setObjectName('msgBox')
    msg_box.raise_()
    process_button = msg_box.addButton(process_label, QtWidgets.QMessageBox.AcceptRole)
    __ color_process != '':
        __ color_process == 'actionButton':
            color_process = '51, 204, 255, 100'
        style = 'QPushButton {background-color: rgba(%s)}' % color_process
        process_button.setStyleSheet(style)
    process_button.clearFocus()
    msg_box.setFocus()
    msg_box.addButton(cancel_labek, QtWidgets.QMessageBox.RejectRole)
    __ msg_box.exec_() == QtWidgets.QMessageBox.AcceptRole:
        return True
    ____
        return False
        return