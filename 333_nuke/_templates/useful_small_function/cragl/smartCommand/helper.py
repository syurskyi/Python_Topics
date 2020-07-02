# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartCommand_v1.0.0/smartCommand/helper.py
______ json
______ __
______ time
______ platform
______ re
______ subprocess
______ sys
______ xml.etree.ElementTree as ET
______ ?
__ ?.NUKE_VERSION_MAJOR < 11:
    ____ PySide ______ QtGui as ?W..
    ____ PySide ______ QtGui
    ____ PySide ______ QtCore
____
    ____ ? ______ ?W..
    ____ ? ______ QtCore
    ____ ? ______ QtGui
____ smartCommand ______ templates
____ smartCommand.info ______ __product__

___ load_icons():
    this_dir = __.path.dirname(__file__)
    dir_icon = __.path.join(this_dir, 'icons')
    dir_icon = __.path.normpath(dir_icon)
    icons = {}
    ___ file_ __ __.listdir(dir_icon):
        name = __.path.splitext(file_)[0]
        path = __.path.join(dir_icon, file_)
        icons[name] = path

    return icons


___ set_style_sheet(widget, style = 'styles.qss'):
    this_dir = __.path.join(__.path.dirname(__file__))
    styles = __.path.join(this_dir, 'styles', style)
    styles = __.path.normpath(styles)
    __ __.path.isfile(styles):
        with open(styles) as file_:
            widget.setStyleSheet(file_.read())


___ move_widget(widget_to_move, click_pos, event):
    x, y = click_pos
    widget_to_move.xy = event.globalPos() - QtCore.QPoint(x, y)
    widget_to_move.move(widget_to_move.xy)


___ get_tool_root(which):
    __ which == 'private':
        cragl_dir = '.cragl'
    ____
        cragl_dir = 'cragl'
    root = __.path.join(__.path.expanduser('~'), cragl_dir, __product__)
    __ no. __.path.isdir(root):
        ___
            __.makedirs(root)
        except IOError:
            write_log('unable to create open tool dir at: {}'.format(root))

    return root


___ write_log(text, tool = 'sc'):
    with open(get_log_file(), 'a') as file_:
        log_time_format = '%d.%m.%Y %H:%M:%S'
        log_time = time.strftime(log_time_format, time.localtime())
        file_.write('{}: {} {}\n'.format(log_time, tool, text))


___ get_log_file():
    connect_dir = __.path.join(__.path.expanduser('~'), '.cragl', 'connect')
    __ no. __.path.isdir(connect_dir):
        __.makedirs(connect_dir)
    log_file = __.path.join(connect_dir, 'connectlog.txt')
    __ no. __.path.isfile(log_file):
        with open(log_file, 'w') as lf:
            log_template = 'connect log\n{}\n'.format('-' * 50)
            lf.write(log_template)
    return log_file


___ load_settings():
    settings_xml = get_settings_xml()
    settings = {}
    __ check_xml_ok(settings_xml):
        settings_tree = ET.parse(settings_xml)
        settings_root = settings_tree.getroot()
        ___ setting __ settings_root.find('settings').findall('setting'):
            value = setting.text
            __ value == 'True':
                value = True
            elif value == 'False':
                value = False
            settings[setting.get('name')] = value

    return settings


___ get_collection_root():
    collection_root = load_settings()['collection_root']
    __ no. __.path.isdir(collection_root):
        ___
            __.makedirs(collection_root)
        except OSError:
            msg = "Cannot create menu direcory in '{}'. Please set a different path.".format(collection_root)
            ?.message(msg)

    return collection_root


___ get_scriptlets_root():
    scriptlet_root = load_settings()['scriptlets']
    __ no. __.path.isdir(scriptlet_root):
        ___
            __.makedirs(scriptlet_root)
        except OSError:
            msg = "Cannot create scriptlet direcory in '{}'. Please set a different path.".format(scriptlet_root)
            ?.message(msg)

    return scriptlet_root


___ default_collection_root():
    root = __.path.join(get_tool_root('public'), 'collections')
    __ no. __.path.isdir(root):
        __.makedirs(root)
    return root


___ default_scriptlets_root():
    root = __.path.join(get_tool_root('public'), 'scriptlets')
    __ no. __.path.isdir(root):
        __.makedirs(root)
    return root


___ create_default_data_roots():
    default_collection_root()
    default_scriptlets_root()


___ get_xml_elements():
    xml = get_settings_xml()
    tree = ET.parse(xml)
    root = tree.getroot()
    return (xml, root, tree)


___ get_settings_xml():
    settings_xml = __.path.join(get_tool_root('private'), 'settings.xml')
    __ no. __.path.isfile(settings_xml):
        ___
            with open(settings_xml, 'w') as look_template:
                template = templates.SETTINGS
                look_template.write(template.strip())
                msg = "{} settings doesn't exist. created template at: {}".format(__product__, settings_xml)
                write_log(msg)
        ______
            msg = 'Failed writing {} settings template at: {}'.format(__product__, settings_xml)
            write_log(msg)

    check_xml_ok(settings_xml)
    check_xml_values_exist()
    return settings_xml


___ check_xml_values_exist():
    ___ key, value __ templates.SETTINGS_DEFAULT_VALUES.items():
        check_xml_value_exists('settings', 'setting', 'name', key, value)


___ check_xml_value_exists(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = __.path.join(get_tool_root('private'), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = False
    item_found = 0
    ___ child __ root.find(parent).findall(section):
        __ child.get(key1) == value1:
            item_found += 1
            __ debug:
                print '{} | settings exists: {}|{}|{}|{}|{}|{}|{}'.format(__product__, parent, section, key1, value1, text, key2, value2)
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
        __ no. elem.text or no. elem.text.strip():
            elem.text = i + '  '
        __ no. elem.tail or no. elem.tail.strip():
            elem.tail = i
        ___ elem __ elem:
            prettyprint(elem, level + 1)

        __ no. elem.tail or no. elem.tail.strip():
            elem.tail = i
    elif level and (no. elem.tail or no. elem.tail.strip()):
        elem.tail = i


___ check_xml_ok(xml):
    ___
        with open(xml, 'r') as xml_file:
            ET.fromstring(xml_file.read())
        return True
    ______
        message = 'The {} settings file seems to be broken. Do you want to reset it now?'.format(__product__)
        reset_settings_xml = ask_dialog(message, process_label='reset', color_process='actionButton')
        __ reset_settings_xml:
            __ __.path.isfile(xml):
                __.remove(xml)
                get_settings_xml()


___ ask_dialog(message, process_label = 'ok', color_process = 'actionButton', cancel_label = 'cancel'):
    msg_box = ?W...QMessageBox(?W...QMessageBox.Warning, 'QMessageBox.warning()', message, ?W...QMessageBox.NoButton, None)
    msg_box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg_box.setObjectName('msgBox')
    msg_box.raise_()
    process_button = msg_box.addButton(process_label, ?W...QMessageBox.AcceptRole)
    __ color_process != '':
        __ color_process == 'actionButton':
            color_process = '51, 204, 255, 100'
        style = 'QPushButton {background-color: rgba(%s)}' % color_process
        process_button.setStyleSheet(style)
    process_button.clearFocus()
    msg_box.setFocus()
    msg_box.addButton(cancel_label, ?W...QMessageBox.RejectRole)
    __ msg_box.exec_() == ?W...QMessageBox.AcceptRole:
        return True
    ____
        return False
        return


___ show_path_browser(title):
    dialog = ?W...QFileDialog()
    dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    dialog.sQT..(title)
    dialog.setFileMode(?W...QFileDialog.Directory)
    dialog.setOption(?W...QFileDialog.ShowDirsOnly)
    __ dialog.exec_() == ?W...QDialog.Accepted:
        return dialog.selectedFiles()[0]


___ update_settings(key, value):
    xml, root, tree = get_xml_elements()
    ___ setting __ root.find('settings').findall('setting'):
        __ setting.get('name') == key:
            setting.text = value

    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


___ get_menus(all_incl = True, exclude_prefix = '_'):
    menus = []
    __ all_incl:
        menus.ap..('all')
    menu_root = get_collection_root()
    ___ file_ __ __.listdir(menu_root):
        __ file_.startswith(exclude_prefix):
            continue
        __ file_.endswith('.xml'):
            ___
                xml_path = __.path.join(menu_root, file_)
                xml_name = __.path.splitext(file_)[0]
                with open(xml_path, 'r') as xml_file:
                    ET.fromstring(xml_file.read())
                menus.ap..(xml_name)
            except ET.ParseError:
                write_log('Skip non well formed menu collection: {}'.format(xml_path))

    return menus


___ add_command(collection_name, command_path, color = None, hotkey = None):
    xml = create_collection(collection_name)
    tree = ET.parse(xml)
    root = tree.getroot()
    collection = root.find('collection')
    remove_command_duplicates(collection, command_path)
    command_item = ET.Element('command')
    command_item.text = command_path
    __ color:
        command_item.set('color', str(color))
    __ hotkey:
        command_item.set('hotkey', sanitize(hotkey))
    collection.insert(0, command_item)
    with open(xml, 'w') as file_:
        prettyprint(root)
        tree.write(file_, encoding='utf-8', xml_declaration=True)


___ sanitize(string):
    return re.sub('[^a-zA-Z0-9+]', '', string)


___ get_history_xml():
    ____ smartCommand.constants ______ HISTORY
    return __.path.join(get_tool_root('private'), '{}.xml'.format(HISTORY))


___ swap_commands(xml, path_1, path_2):
    tree = ET.parse(xml)
    root = tree.getroot()
    command_1 = None
    command_2 = None
    index_1 = 0
    index_2 = 0
    index = 0
    ___ command __ root.find('collection').findall('command'):
        __ command.text == path_1:
            command_1 = command
            index_1 = index
        elif command.text == path_2:
            command_2 = command
            index_2 = index
        index += 1

    __ no. all((command is no. None ___ command __ [command_1, command_2])):
        raise ValueError('No such sufficient data to swap.')
    root.find('collection').remove(command_2)
    root.find('collection').insert(index_1, command_2)
    root.find('collection').remove(command_1)
    root.find('collection').insert(index_2, command_1)
    with open(xml, 'w') as file_:
        prettyprint(root)
        tree.write(file_, encoding='utf-8', xml_declaration=True)
    return


___ get_collection_xml(name):
    collection_root = get_collection_root()
    xml = __.path.join(collection_root, '{}.xml'.format(name))
    __ no. __.path.isfile(xml):
        raise IOError('No such collection xml: {}'.format(xml))
    return xml


___ remove_history_commands(xml, history_max):
    tree = ET.parse(xml)
    root = tree.getroot()
    index = 1
    ___ command __ root.find('collection').findall('command'):
        __ index > history_max:
            root.find('collection').remove(command)
        index += 1

    with open(xml, 'w') as file_:
        prettyprint(root)
        tree.write(file_, encoding='utf-8', xml_declaration=True)


___ create_collection(collection_name):
    __ collection_name == 'history':
        collection_root = get_tool_root('private')
    ____
        collection_root = load_settings()['collection_root']
    xml = __.path.join(collection_root, '{}.xml'.format(collection_name))
    __ no. __.path.isfile(xml):
        write_log("Create new collection '{}.xml'".format(collection_name))
        with open(xml, 'w') as file_:
            file_.write(templates.COLLECTION.format(collection_name=collection_name))
    return xml


___ remove_command_duplicates(menu, command_path):
    equals = [ command_elem ___ command_elem __ menu.findall('command') __ command_elem.text == command_path ]
    ___ element __ equals:
        menu.remove(element)

    return menu


___ get_command_object(path):
    command = ?.menu('Nuke').findItem(path)
    __ no. command:
        return None
    ____
        return command


___ get_next_element(list_, current):
    ___
        return list_[list_.index(current) + 1]
    except IndexError:
        return list_[0]


___ get_previous_element(list_, current):
    ___
        return list_[list_.index(current) - 1]
    except IndexError:
        return list_[le.(list_)]


___ update_command(xml, path, key, value):
    __ no. __.path.isfile(xml):
        raise IOError('No such collection file: {}'.format(xml))
    tree = ET.parse(xml)
    root = tree.getroot()
    ___ command __ root.find('collection').findall('command'):
        __ command.text == path:
            command.set(key, value)
            with open(xml, 'w') as xml:
                prettyprint(root)
                tree.write(xml, encoding='utf-8', xml_declaration=True)
            break
    ____
        raise ValueError('No such command path: {}'.format(path))


___ remove_command(xml, path):
    __ no. __.path.isfile(xml):
        raise IOError('No such collection xml: {}'.format(xml))
    tree = ET.parse(xml)
    root = tree.getroot()
    ___ command __ root.find('collection').findall('command'):
        __ command.text == path:
            root.find('collection').remove(command)
            with open(xml, 'w') as xml:
                prettyprint(root)
                tree.write(xml, encoding='utf-8', xml_declaration=True)
            break
    ____
        raise ValueError('No such command path: {}'.format(path))


___ get_basename(path):
    out = path
    sep = '/'
    __ sep __ path:
        out = path.split(sep)[-1]
    return out


___ get_all_hotkeys():
    hotkey_commands = {}
    collection_root = get_collection_root()
    ___ collection __ get_menus(all_incl=False):
        xml = '{}.xml'.format(collection)
        tree = ET.parse(__.path.join(collection_root, xml))
        root = tree.getroot()
        ___ command __ root.find('collection').findall('command'):
            __ command.get('hotkey'):
                hotkey_commands[command.get('hotkey')] = [command.text, xml]

    return hotkey_commands


___ initialize_hotkeys():
    hotkey_commands = get_all_hotkeys()
    ___ hotkey, command __ hotkey_commands.items():
        path = command[0]
        command_item = ?.menu('Nuke').findItem(path)
        __ command_item:
            command_item.setShortcut(hotkey)


___ load_tooltips(parent, section):
    this_dir = __.path.dirname(__file__)
    tooltips_file = __.path.join(this_dir, 'data', 'tooltips.json')
    tooltips_file = __.path.normpath(tooltips_file)
    __ no. __.path.isfile(tooltips_file):
        return
    with open(tooltips_file) as json_file:
        ___
            ttdata = json.load(json_file)
        except ValueError:
            write_log('Non well-formed tooltips file. Cannot parse file.')
            return

    ___ widget __ parent.findChildren(QtCore.QObject):
        ___ t __ ttdata[section]:
            __ t['tt'] == widget.property('tt'):
                widget.setToolTip('<strong>{}</strong><br />{}'.format(t['ttt'], t['ttc']))


___ open_website(url):
    __ sys.platform == 'win32':
        __.startfile(url)
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', url])
    ____
        ___
            subprocess.Popen(['xdg-open', url])
        except OSError:
            msg = 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.format(url)
            ____ smartCommand ______ dialogs
            dialogs.show_message_box(None, msg)

    return


___ get_basename(path, extension = False):
    basename = __.path.basename(path)
    __ extension:
        return basename
    return __.path.splitext(basename)[0]


___ get_module_docstring(path):
    compile_ = compile(open(path).read(), path, 'exec')
    __ compile_.co_consts and i..(compile_.co_consts[0], basestring):
        docstring = compile_.co_consts[0]
    ____
        docstring = None
    return docstring


___ center_window(window):
    geometry = window.frameGeometry()
    centerpoint = ?W...QDesktopWidget().availableGeometry().center()
    geometry.moveCenter(centerpoint)
    window.move(geometry.topLeft())


___ get_cursor_position():
    return QtGui.QCursor().pos()