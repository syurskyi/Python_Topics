# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartLib_v4.0/smartLib/src/helper.py
______ __
______ ___
______ errno
______ shutil
______ su__
______ xml.etree.ElementTree __ ET
______ collections
______ urllib
______ ti__
______ d_t_
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
______ osl
______ templates
DIR_DOCS _ '.docs'
IMAGE_EXT _ ['exr',
 'cin',
 'dpx',
 'hdr',
 'jpeg',
 'pic',
 'png',
 'sgi',
 'targa',
 'tif',
 'xpm',
 'yuv',
 'jpg',
 'tiff']
VIDEO_EXT _ ['mov',
 'avi',
 'mpg',
 'mpeg',
 'wmv',
 'flv',
 'm4v',
 'mp4']
IGNORE _ ['.DS_Store', '.nk~', '.autosave']

___ load_icons
    this_dir _ __.pa__.d_n_( -f)
    dir_icon _ __.pa__.j..(this_dir, '../', 'icons')
    dir_icon _ __.pa__.n_p_(dir_icon)
    j.. _ __.pa__.j..
    r_ {'icon_logo': j..(dir_icon, 'logo.png'),
     'icon_folder': j..(dir_icon, 'folder.png'),
     'icon_nuke': j..(dir_icon, 'nuke.png'),
     'icon_img': j..(dir_icon, 'img.jpg'),
     'icon_video': j..(dir_icon, 'video.jpg'),
     'icon_copy': j..(dir_icon, 'copy.png'),
     'icon_cut': j..(dir_icon, 'cut.png'),
     'icon_paste': j..(dir_icon, 'paste.png'),
     'icon_delete': j..(dir_icon, 'delete.png'),
     'icon_reveal': j..(dir_icon, 'reveal.jpg'),
     'icon_home': j..(dir_icon, 'home.png'),
     'icon_dirup': j..(dir_icon, 'dirup.png'),
     'icon_doc': j..(dir_icon, 'doc.png'),
     'icon_system': j..(dir_icon, 'system.png'),
     'icon_system_inactive': j..(dir_icon, 'system_inactive.png'),
     'icon_shot': j..(dir_icon, 'shot.png'),
     'icon_shot_inactive': j..(dir_icon, 'shot_inactive.png'),
     'icon_preview_default': j..(dir_icon, 'preview_default.png'),
     'icon_notes': j..(dir_icon, 'notes.png'),
     'icon_notes_inactive': j..(dir_icon, 'notes_inactive.png'),
     'icon_write': j..(dir_icon, 'write.png'),
     'icon_search': j..(dir_icon, 'search.png'),
     'icon_status_done': j..(dir_icon, 'status_done.png'),
     'icon_status_progress': j..(dir_icon, 'status_progress.png'),
     'icon_status_not_started': j..(dir_icon, 'status_not_started.png'),
     'icon_insert': j..(dir_icon, 'insert.png'),
     'icon_read': j..(dir_icon, 'read.png'),
     'icon_pin_pinned': j..(dir_icon, 'pin_unpinned.png'),
     'icon_pin_unpinned': j..(dir_icon, 'pin_pinned.png'),
     'about': j..(dir_icon, 'about.jpg')}


___ check_web_connection
    ___
        urllib.urlopen('http://www.cragl.com')
        r_ T..
    ______
        r_ F..


___ show_message_box(window, m..):
    ?W...QMessageBox().information(window, 'information', m..)


___ message_confirm_overwrite(src, is_file _ T..):
    __ is_file:
        item _ 'File'
    ____
        item _ 'Directory'
    m.. _ "{} '{}' already exists.\nDo you want to overwrite it?".f..(item, src)
    overwrite _ ask_dialog(m.._m.., process_button_text_'Overwrite', color_process_'45,0,0', cancel_button_text_'Cancel')
    r_ overwrite


___ get_smartlib_private_dir
    dir_ _ __.pa__.j..(__.pa__.e__('~'), '.cragl', 'smartLib')
    __ no. __.pa__.isd..(dir_):
        __.m_d_(dir_)
    r_ dir_


___ get_smartlib_public_dir
    dir_ _ __.pa__.j..(__.pa__.e__('~'), 'cragl', 'smartLib')
    __ no. __.pa__.isd..(dir_):
        __.m_d_(dir_)
    r_ dir_


___ get_dir_templates
    dir_ _ __.pa__.j..(get_smartlib_public_dir(), 'shot_templates')
    __ no. __.pa__.isd..(dir_):
        __.m_d_(dir_)
    r_ dir_


___ set_item_icon(listwidget_item, name, is_dir, is_render_dir _ F.., is_footage_dir _ F.., icons _ N..):
    __ is_dir:
        ___
            listwidget_item.setIcon(0, ?G...QIcon(icons['icon_folder']))
            __ is_render_dir:
                listwidget_item.setIcon(0, ?G...QIcon(icons['icon_write']))
            ____ is_footage_dir:
                listwidget_item.setIcon(0, ?G...QIcon(icons['icon_read']))
        ______
            listwidget_item.setIcon(?G...QIcon(icons['icon_folder']))
            __ is_render_dir:
                listwidget_item.setIcon(?G...QIcon(icons['icon_write']))
            ____ is_footage_dir:
                listwidget_item.setIcon(0, ?G...QIcon(icons['icon_read']))

    __ '.' __ name:
        ext _ name.s..('.')[1]
        __ ext __ 'nk':
            ___
                listwidget_item.setIcon(0, ?G...QIcon(icons['icon_nuke']))
            ______
                listwidget_item.setIcon(?G...QIcon(icons['icon_nuke']))

        ____ ext.lower() __ IMAGE_EXT:
            ___
                listwidget_item.setIcon(0, ?G...QIcon(icons['icon_img']))
            ______
                listwidget_item.setIcon(?G...QIcon(icons['icon_img']))

        ____ ext __ VIDEO_EXT:
            ___
                listwidget_item.setIcon(0, ?G...QIcon(icons['icon_video']))
            ______
                listwidget_item.setIcon(?G...QIcon(icons['icon_video']))

        ____
            ___
                listwidget_item.setIcon(0, ?G...QIcon(icons['icon_doc']))
            ______
                listwidget_item.setIcon(?G...QIcon(icons['icon_doc']))


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


___ get_smartLib_installed_root
    this_dir _ __.pa__.d_n_( -f)
    root _ __.pa__.j..(this_dir, '../', '../')
    r_ __.pa__.n_p_(root)


___ write_log(text, tool _ 'sl'):
    w__ o..(get_log_file(), 'a') __ file_:
        log_time_format _ '%d.%m.%Y %H:%M:%S'
        log_time _ ti__.s_t_(log_time_format, ti__.localtime())
        file_.w..('{}: {} {}\n'.f..(log_time, tool, text))


___ _copy(src, dst):
    dst _ __.pa__.j..(dst, __.pa__.b_n_(src))
    __ __.pa__.isd..(src):
        ___
            shutil.copytree(src, dst)
        ______ E.. __ error:
            raise OSError(error)

    ____ __.pa__.isf..(src):
        __ no. __.pa__.isd..(__.pa__.d_n_(dst)):
            __.m_d_(__.pa__.d_n_(dst))
        ___
            shutil.copy(src, dst)
        ______ E.. __ error:
            raise OSError(error)


___ r__(pa__):
    __ __.pa__.isf..(pa__):
        ___
            __.r__(pa__)
            r_ T..
        ______
            r_ F..

    ____ __.pa__.isd..(pa__):
        ___
            shutil.rmtree(pa__)
            r_ T..
        ______
            r_ F..


___ set_style_sheet(widget):
    this_dir _ __.pa__.d_n_( -f)
    styles _ __.pa__.j..(this_dir, '../', 'styles', 'nuke.qss')
    styles _ __.pa__.n_p_(styles)
    __ __.pa__.isf..(styles):
        w__ o..(styles) __ file_:
            widget.setStyleSheet(file_.read())


___ reveal_in_finder(pa__, open_file _ F..):
    pa__ _ __.pa__.n_p_(pa__)
    ___
        __ ___.pl.. __ 'linux2':
            __ open_file:
                ?.scriptOpen(pa__)
                r_
            __ __.pa__.isf..(pa__):
                pa__ _ __.pa__.d_n_(pa__)
            su__.P..(['xdg-open', pa__])
        ____ ___.pl.. __ 'darwin':
            __ open_file:
                su__.call(['open', '--', pa__])
            ____
                su__.call(['open', '-R', pa__])
        ____ ___.pl.. __ 'windows' or ___.pl.. __ 'win32':
            __ ':' __ pa__:
                __ ':{}'.f..(__.pa__.sep) no. __ pa__:
                    pa__ _ pa__.r..(':', ':{}'.f..(__.pa__.sep))
            __ __.pa__.isf..(pa__):
                pa__ _ __.pa__.d_n_(pa__)
            su__.call(['explorer', pa__])
    ______
        m..('Failed opening: {}'.f..(pa__))


___ get_home_dir
    r_ __.pa__.e__('~')


___ load_bookmarks
    bookmarklist _ # list
    bookmarklist.ap..('bookmarks')
    bookmarklist.ap..('add to bookmarks')
    bookmarklist.ap..('delete from bookmarks')
    bookmarklist.ap..('--------------------')
    settingsXML _ get_settings_xml()
    settings_tree _ ET.parse(settingsXML)
    settings_root _ settings_tree.getroot()
    ___ child __ settings_root.find('bookmarks').f_a_('bookmark'):
        bookmarklist.ap..(child.text)

    r_ bookmarklist


___ get_settings_xml
    settings_xml _ __.pa__.j..(get_smartlib_private_dir(), 'settings.xml')
    __ no. __.pa__.isf..(settings_xml):
        ___
            w__ o..(settings_xml, 'w') __ xml:
                template _ templates.SETTINGS.f..(user_home_dir___.pa__.e__('~'))
                xml.w..(template.strip())
        ______ E.. __ error:
            write_log("Couldn't write settings xml template. {}".f..(error))

    check_xml_values_exist()
    check_status_exists()
    check_xml_ok(settings_xml)
    r_ settings_xml


___ check_xml_values_exist
    settings _ {'show_system': 'True',
     'show_shot': 'True',
     'show_notes': 'True',
     'hidden_files': 'False',
     'force_create_render_dir': 'True',
     'padding': '4',
     'ext': 'exr',
     'print_path': '',
     'padding_delimiter': '.',
     'collapse_image_sequences': 'True',
     'shot_enable_drag': 'False',
     'shot_thumb_gamma': '1.0',
     'nukescripts_ignore': 'backup, bckp, annotation',
     'pin': 'True',
     'default_w': '1920',
     'default_h': '1080',
     'default_fps': '24',
     'default_pixel_aspect': '1',
     'user': ' ',
     'tooltips': 'True'}
    ___ key, v..  __ settings.i..
        check_xml_value_exists('settings', 'setting', 'name', key, v.. )

    navigations _ {'system': '',
     'project': '',
     'shot': ''}
    ___ key, v..  __ navigations.i..
        check_xml_value_exists('navigation', 'navi', 'name', key, v.. )

    check_xml_parent_val_exists('templateDefaults')


___ check_xml_value_exists(parent, section, key1, value1, text, key2 _ '', value2 _ ''):
    xml _ __.pa__.j..(get_smartlib_private_dir(), 'settings.xml')
    tree _ ET.parse(xml)
    root _ tree.getroot()
    debug _ F..
    item_found _ 0
    ___ child __ root.find(parent).f_a_(section):
        __ child.get(key1) __ value1:
            item_found +_ 1
            __ debug:
                print 'smartLib | settings exists: {}|{}|{}|{}|{}|{}|{}'.f..(parent, section, key1, value1, text, key2, value2)
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


___ check_xml_parent_val_exists(section):
    xml _ __.pa__.j..(get_smartlib_private_dir(), 'settings.xml')
    tree _ ET.parse(xml)
    root _ tree.getroot()
    __ root.find(section) __ N..:
        elem _ ET.Element(section)
        root.ap..(elem)
        w__ o..(xml, 'w') __ xml:
            prettyprint(root)
            tree.w..(xml, encoding_'utf-8', xml_declaration_T..)
        write_log('settings xml added: {}'.f..(section))
    r_


___ check_status_exists
    status_found _ 0
    xml _ __.pa__.j..(get_smartlib_private_dir(), 'settings.xml')
    tree _ ET.parse(xml)
    root _ tree.getroot()
    __ le.(root.find('statuslist')):
        ___ child __ root.find('statuslist').f_a_('status'):
            status_found +_ 1

    __ status_found __ 0:
        default_status _ templates.DEFAULT_STATUS
        __ root.find('statuslist') __ N..:
            statuslist_elem _ ET.Element('statuslist')
            root.ap..(statuslist_elem)
        ___ key __ sorted(default_status):
            status_elem _ ET.Element('status')
            status_elem.set('z-index', key)
            status_elem.set('color', default_status[key][0])
            status_elem.text _ default_status[key][1]
            status_elem.set('default', default_status[key][2])
            root.find('statuslist').ap..(status_elem)

        w__ o..(xml, 'w') __ xml:
            prettyprint(root)
            tree.w..(xml, encoding_'utf-8', xml_declaration_T..)
    r_


___ write_template_default(projectpath, template):
    xml _ __.pa__.j..(get_smartlib_private_dir(), 'settings.xml')
    tree _ ET.parse(xml)
    root _ tree.getroot()
    elem_exists _ F..
    ___ project __ root.find('templateDefaults').f_a_('project'):
        __ project.get('path') __ projectpath:
            elem_exists _ T..
            project.text _ template
            break

    __ no. elem_exists:
        projectelement _ ET.Element('project')
        projectelement.set('path', projectpath)
        projectelement.text _ template
        root.find('templateDefaults').ap..(projectelement)
    w__ o..(xml, 'w') __ xml:
        prettyprint(root)
        tree.w..(xml, encoding_'utf-8', xml_declaration_T..)


___ load_template_default(project_path):
    xml _ __.pa__.j..(get_smartlib_private_dir(), 'settings.xml')
    tree _ ET.parse(xml)
    root _ tree.getroot()
    ___ project __ root.find('templateDefaults').f_a_('project'):
        __ project.get('path') __ project_path:
            r_ project.text

    r_ ''


___ load_status_list
    xml _ __.pa__.j..(get_smartlib_private_dir(), 'settings.xml')
    tree _ ET.parse(xml)
    root _ tree.getroot()
    status_list _ {}
    __ le.(root.find('statuslist')):
        ___ child __ root.find('statuslist').f_a_('status'):
            data _ [child.get('color'), child.text, child.get('default')]
            status_list[child.get('z-index')] _ data

    r_ status_list


___ load_default_status
    settings_xml _ get_settings_xml()
    settings_tree _ ET.parse(settings_xml)
    settings_root _ settings_tree.getroot()
    w__ o..(settings_xml, 'r'):
        ___ child __ settings_root.find('statuslist').f_a_('status'):
            __ child.get('default') __ '1':
                r_ [child.text, child.get('color')]


___ ask_dialog(m.. _ '', process_button_text _ '', color_process _ '', cancel_button_text _ ''):
    msg_box _ ?W...QMessageBox(?W...QMessageBox.Warning, 'QMessageBox.warning()', m.., ?W...QMessageBox.NoButton, N..)
    msg_box.sWF..(?C...__.WindowStaysOnTopHint)
    msg_box.setObjectName('msgBox')
    msg_box.raise_()
    process_button _ msg_box.addButton(process_button_text, ?W...QMessageBox.AcceptRole)
    __ color_process !_ '':
        __ color_process __ 'actionButton':
            color_process _ '51, 204, 255, 100'
        style _ 'QPushButton {background-color: rgba(@)}' % color_process
        process_button.setStyleSheet(style)
    process_button.clearFocus()
    msg_box.setFocus()
    msg_box.addButton(cancel_button_text, ?W...QMessageBox.RejectRole)
    __ msg_box.exec_() __ ?W...QMessageBox.AcceptRole:
        r_ T..
    ____
        r_ F..
        r_


___ check_xml_ok(xml):
    ___
        w__ o..(xml, 'r') __ xml_file:
            ET.fromstring(xml_file.read())
        r_ T..
    ______
        __ xml __ get_settings_xml
            m.. _ 'The smartLib settings file seems to be broken. Do you want to reset it now?'
            write_log('smartLib settings file broken.')
        ____
            meta_xml _ __.pa__.j..(__.pa__.d_n_(xml), '../')
            meta_xml _ __.pa__.n_p_(meta_xml)
            m.. _ 'The meta xml for {} file seems to be broken. Do you want to reset it now?'.f..(meta_xml)
            write_log('The meta xml for {} file broken.'.f..(meta_xml))
        reset_xml _ ask_dialog(m.._m.., process_button_text_'reset', color_process_'actionButton', cancel_button_text_'Cancel')
        __ reset_xml:
            __ __.pa__.isf..(xml):
                __.r__(xml)
                get_settings_xml()
        r_ F..


___ load_settings
    settings_xml _ get_settings_xml()
    settings_tree _ ET.parse(settings_xml)
    settings_root _ settings_tree.getroot()
    settings _ {}
    ___ setting __ settings_root.find('settings').f_a_('setting'):
        __ setting.text:
            settings[setting.get('name')] _ setting.text
        ____
            settings[setting.get('name')] _ ''

    ___ navi __ settings_root.find('navigation').f_a_('navi'):
        __ navi.text an. __.pa__.isd..(navi.text):
            settings['current_{}'.f..(navi.get('name'))] _ navi.text
        ____
            settings['current_{}'.f..(navi.get('name'))] _ ''

    r_ settings


___ center_window(window):
    qr _ window.frameGeometry()
    cp _ ?W...QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


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


___ write_xml(xml, root, tree):
    prettyprint(root)
    tree.w..(xml, encoding_'utf-8', xml_declaration_T..)
    r_ T..


___ collect_nuke_scripts_no_ignore(pa__):
    nuke_scripts _ collections.OrderedDict()
    ignore_list _ load_settings()['nukescripts_ignore']
    __ ignore_list:
        ignore_list _ ignore_list.s..(',')
    ____
        ignore_list _ # list
    ignore_list.extend(['.nk~', '.autosave'])
    ___ root, dirs, files __ __.walk(pa__):
        ___ name __ files:
            file _ __.pa__.j..(root, name)
            __ __.pa__.s_t_(file)[1] __ '.nk':
                ignore_count _ 0
                ___ ignore __ ignore_list:
                    __ ignore.strip() __ file:
                        ignore_count +_ 1

                __ ignore_count __ 0:
                    nuke_script _ __.pa__.b_n_(file)
                    nuke_script_name _ __.pa__.s_t_(nuke_script)[0]
                    nuke_scripts[file] _ nuke_script_name

    nuke_scripts _ sorted(nuke_scripts.i..(), key_lambda x: x[1])
    nuke_scripts.reverse()
    r_ nuke_scripts


___ open_nukescript(name, nuke_scripts):
    ___ script __ nuke_scripts:
        __ script[1] __ name:
            ?.scriptOpen(script[0])


___ write_location(location, v.. ):
    settings_xml _ get_settings_xml()
    settings_tree _ ET.parse(settings_xml)
    settings_root _ settings_tree.getroot()
    w__ o..(settings_xml, 'r'):
        ___ child __ settings_root.find('navigation').f_a_('navi'):
            __ child.get('name') __ location:
                child.text _ v..

    w__ o..(settings_xml, 'w') __ xml:
        prettyprint(settings_root)
        settings_tree.w..(xml, encoding_'utf-8', xml_declaration_T..)


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
            show_message_box(N.., msg)

    r_


___ set_preview_image(delete_nodes _ T..):
    __ no. osl.cl
        r_
    preview_image_width _ 500
    ___
        sel _ ?.sN__
    ______
        ?.m..('Please select a node to create a preview image.')
        r_

    __ sel.C..  __ 'Viewer':
        r_
    __ get_script_name() __ '' or get_script_name() __ 'Root':
        ?.m..("Your nukescript hasn't been saved, yet. Please save your script first.")
        r_
    root_dir_docs _ get_dir_docs_current_nukescript()
    __ root_dir_docs __ '':
        r_
    reformat _ ?.cN..('Reformat', inpanel_F..)
    reformat.setInput(0, sel)
    reformat.setXYpos(sel.xpos(), sel.yp__() + 50)
    reformat['type'].sV..('to box')
    reformat['box_width'].sV..(preview_image_width)
    gamma _ ?.cN..('Gamma')
    gamma.setInput(0, reformat)
    gamma.setXYpos(sel.xpos(), reformat.yp__() + 50)
    gamma['value'].sV..(fl..(load_settings()['shot_thumb_gamma']))
    w.. _ ?.cN..('Write', inpanel_F..)
    w...setInput(0, gamma)
    w...setXYpos(gamma.xpos(), gamma.yp__() + 50)
    w...knob('name').sV..('create preview')
    w...knob('use_limit').sV..(T..)
    w...knob('first').sV..(?.frame())
    w...knob('last').sV..(?.frame())
    w...knob('file_type').sV..('jpg')
    preview_path _ __.pa__.j..(root_dir_docs, '__preview.jpg')
    preview_path _ preview_path.r..(__.pa__.sep, '/')
    w...knob('file').sV..(preview_path)
    ?.execute(w.., ?.frame(), ?.frame())
    __ delete_nodes:
        ?.delete(reformat)
        ?.delete(gamma)
        ?.delete(w..)


___ get_dir_docs_current_nukescript
    up_level _ 7
    current_script_dir _ __.pa__.d_n_(?.r.. .n..
    __ current_script_dir __ 'Root' or current_script_dir __ '':
        r_ ''
    root_dir_docs _ ''
    dirs _ # list
    dirs.ap..(__.pa__.n_p_(current_script_dir))
    ___ i __ ra..(up_level - 1):
        dir _ __.pa__.n_p_(__.pa__.abspath(__.pa__.j..(__.pa__.d_n_(dirs[i - 1]))))
        dirs.ap..(dir)

    ___ i __ ra..(up_level - 1):
        dir_content _ __.l_d_(dirs[i])
        __ DIR_DOCS __ dir_content:
            root_dir_docs _ __.pa__.n_p_(__.pa__.j..(dirs[i], DIR_DOCS))
            r_ root_dir_docs

    __ root_dir_docs __ '':
        write_log("Wasn't able to find the _docs directory for the shot. Recursion depth for the shot is too high.")
        r_


___ get_meta_xml(pa__):
    __ __.pa__.isd..(pa__):
        metaxml _ __.pa__.j..(pa__, DIR_DOCS, 'meta.xml')
        ___
            __ no. __.pa__.isd..(__.pa__.d_n_(metaxml)):
                __.m_d_(__.pa__.d_n_(metaxml))
        ______
            r_

        __ no. __.pa__.isf..(metaxml):
            ___
                w__ o..(metaxml, 'w') __ file_:
                    template _ templates.META
                    file_.w..(template.strip())
            ______
                write_log("Couldn't write meta xml template at: {}".f..(metaxml))

        check_meta_xml_values_exist(metaxml)
        r_ metaxml


___ check_meta_xml_values_exist(metaxml):
    check_meta_xml_value_exists(metaxml, 'notes', 'note', 'name', 'footagepath', ' ', key2_'loc', value2_'local')
    check_meta_xml_value_exists(metaxml, 'notes', 'note', 'name', 'user', ' ')


___ check_meta_xml_value_exists(metaxml_path, parent, section, key1, value1, text, key2 _ '', value2 _ ''):
    tree _ ET.parse(metaxml_path)
    root _ tree.getroot()
    debug _ F..
    item_found _ 0
    ___ child __ root.find(parent).f_a_(section):
        __ child.get(key1) __ value1:
            item_found +_ 1
            __ debug:
                print 'smartLib | metaxml exists: {}|{}|{}|{}|{}|{}|{}'.f..(parent, section, key1, value1, text, key2, value2)
            r_

    __ item_found __ 0:
        elem _ ET.Element(section)
        elem.set(key1, value1)
        __ key2 !_ '':
            elem.set(key2, value2)
        elem.text _ text
        root.find(parent).ap..(elem)
        w__ o..(metaxml_path, 'w') __ xml:
            prettyprint(root)
            tree.w..(xml, encoding_'utf-8', xml_declaration_T..)
        write_log('settings metaxml added: {}|{}|{}|{}|{}|{}|{}'.f..(parent, section, key1, value1, text, key2, value2))


___ m..(m..):
    msg_box _ ?W...QMessageBox()
    msg_box.sWF..(?C...__.WindowStaysOnTopHint)
    msg_box.setText(m..)
    msg_box.raise_()
    msg_box.exec_()


___ dialog_set_preview_image(smartlib):
    dialog _ ?W...QFileDialog()
    dialog.sWF..(?C...__.WindowStaysOnTopHint)
    dialog.setWindowIcon(?G...QIcon(load_icons()['icon_logo']))
    dialog.sQT..('choose image file')
    dialog.setNameFilter('jpg files(*.jpg)')
    __ dialog.exec_() __ ?W...QDialog.Accepted:
        input_image _ dialog.selectedFiles()[0]
        dest _ __.pa__.j..(smartlib.current_shot_widget.pa__, DIR_DOCS, '__preview.jpg')
        __ no. __.pa__.isd..(__.pa__.d_n_(dest)):
            __.m_d_(__.pa__.d_n_(dest))
        save_image_scaled(input_image, dest)
        smartlib.current_shot_widget.refresh()
        current_project _ load_settings()['current_project']
        smartlib.table_current_project.load_shots(current_project)


___ save_image_scaled(src, dest):
    img _ ?G...QImage(src)
    ___
        pixmap _ ?G...QPixmap(img.scaledToWidth(500))
        pixmap.save(dest)
        r_ T..
    ______
        write_log('Cannot create image scaled.')
        r_ F..


___ get_script_name
    script _ ?.r.. .n..
    script_name _ __.pa__.b_n_(script)
    r_ __.pa__.s_t_(script_name)[0]


___ setup_renderpath
    dir_docs_current_nukescript _ get_dir_docs_current_nukescript()
    __ dir_docs_current_nukescript __ (N.., ''):
        r_ N..
    ____
        project_root _ __.pa__.d_n_(dir_docs_current_nukescript)
        metaxml _ __.pa__.j..(dir_docs_current_nukescript, 'meta.xml')
        script_name _ get_script_name()
        __ __.pa__.isf..(metaxml) an. script_name no. __ ('', 'Root'):
            meta_tree _ ET.parse(metaxml)
            meta_root _ meta_tree.getroot()
            ___ child __ meta_root.find('notes').f_a_('note'):
                __ child.get('name') __ 'renderpath':
                    ___
                        __ child.text.strip() !_ '':
                            __ child.get('loc') __ 'global':
                                render_dir _ '{}'.f..(child.text)
                            ____
                                render_dir _ '{}{}'.f..(project_root, child.text)
                            render_file _ '{}{}%0{}d.{}'.f..(script_name, load_settings()['padding_delimiter'], load_settings()['padding'], load_settings()['ext'])
                            render_full_path _ __.pa__.j..(render_dir, script_name, render_file)
                            render_dir _ __.pa__.d_n_(render_full_path)
                            __ no. __.pa__.isd..(render_dir):
                                __.m_d_(render_dir)
                            ?.tN..()['file'].sV..(render_full_path)
                            ?.tN..()['file_type'].sV..(load_settings()['ext'])
                    ______
                        p..

        r_ N..


___ load_templates
    dir_templates _ get_dir_templates()
    templates _ # list
    ___ item __ __.l_d_(dir_templates):
        element _ __.pa__.j..(dir_templates, item)
        __ __.pa__.isd..(element) an. item !_ DIR_DOCS:
            templates.ap..(item)

    r_ templates


___ get_render_path(xml):
    __ __.pa__.isf..(xml):
        ___
            meta_tree _ ET.parse(xml)
            meta_root _ meta_tree.getroot()
        ______
            write_log('Unable to parse metaxml.')
            r_

        ___ child __ meta_root.find('notes').f_a_('note'):
            __ child.get('name') __ 'renderpath':
                r_ child.text

    ____
        write_log("Metaxml doesn't exist in: {}".f..(xml))


___ rename_item(sender, path_orig, window):
    inp _ ?W...QInputDialog()
    inp.setObjectName('inp')
    __ __.pa__.isf..(path_orig):
        item _ 'file'
    ____
        item _ 'directory'
    title _ 'Enter new name'
    msg _ 'Enter the new name for the {}:'.f..(item)
    file_name _ __.pa__.b_n_(path_orig)
    name, ok _ inp.getText(window, title, msg, text_file_name)
    __ ok:
        name _ name.r..('/', '')
        new_name_full_path _ __.pa__.j..(__.pa__.d_n_(path_orig), name)
        __ __.pa__.isf..(path_orig):
            __ '.' no. __ name:
                ext _ __.pa__.s_t_(__.pa__.b_n_(path_orig))[1]
                new_name_full_path _ '{}{}'.f..(new_name_full_path, ext)
        __ sender __ 'smartlibshotwindow':
            __.rename(path_orig, new_name_full_path)
            window.populate_tree()
        __ sender __ 'shot_templates':
            __.rename(path_orig, new_name_full_path)
            window.load_shot_template_in_tree()
        __ sender __ 'saved_projects':
            settingsXML _ get_settings_xml()
            settingstree _ ET.parse(settingsXML)
            settingsroot _ settingstree.getroot()
            ___ child __ settingsroot.find('projectslist').f_a_('project'):
                __ child.text __ path_orig:
                    child.set('name', name)

            write_xml(settingsXML, settingsroot, settingstree)
            window.populate_saved_projects()


___ force_create_render_dir
    filename _ ?.filename(?.tN..())
    d_n_ _ __.pa__.d_n_(filename)
    osdir _ ?.callbacks.filenameFilter(d_n_)
    ___
        __.m_d_(osdir)
    ______ OSError __ e:
        __ e.errno !_ errno.EEXIST:
            raise


___ get_finder_name
    __ ___.pl.. __ 'darwin':
        r_ 'finder'
    ____
        r_ 'explorer'


___ import_from_footage_directory
    dir_docs _ get_dir_docs_current_nukescript()
    ___
        __ dir_docs __ '':
            raise ValueError
        meta_xml _ __.pa__.j..(dir_docs, 'meta.xml')
        __ no. __.pa__.isf..(meta_xml):
            raise ValueError
        metatree _ ET.parse(meta_xml)
        ___ note __ metatree.find('notes').f_a_('note'):
            __ note.get('name') __ 'footagepath':
                shot_root _ __.pa__.n_p_(__.pa__.j..(dir_docs, '../'))
                shot_root _ shot_root.r..(__.pa__.sep, '/')
                __ note.text __ no. N..:
                    __ note.get('loc') __ 'global':
                        start_path _ note.text
                    __ note.get('loc') __ 'local':
                        __ note.text[0] __ __.pa__.sep or note.text[0] __ '/':
                            note.text _ note.text[1:]
                        __ note.text an. note.text !_ '' an. note.text !_ ' ':
                            start_path _ __.pa__.j..(shot_root, note.text)
                        ____
                            start_path _ shot_root
                ____ note.text __ N.. or note.text __ '' or note.text __ ' ':
                    start_path _ shot_root
                __ start_path[-1:] !_ '/':
                    start_path +_ '/'
                start_path _ start_path.r..(__.pa__.sep, '/')
                load_footage(path_start_path)

    ______
        p..

    r_


___ load_footage(defaulttype _ 'Read', pa__ _ ''):
    sel_node _ N..
    default_dir _ N..
    ___
        sel_node _ ?.sN__
    ______
        p..

    __ sel_node:
        __ 'file' __ sel_node.knobs
            default_dir _ sel_node['file'].v..
        __ no. default_dir an. 'proxy' __ sel_node.knobs
            default_dir _ sel_node['proxy'].v..
    __ default_dir __ '':
        default_dir _ N..
    files _ ?.getClipname('______ from footage directory', default_path, multiple_T..)
    __ files !_ N..:
        max_files _ ?.numvalue('preferences.maxPanels')
        n _ le.(files)
        ___ f __ files:
            is_abc _ F..
            stripped _ ?.stripFrameRange(f)
            nodeType _ defaulttype
            __ ?.create.isAudioFilename(stripped):
                nodeType _ 'AudioRead'
            __ ?.create.isGeoFilename(stripped):
                nodeType _ 'ReadGeo2'
            __ ?.create.isAbcFilename(stripped):
                is_abc _ T..
            __ ?.create.isDeepFilename(stripped):
                nodeType _ 'DeepRead'
            use_in_panel _ T..
            __ max_files !_ 0 an. n > max_files:
                use_in_panel _ F..
            n _ n - 1
            __ is_abc:
                ?.createScenefileBrowser(f, '')
            ____
                ___
                    ?.cN..(nodeType, 'file {' + f + '}', inpanel_use_in_panel)
                ______ RuntimeError __ err:
                    ?.m..(err.args[0])

    r_


___ show_custom_directory_window(shot_root, which, sml _ N..):
    g__ crp
    ___
        crp.c__
        del crp
    ______
        p..

    crp _ CustomPath(shot_root, sml, which)
    crp.raise_()
    crp.s__


___ create_new_directory(widget, list_):
    inp _ ?W...QInputDialog()
    inp.setObjectName('inp')
    title _ 'Enter name'
    msg _ 'Enter the name of the new folder:'
    dir_name, ok _ inp.getText(widget, title, msg)
    __ ok:
        dest _ list_.data(0, ?C...__.UserRole)
        __ __.pa__.isf..(dest):
            dest _ __.pa__.d_n_(dest)
        dest _ dest.r..('\\', '/')

        ___ create_directory(dir_name):
            dir_path_full _ __.pa__.j..(dest, dir_name)
            __ no. __.pa__.isd..(dir_path_full):
                __.m_d_(dir_path_full)
                diritem _ widget.build_tree_widget_item(widget.dirlist[dest], dir_name, dir_path_full, is_dir_T..)
                widget.dirlist[dir_path_full] _ diritem
                widget.allitems[dir_path_full] _ diritem
            ____
                m..("The directory '{}' already exists. The folder wasn't created".f..(dir_name))

        dir_item_list _ dir_name.s..(',')
        ___ dir_item __ dir_item_list:
            dir_item _ dir_item.strip()
            create_directory(dir_item)


___ error_loading(pa__, sml):
    m.. _ 'Cannot find the bookmark:\n{}\n\n No such directory.Do you like to delete it from the bookmarks?'.f..(pa__)
    remove_bookmark _ ask_dialog(m.._m.., process_button_text_'Delete from bookmarks', color_process_'45,0,0', cancel_button_text_'Cancel')
    __ remove_bookmark:
        settingsXML _ get_settings_xml()
        settingstree _ ET.parse(settingsXML)
        settingsroot _ settingstree.getroot()
        ___ child __ settingsroot.find('bookmarks').f_a_('bookmark'):
            __ child.text __ pa__:
                settingsroot.find('bookmarks').r__(child)

        write_xml(settingsXML, settingsroot, settingstree)
        sml.combo_bookmarks.removeItem(sml.combo_bookmarks.findText(pa__))


___ get_project_information(project_full_path):
    shot_information _ {}
    ___ shot __ __.l_d_(project_full_path):
        shot_full_path _ __.pa__.j..(project_full_path, shot)
        __ __.pa__.isd..(shot_full_path) an. shot !_ '.docs':
            metaxml _ __.pa__.j..(shot_full_path, '.docs', 'meta.xml')
            __ __.pa__.isf..(metaxml):
                w__ o..(metaxml, 'r') __ metaxml:
                    shot_info _ # list
                    tree _ ET.parse(metaxml)
                    root _ tree.getroot()
                    ___ child __ root.find('notes').f_a_('note'):
                        __ child.get('name') __ 'status':
                            status _ child.text
                            __ status __ N.. or status __ '':
                                status _ ''
                            shot_info.ap..(status)
                        __ child.get('name') __ 'shotnotes':
                            shot_info.ap..(child.text)

            thumbnail _ __.pa__.j..(shot_full_path, '.docs', '__preview.jpg')
            __ __.pa__.isf..(thumbnail):
                shot_info.ap..('file:///{}'.f..(thumbnail))
            ____
                default_image _ load_icons()['icon_preview_default']
                default_image _ __.pa__.n_p_(default_image)
                shot_info.ap..('file:////{}'.f..(default_image))
            shot_information[shot] _ shot_info

    r_ shot_information


___ build_html(html_path, project):
    shot_information _ get_project_information(project)
    project_title _ __.pa__.s..(project)[-1]
    time_now _ d_t_.d_t_.fromtimestamp(__.(ti__.ti__())).s_t_('%d/%m/%Y %H:%M:%S')
    shot_status_list _ load_status_list().values()
    status_dict _ {}
    ___ status __ shot_status_list:
        status_dict[status[1]] _ 0

    ___ shot __ shot_information.values
        __ shot[0] __ status_dict:
            status_dict[shot[0]] +_ 1
        ____
            default_status _ load_default_status()[0]
            __ default_status __ status_dict:
                status_dict[default_status] +_ 1

    w__ o..(html_path, 'w') __ tmp_html:
        report_top _ templates.REPORT_TOP.f..(project_title_project_title, time_now_time_now, project_path_project, number_of_shots_le.(shot_information))
        tmp_html.w..(report_top)
    ___ key __ sorted(status_dict):
        w__ o..(html_path, 'a') __ tmp_html:
            bg_color _ '255,255,255'
            ___ status __ shot_status_list:
                __ key __ status[1]:
                    bg_color _ status[0]

            __ status_dict[key] !_ 0:
                percent _ 100.0 / le.(shot_information) * status_dict[key]
                percent_graph _ percent - 1
            ____
                percent _ 0.0
                percent_graph _ 0.0
            percent _ '{0:.1f}'.f..(percent)
            tmp_html.w..("\n                <span style='background-color: rgb({color}); display: inline-block; width:{width}%;'>&nbsp;</span>\n            ".f..(color_bg_color, width_percent_graph))

    ___ key __ sorted(status_dict):
        w__ o..(html_path, 'a') __ tmp_html:
            bg_color _ '255,255,255'
            ___ status __ shot_status_list:
                __ key __ status[1]:
                    bg_color _ status[0]

            __ status_dict[key] !_ 0:
                percent _ 100.0 / le.(shot_information) * status_dict[key]
            ____
                percent _ 0.0
            percent _ '{0:.1f}'.f..(percent)
            tmp_html.w..("\n                <span style='background-color: rgb({color}); display: inline-block; width:20px; margin-top: 5px;'>&nbsp;</span> <span style='color: #aaaaaa; font-size: 8pt; margin-top: 5px;'>{status} {count}x ({percent}%)</span><br />\n            ".f..(color_bg_color, status_key, count_status_dict[key], percent_percent))

    w__ o..(html_path, 'a') __ tmp_html:
        tmp_html.w..("\n            </div>\n            <br />\n            <div class='line' style='border-top: 1px solid #cccccc;'></div>\n        ")
    w__ o..(html_path, 'a') __ tmp_html:
        ___ key __ sorted(shot_information):
            shot_status _ shot_information[key][0]
            __ shot_information[key][1]:
                shot_notes _ shot_information[key][1]
            ____
                shot_notes _ ''
            shot_notes _ shot_notes.r..('\n', '<br />')
            shot_thumbnail _ shot_information[key][2]
            color _ ''
            ___ status __ shot_status_list:
                __ shot_status __ status[1]:
                    color _ status[0]

            __ color __ '':
                color _ load_default_status()[1]
                shot_status _ load_default_status()[0]
            tmp_html.w..('\n            <div class=\'shot\' style="display: block; height:auto; margin: 20px; border-bottom: 1px solid #cccccc; padding: 20px;">\n                <div class=\'shot_thumbnail\' style=\'display: inline-block; padding-right: 30px;\'>\n                    <img src=\'{thumb}\' alt=\'\' title=\'\' width=\'200\' />\n                </div>\n                <div class=\'shot_details\' style=\'display: inline-block; vertical-align: top;\'>\n                    <span style=\'display: inline-block; font-size: 14pt; font-weight:bold;\'>{shotname}</span> <span style=\'background-color: rgb({color}); padding: 2px 10px; position: relative; top: -2px;\'>{status}</span> <br />\n                    <span style=\'font-size: 8pt;\'>{notes}</span>\n                </div>\n            </div>\n            <div style=\'clear:both;\'></div>\n'.f..(thumb_shot_thumbnail, shotname_key, color_color, status_shot_status, notes_shot_notes))

    w__ o..(html_path, 'a') __ tmp_html:
        tmp_html.w..('\n        </div>\n    </div>\n</body>\n</html>\n')
        r_ html_path


___ build_pdf(build_path, project, output_filename _ '', parent _ N..):
    ___
        ____ ? ______ QtWebKit
    ______ E..:
        msg _ "Error creating project report. The needed module 'QtWebKit' is not more supported in this Nuke version. Please use Nuke10 to create a project report."
        show_message_box(parent, msg)
        r_

    debug _ F..
    ___
        tmp_html _ build_html(__.pa__.j..(get_smartlib_public_dir(), 'tmp.html'), project)
        __ debug:
            print 'tmp_html: ', tmp_html
        web _ QtWebKit.QWebView()
        web.l..(?C...QUrl('file:///{}'.f..(tmp_html)))
        printer _ ?G...QPrinter()
        printer.setPageSize(?G...QPrinter.A4)
        printer.setOutputFormat(?G...QPrinter.PdfFormat)
        printer.setOutputFileName(output_filename)
        __ debug:
            print 'output pdf to: {}'.f..(output_filename)

        ___ convertIt
            web.print_(printer)

        ?C...QObject.c..(web, ?C...SIGNAL('loadFinished(bool)'), convertIt)
        __ __.pa__.isf..(tmp_html):
            ___
                __.r__(tmp_html)
            ______ E..:
                p..

        r_ 'created_pdf'
    ______ E.. __ e:
        r_ e


___ get_sequences_sets(dirpath):
    sequences _ # list
    sequences_set _ # list
    dir_content _ __.l_d_(dirpath)
    ___ file __ dir_content:
        __ file __ IGNORE:
            c___
        __ __.pa__.isd..(__.pa__.j..(dirpath, file)):
            c___
        filename_noext, ext _ __.pa__.s_t_(file)
        ext _ ext.r..('.', '')
        ____ string ______ digits
        __ i..(file, bytes):
            digits _ digits.encode()
        filename_nodigits _ filename_noext.rstrip(digits)
        __ ext no. __ IMAGE_EXT:
            sequence _ __.pa__.n_p_(__.pa__.j..(dirpath, file))
            sequence _ sequence.r..(__.pa__.sep, '/')
            sequences.ap..(sequence)
        ____
            __ le.(filename_nodigits) __ le.(filename_noext) an. file no. __ IGNORE an. file no. __ sequences:
                sequence _ __.pa__.n_p_(__.pa__.j..(dirpath, file))
                sequence _ sequence.r..(__.pa__.sep, '/')
                sequences.ap..(sequence)
                c___
            __ filename_nodigits no. __ sequences_set an. file no. __ IGNORE an. file no. __ sequences:
                sequences_set.ap..(filename_nodigits)
                sequence _ __.pa__.n_p_(__.pa__.j..(dirpath, file))
                sequence _ sequence.r..(__.pa__.sep, '/')
                sequences.ap..(sequence)

    r_ sequences


___ image_sequence_resolve_all(filepath):
    filepath _ st.(filepath.r..(__.pa__.sep, '/'))
    basedir, filename _ __.pa__.s..(filepath)
    filename_noext, ext _ __.pa__.s_t_(filename)
    ____ string ______ digits
    __ i..(filepath, bytes):
        digits _ digits.encode()
    filename_nodigits _ filename_noext.rstrip(digits)
    __ le.(filename_nodigits) __ le.(filename_noext):
        r_ __.pa__.j..(basedir, filename)
    files _ __.l_d_(basedir)
    image_sequence_list _ [ __.pa__.j..(f) ___ f __ files __ f.startswith(filename_nodigits) an. f.endswith(ext) an. f[le.(filename_nodigits):-le.(ext) __ ext ____ -1].isdigit() ]
    seq_start _ image_sequence_list[0]
    seq_start _ seq_start.r..(filename_nodigits, '')
    seq_start _ seq_start.r..(ext, '')
    seq_end _ image_sequence_list[-1:][0]
    seq_end _ seq_end.r..(filename_nodigits, '')
    seq_end _ seq_end.r..(ext, '')
    seq_preview _ '{}[{}-{}]{}'.f..(filename_nodigits, seq_start, seq_end, ext)
    seq_full_path _ __.pa__.j..(basedir, seq_preview)
    seq_full_path _ seq_full_path.r..(__.pa__.sep, '/')
    r_ seq_full_path


___ collapse_sequences(dirpath):
    sequences_in_dir _ # list
    sequence_sets _ # list
    dirpath _ dirpath.r..(__.pa__.sep, '/')
    ___ root, dirs, seq __ __.walk(dirpath):
        sequence_sub_sets _ get_sequences_sets(root)
        __ __.pa__.b_n_(root) __ DIR_DOCS:
            c___
        ___ sequence_item __ sequence_sub_sets:
            sequence_item _ __.pa__.n_p_(sequence_item)
            sequence_item _ sequence_item.r..(__.pa__.sep, '/')
            sequence_sets.ap..(sequence_item)

    ___ seq __ sequence_sets:
        ext _ __.pa__.s_t_(seq)[1]
        ext _ ext.r..('.', '')
        __ ext no. __ IGNORE an. __.pa__.b_n_(seq) no. __ IGNORE:
            __ ext no. __ IMAGE_EXT:
                item _ seq
                item _ item.r..(__.pa__.sep, '/')
                sequences_in_dir.ap..(item)
            ____
                item _ image_sequence_resolve_all(seq)
                item _ __.pa__.n_p_(item)
                item _ item.r..(__.pa__.sep, '/')
                sequences_in_dir.ap..(item)

    r_ sequences_in_dir


___ insert_shot_notes
    shot_root _ get_dir_docs_current_nukescript()
    __ shot_root __ '' or shot_root __ N..:
        r_
    ____
        shot_root _ shot_root.r..(DIR_DOCS, '')
        meta_xml _ get_meta_xml(shot_root)
        __ no. __.pa__.isf..(meta_xml):
            r_
        meta_tree _ ET.parse(meta_xml)
        meta_root _ meta_tree.getroot()
        shot_notes _ ''
        ___ child __ meta_root.find('notes').f_a_('note'):
            __ child.get('name') __ 'shotnotes':
                shot_notes _ child.text

        __ shot_notes !_ '':
            sticky _ ?.cN..('StickyNote')
            sticky['label'].sV..(shot_notes)
            sticky['note_font_size'].sV..(20)
        r_


___ show_edit_template_script(window, pa__):
    g__ ets
    script_values _ get_script_values(pa__, window)
    set_default_format _ F..
    __ 'format' __ script_values:
        __ script_values['format'] __ '0':
            set_default_format _ T..
    ____
        set_default_format _ T..
    __ set_default_format:
        settings _ load_settings()
        w _ settings['default_w']
        h _ settings['default_h']
        pixel_aspect_ratio _ settings['default_pixel_aspect']
        format_default _ '{} {} 0 0 {} {} {} HD'.f..(w, h, w, h, pixel_aspect_ratio)
        script_values['format'] _ format_default
        script_values['fps'] _ settings['default_fps']
    ___
        ets.c__
        del ets
    ______
        p..

    ets _ osl.EditTemplateScript(pa__, script_values)
    ets.s__
    ets.raise_()
    r_ ets


___ get_script_values(pa__, window):
    script_values _ {}
    __ no. __.pa__.isf..(pa__):
        msg _ "The file '{}' does not exist".f..(pa__)
        show_message_box(window, msg)
        r_ {}
    __ __.pa__.s_t_(pa__)[1] !_ '.nk':
        msg _ "The file '{}' is no nuke script.".f..(pa__)
        show_message_box(window, msg)
        r_ {}
    this_dir _ __.pa__.d_n_( -f)
    processor _ __.pa__.j..(this_dir, '../', 'trm', 'scripts.py')
    processor _ __.pa__.n_p_(processor)
    cmd _ '"{nuke_exe}" -i -t "{scriptProcess}" get "{path}" " "'.f..(nuke_exe___.pa__.n_p_(?.env['ExecutablePath']), scriptProcess_processor, path_path)
    process _ su__.P..(cmd, shell_T.., stdin_subprocess.PIPE, stdout_subprocess.PIPE)
    process.wait()
    ___ line __ process.stdout:
        line _ st.(line.rstrip())
        __ 'script@' __ line:
            script_value _ line.r..('script@', '')
            key _ script_value.s..(':')[0]
            val _ st.(script_value.s..(':')[1])
            script_values[key] _ val

    r_ script_values


___ set_script_values(pa__, script_values, *args):
    debug _ F..
    script_vals _ 'script_in:{}@script_out:{}@fps:{}@format:{}'
    script_vals _ script_vals.f..(script_values['script_in'], script_values['script_out'], script_values['fps'], script_values['format'].r..(' ', '_'))
    this_dir _ __.pa__.d_n_( -f)
    processor _ __.pa__.j..(this_dir, '../', 'trm', 'scripts.py')
    processor _ __.pa__.n_p_(processor)
    cmd _ '"{nuke_exe}" -i -t "{scriptProcess}" set "{path}" {vals}'.f..(nuke_exe___.pa__.n_p_(?.env['ExecutablePath']), scriptProcess_processor, path_path, vals_script_vals)
    process _ su__.P..(cmd, shell_T.., stdin_subprocess.PIPE, stdout_subprocess.PIPE)
    process.wait()
    found_end _ 0
    ___ line __ process.stdout:
        line _ st.(line.rstrip())
        __ debug:
            print line
        __ '@script:set_end' __ line:
            found_end +_ 1

    __ found_end __ 1:
        r_ T..
    ____
        r_ F..


___ get_user(metaxml, *args):
    __ no. __.pa__.isf..(metaxml):
        r_ ''
    metatree _ ET.parse(metaxml)
    metaroot _ metatree.getroot()
    w__ o..(metaxml, 'r') __ xml:
        ___ child __ metaroot.find('notes').f_a_('note'):
            __ child.get('name') __ 'user':
                r_ child.text


___ set_user(user, dir_docs _ ''):
    __ dir_docs __ '':
        dir_docs _ get_dir_docs_current_nukescript()
    __ dir_docs:
        meta_xml _ __.pa__.j..(dir_docs, 'meta.xml')
        __ no. __.pa__.isf..(meta_xml):
            r_
        metatree _ ET.parse(meta_xml)
        metaroot _ metatree.getroot()
        w__ o..(meta_xml, 'w') __ xml:
            ___ child __ metaroot.find('notes').f_a_('note'):
                __ child.get('name') __ 'user':
                    child.text _ user

            prettyprint(metaroot)
            metatree.w..(xml, encoding_'utf-8', xml_declaration_T..)


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


c_ CustomPath(?W...?W..):

    ___  - (, shot_root, sml, which):
        s_(CustomPath, ). - ()
        shot_root _ shot_root
        sml _ sml
        which _ which
        sQT..('Set custom {} path'.f..(which))
        sWF..(?C...__.WindowStaysOnTopHint)
        setMinimumWidth(600)
        build_ui()

    ___ build_ui
        create_widgets()
        create_layouts()
        create_signals()

    ___ create_widgets
        info _ 'Here you can set a custom {} path that can be outside of the shot'.f..(which)
        label_info _ ?W...?L..(info)
        label_path _ ?W...?L..('path: ')
        input_path _ ?W...QLineEdit(load_custom_path(which))
        push_browse _ ?W...?PB..()
        push_browse.setIcon(?G...QIcon(load_icons()['icon_folder']))
        push_browse.setObjectName('simple')
        push_save _ ?W...?PB..('save')
        push_save.setObjectName('actionButtonBig')
        push_close _ ?W...?PB..('close')

    ___ create_layouts
        layout_top _ ?W...QHBoxLayout()
        layout_top.aW..(label_path)
        layout_top.aW..(input_path)
        layout_top.aW..(push_browse)
        layout_push _ ?W...QHBoxLayout()
        layout_push.aW..(push_save)
        layout_push.aW..(push_close)
        layout_main _ ?W...?VB..
        layout_main.aW..(label_info)
        layout_main.addLayout(layout_top)
        layout_main.addLayout(layout_push)
        sL..(layout_main)
        set_style_sheet()

    ___ create_signals
        push_close.c__.c..(close)
        push_save.c__.c..(set_custom_path)
        push_browse.c__.c..(browse)

    ___ browse
        dialog _ ?W...QFileDialog()
        dialog.sWF..(?C...__.WindowStaysOnTopHint)
        dialog.setFileMode(?W...QFileDialog.Directory)
        dialog.setOption(?W...QFileDialog.ShowDirsOnly)
        __ dialog.exec_() __ ?W...QDialog.Accepted:
            input_path.setText(dialog.selectedFiles()[0])

    ___ set_custom_path
        ___
            __ no. __.pa__.isd..(input_path.text()):
                __.m_d_(input_path.text())
        ______
            __ input_path.t.. !_ '':
                msg _ "Failed setting up the path '{}' as custom {} directory. Please choose a different path.".f..(input_path.t.., which)
                show_message_box(, msg)
                r_

        meta_xml _ get_meta_xml(shot_root)
        metatree _ ET.parse(meta_xml)
        metaroot _ metatree.getroot()
        w__ o..(meta_xml, 'w') __ xml:
            ___ child __ metaroot.find('notes').f_a_('note'):
                __ which __ 'render':
                    __ child.get('name') __ 'renderpath':
                        child.text _ input_path.t..
                        child.set('loc', 'global')
                        __ input_path.t.. __ '':
                            child.set('loc', 'local')
                ____ which __ 'footage':
                    __ child.get('name') __ 'footagepath':
                        child.text _ input_path.t..
                        child.set('loc', 'global')
                        __ input_path.t.. __ '':
                            child.set('loc', 'local')

            prettyprint(metaroot)
            metatree.w..(xml, encoding_'utf-8', xml_declaration_T..)
        __ input_path.t.. __ '':
            msg _ 'Successfully cleared the custom {} path'.f..(which)
            show_message_box(, msg)
        ____
            msg _ "Successfully set up the custom {} path to: '{}'".f..(which, input_path.text())
            show_message_box(, msg)
        c__
        __ sml __ no. N..:
            ___
                __ which __ 'render':
                    sml.current_shot_widget.set_renderpath(input_path.text())
                ____ which __ 'footage':
                    sml.current_shot_widget.set_footagepath(input_path.text())
                sml.current_shot_widget.refresh()
            ______ E.. __ e:
                p..

        r_

    ___ load_custom_path(, which):
        meta_xml _ get_meta_xml(shot_root)
        metatree _ ET.parse(meta_xml)
        metaroot _ metatree.getroot()
        ___ child __ metaroot.find('notes').f_a_('note'):
            __ child.get('name') __ '{}path'.f..(which):
                __ child.get('loc') an. child.get('loc') __ 'global':
                    r_ child.text
                ____
                    r_ ''

    ___ keyPressEvent(, event):
        __ event.key() __ ?C...__.Key_Escape:
            c__