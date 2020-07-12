# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartCommand_v1.0.0/smartCommand/helper.py
______ j___
______ __
______ ti__
______ pl..
______ re
______ subprocess
______ ___
______ xml.etree.ElementTree __ ET
______ ?
__ ?.NUKE_VERSION_MAJOR < 11:
    ____ ? ______ ?G.. __ ?W..
    ____ ? ______ ?G..
    ____ ? ______ ?C..
____
    ____ ? ______ ?W..
    ____ ? ______ ?C..
    ____ ? ______ ?G..
____ smartCommand ______ templates
____ smartCommand.info ______ __product__

___ load_icons():
    this_dir = __.path.dirname( -f)
    dir_icon = __.path.join(this_dir, 'icons')
    dir_icon = __.path.n_p_(dir_icon)
    icons = {}
    ___ file_ __ __.listdir(dir_icon):
        name = __.path.splitext(file_)[0]
        path = __.path.join(dir_icon, file_)
        icons[name] = path

    r_ icons


___ set_style_sheet(widget, style = 'styles.qss'):
    this_dir = __.path.join(__.path.dirname( -f))
    styles = __.path.join(this_dir, 'styles', style)
    styles = __.path.n_p_(styles)
    __ __.path.isfile(styles):
        w__ o..(styles) __ file_:
            widget.setStyleSheet(file_.read())


___ move_widget(widget_to_move, click_pos, event):
    x, y = click_pos
    widget_to_move.xy = event.globalPos() - ?C...QPoint(x, y)
    widget_to_move.move(widget_to_move.xy)


___ get_tool_root(which):
    __ which __ 'private':
        cragl_dir = '.cragl'
    ____
        cragl_dir = 'cragl'
    root = __.path.join(__.path.expanduser('~'), cragl_dir, __product__)
    __ no. __.path.isdir(root):
        ___
            __.makedirs(root)
        except IOError:
            write_log('unable to create open tool dir at: {}'.f..(root))

    r_ root


___ write_log(text, tool = 'sc'):
    w__ o..(get_log_file(), 'a') __ file_:
        log_time_format = '%d.%m.%Y %H:%M:%S'
        log_time = ti__.strftime(log_time_format, ti__.localtime())
        file_.write('{}: {} {}\n'.f..(log_time, tool, text))


___ get_log_file():
    connect_dir = __.path.join(__.path.expanduser('~'), '.cragl', 'connect')
    __ no. __.path.isdir(connect_dir):
        __.makedirs(connect_dir)
    log_file = __.path.join(connect_dir, 'connectlog.txt')
    __ no. __.path.isfile(log_file):
        w__ o..(log_file, 'w') __ lf:
            log_template = 'connect log\n{}\n'.f..('-' * 50)
            lf.write(log_template)
    r_ log_file


___ load_settings():
    settings_xml = get_settings_xml()
    settings = {}
    __ check_xml_ok(settings_xml):
        settings_tree = ET.parse(settings_xml)
        settings_root = settings_tree.getroot()
        ___ setting __ settings_root.find('settings').f_a_('setting'):
            value = setting.text
            __ value __ 'True':
                value = T..
            ____ value __ 'False':
                value = F..
            settings[setting.get('name')] = value

    r_ settings


___ get_collection_root():
    collection_root = load_settings()['collection_root']
    __ no. __.path.isdir(collection_root):
        ___
            __.makedirs(collection_root)
        except OSError:
            msg = "Cannot create menu direcory in '{}'. Please set a different path.".f..(collection_root)
            ?.m..(msg)

    r_ collection_root


___ get_scriptlets_root():
    scriptlet_root = load_settings()['scriptlets']
    __ no. __.path.isdir(scriptlet_root):
        ___
            __.makedirs(scriptlet_root)
        except OSError:
            msg = "Cannot create scriptlet direcory in '{}'. Please set a different path.".f..(scriptlet_root)
            ?.m..(msg)

    r_ scriptlet_root


___ default_collection_root():
    root = __.path.join(get_tool_root('public'), 'collections')
    __ no. __.path.isdir(root):
        __.makedirs(root)
    r_ root


___ default_scriptlets_root():
    root = __.path.join(get_tool_root('public'), 'scriptlets')
    __ no. __.path.isdir(root):
        __.makedirs(root)
    r_ root


___ create_default_data_roots():
    default_collection_root()
    default_scriptlets_root()


___ get_xml_elements():
    xml = get_settings_xml()
    tree = ET.parse(xml)
    root = tree.getroot()
    r_ (xml, root, tree)


___ get_settings_xml():
    settings_xml = __.path.join(get_tool_root('private'), 'settings.xml')
    __ no. __.path.isfile(settings_xml):
        ___
            w__ o..(settings_xml, 'w') __ look_template:
                template = templates.SETTINGS
                look_template.write(template.strip())
                msg = "{} settings doesn't exist. created template at: {}".f..(__product__, settings_xml)
                write_log(msg)
        ______
            msg = 'Failed writing {} settings template at: {}'.f..(__product__, settings_xml)
            write_log(msg)

    check_xml_ok(settings_xml)
    check_xml_values_exist()
    r_ settings_xml


___ check_xml_values_exist():
    ___ key, value __ templates.SETTINGS_DEFAULT_VALUES.items():
        check_xml_value_exists('settings', 'setting', 'name', key, value)


___ check_xml_value_exists(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = __.path.join(get_tool_root('private'), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = F..
    item_found = 0
    ___ child __ root.find(parent).f_a_(section):
        __ child.get(key1) __ value1:
            item_found += 1
            __ debug:
                print '{} | settings exists: {}|{}|{}|{}|{}|{}|{}'.f..(__product__, parent, section, key1, value1, text, key2, value2)
            r_

    __ item_found __ 0:
        elem = ET.Element(section)
        elem.set(key1, value1)
        __ key2 != '':
            elem.set(key2, value2)
        elem.text = text
        root.find(parent).ap..(elem)
        w__ o..(xml, 'w') __ xml:
            prettyprint(root)
            tree.write(xml, encoding='utf-8', xml_declaration=T..)
        write_log('settings xml added: {}|{}|{}|{}|{}|{}|{}'.f..(parent, section, key1, value1, text, key2, value2))


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


___ check_xml_ok(xml):
    ___
        w__ o..(xml, 'r') __ xml_file:
            ET.fromstring(xml_file.read())
        r_ T..
    ______
        m.. = 'The {} settings file seems to be broken. Do you want to reset it now?'.f..(__product__)
        reset_settings_xml = ask_dialog(m.., process_label='reset', color_process='actionButton')
        __ reset_settings_xml:
            __ __.path.isfile(xml):
                __.remove(xml)
                get_settings_xml()


___ ask_dialog(m.., process_label = 'ok', color_process = 'actionButton', cancel_label = 'cancel'):
    msg_box = ?W...QMessageBox(?W...QMessageBox.Warning, 'QMessageBox.warning()', m.., ?W...QMessageBox.NoButton, N..)
    msg_box.setWindowFlags(?C...__.WindowStaysOnTopHint)
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
    msg_box.addButton(cancel_label, ?W...QMessageBox.RejectRole)
    __ msg_box.exec_() __ ?W...QMessageBox.AcceptRole:
        r_ T..
    ____
        r_ F..
        r_


___ show_path_browser(title):
    dialog = ?W...QFileDialog()
    dialog.setWindowFlags(?C...__.WindowStaysOnTopHint)
    dialog.sQT..(title)
    dialog.setFileMode(?W...QFileDialog.Directory)
    dialog.setOption(?W...QFileDialog.ShowDirsOnly)
    __ dialog.exec_() __ ?W...QDialog.Accepted:
        r_ dialog.selectedFiles()[0]


___ update_settings(key, value):
    xml, root, tree = get_xml_elements()
    ___ setting __ root.find('settings').f_a_('setting'):
        __ setting.get('name') __ key:
            setting.text = value

    w__ o..(xml, 'w') __ xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=T..)


___ get_menus(all_incl = T.., exclude_prefix = '_'):
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
                w__ o..(xml_path, 'r') __ xml_file:
                    ET.fromstring(xml_file.read())
                menus.ap..(xml_name)
            except ET.ParseError:
                write_log('Skip non well formed menu collection: {}'.f..(xml_path))

    r_ menus


___ add_command(collection_name, command_path, color = N.., hotkey = N..):
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
    w__ o..(xml, 'w') __ file_:
        prettyprint(root)
        tree.write(file_, encoding='utf-8', xml_declaration=T..)


___ sanitize(string):
    r_ re.sub('[^a-zA-Z0-9+]', '', string)


___ get_history_xml():
    ____ smartCommand.constants ______ HISTORY
    r_ __.path.join(get_tool_root('private'), '{}.xml'.f..(HISTORY))


___ swap_commands(xml, path_1, path_2):
    tree = ET.parse(xml)
    root = tree.getroot()
    command_1 = N..
    command_2 = N..
    index_1 = 0
    index_2 = 0
    index = 0
    ___ command __ root.find('collection').f_a_('command'):
        __ command.text __ path_1:
            command_1 = command
            index_1 = index
        ____ command.text __ path_2:
            command_2 = command
            index_2 = index
        index += 1

    __ no. all((command is no. N.. ___ command __ [command_1, command_2])):
        raise ValueError('No such sufficient data to swap.')
    root.find('collection').remove(command_2)
    root.find('collection').insert(index_1, command_2)
    root.find('collection').remove(command_1)
    root.find('collection').insert(index_2, command_1)
    w__ o..(xml, 'w') __ file_:
        prettyprint(root)
        tree.write(file_, encoding='utf-8', xml_declaration=T..)
    r_


___ get_collection_xml(name):
    collection_root = get_collection_root()
    xml = __.path.join(collection_root, '{}.xml'.f..(name))
    __ no. __.path.isfile(xml):
        raise IOError('No such collection xml: {}'.f..(xml))
    r_ xml


___ remove_history_commands(xml, history_max):
    tree = ET.parse(xml)
    root = tree.getroot()
    index = 1
    ___ command __ root.find('collection').f_a_('command'):
        __ index > history_max:
            root.find('collection').remove(command)
        index += 1

    w__ o..(xml, 'w') __ file_:
        prettyprint(root)
        tree.write(file_, encoding='utf-8', xml_declaration=T..)


___ create_collection(collection_name):
    __ collection_name __ 'history':
        collection_root = get_tool_root('private')
    ____
        collection_root = load_settings()['collection_root']
    xml = __.path.join(collection_root, '{}.xml'.f..(collection_name))
    __ no. __.path.isfile(xml):
        write_log("Create new collection '{}.xml'".f..(collection_name))
        w__ o..(xml, 'w') __ file_:
            file_.write(templates.COLLECTION.f..(collection_name=collection_name))
    r_ xml


___ remove_command_duplicates(menu, command_path):
    equals = [ command_elem ___ command_elem __ menu.f_a_('command') __ command_elem.text __ command_path ]
    ___ element __ equals:
        menu.remove(element)

    r_ menu


___ get_command_object(path):
    command = ?.menu('Nuke').findItem(path)
    __ no. command:
        r_ N..
    ____
        r_ command


___ get_next_element(list_, current):
    ___
        r_ list_[list_.index(current) + 1]
    except IndexError:
        r_ list_[0]


___ get_previous_element(list_, current):
    ___
        r_ list_[list_.index(current) - 1]
    except IndexError:
        r_ list_[le.(list_)]


___ update_command(xml, path, key, value):
    __ no. __.path.isfile(xml):
        raise IOError('No such collection file: {}'.f..(xml))
    tree = ET.parse(xml)
    root = tree.getroot()
    ___ command __ root.find('collection').f_a_('command'):
        __ command.text __ path:
            command.set(key, value)
            w__ o..(xml, 'w') __ xml:
                prettyprint(root)
                tree.write(xml, encoding='utf-8', xml_declaration=T..)
            break
    ____
        raise ValueError('No such command path: {}'.f..(path))


___ remove_command(xml, path):
    __ no. __.path.isfile(xml):
        raise IOError('No such collection xml: {}'.f..(xml))
    tree = ET.parse(xml)
    root = tree.getroot()
    ___ command __ root.find('collection').f_a_('command'):
        __ command.text __ path:
            root.find('collection').remove(command)
            w__ o..(xml, 'w') __ xml:
                prettyprint(root)
                tree.write(xml, encoding='utf-8', xml_declaration=T..)
            break
    ____
        raise ValueError('No such command path: {}'.f..(path))


___ get_basename(path):
    out = path
    sep = '/'
    __ sep __ path:
        out = path.split(sep)[-1]
    r_ out


___ get_all_hotkeys():
    hotkey_commands = {}
    collection_root = get_collection_root()
    ___ collection __ get_menus(all_incl=F..):
        xml = '{}.xml'.f..(collection)
        tree = ET.parse(__.path.join(collection_root, xml))
        root = tree.getroot()
        ___ command __ root.find('collection').f_a_('command'):
            __ command.get('hotkey'):
                hotkey_commands[command.get('hotkey')] = [command.text, xml]

    r_ hotkey_commands


___ initialize_hotkeys():
    hotkey_commands = get_all_hotkeys()
    ___ hotkey, command __ hotkey_commands.items():
        path = command[0]
        command_item = ?.menu('Nuke').findItem(path)
        __ command_item:
            command_item.setShortcut(hotkey)


___ load_tooltips(parent, section):
    this_dir = __.path.dirname( -f)
    tooltips_file = __.path.join(this_dir, 'data', 'tooltips.json')
    tooltips_file = __.path.n_p_(tooltips_file)
    __ no. __.path.isfile(tooltips_file):
        r_
    w__ o..(tooltips_file) __ json_file:
        ___
            ttdata = j___.load(json_file)
        except ValueError:
            write_log('Non well-formed tooltips file. Cannot parse file.')
            r_

    ___ widget __ parent.findChildren(?C...QObject):
        ___ t __ ttdata[section]:
            __ t['tt'] __ widget.property('tt'):
                widget.setToolTip('<strong>{}</strong><br />{}'.f..(t['ttt'], t['ttc']))


___ open_website(url):
    __ ___.pl.. __ 'win32':
        __.startfile(url)
    ____ ___.pl.. __ 'darwin':
        subprocess.P..(['open', url])
    ____
        ___
            subprocess.P..(['xdg-open', url])
        except OSError:
            msg = 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.f..(url)
            ____ smartCommand ______ dialogs
            dialogs.show_message_box(N.., msg)

    r_


___ get_basename(path, extension = F..):
    basename = __.path.basename(path)
    __ extension:
        r_ basename
    r_ __.path.splitext(basename)[0]


___ get_module_docstring(path):
    compile_ = compile(o..(path).read(), path, 'exec')
    __ compile_.co_consts and i..(compile_.co_consts[0], basestring):
        docstring = compile_.co_consts[0]
    ____
        docstring = N..
    r_ docstring


___ center_window(window):
    geometry = window.frameGeometry()
    centerpoint = ?W...QDesktopWidget().availableGeometry().center()
    geometry.moveCenter(centerpoint)
    window.move(geometry.topLeft())


___ get_cursor_position():
    r_ ?G...QCursor().pos()