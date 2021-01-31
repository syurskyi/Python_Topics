# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartCommand_v1.0.0/smartCommand/helper.py
______ j___
______ __
______ ti__
______ pl..
______ re
______ su__
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

___ load_icons
    this_dir _ __.pa__.d_n_( -f)
    dir_icon _ __.pa__.j..(this_dir, 'icons')
    dir_icon _ __.pa__.n_p_(dir_icon)
    icons _ {}
    ___ file_ __ __.l_d_(dir_icon):
        name _ __.pa__.s_t_(file_)[0]
        pa__ _ __.pa__.j..(dir_icon, file_)
        icons[name] _ pa__

    r_ icons


___ set_style_sheet(widget, style _ 'styles.qss'):
    this_dir _ __.pa__.j..(__.pa__.d_n_( -f))
    styles _ __.pa__.j..(this_dir, 'styles', style)
    styles _ __.pa__.n_p_(styles)
    __ __.pa__.isf..(styles):
        w__ o..(styles) __ file_:
            widget.setStyleSheet(file_.read())


___ move_widget(widget_to_move, click_pos, event):
    x, y _ click_pos
    widget_to_move.xy _ event.globalPos() - ?C..._P..(x, y)
    widget_to_move.move(widget_to_move.xy)


___ get_tool_root(which):
    __ which __ 'private':
        cragl_dir _ '.cragl'
    ____
        cragl_dir _ 'cragl'
    root _ __.pa__.j..(__.pa__.e__('~'), cragl_dir, __product__)
    __ no. __.pa__.isd..(root):
        ___
            __.m_d_(root)
        ______ IOError:
            write_log('unable to create open tool dir at: {}'.f..(root))

    r_ root


___ write_log(text, tool _ 'sc'):
    w__ o..(get_log_file(), 'a') __ file_:
        log_time_format _ '%d.%m.%Y %H:%M:%S'
        log_time _ ti__.s_t_(log_time_format, ti__.localtime())
        file_.w..('{}: {} {}\n'.f..(log_time, tool, text))


___ get_log_file
    connect_dir _ __.pa__.j..(__.pa__.e__('~'), '.cragl', 'connect')
    __ no. __.pa__.isd..(connect_dir):
        __.m_d_(connect_dir)
    log_file _ __.pa__.j..(connect_dir, 'connectlog.txt')
    __ no. __.pa__.isf..(log_file):
        w__ o..(log_file, 'w') __ lf:
            log_template _ 'connect log\n{}\n'.f..('-' * 50)
            lf.w..(log_template)
    r_ log_file


___ load_settings
    settings_xml _ get_settings_xml()
    settings _ {}
    __ check_xml_ok(settings_xml):
        settings_tree _ ET.parse(settings_xml)
        settings_root _ settings_tree.getroot()
        ___ setting __ settings_root.find('settings').f_a_('setting'):
            v..  _ setting.text
            __ v..  __ 'True':
                v..  _ T..
            ____ v..  __ 'False':
                v..  _ F..
            settings[setting.get('name')] _ v..

    r_ settings


___ get_collection_root
    collection_root _ load_settings()['collection_root']
    __ no. __.pa__.isd..(collection_root):
        ___
            __.m_d_(collection_root)
        ______ OSError:
            msg _ "Cannot create menu direcory in '{}'. Please set a different path.".f..(collection_root)
            ?.m..(msg)

    r_ collection_root


___ get_scriptlets_root
    scriptlet_root _ load_settings()['scriptlets']
    __ no. __.pa__.isd..(scriptlet_root):
        ___
            __.m_d_(scriptlet_root)
        ______ OSError:
            msg _ "Cannot create scriptlet direcory in '{}'. Please set a different path.".f..(scriptlet_root)
            ?.m..(msg)

    r_ scriptlet_root


___ default_collection_root
    root _ __.pa__.j..(get_tool_root('public'), 'collections')
    __ no. __.pa__.isd..(root):
        __.m_d_(root)
    r_ root


___ default_scriptlets_root
    root _ __.pa__.j..(get_tool_root('public'), 'scriptlets')
    __ no. __.pa__.isd..(root):
        __.m_d_(root)
    r_ root


___ create_default_data_roots
    default_collection_root()
    default_scriptlets_root()


___ get_xml_elements
    xml _ get_settings_xml()
    tree _ ET.parse(xml)
    root _ tree.getroot()
    r_ (xml, root, tree)


___ get_settings_xml
    settings_xml _ __.pa__.j..(get_tool_root('private'), 'settings.xml')
    __ no. __.pa__.isf..(settings_xml):
        ___
            w__ o..(settings_xml, 'w') __ look_template:
                template _ templates.SETTINGS
                look_template.w..(template.strip())
                msg _ "{} settings doesn't exist. created template at: {}".f..(__product__, settings_xml)
                write_log(msg)
        ______
            msg _ 'Failed writing {} settings template at: {}'.f..(__product__, settings_xml)
            write_log(msg)

    check_xml_ok(settings_xml)
    check_xml_values_exist()
    r_ settings_xml


___ check_xml_values_exist
    ___ key, v..  __ templates.SETTINGS_DEFAULT_VALUES.i..
        check_xml_value_exists('settings', 'setting', 'name', key, v.. )


___ check_xml_value_exists(parent, section, key1, value1, text, key2 _ '', value2 _ ''):
    xml _ __.pa__.j..(get_tool_root('private'), 'settings.xml')
    tree _ ET.parse(xml)
    root _ tree.getroot()
    debug _ F..
    item_found _ 0
    ___ child __ root.find(parent).f_a_(section):
        __ child.get(key1) __ value1:
            item_found +_ 1
            __ debug:
                print '{} | settings exists: {}|{}|{}|{}|{}|{}|{}'.f..(__product__, parent, section, key1, value1, text, key2, value2)
            r_

    __ item_found __ 0:
        elem _ ET.Element(section)
        elem.set(key1, value1)
        __ key2 !_ '':
            elem.set(key2, value2)
        elem.text _ text
        root.find(parent).ap..(elem)
        w__ o..(xml, 'w') __ xml:
            prettyprint(root)
            tree.w..(xml, encoding_'utf-8', xml_declaration_T..)
        write_log('settings xml added: {}|{}|{}|{}|{}|{}|{}'.f..(parent, section, key1, value1, text, key2, value2))


___ prettyprint(elem, level _ 0):
    i _ '\n' + level * '  '
    __ le.(elem):
        __ no. elem.text or no. elem.text.strip
            elem.text _ i + '  '
        __ no. elem.tail or no. elem.tail.strip
            elem.tail _ i
        ___ elem __ elem:
            prettyprint(elem, level + 1)

        __ no. elem.tail or no. elem.tail.strip
            elem.tail _ i
    ____ level an. (no. elem.tail or no. elem.tail.strip()):
        elem.tail _ i


___ check_xml_ok(xml):
    ___
        w__ o..(xml, 'r') __ xml_file:
            ET.fromstring(xml_file.read())
        r_ T..
    ______
        m.. _ 'The {} settings file seems to be broken. Do you want to reset it now?'.f..(__product__)
        reset_settings_xml _ ask_dialog(m.., process_label_'reset', color_process_'actionButton')
        __ reset_settings_xml:
            __ __.pa__.isf..(xml):
                __.r__(xml)
                get_settings_xml()


___ ask_dialog(m.., process_label _ 'ok', color_process _ 'actionButton', cancel_label _ 'cancel'):
    msg_box _ ?W...QMessageBox(?W...QMessageBox.Warning, 'QMessageBox.warning()', m.., ?W...QMessageBox.NoButton, N..)
    msg_box.sWF..(?C...__.WindowStaysOnTopHint)
    msg_box.setObjectName('msgBox')
    msg_box.raise_()
    process_button _ msg_box.addButton(process_label, ?W...QMessageBox.AcceptRole)
    __ color_process !_ '':
        __ color_process __ 'actionButton':
            color_process _ '51, 204, 255, 100'
        style _ 'QPushButton {background-color: rgba(@)}' % color_process
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
    dialog _ ?W...QFileDialog()
    dialog.sWF..(?C...__.WindowStaysOnTopHint)
    dialog.sQT..(title)
    dialog.setFileMode(?W...QFileDialog.Directory)
    dialog.setOption(?W...QFileDialog.ShowDirsOnly)
    __ dialog.exec_() __ ?W...QDialog.Accepted:
        r_ dialog.selectedFiles()[0]


___ update_settings(key, v.. ):
    xml, root, tree _ get_xml_elements()
    ___ setting __ root.find('settings').f_a_('setting'):
        __ setting.get('name') __ key:
            setting.text _ v..

    w__ o..(xml, 'w') __ xml:
        prettyprint(root)
        tree.w..(xml, encoding_'utf-8', xml_declaration_T..)


___ get_menus(all_incl _ T.., exclude_prefix _ '_'):
    menus _ # list
    __ all_incl:
        menus.ap..('all')
    menu_root _ get_collection_root()
    ___ file_ __ __.l_d_(menu_root):
        __ file_.startswith(exclude_prefix):
            c___
        __ file_.endswith('.xml'):
            ___
                xml_path _ __.pa__.j..(menu_root, file_)
                xml_name _ __.pa__.s_t_(file_)[0]
                w__ o..(xml_path, 'r') __ xml_file:
                    ET.fromstring(xml_file.read())
                menus.ap..(xml_name)
            ______ ET.ParseError:
                write_log('Skip non well formed menu collection: {}'.f..(xml_path))

    r_ menus


___ add_command(collection_name, command_path, color _ N.., hotkey _ N..):
    xml _ create_collection(collection_name)
    tree _ ET.parse(xml)
    root _ tree.getroot()
    collection _ root.find('collection')
    remove_command_duplicates(collection, command_path)
    command_item _ ET.Element('command')
    command_item.text _ command_path
    __ color:
        command_item.set('color', st.(color))
    __ hotkey:
        command_item.set('hotkey', sanitize(hotkey))
    collection.insert(0, command_item)
    w__ o..(xml, 'w') __ file_:
        prettyprint(root)
        tree.w..(file_, encoding_'utf-8', xml_declaration_T..)


___ sanitize(string):
    r_ re.sub('[^a-zA-Z0-9+]', '', string)


___ get_history_xml
    ____ smartCommand.constants ______ HISTORY
    r_ __.pa__.j..(get_tool_root('private'), '{}.xml'.f..(HISTORY))


___ swap_commands(xml, path_1, path_2):
    tree _ ET.parse(xml)
    root _ tree.getroot()
    command_1 _ N..
    command_2 _ N..
    index_1 _ 0
    index_2 _ 0
    index _ 0
    ___ command __ root.find('collection').f_a_('command'):
        __ command.text __ path_1:
            command_1 _ command
            index_1 _ index
        ____ command.text __ path_2:
            command_2 _ command
            index_2 _ index
        index +_ 1

    __ no. all((command __ no. N.. ___ command __ [command_1, command_2])):
        raise ValueError('No such sufficient data to swap.')
    root.find('collection').r__(command_2)
    root.find('collection').insert(index_1, command_2)
    root.find('collection').r__(command_1)
    root.find('collection').insert(index_2, command_1)
    w__ o..(xml, 'w') __ file_:
        prettyprint(root)
        tree.w..(file_, encoding_'utf-8', xml_declaration_T..)
    r_


___ get_collection_xml(name):
    collection_root _ get_collection_root()
    xml _ __.pa__.j..(collection_root, '{}.xml'.f..(name))
    __ no. __.pa__.isf..(xml):
        raise IOError('No such collection xml: {}'.f..(xml))
    r_ xml


___ remove_history_commands(xml, history_max):
    tree _ ET.parse(xml)
    root _ tree.getroot()
    index _ 1
    ___ command __ root.find('collection').f_a_('command'):
        __ index > history_max:
            root.find('collection').r__(command)
        index +_ 1

    w__ o..(xml, 'w') __ file_:
        prettyprint(root)
        tree.w..(file_, encoding_'utf-8', xml_declaration_T..)


___ create_collection(collection_name):
    __ collection_name __ 'history':
        collection_root _ get_tool_root('private')
    ____
        collection_root _ load_settings()['collection_root']
    xml _ __.pa__.j..(collection_root, '{}.xml'.f..(collection_name))
    __ no. __.pa__.isf..(xml):
        write_log("Create new collection '{}.xml'".f..(collection_name))
        w__ o..(xml, 'w') __ file_:
            file_.w..(templates.COLLECTION.f..(collection_name_collection_name))
    r_ xml


___ remove_command_duplicates(m__, command_path):
    equals _ [ command_elem ___ command_elem __ m__.f_a_('command') __ command_elem.text __ command_path ]
    ___ element __ equals:
        m__.r__(element)

    r_ m__


___ get_command_object(pa__):
    command _ ?.m__('Nuke').fI..(pa__)
    __ no. command:
        r_ N..
    ____
        r_ command


___ get_next_element(list_, current):
    ___
        r_ list_[list_.index(current) + 1]
    ______ IndexError:
        r_ list_[0]


___ get_previous_element(list_, current):
    ___
        r_ list_[list_.index(current) - 1]
    ______ IndexError:
        r_ list_[le.(list_)]


___ update_command(xml, pa__, key, v.. ):
    __ no. __.pa__.isf..(xml):
        raise IOError('No such collection file: {}'.f..(xml))
    tree _ ET.parse(xml)
    root _ tree.getroot()
    ___ command __ root.find('collection').f_a_('command'):
        __ command.text __ pa__:
            command.set(key, v.. )
            w__ o..(xml, 'w') __ xml:
                prettyprint(root)
                tree.w..(xml, encoding_'utf-8', xml_declaration_T..)
            break
    ____
        raise ValueError('No such command path: {}'.f..(pa__))


___ remove_command(xml, pa__):
    __ no. __.pa__.isf..(xml):
        raise IOError('No such collection xml: {}'.f..(xml))
    tree _ ET.parse(xml)
    root _ tree.getroot()
    ___ command __ root.find('collection').f_a_('command'):
        __ command.text __ pa__:
            root.find('collection').r__(command)
            w__ o..(xml, 'w') __ xml:
                prettyprint(root)
                tree.w..(xml, encoding_'utf-8', xml_declaration_T..)
            break
    ____
        raise ValueError('No such command path: {}'.f..(pa__))


___ get_basename(pa__):
    out _ pa__
    sep _ '/'
    __ sep __ pa__:
        out _ pa__.s..(sep)[-1]
    r_ out


___ get_all_hotkeys
    hotkey_commands _ {}
    collection_root _ get_collection_root()
    ___ collection __ get_menus(all_incl_F..):
        xml _ '{}.xml'.f..(collection)
        tree _ ET.parse(__.pa__.j..(collection_root, xml))
        root _ tree.getroot()
        ___ command __ root.find('collection').f_a_('command'):
            __ command.get('hotkey'):
                hotkey_commands[command.get('hotkey')] _ [command.text, xml]

    r_ hotkey_commands


___ initialize_hotkeys
    hotkey_commands _ get_all_hotkeys()
    ___ hotkey, command __ hotkey_commands.i..
        pa__ _ command[0]
        command_item _ ?.m__('Nuke').fI..(pa__)
        __ command_item:
            command_item.setShortcut(hotkey)


___ load_tooltips(parent, section):
    this_dir _ __.pa__.d_n_( -f)
    tooltips_file _ __.pa__.j..(this_dir, 'data', 'tooltips.json')
    tooltips_file _ __.pa__.n_p_(tooltips_file)
    __ no. __.pa__.isf..(tooltips_file):
        r_
    w__ o..(tooltips_file) __ json_file:
        ___
            ttdata _ j___.l..(json_file)
        ______ ValueError:
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
        su__.P..(['open', url])
    ____
        ___
            su__.P..(['xdg-open', url])
        ______ OSError:
            msg _ 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.f..(url)
            ____ smartCommand ______ dialogs
            dialogs.show_message_box(N.., msg)

    r_


___ get_basename(pa__, extension _ F..):
    b_n_ _ __.pa__.b_n_(pa__)
    __ extension:
        r_ b_n_
    r_ __.pa__.s_t_(b_n_)[0]


___ get_module_docstring(pa__):
    compile_ _ compile(o..(pa__).read(), pa__, 'exec')
    __ compile_.co_consts an. i..(compile_.co_consts[0], basestring):
        docstring _ compile_.co_consts[0]
    ____
        docstring _ N..
    r_ docstring


___ center_window(window):
    geometry _ window.frameGeometry()
    centerpoint _ ?W...QDesktopWidget().availableGeometry().center()
    geometry.moveCenter(centerpoint)
    window.move(geometry.topLeft())


___ get_cursor_position
    r_ ?G..._C..().p..