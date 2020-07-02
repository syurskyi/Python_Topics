# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartLook_v2.0/smartLook/src/helper.py
______ time
______ hashlib
______ random
______ __
______ ___
______ subprocess
______ urllib
______ xml.etree.ElementTree as ET
______ collections
______ pl..
______ struct
______ imghdr
______ json
______ ?
______ ?
__ ?.NUKE_VERSION_MAJOR < 11:
    ____ PySide ______ QtGui as ?W..
    ____ PySide ______ QtGui
    ____ PySide ______ QtCore
____
    ____ ? ______ ?W..
    ____ ? ______ QtGui
    ____ ? ______ QtCore
______ templates

___ load_icons(*args):
    this_dir = __.path.dirname(__file__)
    dir_icon = __.path.join(this_dir, '../', 'icons')
    dir_icon = __.path.normpath(dir_icon)
    join = __.path.join
    r_ {'about': join(dir_icon, 'about.jpg'),
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
            __ no. __.path.isdir(pool.text):
                ___
                    __.makedirs(pool.text)
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
    r_ settings


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

    r_ hotkeys


___ get_settings_xml(*args):
    settings_xml = __.path.join(get_tool_private_root(), 'settings.xml')
    __ no. __.path.isfile(settings_xml):
        ___
            with open(settings_xml, 'w') as look_template:
                template = templates.SETTINGS.format(standard_pool=get_standard_preset_pool())
                look_template.write(template.strip())
                msg = "smartLook settings doesn't exist. created template at: {}".format(settings_xml)
                write_log(msg)
        ______
            msg = 'Failed writing smartLook settings template at: {}'.format(settings_xml)
            write_log(msg)

    check_xml_ok(settings_xml)
    check_xml_values_exist()
    r_ settings_xml


___ check_xml_values_exist(*args):
    default_snapshotdir = __.path.join(get_default_snapshot_root_dir(), 'temp')
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
    default_snapshots_root = __.path.join(get_tool_public_root(), 'snapshots')
    __ no. __.path.isdir(default_snapshots_root):
        ___
            __.makedirs(default_snapshots_root)
        ______
            msg = "Unable to create default snapshot root directory at: '{}'".format(default_snapshots_root)
            show_message_box(None, msg)

    r_ default_snapshots_root


___ load_advanced_settings(*args):
    advanced_settings = __.path.join(get_tool_public_root(), 'advancedsettings.set')
    advanced_settings_default = templates.ADVANCED_SETTINGS_DEFAULT
    __ no. __.path.isfile(advanced_settings):
        ___
            with open(advanced_settings, 'w') as advset:
                advset.write(advanced_settings_default)
        except Exception as e:
            print e
            write_log('Error writing advanced settings file: {}'.format(e))

    ___
        with open(advanced_settings, 'r') as advset:
            content = advset.read()
    except Exception as e:
        r_ 'Unable to read advanced settings file. {}'.format(e)

    r_ content


___ parse_advanced_settings(*args):
    advanced_settings_lines = []
    advanced_settings = {}
    vars_line = '-lk'
    advanced_settings_file = __.path.join(get_tool_public_root(), 'advancedsettings.set')
    ___
        with open(advanced_settings_file, 'r') as advset:
            advanced_settings_lines = [ line ___ line __ advset.readlines() __ line[:le.(vars_line)] __ vars_line ]
    ______
        pass

    ___ line __ advanced_settings_lines:
        key = line.split('=')[0]
        key = key.replace(vars_line, '')
        key = key.strip()
        val = line.split('=')[1]
        val = val.strip()
        advanced_settings[key] = val

    r_ advanced_settings


___ get_standard_preset_pool(*args):
    standardpool = __.path.join(get_tool_public_root(), 'standardpool')
    __ no. __.path.isdir(standardpool):
        __.makedirs(standardpool)
    r_ standardpool


___ check_xml_ok(xml, *args):
    ___
        with open(xml, 'r') as xml_file:
            ET.fromstring(xml_file.read())
        r_ True
    ______
        m.. = 'The smartLook settings file seems to be broken. Do you want to reset it now?'
        reset_settings_xml = ask_dialog(m.., process_label='reset', color_process='actionButton')
        __ reset_settings_xml:
            __ __.path.isfile(xml):
                __.remove(xml)
                get_settings_xml()


___ show_message_box(window, m.., *args):
    msg = ?W...QMessageBox()
    msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg.information(window, 'information', m..)


___ open_website(url, *args):
    __ ___.pl.. __ 'win32':
        __.startfile(url)
    ____ ___.pl.. __ 'darwin':
        subprocess.P..(['open', url])
    ____
        ___
            subprocess.P..(['xdg-open', url])
        except OSError:
            msg = 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.format(url)
            show_message_box(None, msg)

    r_


___ set_style_sheet(widget):
    this_dir = __.path.dirname(__file__)
    styles = __.path.join(this_dir, '../', 'styles', 'styles.qss')
    styles = __.path.normpath(styles)
    __ __.path.isfile(styles):
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

    r_ (x - offset, y - offset)


___ create_uid(*args):
    val = '{}_{}'.format(time.time(), random.random())
    r_ hashlib.md5(val).hexdigest()


___ find_looks_group(*args):
    ___
        r_ [ node ___ node __ ?.allNodes('Group') __ node.knob('looks_group') ][0]
    except IndexError:
        show_message_box(None, "Cannot find 'looks' group in nodegraph.")

    r_


___ get_installed_root_dir(*args):
    root = __.path.join(__.path.dirname(__file__), '../', '../')
    r_ __.path.normpath(root)


___ get_tool_public_root(*args):
    root = __.path.join(__.path.expanduser('~'), 'cragl', 'smartLook')
    __ no. __.path.isdir(root):
        ___
            __.makedirs(root)
        ______
            write_log('unable to create open dir')

    r_ root


___ get_tool_private_root(*args):
    root = __.path.join(__.path.expanduser('~'), '.cragl', 'smartLook')
    __ no. __.path.isdir(root):
        ___
            __.makedirs(root)
        ______
            write_log('unable to create open dir')

    r_ root


___ get_log_file(*args):
    connect_dir = __.path.join(__.path.expanduser('~'), '.cragl', 'connect')
    __ no. __.path.isdir(connect_dir):
        __.makedirs(connect_dir)
    log_file = __.path.join(connect_dir, 'connectlog.txt')
    __ no. __.path.isfile(log_file):
        with open(log_file, 'w') as lf:
            log_template = 'connect log\n{}\n'.format('-' * 50)
            lf.write(log_template)
    r_ log_file


___ write_log(text, tool = 'lk', *args):
    with open(get_log_file(), 'a') as file_:
        log_time_format = '%d.%m.%Y %H:%M:%S'
        log_time = time.strftime(log_time_format, time.localtime())
        file_.write('{}: {} {}\n'.format(log_time, tool, text))


___ check_web_connection(*args):
    ___
        urllib.urlopen('http://www.cragl.com')
        r_ True
    ______
        r_ False


___ check_xml_value_exists(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = __.path.join(get_tool_private_root(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = False
    item_found = 0
    ___ child __ root.find(parent).findall(section):
        __ child.get(key1) __ value1:
            item_found += 1
            __ debug:
                print 'smartLook | settings exists: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2)
            r_

    __ item_found __ 0:
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
        __ no. elem.text or no. elem.text.strip():
            elem.text = i + '  '
        __ no. elem.tail or no. elem.tail.strip():
            elem.tail = i
        ___ elem __ elem:
            prettyprint(elem, level + 1)

        __ no. elem.tail or no. elem.tail.strip():
            elem.tail = i
    ____ level and (no. elem.tail or no. elem.tail.strip()):
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
        __ hotkeys['{}_ctrl'.format(e)] __ 'True':
            hotkey = 'ctrl+'
        __ hotkeys['{}_shift'.format(e)] __ 'True':
            hotkey += 'shift+'
        __ hotkeys['{}_alt'.format(e)] __ 'True':
            hotkey += 'alt+'
        __ hotkeys[e] is None:
            hotkeys_build[e] = ''
        ____
            hotkey += hotkeys[e]
            hotkeys_build[e] = hotkey

    r_ hotkeys_build


___ set_hotkeys(*args):
    hotkeys = build_hotkeys()
    hotkeys_dict = {'snapshot browser': 'snapshotbrowser',
     'take snapshot': 'snapshot',
     'looks slider': 'looks_slider',
     '______ node | toolset': '______',
     'export node | toolset': 'export',
     "delete selected node's looks": 'delete_look_knobs',
     'set looks': 'set_looks',
     'resolution slider': 'resolution_slider',
     'settings': 'looks_settings'}
    ___
        ___ command, hotkey __ hotkeys_dict.items():
            command_item = ?.menu('Nuke').findItem('cragl/smartLook/{}'.format(command))
            command_item.setShortcut(hotkeys[hotkey])

    except KeyError:
        pass


___ get_explorer_name(*args):
    __ ___.pl.. __ 'darwin':
        r_ 'finder'
    ____
        r_ 'explorer'


___ open_in_explorer(path, parent = None, *args):
    __ no. __.path.isdir(path):
        msg = "Unable to open directory '{}'. The path doesn't exist.".format(path)
        show_message_box(parent, msg)
        r_
    __ pl...system() __ 'Windows':
        __.startfile(path)
    ____ pl...system() __ 'Darwin':
        subprocess.P..(['open', path])
    ____
        subprocess.P..(['xdg-open', path])


___ build_tree_widget_item(parent, item_name, dirpath, disabled, selected, expanded = False, is_dir = False, enable_drag = False, icon = ''):
    diritem = ?W...QTreeWidgetItem(parent, [item_name])
    diritem.setData(0, QtCore.Qt.UserRole, dirpath)
    __ enable_drag __ 'False':
        diritem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
    diritem.setExpanded(expanded)
    diritem.setSelected(selected)
    __ disabled:
        diritem.setDisabled(True)
    dirpath = __.path.normpath(dirpath)
    __ is_dir:
        __ icon __ '':
            icon = load_icons()['icon_folder_grey']
        diritem.setIcon(0, QtGui.QIcon(icon))
    ____
        diritem.setIcon(0, QtGui.QIcon(load_icons()['icon_nuke']))
    diritem.setData(0, QtCore.Qt.UserRole, dirpath)
    r_ diritem


___ get_image_size(src, *args):
    with open(src, 'rb') as fhandle:
        head = fhandle.read(24)
        __ le.(head) != 24:
            r_ (1, 1)
        __ imghdr.what(src) __ 'png':
            check = struct.unpack('>i', head[4:8])[0]
            __ check != 218765834:
                r_ (1, 1)
            width, height = struct.unpack('>ii', head[16:24])
        ____ imghdr.what(src) __ 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        ____ imghdr.what(src) __ 'jpeg':
            ___
                fhandle.seek(0)
                size = 2
                ftype = 0
                while no. 192 <= ftype <= 207:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) __ 255:
                        byte = fhandle.read(1)

                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2

                fhandle.seek(1, 1)
                height, width = struct.unpack('>HH', fhandle.read(4))
            ______
                r_ (1, 1)

        ____
            r_
        r_ (width, height)


___ update_xml(key, value, *args):
    settings_xml = get_settings_xml()
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    ___ setting __ settings_root.find('settings').findall('setting'):
        __ setting.get('name') __ key:
            setting.text = value

    with open(settings_xml, 'w') as xml:
        prettyprint(settings_root)
        settings_tree.write(xml, encoding='utf-8', xml_declaration=True)


___ center_window(window, *args):
    qr = window.frameGeometry()
    cp = ?W...QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


___ get_connected_nodes(node, *args):
    connected_nodes = []
    ignore_list = ['Viewer']
    ?.clear_selection_recursive()
    node.setSelected(True)
    connected_nodes.ap..(node)
    ?.selectConnectedNodes()
    ___ node __ ?.sN..:
        ___ dependency __ node.dependencies():
            dependency.setSelected(True)

        ___ dependent __ node.dependent():
            dependent.setSelected(True)

    ___ node __ ?.sN..:
        __ node.Class() no. __ ignore_list:
            connected_nodes.ap..(node)

    ?.clear_selection_recursive()
    r_ list(set(connected_nodes))


___ load_tooltips(parent, section, *args):
    this_dir = __.path.dirname(__file__)
    tooltips_file = __.path.join(this_dir, '../', 'data', 'tooltips.json')
    tooltips_file = __.path.normpath(tooltips_file)
    __ no. __.path.isfile(tooltips_file):
        r_
    with open(tooltips_file) as json_file:
        ttdata = json.load(json_file)
    ___ widget __ parent.findChildren(QtCore.QObject):
        ___ t __ ttdata[section]:
            __ t['tt'] __ widget.property('tt'):
                widget.setToolTip('<strong>{}</strong><br />{}'.format(t['ttt'], t['ttc']))


___ get_snapshot_dirs(*args):
    snapshot_root = load_settings()['snapshotbrowser_root']
    r_ [ d ___ d __ __.listdir(snapshot_root) __ __.path.isdir(__.path.join(snapshot_root, d)) ]


___ set_flag(snapshotbowser, thumbnail_src, color, *args):
    metaxml = '{}.xml'.format(__.path.splitext(thumbnail_src)[0])
    __ no. __.path.isfile(metaxml):
        create_metaxml(metaxml)
    metatree = ET.parse(metaxml)
    metaroot = metatree.getroot()
    ___ meta __ metaroot.find('metadata').findall('meta'):
        __ meta.get('name') __ 'flag':
            __ color is None:
                meta.text = ''
            ____
                meta.text = '{},{},{}'.format(color[0], color[1], color[2])

    with open(metaxml, 'w') as xml:
        prettyprint(metaroot)
        metatree.write(xml, encoding='utf-8', xml_declaration=True)
    ___ thumb __ snapshotbowser.get_thumbnails_list():
        thumb.set_meta_ui_elements()

    r_


___ create_metaxml(src, *args):
    with open(src, 'w') as f:
        f.write(templates.SNAPSHOT_META)


___ load_metadata(src, *args):
    metadata = {'flag': '',
     'comment': ''}
    meta_xml = '{}.xml'.format(__.path.splitext(src)[0])
    __ __.path.isfile(meta_xml):
        ___
            meta_tree = ET.parse(meta_xml)
            meta_root = meta_tree.getroot()
        ______
            msg = "corrupt metaxml, create new one for '{}'".format(meta_xml)
            write_log(msg)
            __ __.path.isfile(meta_xml):
                __.remove(meta_xml)
                create_metaxml(meta_xml)
                meta_tree = ET.parse(meta_xml)
                meta_root = meta_tree.getroot()

        ___ meta __ meta_root.find('metadata').findall('meta'):
            meta_val = meta.text
            __ no. meta_val:
                meta_val = ''
            metadata[meta.get('name')] = meta_val

    r_ metadata


___ get_resolution(*args):
    __ ?.activeViewer():
        r_ ?.activeViewer().node()['downrez'].getValue()


___ ask_dialog(m.., process_label = 'ok', color_process = 'actionButton', cancel_labek = 'cancel'):
    msg_box = ?W...QMessageBox(?W...QMessageBox.Warning, 'QMessageBox.warning()', m.., ?W...QMessageBox.NoButton, None)
    msg_box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg_box.setObjectName('msgBox')
    msg_box.raise_()
    process_button = msg_box.addButton(process_label, ?W...QMessageBox.AcceptRole)
    __ color_process != '':
        __ color_process __ 'actionButton':
            color_process = '51, 204, 255, 100'
        style = 'QPushButton {background-color: rgba(%s)}' % color_process
        process_button.setStyleSheet(style)
    process_button.clearFocus()
    msg_box.setFocus()
    msg_box.addButton(cancel_labek, ?W...QMessageBox.RejectRole)
    __ msg_box.exec_() __ ?W...QMessageBox.AcceptRole:
        r_ True
    ____
        r_ False
        r_