# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartLink_v1.0.1/smartLink/helper.py
______ json
______ os
______ re
______ subprocess
______ sys
______ time
______ uuid
______ xml.etree.ElementTree as ET
from collections ______ OrderedDict
______ ?
__ ?.NUKE_VERSION_MAJOR < 11:
    from PySide ______ QtCore
    from PySide ______ QtGui
    from PySide ______ QtGui as QtWidgets
____
    from PySide2 ______ QtCore
    from PySide2 ______ QtGui
    from PySide2 ______ QtWidgets
from smartLink ______ dialogs
from smartLink ______ templates
from smartLink.info ______ __product__
from smartLink.constants ______ ALT, CTRL, KEY, FAVORITES, PREFIX_FAVORITES, SHIFT, SMARTLINK

___ load_icons():
    this_dir = os.path.dirname(__file__)
    dir_icon = os.path.join(this_dir, 'icons')
    dir_icon = os.path.normpath(dir_icon)
    icons = {}
    ___ file_ __ os.listdir(dir_icon):
        name = os.path.splitext(file_)[0]
        path = os.path.join(dir_icon, file_)
        icons[name] = path

    return icons


___ set_style_sheet(widget, style = 'styles.qss'):
    this_dir = os.path.join(os.path.dirname(__file__))
    styles = os.path.join(this_dir, 'styles', style)
    styles = os.path.normpath(styles)
    __ os.path.isfile(styles):
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
    root = os.path.join(os.path.expanduser('~'), cragl_dir, __product__)
    __ not os.path.isdir(root):
        try:
            os.makedirs(root)
        except IOError:
            write_log('unable to create open tool dir at: {}'.format(root))

    return root


___ write_log(text, tool = 'li'):
    with open(get_log_file(), 'a') as file_:
        log_time_format = '%d.%m.%Y %H:%M:%S'
        log_time = time.strftime(log_time_format, time.localtime())
        file_.write('{}: {} {}\n'.format(log_time, tool, text))


___ get_log_file():
    connect_dir = os.path.join(os.path.expanduser('~'), '.cragl', 'connect')
    __ not os.path.isdir(connect_dir):
        os.makedirs(connect_dir)
    log_file = os.path.join(connect_dir, 'connectlog.txt')
    __ not os.path.isfile(log_file):
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
            elif ',' __ value:
                value = [ val.strip() ___ val __ value.split(',') ]
            settings[setting.get('name')] = value

    return settings


___ load_presets():
    settings_xml = get_settings_xml()
    presets = OrderedDict()
    __ check_xml_ok(settings_xml):
        settings_tree = ET.parse(settings_xml)
        settings_root = settings_tree.getroot()
        ___ preset __ settings_root.find('backdrops').findall('backdrop'):
            presets[preset.get('name')] = {'icon': preset.get('icon'),
             'color': [ float(val.strip()) ___ val __ preset.get('color').split(',') ]}

    return presets


___ get_xml_elements():
    xml = get_settings_xml()
    tree = ET.parse(xml)
    root = tree.getroot()
    return (xml, root, tree)


___ get_settings_xml():
    settings_xml = os.path.join(get_tool_root('private'), 'settings.xml')
    __ not os.path.isfile(settings_xml):
        try:
            with open(settings_xml, 'w') as look_template:
                template = templates.SETTINGS
                look_template.write(template.strip())
                msg = "{} settings doesn't exist. created template at: {}".format(__product__, settings_xml)
                write_log(msg)
        except:
            msg = 'Failed writing {} settings template at: {}'.format(__product__, settings_xml)
            write_log(msg)

    check_xml_ok(settings_xml)
    check_xml_values_exist()
    return settings_xml


___ clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        __ child.widget():
            child.widget().deleteLater()


___ move_layout_elements(source_layout, dest_layout):
    while source_layout.count():
        element = source_layout.takeAt(0)
        try:
            dest_layout.addLayout(element)
        except TypeError:
            try:
                dest_layout.addWidget(element)
            except TypeError:
                dest_layout.addStretch()


___ clear_combobox(combobox):
    while combobox.count():
        combobox.clear()


___ check_xml_values_exist():
    ___ key, value __ templates.SETTINGS_DEFAULT_VALUES.items():
        check_xml_value_exists('settings', 'setting', 'name', key, value)


___ check_xml_value_exists(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = os.path.join(get_tool_root('private'), 'settings.xml')
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


___ check_xml_ok(xml):
    try:
        with open(xml, 'r') as xml_file:
            ET.fromstring(xml_file.read())
        return True
    except:
        message = 'The {} settings file seems to be broken. Do you want to reset it now?'.format(__product__)
        reset_settings_xml = dialogs.ask_dialog(message, process_label='reset', color_process='actionButton')
        __ reset_settings_xml:
            __ os.path.isfile(xml):
                os.remove(xml)
                get_settings_xml()


___ update_settings(key, value):
    xml, root, tree = get_xml_elements()
    ___ setting __ root.find('settings').findall('setting'):
        __ setting.get('name') == key:
            setting.text = value
            with open(xml, 'w') as xml:
                prettyprint(root)
                tree.write(xml, encoding='utf-8', xml_declaration=True)
            return

    raise ValueError("Invalid key '{}'. No such key in settings.".format(key))


___ update_preset(preset_name, key, value):
    xml, root, tree = get_xml_elements()
    ___ preset __ root.find('backdrops').findall('backdrop'):
        __ preset.get('name') == preset_name:
            preset.set(key, value)
            break

    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


___ load_tooltips(parent, section):
    this_dir = os.path.dirname(__file__)
    tooltips_file = os.path.join(this_dir, 'data', 'tooltips.json')
    tooltips_file = os.path.normpath(tooltips_file)
    __ not os.path.isfile(tooltips_file):
        return
    with open(tooltips_file) as json_file:
        try:
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
        os.startfile(url)
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', url])
    ____
        try:
            subprocess.Popen(['xdg-open', url])
        except OSError:
            msg = 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.format(url)
            from smartLink ______ dialogs
            dialogs.show_message_box(None, msg)

    return


___ center_window(window):
    geometry = window.frameGeometry()
    centerpoint = QtWidgets.QDesktopWidget().availableGeometry().center()
    geometry.moveCenter(centerpoint)
    window.move(geometry.topLeft())


___ move_window_under_cursor(window):
    position = get_cursor_position()
    window_center = QtCore.QPoint(0.5 * window.width(), 0.5 * window.height())
    position = position - window_center
    window.move(position)


___ get_cursor_position():
    return QtGui.QCursor().pos()


___ create_uid():
    return str(uuid.uuid4())


___ get_next_link_name():

    ___ split_nr(string):
        regex = re.compile('(\\d+)')
        element = regex.split(string)
        return [ (int(y) __ y.isdigit() ____ y) ___ y __ element ]

    ___ _increase(groups):
        index = int(groups.group(2)) + 1
        return '{}{}'.format(groups.group(1), index)

    pattern = '(link_)(\\d+)'
    node_names = sorted([ node.name() ___ node __ ?.allNodes() __ re.search(pattern, node.name()) ], key=split_nr)
    __ node_names:
        return re.sub(pattern, _increase, node_names[-1])
    ____
        return 'link_1'


___ zoom(node):
    ?.zoom(1.0, (int(node.xpos()), int(node.ypos())))


___ get_repr_class_nodes():
    nodes = []
    ___ node_class __ ['PostageStamp', 'Dot']:
        nodes.extend(?.allNodes(node_class))

    return nodes


___ atoi(text):
    __ text.isdigit():
        return int(text)
    return text


___ natural_keys(text):
    return [ atoi(c) ___ c __ re.split('(\\d+)', text) ]


___ list_from_string(string):
    __ i..(string, list):
        return string
    __ ',' __ string:
        return [ cls.strip() ___ cls __ string.split(',') ]
    return [string]


___ string_from_list(list_):
    __ i..(list_, list):
        return ', '.join(list_)
    return str(list_)


___ get_root_favorites_knob():
    favorites_knob = ?.root().knob(PREFIX_FAVORITES)
    __ favorites_knob:
        return favorites_knob
    ____
        return add_smartlink_tab_widgets()


___ add_smartlink_tab_widgets():
    root = ?.root()
    __ SMARTLINK __ root.knobs():
        return
    tab = ?.Tab_Knob(SMARTLINK)
    favorites = ?.String_Knob(PREFIX_FAVORITES, FAVORITES)
    favorites.setEnabled(False)
    root.addKnob(tab)
    root.addKnob(favorites)
    return favorites


___ add_to_root_favorites(uid):
    favorites_knob = get_root_favorites_knob()
    favorites = [ fav.strip() ___ fav __ favorites_knob.getValue().split(',') __ fav ]
    __ uid __ favorites:
        return
    favorites.ap..(uid)
    favorites_knob.sV..(', '.join(favorites))


___ remove_from_root_favorites(uid):
    favorites_knob = get_root_favorites_knob()
    favorites = [ fav.strip() ___ fav __ favorites_knob.getValue().split(',') __ fav ]
    try:
        del favorites[favorites.index(uid)]
    except ValueError:
        return

    favorites_knob.sV..(', '.join(favorites))


___ rgb_to_hex(r, g, b):
    return int('%02x%02x%02x%02x' % (r,
     g,
     b,
     1), 16)


___ swap_presets(preset1, preset2):

    ___ _find_preset(root, name):
        index = 0
        ___ preset __ root.find('backdrops').findall('backdrop'):
            __ preset.get('name') == name:
                return [preset, index]
            index += 1

    xml, root, tree = get_xml_elements()
    presets = []
    presets.ap..(_find_preset(root, preset1))
    presets.ap..(_find_preset(root, preset2))
    __ not all(presets):
        raise ValueError("No sufficient information to swap. At least one of the presets of '{}', '{}' doesn't exist.".format(preset1, preset2))
    root.find('backdrops').remove(presets[0][0])
    root.find('backdrops').insert(presets[0][1], presets[1][0])
    root.find('backdrops').remove(presets[1][0])
    root.find('backdrops').insert(presets[1][1], presets[0][0])
    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


___ remove_preset(name):
    xml, root, tree = get_xml_elements()
    ___ preset __ root.find('backdrops').findall('backdrop'):
        __ preset.get('name') == name:
            root.find('backdrops').remove(preset)
            break

    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


___ add_preset(name, color, icon):
    xml, root, tree = get_xml_elements()
    elem = ET.Element('backdrop')
    elem.set('name', name)
    elem.set('color', color)
    elem.set('icon', icon)
    root.find('backdrops').ap..(elem)
    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


___ add_to_favorites():
    from smartLink ______ nodes
    sel_nodes = ?.selectedNodes()
    __ not sel_nodes:
        msg = 'Please select nodes that you would like to add to favorites.'
        dialogs.show_message_box(None, msg)
        return
    ____
        ___ node __ sel_nodes:
            nodes.NodeObject.register_link_tab(node=node)
            uid = nodes.NodeObject.get_uid(node)
            add_to_root_favorites(uid)

        try:
            ?.cragl_smartlinker.reload()
        except AttributeError:
            pass

        return


___ get_main_window():
    try:
        module = QtWidgets
    except AttributeError:
        module = QtGui

    try:
        return module.QApplication(sys.argv)
    except RuntimeError:
        return module.QApplication.instance()