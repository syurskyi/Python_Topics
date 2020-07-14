# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartLink_v1.0.1/smartLink/helper.py
______ j___
______ __
______ re
______ subprocess
______ ___
______ ti__
______ uuid
______ xml.etree.ElementTree __ ET
____ collections ______ OrderedDict
______ ?
__ ?.NUKE_VERSION_MAJOR < 11:
    ____ ? ______ ?C..
    ____ ? ______ ?G..
    ____ ? ______ ?G.. __ ?W..
____
    ____ ? ______ ?C..
    ____ ? ______ ?G..
    ____ ? ______ ?W..
____ smartLink ______ dialogs
____ smartLink ______ templates
____ smartLink.info ______ __product__
____ smartLink.constants ______ ALT, CTRL, KEY, FAVORITES, PREFIX_FAVORITES, SHIFT, SMARTLINK

___ load_icons():
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
    widget_to_move.xy _ event.globalPos() - ?C...QPoint(x, y)
    widget_to_move.move(widget_to_move.xy)


___ get_tool_root(which):
    __ which __ 'private':
        cragl_dir _ '.cragl'
    ____
        cragl_dir _ 'cragl'
    root _ __.pa__.j..(__.pa__.expanduser('~'), cragl_dir, __product__)
    __ no. __.pa__.isd..(root):
        ___
            __.m_d_(root)
        except IOError:
            write_log('unable to create open tool dir at: {}'.f..(root))

    r_ root


___ write_log(text, tool _ 'li'):
    w__ o..(get_log_file(), 'a') __ file_:
        log_time_format _ '%d.%m.%Y %H:%M:%S'
        log_time _ ti__.strftime(log_time_format, ti__.localtime())
        file_.w..('{}: {} {}\n'.f..(log_time, tool, text))


___ get_log_file():
    connect_dir _ __.pa__.j..(__.pa__.expanduser('~'), '.cragl', 'connect')
    __ no. __.pa__.isd..(connect_dir):
        __.m_d_(connect_dir)
    log_file _ __.pa__.j..(connect_dir, 'connectlog.txt')
    __ no. __.pa__.isf..(log_file):
        w__ o..(log_file, 'w') __ lf:
            log_template _ 'connect log\n{}\n'.f..('-' * 50)
            lf.w..(log_template)
    r_ log_file


___ load_settings():
    settings_xml _ get_settings_xml()
    settings _ {}
    __ check_xml_ok(settings_xml):
        settings_tree _ ET.parse(settings_xml)
        settings_root _ settings_tree.getroot()
        ___ setting __ settings_root.find('settings').f_a_('setting'):
            value _ setting.text
            __ value __ 'True':
                value _ T..
            ____ value __ 'False':
                value _ F..
            ____ ',' __ value:
                value _ [ val.strip() ___ val __ value.split(',') ]
            settings[setting.get('name')] _ value

    r_ settings


___ load_presets():
    settings_xml _ get_settings_xml()
    presets _ OrderedDict()
    __ check_xml_ok(settings_xml):
        settings_tree _ ET.parse(settings_xml)
        settings_root _ settings_tree.getroot()
        ___ preset __ settings_root.find('backdrops').f_a_('backdrop'):
            presets[preset.get('name')] _ {'icon': preset.get('icon'),
             'color': [ float(val.strip()) ___ val __ preset.get('color').split(',') ]}

    r_ presets


___ get_xml_elements():
    xml _ get_settings_xml()
    tree _ ET.parse(xml)
    root _ tree.getroot()
    r_ (xml, root, tree)


___ get_settings_xml():
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


___ clear_layout(layout):
    while layout.count():
        child _ layout.takeAt(0)
        __ child.widget():
            child.widget().deleteLater()


___ move_layout_elements(source_layout, dest_layout):
    while source_layout.count():
        element _ source_layout.takeAt(0)
        ___
            dest_layout.addLayout(element)
        except TypeError:
            ___
                dest_layout.aW..(element)
            except TypeError:
                dest_layout.addStretch()


___ clear_combobox(combobox):
    while combobox.count():
        combobox.clear()


___ check_xml_values_exist():
    ___ key, value __ templates.SETTINGS_DEFAULT_VALUES.i..():
        check_xml_value_exists('settings', 'setting', 'name', key, value)


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
        __ no. elem.text or no. elem.text.strip():
            elem.text _ i + '  '
        __ no. elem.tail or no. elem.tail.strip():
            elem.tail _ i
        ___ elem __ elem:
            prettyprint(elem, level + 1)

        __ no. elem.tail or no. elem.tail.strip():
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
        reset_settings_xml _ dialogs.ask_dialog(m.., process_label_'reset', color_process_'actionButton')
        __ reset_settings_xml:
            __ __.pa__.isf..(xml):
                __.remove(xml)
                get_settings_xml()


___ update_settings(key, value):
    xml, root, tree _ get_xml_elements()
    ___ setting __ root.find('settings').f_a_('setting'):
        __ setting.get('name') __ key:
            setting.text _ value
            w__ o..(xml, 'w') __ xml:
                prettyprint(root)
                tree.w..(xml, encoding_'utf-8', xml_declaration_T..)
            r_

    raise ValueError("Invalid key '{}'. No such key in settings.".f..(key))


___ update_preset(preset_name, key, value):
    xml, root, tree _ get_xml_elements()
    ___ preset __ root.find('backdrops').f_a_('backdrop'):
        __ preset.get('name') __ preset_name:
            preset.set(key, value)
            break

    w__ o..(xml, 'w') __ xml:
        prettyprint(root)
        tree.w..(xml, encoding_'utf-8', xml_declaration_T..)


___ load_tooltips(parent, section):
    this_dir _ __.pa__.d_n_( -f)
    tooltips_file _ __.pa__.j..(this_dir, 'data', 'tooltips.json')
    tooltips_file _ __.pa__.n_p_(tooltips_file)
    __ no. __.pa__.isf..(tooltips_file):
        r_
    w__ o..(tooltips_file) __ json_file:
        ___
            ttdata _ j___.l..(json_file)
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
            msg _ 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.f..(url)
            ____ smartLink ______ dialogs
            dialogs.show_message_box(N.., msg)

    r_


___ center_window(window):
    geometry _ window.frameGeometry()
    centerpoint _ ?W...QDesktopWidget().availableGeometry().center()
    geometry.moveCenter(centerpoint)
    window.move(geometry.topLeft())


___ move_window_under_cursor(window):
    position _ get_cursor_position()
    window_center _ ?C...QPoint(0.5 * window.width(), 0.5 * window.height())
    position _ position - window_center
    window.move(position)


___ get_cursor_position():
    r_ ?G...QCursor().pos()


___ create_uid():
    r_ str(uuid.uuid4())


___ get_next_link_name():

    ___ split_nr(string):
        regex _ re.compile('(\\d+)')
        element _ regex.split(string)
        r_ [ (in.(y) __ y.isdigit() ____ y) ___ y __ element ]

    ___ _increase(groups):
        index _ in.(groups.group(2)) + 1
        r_ '{}{}'.f..(groups.group(1), index)

    pattern _ '(link_)(\\d+)'
    node_names _ sorted([ node.name() ___ node __ ?.allNodes() __ re.search(pattern, node.name()) ], key_split_nr)
    __ node_names:
        r_ re.sub(pattern, _increase, node_names[-1])
    ____
        r_ 'link_1'


___ zoom(node):
    ?.zoom(1.0, (in.(node.xpos()), in.(node.ypos())))


___ get_repr_class_nodes():
    nodes _ # list
    ___ node_class __ ['PostageStamp', 'Dot']:
        nodes.extend(?.allNodes(node_class))

    r_ nodes


___ atoi(text):
    __ text.isdigit():
        r_ in.(text)
    r_ text


___ natural_keys(text):
    r_ [ atoi(c) ___ c __ re.split('(\\d+)', text) ]


___ list_from_string(string):
    __ i..(string, list):
        r_ string
    __ ',' __ string:
        r_ [ cls.strip() ___ cls __ string.split(',') ]
    r_ [string]


___ string_from_list(list_):
    __ i..(list_, list):
        r_ ', '.j..(list_)
    r_ str(list_)


___ get_root_favorites_knob():
    favorites_knob _ ?.root().knob(PREFIX_FAVORITES)
    __ favorites_knob:
        r_ favorites_knob
    ____
        r_ add_smartlink_tab_widgets()


___ add_smartlink_tab_widgets():
    root _ ?.root()
    __ SMARTLINK __ root.knobs():
        r_
    tab _ ?.T_K..(SMARTLINK)
    favorites _ ?.S_K..(PREFIX_FAVORITES, FAVORITES)
    favorites.setEnabled(F..)
    root.aK..(tab)
    root.aK..(favorites)
    r_ favorites


___ add_to_root_favorites(uid):
    favorites_knob _ get_root_favorites_knob()
    favorites _ [ fav.strip() ___ fav __ favorites_knob.gV...split(',') __ fav ]
    __ uid __ favorites:
        r_
    favorites.ap..(uid)
    favorites_knob.sV..(', '.j..(favorites))


___ remove_from_root_favorites(uid):
    favorites_knob _ get_root_favorites_knob()
    favorites _ [ fav.strip() ___ fav __ favorites_knob.gV...split(',') __ fav ]
    ___
        del favorites[favorites.index(uid)]
    except ValueError:
        r_

    favorites_knob.sV..(', '.j..(favorites))


___ rgb_to_hex(r, g, b):
    r_ in.('%02x%02x%02x%02x' % (r,
     g,
     b,
     1), 16)


___ swap_presets(preset1, preset2):

    ___ _find_preset(root, name):
        index _ 0
        ___ preset __ root.find('backdrops').f_a_('backdrop'):
            __ preset.get('name') __ name:
                r_ [preset, index]
            index +_ 1

    xml, root, tree _ get_xml_elements()
    presets _ # list
    presets.ap..(_find_preset(root, preset1))
    presets.ap..(_find_preset(root, preset2))
    __ no. all(presets):
        raise ValueError("No sufficient information to swap. At least one of the presets of '{}', '{}' doesn't exist.".f..(preset1, preset2))
    root.find('backdrops').remove(presets[0][0])
    root.find('backdrops').insert(presets[0][1], presets[1][0])
    root.find('backdrops').remove(presets[1][0])
    root.find('backdrops').insert(presets[1][1], presets[0][0])
    w__ o..(xml, 'w') __ xml:
        prettyprint(root)
        tree.w..(xml, encoding_'utf-8', xml_declaration_T..)


___ remove_preset(name):
    xml, root, tree _ get_xml_elements()
    ___ preset __ root.find('backdrops').f_a_('backdrop'):
        __ preset.get('name') __ name:
            root.find('backdrops').remove(preset)
            break

    w__ o..(xml, 'w') __ xml:
        prettyprint(root)
        tree.w..(xml, encoding_'utf-8', xml_declaration_T..)


___ add_preset(name, color, icon):
    xml, root, tree _ get_xml_elements()
    elem _ ET.Element('backdrop')
    elem.set('name', name)
    elem.set('color', color)
    elem.set('icon', icon)
    root.find('backdrops').ap..(elem)
    w__ o..(xml, 'w') __ xml:
        prettyprint(root)
        tree.w..(xml, encoding_'utf-8', xml_declaration_T..)


___ add_to_favorites():
    ____ smartLink ______ nodes
    sel_nodes _ ?.sN..
    __ no. sel_nodes:
        msg _ 'Please select nodes that you would like to add to favorites.'
        dialogs.show_message_box(N.., msg)
        r_
    ____
        ___ node __ sel_nodes:
            nodes.NodeObject.register_link_tab(node_node)
            uid _ nodes.NodeObject.get_uid(node)
            add_to_root_favorites(uid)

        ___
            ?.cragl_smartlinker.reload()
        except AttributeError:
            pass

        r_


___ get_main_window():
    ___
        module _ ?W..
    except AttributeError:
        module _ ?G..

    ___
        r_ module.?A..(___.argv)
    except RuntimeError:
        r_ module.?A...ins..)