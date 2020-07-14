# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartLook_v2.0/smartLook/src/helper.py
______ ti__
______ hashlib
______ random
______ __
______ ___
______ subprocess
______ urllib
______ xml.etree.ElementTree __ ET
______ collections
______ pl..
______ struct
______ imghdr
______ j___
______ ?
______ ?
__ ?.NUKE_VERSION_MAJOR < 11:
    ____ ? ______ ?G.. __ ?W..
    ____ ? ______ ?G..
    ____ ? ______ ?C..
____
    ____ ? ______ ?W..
    ____ ? ______ ?G..
    ____ ? ______ ?C..
______ templates

___ load_icons(_args):
    this_dir _ __.pa__.d_n_( -f)
    dir_icon _ __.pa__.j..(this_dir, '../', 'icons')
    dir_icon _ __.pa__.n_p_(dir_icon)
    j.. _ __.pa__.j..
    r_ {'about': j..(dir_icon, 'about.jpg'),
     'icon_logo': j..(dir_icon, 'logo.png'),
     'icon_logo_grey': j..(dir_icon, 'logo_grey.png'),
     'icon_pool': j..(dir_icon, 'pool.png'),
     'icon_star': j..(dir_icon, 'look_star.png'),
     'icon_update': j..(dir_icon, 'look_update.png'),
     'icon_delete': j..(dir_icon, 'look_delete.png'),
     'icon_import': j..(dir_icon, 'look_import.png'),
     'icon_export': j..(dir_icon, 'look_export.png'),
     'icon_edit': j..(dir_icon, 'edit.png'),
     'icon_page': j..(dir_icon, 'page.png'),
     'icon_folder': j..(dir_icon, 'folder.png'),
     'icon_folder_white': j..(dir_icon, 'folder_white.png'),
     'icon_folder_grey': j..(dir_icon, 'folder_grey.png'),
     'icon_explorer': j..(dir_icon, 'explorer.png'),
     'icon_nuke': j..(dir_icon, 'nuke.png'),
     'icon_nodes': j..(dir_icon, 'nodes.png'),
     'icon_toolsets': j..(dir_icon, 'toolsets.png'),
     'icon_insert': j..(dir_icon, 'insert.png'),
     'icon_insert_nk': j..(dir_icon, 'insert_nk.png'),
     'icon_insert_img': j..(dir_icon, 'insert_img.jpg'),
     'icon_refresh': j..(dir_icon, 'refresh.png'),
     'icon_snapshot': j..(dir_icon, 'snapshot.png'),
     'icon_x': j..(dir_icon, 'x.png'),
     'icon_settings': j..(dir_icon, 'settings.png'),
     'icon_maximize': j..(dir_icon, 'maximize.png'),
     'icon_half': j..(dir_icon, 'half.png'),
     'icon_eye': j..(dir_icon, 'eye.png'),
     'icon_delete_all': j..(dir_icon, 'delete_all.png'),
     'icon_reveal': j..(dir_icon, 'reveal.png'),
     'icon_flag': j..(dir_icon, 'flag.png'),
     'icon_nocolor': j..(dir_icon, 'nocolor.png'),
     'icon_comment': j..(dir_icon, 'comment.png'),
     'icon_plus': j..(dir_icon, 'plus.png'),
     'icon_minus': j..(dir_icon, 'minus.png')}


___ load_settings(*args):
    settings_xml _ get_settings_xml()
    settings _ {}
    __ check_xml_ok(settings_xml):
        settingstree _ ET.parse(settings_xml)
        settingsroot _ settingstree.getroot()
        ___ setting __ settingsroot.find('settings').f_a_('setting'):
            settings[setting.get('name')] _ setting.text

        pools _ collections.OrderedDict()
        ___ pool __ settingsroot.find('pools').f_a_('pool'):
            pools[pool.get('name')] _ pool.text
            __ no. __.pa__.isd..(pool.text):
                ___
                    __.m_d_(pool.text)
                    msg _ 'created missing pools dir at {}'.f..(pool.text)
                    write_log(msg)
                except Exception __ error:
                    msg _ 'Unable to create pools dir at {}; {}'.f..(pool.text, error)
                    write_log(msg)

            pools_sorted _ collections.OrderedDict(sorted(pools.i..()))

        settings['pools'] _ pools_sorted
        flags _ # list
        ___ flag __ settingsroot.find('flags').f_a_('flag'):
            flags.ap..(flag.text)

        settings['flags'] _ flags
    r_ settings


___ load_hotkeys(*args):
    settings_xml _ get_settings_xml()
    hotkeys _ collections.OrderedDict()
    __ check_xml_ok(settings_xml):
        settingstree _ ET.parse(settings_xml)
        settingsroot _ settingstree.getroot()
        ___ setting __ settingsroot.find('hotkeys').f_a_('hotkey'):
            name _ setting.get('name')
            hotkeys[name] _ setting.text
            hotkeys['{}_ctrl'.f..(name)] _ setting.get('ctrl')
            hotkeys['{}_shift'.f..(name)] _ setting.get('shift')
            hotkeys['{}_alt'.f..(name)] _ setting.get('alt')

    r_ hotkeys


___ get_settings_xml(*args):
    settings_xml _ __.pa__.j..(get_tool_private_root(), 'settings.xml')
    __ no. __.pa__.isf..(settings_xml):
        ___
            w__ o..(settings_xml, 'w') __ look_template:
                template _ templates.SETTINGS.f..(standard_pool_get_standard_preset_pool())
                look_template.w..(template.strip())
                msg _ "smartLook settings doesn't exist. created template at: {}".f..(settings_xml)
                write_log(msg)
        ______
            msg _ 'Failed writing smartLook settings template at: {}'.f..(settings_xml)
            write_log(msg)

    check_xml_ok(settings_xml)
    check_xml_values_exist()
    r_ settings_xml


___ check_xml_values_exist(*args):
    default_snapshotdir _ __.pa__.j..(get_default_snapshot_root_dir(), 'temp')
    settings _ {'tooltips': 'True',
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
    ___ key, value __ settings.i..():
        check_xml_value_exists('settings', 'setting', 'name', key, value)


___ get_default_snapshot_root_dir(*args):
    default_snapshots_root _ __.pa__.j..(get_tool_public_root(), 'snapshots')
    __ no. __.pa__.isd..(default_snapshots_root):
        ___
            __.m_d_(default_snapshots_root)
        ______
            msg _ "Unable to create default snapshot root directory at: '{}'".f..(default_snapshots_root)
            show_message_box(N.., msg)

    r_ default_snapshots_root


___ load_advanced_settings(*args):
    advanced_settings _ __.pa__.j..(get_tool_public_root(), 'advancedsettings.set')
    advanced_settings_default _ templates.ADVANCED_SETTINGS_DEFAULT
    __ no. __.pa__.isf..(advanced_settings):
        ___
            w__ o..(advanced_settings, 'w') __ advset:
                advset.w..(advanced_settings_default)
        except Exception __ e:
            print e
            write_log('Error writing advanced settings file: {}'.f..(e))

    ___
        w__ o..(advanced_settings, 'r') __ advset:
            content _ advset.read()
    except Exception __ e:
        r_ 'Unable to read advanced settings file. {}'.f..(e)

    r_ content


___ parse_advanced_settings(*args):
    advanced_settings_lines _ # list
    advanced_settings _ {}
    vars_line _ '-lk'
    advanced_settings_file _ __.pa__.j..(get_tool_public_root(), 'advancedsettings.set')
    ___
        w__ o..(advanced_settings_file, 'r') __ advset:
            advanced_settings_lines _ [ line ___ line __ advset.readlines() __ line[:le.(vars_line)] __ vars_line ]
    ______
        pass

    ___ line __ advanced_settings_lines:
        key _ line.split('=')[0]
        key _ key.r..(vars_line, '')
        key _ key.strip()
        val _ line.split('=')[1]
        val _ val.strip()
        advanced_settings[key] _ val

    r_ advanced_settings


___ get_standard_preset_pool(*args):
    standardpool _ __.pa__.j..(get_tool_public_root(), 'standardpool')
    __ no. __.pa__.isd..(standardpool):
        __.m_d_(standardpool)
    r_ standardpool


___ check_xml_ok(xml, *args):
    ___
        w__ o..(xml, 'r') __ xml_file:
            ET.fromstring(xml_file.read())
        r_ T..
    ______
        m.. _ 'The smartLook settings file seems to be broken. Do you want to reset it now?'
        reset_settings_xml _ ask_dialog(m.., process_label_'reset', color_process_'actionButton')
        __ reset_settings_xml:
            __ __.pa__.isf..(xml):
                __.remove(xml)
                get_settings_xml()


___ show_message_box(window, m.., *args):
    msg _ ?W...QMessageBox()
    msg.setWindowFlags(?C...__.WindowStaysOnTopHint)
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
            msg _ 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.f..(url)
            show_message_box(N.., msg)

    r_


___ set_style_sheet(widget):
    this_dir _ __.pa__.d_n_( -f)
    styles _ __.pa__.j..(this_dir, '../', 'styles', 'styles.qss')
    styles _ __.pa__.n_p_(styles)
    __ __.pa__.isf..(styles):
        w__ o..(styles) __ file_:
            widget.setStyleSheet(file_.read())


___ get_topleft_coordinates(*args):
    x _ 0
    y _ 0
    offset _ 200
    ___ n __ ?.allNodes():
        __ n.xpos() < x:
            x _ n.xpos()
        __ n.ypos() < y:
            y _ n.ypos()

    r_ (x - offset, y - offset)


___ create_uid(*args):
    val _ '{}_{}'.f..(ti__.ti__(), random.random())
    r_ hashlib.md5(val).hexdigest()


___ find_looks_group(*args):
    ___
        r_ [ node ___ node __ ?.allNodes('Group') __ node.knob('looks_group') ][0]
    except IndexError:
        show_message_box(N.., "Cannot find 'looks' group in nodegraph.")

    r_


___ get_installed_root_dir(*args):
    root _ __.pa__.j..(__.pa__.d_n_( -f), '../', '../')
    r_ __.pa__.n_p_(root)


___ get_tool_public_root(*args):
    root _ __.pa__.j..(__.pa__.expanduser('~'), 'cragl', 'smartLook')
    __ no. __.pa__.isd..(root):
        ___
            __.m_d_(root)
        ______
            write_log('unable to create open dir')

    r_ root


___ get_tool_private_root(*args):
    root _ __.pa__.j..(__.pa__.expanduser('~'), '.cragl', 'smartLook')
    __ no. __.pa__.isd..(root):
        ___
            __.m_d_(root)
        ______
            write_log('unable to create open dir')

    r_ root


___ get_log_file(*args):
    connect_dir _ __.pa__.j..(__.pa__.expanduser('~'), '.cragl', 'connect')
    __ no. __.pa__.isd..(connect_dir):
        __.m_d_(connect_dir)
    log_file _ __.pa__.j..(connect_dir, 'connectlog.txt')
    __ no. __.pa__.isf..(log_file):
        w__ o..(log_file, 'w') __ lf:
            log_template _ 'connect log\n{}\n'.f..('-' * 50)
            lf.w..(log_template)
    r_ log_file


___ write_log(text, tool _ 'lk', *args):
    w__ o..(get_log_file(), 'a') __ file_:
        log_time_format _ '%d.%m.%Y %H:%M:%S'
        log_time _ ti__.strftime(log_time_format, ti__.localtime())
        file_.w..('{}: {} {}\n'.f..(log_time, tool, text))


___ check_web_connection(*args):
    ___
        urllib.urlopen('http://www.cragl.com')
        r_ T..
    ______
        r_ F..


___ check_xml_value_exists(parent, section, key1, value1, text, key2 _ '', value2 _ ''):
    xml _ __.pa__.j..(get_tool_private_root(), 'settings.xml')
    tree _ ET.parse(xml)
    root _ tree.getroot()
    debug _ F..
    item_found _ 0
    ___ child __ root.find(parent).f_a_(section):
        __ child.get(key1) __ value1:
            item_found +_ 1
            __ debug:
                print 'smartLook | settings exists: {}|{}|{}|{}|{}|{}|{}'.f..(parent, section, key1, value1, text, key2, value2)
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


___ build_hotkeys(*args):
    hotkeys _ load_hotkeys()
    hotkeys_build _ {}
    settings_xml _ get_settings_xml()
    settingstree _ ET.parse(settings_xml)
    settingsroot _ settingstree.getroot()
    elements _ # list
    ___ hotkey __ settingsroot.find('hotkeys').f_a_('hotkey'):
        elements.ap..(hotkey.get('name'))

    ___ e __ elements:
        hotkey _ ''
        __ hotkeys['{}_ctrl'.f..(e)] __ 'True':
            hotkey _ 'ctrl+'
        __ hotkeys['{}_shift'.f..(e)] __ 'True':
            hotkey +_ 'shift+'
        __ hotkeys['{}_alt'.f..(e)] __ 'True':
            hotkey +_ 'alt+'
        __ hotkeys[e] __ N..:
            hotkeys_build[e] _ ''
        ____
            hotkey +_ hotkeys[e]
            hotkeys_build[e] _ hotkey

    r_ hotkeys_build


___ set_hotkeys(*args):
    hotkeys _ build_hotkeys()
    hotkeys_dict _ {'snapshot browser': 'snapshotbrowser',
     'take snapshot': 'snapshot',
     'looks slider': 'looks_slider',
     '______ node | toolset': '______',
     'export node | toolset': 'export',
     "delete selected node's looks": 'delete_look_knobs',
     'set looks': 'set_looks',
     'resolution slider': 'resolution_slider',
     'settings': 'looks_settings'}
    ___
        ___ command, hotkey __ hotkeys_dict.i..():
            command_item _ ?.menu('Nuke').fI..('cragl/smartLook/{}'.f..(command))
            command_item.setShortcut(hotkeys[hotkey])

    except KeyError:
        pass


___ get_explorer_name(*args):
    __ ___.pl.. __ 'darwin':
        r_ 'finder'
    ____
        r_ 'explorer'


___ open_in_explorer(pa__, parent _ N.., *args):
    __ no. __.pa__.isd..(pa__):
        msg _ "Unable to open directory '{}'. The path doesn't exist.".f..(pa__)
        show_message_box(parent, msg)
        r_
    __ pl...system() __ 'Windows':
        __.startfile(pa__)
    ____ pl...system() __ 'Darwin':
        subprocess.P..(['open', pa__])
    ____
        subprocess.P..(['xdg-open', pa__])


___ build_tree_widget_item(parent, item_name, dirpath, disabled, selected, expanded _ F.., is_dir _ F.., enable_drag _ F.., icon _ ''):
    diritem _ ?W...QTreeWidgetItem(parent, [item_name])
    diritem.setData(0, ?C...__.UserRole, dirpath)
    __ enable_drag __ 'False':
        diritem.setFlags(?C...__.ItemIsSelectable | ?C...__.ItemIsEnabled | ?C...__.ItemIsUserCheckable)
    diritem.setExpanded(expanded)
    diritem.setSelected(selected)
    __ disabled:
        diritem.setDisabled(T..)
    dirpath _ __.pa__.n_p_(dirpath)
    __ is_dir:
        __ icon __ '':
            icon _ load_icons()['icon_folder_grey']
        diritem.setIcon(0, ?G...QIcon(icon))
    ____
        diritem.setIcon(0, ?G...QIcon(load_icons()['icon_nuke']))
    diritem.setData(0, ?C...__.UserRole, dirpath)
    r_ diritem


___ get_image_size(src, *args):
    w__ o..(src, 'rb') __ fhandle:
        head _ fhandle.read(24)
        __ le.(head) !_ 24:
            r_ (1, 1)
        __ imghdr.what(src) __ 'png':
            check _ struct.unpack('>i', head[4:8])[0]
            __ check !_ 218765834:
                r_ (1, 1)
            width, height _ struct.unpack('>ii', head[16:24])
        ____ imghdr.what(src) __ 'gif':
            width, height _ struct.unpack('<HH', head[6:10])
        ____ imghdr.what(src) __ 'jpeg':
            ___
                fhandle.seek(0)
                size _ 2
                ftype _ 0
                while no. 192 <_ ftype <_ 207:
                    fhandle.seek(size, 1)
                    byte _ fhandle.read(1)
                    while ord(byte) __ 255:
                        byte _ fhandle.read(1)

                    ftype _ ord(byte)
                    size _ struct.unpack('>H', fhandle.read(2))[0] - 2

                fhandle.seek(1, 1)
                height, width _ struct.unpack('>HH', fhandle.read(4))
            ______
                r_ (1, 1)

        ____
            r_
        r_ (width, height)


___ update_xml(key, value, *args):
    settings_xml _ get_settings_xml()
    settings_tree _ ET.parse(settings_xml)
    settings_root _ settings_tree.getroot()
    ___ setting __ settings_root.find('settings').f_a_('setting'):
        __ setting.get('name') __ key:
            setting.text _ value

    w__ o..(settings_xml, 'w') __ xml:
        prettyprint(settings_root)
        settings_tree.w..(xml, encoding_'utf-8', xml_declaration_T..)


___ center_window(window, *args):
    qr _ window.frameGeometry()
    cp _ ?W...QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


___ get_connected_nodes(node, *args):
    connected_nodes _ # list
    ignore_list _ ['Viewer']
    ?.clear_selection_recursive()
    node.setSelected(T..)
    connected_nodes.ap..(node)
    ?.selectConnectedNodes()
    ___ node __ ?.sN..:
        ___ dependency __ node.dependencies():
            dependency.setSelected(T..)

        ___ dependent __ node.dependent():
            dependent.setSelected(T..)

    ___ node __ ?.sN..:
        __ node.Class() no. __ ignore_list:
            connected_nodes.ap..(node)

    ?.clear_selection_recursive()
    r_ list(set(connected_nodes))


___ load_tooltips(parent, section, *args):
    this_dir _ __.pa__.d_n_( -f)
    tooltips_file _ __.pa__.j..(this_dir, '../', 'data', 'tooltips.json')
    tooltips_file _ __.pa__.n_p_(tooltips_file)
    __ no. __.pa__.isf..(tooltips_file):
        r_
    w__ o..(tooltips_file) __ json_file:
        ttdata _ j___.l..(json_file)
    ___ widget __ parent.findChildren(?C...QObject):
        ___ t __ ttdata[section]:
            __ t['tt'] __ widget.property('tt'):
                widget.setToolTip('<strong>{}</strong><br />{}'.f..(t['ttt'], t['ttc']))


___ get_snapshot_dirs(*args):
    snapshot_root _ load_settings()['snapshotbrowser_root']
    r_ [ d ___ d __ __.l_d_(snapshot_root) __ __.pa__.isd..(__.pa__.j..(snapshot_root, d)) ]


___ set_flag(snapshotbowser, thumbnail_src, color, *args):
    metaxml _ '{}.xml'.f..(__.pa__.s_t_(thumbnail_src)[0])
    __ no. __.pa__.isf..(metaxml):
        create_metaxml(metaxml)
    metatree _ ET.parse(metaxml)
    metaroot _ metatree.getroot()
    ___ meta __ metaroot.find('metadata').f_a_('meta'):
        __ meta.get('name') __ 'flag':
            __ color __ N..:
                meta.text _ ''
            ____
                meta.text _ '{},{},{}'.f..(color[0], color[1], color[2])

    w__ o..(metaxml, 'w') __ xml:
        prettyprint(metaroot)
        metatree.w..(xml, encoding_'utf-8', xml_declaration_T..)
    ___ thumb __ snapshotbowser.get_thumbnails_list():
        thumb.set_meta_ui_elements()

    r_


___ create_metaxml(src, *args):
    w__ o..(src, 'w') __ f:
        f.w..(templates.SNAPSHOT_META)


___ load_metadata(src, *args):
    metadata _ {'flag': '',
     'comment': ''}
    meta_xml _ '{}.xml'.f..(__.pa__.s_t_(src)[0])
    __ __.pa__.isf..(meta_xml):
        ___
            meta_tree _ ET.parse(meta_xml)
            meta_root _ meta_tree.getroot()
        ______
            msg _ "corrupt metaxml, create new one for '{}'".f..(meta_xml)
            write_log(msg)
            __ __.pa__.isf..(meta_xml):
                __.remove(meta_xml)
                create_metaxml(meta_xml)
                meta_tree _ ET.parse(meta_xml)
                meta_root _ meta_tree.getroot()

        ___ meta __ meta_root.find('metadata').f_a_('meta'):
            meta_val _ meta.text
            __ no. meta_val:
                meta_val _ ''
            metadata[meta.get('name')] _ meta_val

    r_ metadata


___ get_resolution(*args):
    __ ?.activeViewer():
        r_ ?.activeViewer().node()['downrez'].gV..


___ ask_dialog(m.., process_label _ 'ok', color_process _ 'actionButton', cancel_labek _ 'cancel'):
    msg_box _ ?W...QMessageBox(?W...QMessageBox.Warning, 'QMessageBox.warning()', m.., ?W...QMessageBox.NoButton, N..)
    msg_box.setWindowFlags(?C...__.WindowStaysOnTopHint)
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
    msg_box.addButton(cancel_labek, ?W...QMessageBox.RejectRole)
    __ msg_box.exec_() __ ?W...QMessageBox.AcceptRole:
        r_ T..
    ____
        r_ F..
        r_