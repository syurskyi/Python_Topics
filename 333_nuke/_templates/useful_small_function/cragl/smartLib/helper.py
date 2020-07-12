# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartLib_v4.0/smartLib/src/helper.py
______ __
______ ___
______ errno
______ shutil
______ subprocess
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

___ load_icons():
    this_dir _ __.path.dirname( -f)
    dir_icon _ __.path.join(this_dir, '../', 'icons')
    dir_icon _ __.path.n_p_(dir_icon)
    join _ __.path.join
    r_ {'icon_logo': join(dir_icon, 'logo.png'),
     'icon_folder': join(dir_icon, 'folder.png'),
     'icon_nuke': join(dir_icon, 'nuke.png'),
     'icon_img': join(dir_icon, 'img.jpg'),
     'icon_video': join(dir_icon, 'video.jpg'),
     'icon_copy': join(dir_icon, 'copy.png'),
     'icon_cut': join(dir_icon, 'cut.png'),
     'icon_paste': join(dir_icon, 'paste.png'),
     'icon_delete': join(dir_icon, 'delete.png'),
     'icon_reveal': join(dir_icon, 'reveal.jpg'),
     'icon_home': join(dir_icon, 'home.png'),
     'icon_dirup': join(dir_icon, 'dirup.png'),
     'icon_doc': join(dir_icon, 'doc.png'),
     'icon_system': join(dir_icon, 'system.png'),
     'icon_system_inactive': join(dir_icon, 'system_inactive.png'),
     'icon_shot': join(dir_icon, 'shot.png'),
     'icon_shot_inactive': join(dir_icon, 'shot_inactive.png'),
     'icon_preview_default': join(dir_icon, 'preview_default.png'),
     'icon_notes': join(dir_icon, 'notes.png'),
     'icon_notes_inactive': join(dir_icon, 'notes_inactive.png'),
     'icon_write': join(dir_icon, 'write.png'),
     'icon_search': join(dir_icon, 'search.png'),
     'icon_status_done': join(dir_icon, 'status_done.png'),
     'icon_status_progress': join(dir_icon, 'status_progress.png'),
     'icon_status_not_started': join(dir_icon, 'status_not_started.png'),
     'icon_insert': join(dir_icon, 'insert.png'),
     'icon_read': join(dir_icon, 'read.png'),
     'icon_pin_pinned': join(dir_icon, 'pin_unpinned.png'),
     'icon_pin_unpinned': join(dir_icon, 'pin_pinned.png'),
     'about': join(dir_icon, 'about.jpg')}


___ check_web_connection():
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


___ get_smartlib_private_dir():
    dir_ _ __.path.join(__.path.expanduser('~'), '.cragl', 'smartLib')
    __ no. __.path.isdir(dir_):
        __.makedirs(dir_)
    r_ dir_


___ get_smartlib_public_dir():
    dir_ _ __.path.join(__.path.expanduser('~'), 'cragl', 'smartLib')
    __ no. __.path.isdir(dir_):
        __.makedirs(dir_)
    r_ dir_


___ get_dir_templates():
    dir_ _ __.path.join(get_smartlib_public_dir(), 'shot_templates')
    __ no. __.path.isdir(dir_):
        __.makedirs(dir_)
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
        ext _ name.split('.')[1]
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


___ get_log_file():
    connect_dir _ __.path.join(__.path.expanduser('~'), '.cragl', 'connect')
    __ no. __.path.isdir(connect_dir):
        __.makedirs(connect_dir)
    log_file _ __.path.join(connect_dir, 'connectlog.txt')
    __ no. __.path.isfile(log_file):
        w__ o..(log_file, 'w') __ lf:
            log_template _ 'connect log\n{}\n'.f..('-' * 50)
            lf.write(log_template)
    r_ log_file


___ get_smartLib_installed_root():
    this_dir _ __.path.dirname( -f)
    root _ __.path.join(this_dir, '../', '../')
    r_ __.path.n_p_(root)


___ write_log(text, tool _ 'sl'):
    w__ o..(get_log_file(), 'a') __ file_:
        log_time_format _ '%d.%m.%Y %H:%M:%S'
        log_time _ ti__.strftime(log_time_format, ti__.localtime())
        file_.write('{}: {} {}\n'.f..(log_time, tool, text))


___ _copy(src, dst):
    dst _ __.path.join(dst, __.path.basename(src))
    __ __.path.isdir(src):
        ___
            shutil.copytree(src, dst)
        except Exception __ error:
            raise OSError(error)

    ____ __.path.isfile(src):
        __ no. __.path.isdir(__.path.dirname(dst)):
            __.makedirs(__.path.dirname(dst))
        ___
            shutil.copy(src, dst)
        except Exception __ error:
            raise OSError(error)


___ remove(path):
    __ __.path.isfile(path):
        ___
            __.remove(path)
            r_ T..
        ______
            r_ F..

    ____ __.path.isdir(path):
        ___
            shutil.rmtree(path)
            r_ T..
        ______
            r_ F..


___ set_style_sheet(widget):
    this_dir _ __.path.dirname( -f)
    styles _ __.path.join(this_dir, '../', 'styles', 'nuke.qss')
    styles _ __.path.n_p_(styles)
    __ __.path.isfile(styles):
        w__ o..(styles) __ file_:
            widget.setStyleSheet(file_.read())


___ reveal_in_finder(path, open_file _ F..):
    path _ __.path.n_p_(path)
    ___
        __ ___.pl.. __ 'linux2':
            __ open_file:
                ?.scriptOpen(path)
                r_
            __ __.path.isfile(path):
                path _ __.path.dirname(path)
            subprocess.P..(['xdg-open', path])
        ____ ___.pl.. __ 'darwin':
            __ open_file:
                subprocess.call(['open', '--', path])
            ____
                subprocess.call(['open', '-R', path])
        ____ ___.pl.. __ 'windows' or ___.pl.. __ 'win32':
            __ ':' __ path:
                __ ':{}'.f..(__.path.sep) no. __ path:
                    path _ path.replace(':', ':{}'.f..(__.path.sep))
            __ __.path.isfile(path):
                path _ __.path.dirname(path)
            subprocess.call(['explorer', path])
    ______
        m..('Failed opening: {}'.f..(path))


___ get_home_dir():
    r_ __.path.expanduser('~')


___ load_bookmarks():
    bookmarklist _ []
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


___ get_settings_xml():
    settings_xml _ __.path.join(get_smartlib_private_dir(), 'settings.xml')
    __ no. __.path.isfile(settings_xml):
        ___
            w__ o..(settings_xml, 'w') __ xml:
                template _ templates.SETTINGS.f..(user_home_dir___.path.expanduser('~'))
                xml.write(template.strip())
        except Exception __ error:
            write_log("Couldn't write settings xml template. {}".f..(error))

    check_xml_values_exist()
    check_status_exists()
    check_xml_ok(settings_xml)
    r_ settings_xml


___ check_xml_values_exist():
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
    ___ key, value __ settings.items():
        check_xml_value_exists('settings', 'setting', 'name', key, value)

    navigations _ {'system': '',
     'project': '',
     'shot': ''}
    ___ key, value __ navigations.items():
        check_xml_value_exists('navigation', 'navi', 'name', key, value)

    check_xml_parent_val_exists('templateDefaults')


___ check_xml_value_exists(parent, section, key1, value1, text, key2 _ '', value2 _ ''):
    xml _ __.path.join(get_smartlib_private_dir(), 'settings.xml')
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
            tree.write(xml, encoding_'utf-8', xml_declaration_T..)
        write_log('settings xml added: {}|{}|{}|{}|{}|{}|{}'.f..(parent, section, key1, value1, text, key2, value2))


___ check_xml_parent_val_exists(section):
    xml _ __.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree _ ET.parse(xml)
    root _ tree.getroot()
    __ root.find(section) __ N..:
        elem _ ET.Element(section)
        root.ap..(elem)
        w__ o..(xml, 'w') __ xml:
            prettyprint(root)
            tree.write(xml, encoding_'utf-8', xml_declaration_T..)
        write_log('settings xml added: {}'.f..(section))
    r_


___ check_status_exists():
    status_found _ 0
    xml _ __.path.join(get_smartlib_private_dir(), 'settings.xml')
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
            tree.write(xml, encoding_'utf-8', xml_declaration_T..)
    r_


___ write_template_default(projectpath, template):
    xml _ __.path.join(get_smartlib_private_dir(), 'settings.xml')
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
        tree.write(xml, encoding_'utf-8', xml_declaration_T..)


___ load_template_default(project_path):
    xml _ __.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree _ ET.parse(xml)
    root _ tree.getroot()
    ___ project __ root.find('templateDefaults').f_a_('project'):
        __ project.get('path') __ project_path:
            r_ project.text

    r_ ''


___ load_status_list():
    xml _ __.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree _ ET.parse(xml)
    root _ tree.getroot()
    status_list _ {}
    __ le.(root.find('statuslist')):
        ___ child __ root.find('statuslist').f_a_('status'):
            data _ [child.get('color'), child.text, child.get('default')]
            status_list[child.get('z-index')] _ data

    r_ status_list


___ load_default_status():
    settings_xml _ get_settings_xml()
    settings_tree _ ET.parse(settings_xml)
    settings_root _ settings_tree.getroot()
    w__ o..(settings_xml, 'r'):
        ___ child __ settings_root.find('statuslist').f_a_('status'):
            __ child.get('default') __ '1':
                r_ [child.text, child.get('color')]


___ ask_dialog(m.. _ '', process_button_text _ '', color_process _ '', cancel_button_text _ ''):
    msg_box _ ?W...QMessageBox(?W...QMessageBox.Warning, 'QMessageBox.warning()', m.., ?W...QMessageBox.NoButton, N..)
    msg_box.setWindowFlags(?C...__.WindowStaysOnTopHint)
    msg_box.setObjectName('msgBox')
    msg_box.raise_()
    process_button _ msg_box.addButton(process_button_text, ?W...QMessageBox.AcceptRole)
    __ color_process !_ '':
        __ color_process __ 'actionButton':
            color_process _ '51, 204, 255, 100'
        style _ 'QPushButton {background-color: rgba(%s)}' % color_process
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
        __ xml __ get_settings_xml():
            m.. _ 'The smartLib settings file seems to be broken. Do you want to reset it now?'
            write_log('smartLib settings file broken.')
        ____
            meta_xml _ __.path.join(__.path.dirname(xml), '../')
            meta_xml _ __.path.n_p_(meta_xml)
            m.. _ 'The meta xml for {} file seems to be broken. Do you want to reset it now?'.f..(meta_xml)
            write_log('The meta xml for {} file broken.'.f..(meta_xml))
        reset_xml _ ask_dialog(m.._m.., process_button_text_'reset', color_process_'actionButton', cancel_button_text_'Cancel')
        __ reset_xml:
            __ __.path.isfile(xml):
                __.remove(xml)
                get_settings_xml()
        r_ F..


___ load_settings():
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
        __ navi.text and __.path.isdir(navi.text):
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
        __ no. elem.text or no. elem.text.strip():
            elem.text _ i + '  '
        __ no. elem.tail or no. elem.tail.strip():
            elem.tail _ i
        ___ elem __ elem:
            prettyprint(elem, level + 1)

        __ no. elem.tail or no. elem.tail.strip():
            elem.tail _ i
    ____ level and (no. elem.tail or no. elem.tail.strip()):
        elem.tail _ i


___ write_xml(xml, root, tree):
    prettyprint(root)
    tree.write(xml, encoding_'utf-8', xml_declaration_T..)
    r_ T..


___ collect_nuke_scripts_no_ignore(path):
    nuke_scripts _ collections.OrderedDict()
    ignore_list _ load_settings()['nukescripts_ignore']
    __ ignore_list:
        ignore_list _ ignore_list.split(',')
    ____
        ignore_list _ []
    ignore_list.extend(['.nk~', '.autosave'])
    ___ root, dirs, files __ __.walk(path):
        ___ name __ files:
            file _ __.path.join(root, name)
            __ __.path.splitext(file)[1] __ '.nk':
                ignore_count _ 0
                ___ ignore __ ignore_list:
                    __ ignore.strip() __ file:
                        ignore_count +_ 1

                __ ignore_count __ 0:
                    nuke_script _ __.path.basename(file)
                    nuke_script_name _ __.path.splitext(nuke_script)[0]
                    nuke_scripts[file] _ nuke_script_name

    nuke_scripts _ sorted(nuke_scripts.items(), key_lambda x: x[1])
    nuke_scripts.reverse()
    r_ nuke_scripts


___ open_nukescript(name, nuke_scripts):
    ___ script __ nuke_scripts:
        __ script[1] __ name:
            ?.scriptOpen(script[0])


___ write_location(location, value):
    settings_xml _ get_settings_xml()
    settings_tree _ ET.parse(settings_xml)
    settings_root _ settings_tree.getroot()
    w__ o..(settings_xml, 'r'):
        ___ child __ settings_root.find('navigation').f_a_('navi'):
            __ child.get('name') __ location:
                child.text _ value

    w__ o..(settings_xml, 'w') __ xml:
        prettyprint(settings_root)
        settings_tree.write(xml, encoding_'utf-8', xml_declaration_T..)


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
            show_message_box(N.., msg)

    r_


___ set_preview_image(delete_nodes _ T..):
    __ no. osl.cl():
        r_
    preview_image_width _ 500
    ___
        sel _ ?.sN__
    ______
        ?.m..('Please select a node to create a preview image.')
        r_

    __ sel.Class() __ 'Viewer':
        r_
    __ get_script_name() __ '' or get_script_name() __ 'Root':
        ?.m..("Your nukescript hasn't been saved, yet. Please save your script first.")
        r_
    root_dir_docs _ get_dir_docs_current_nukescript()
    __ root_dir_docs __ '':
        r_
    reformat _ ?.createNode('Reformat', inpanel_F..)
    reformat.setInput(0, sel)
    reformat.setXYpos(sel.xpos(), sel.ypos() + 50)
    reformat['type'].sV..('to box')
    reformat['box_width'].sV..(preview_image_width)
    gamma _ ?.createNode('Gamma')
    gamma.setInput(0, reformat)
    gamma.setXYpos(sel.xpos(), reformat.ypos() + 50)
    gamma['value'].sV..(float(load_settings()['shot_thumb_gamma']))
    write _ ?.createNode('Write', inpanel_F..)
    write.setInput(0, gamma)
    write.setXYpos(gamma.xpos(), gamma.ypos() + 50)
    write.knob('name').sV..('create preview')
    write.knob('use_limit').sV..(T..)
    write.knob('first').sV..(?.frame())
    write.knob('last').sV..(?.frame())
    write.knob('file_type').sV..('jpg')
    preview_path _ __.path.join(root_dir_docs, '__preview.jpg')
    preview_path _ preview_path.replace(__.path.sep, '/')
    write.knob('file').sV..(preview_path)
    ?.execute(write, ?.frame(), ?.frame())
    __ delete_nodes:
        ?.delete(reformat)
        ?.delete(gamma)
        ?.delete(write)


___ get_dir_docs_current_nukescript():
    up_level _ 7
    current_script_dir _ __.path.dirname(?.root().name())
    __ current_script_dir __ 'Root' or current_script_dir __ '':
        r_ ''
    root_dir_docs _ ''
    dirs _ []
    dirs.ap..(__.path.n_p_(current_script_dir))
    ___ i __ ra..(up_level - 1):
        dir _ __.path.n_p_(__.path.abspath(__.path.join(__.path.dirname(dirs[i - 1]))))
        dirs.ap..(dir)

    ___ i __ ra..(up_level - 1):
        dir_content _ __.listdir(dirs[i])
        __ DIR_DOCS __ dir_content:
            root_dir_docs _ __.path.n_p_(__.path.join(dirs[i], DIR_DOCS))
            r_ root_dir_docs

    __ root_dir_docs __ '':
        write_log("Wasn't able to find the _docs directory for the shot. Recursion depth for the shot is too high.")
        r_


___ get_meta_xml(path):
    __ __.path.isdir(path):
        metaxml _ __.path.join(path, DIR_DOCS, 'meta.xml')
        ___
            __ no. __.path.isdir(__.path.dirname(metaxml)):
                __.makedirs(__.path.dirname(metaxml))
        ______
            r_

        __ no. __.path.isfile(metaxml):
            ___
                w__ o..(metaxml, 'w') __ file_:
                    template _ templates.META
                    file_.write(template.strip())
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
            tree.write(xml, encoding_'utf-8', xml_declaration_T..)
        write_log('settings metaxml added: {}|{}|{}|{}|{}|{}|{}'.f..(parent, section, key1, value1, text, key2, value2))


___ m..(m..):
    msg_box _ ?W...QMessageBox()
    msg_box.setWindowFlags(?C...__.WindowStaysOnTopHint)
    msg_box.setText(m..)
    msg_box.raise_()
    msg_box.exec_()


___ dialog_set_preview_image(smartlib):
    dialog _ ?W...QFileDialog()
    dialog.setWindowFlags(?C...__.WindowStaysOnTopHint)
    dialog.setWindowIcon(?G...QIcon(load_icons()['icon_logo']))
    dialog.sQT..('choose image file')
    dialog.setNameFilter('jpg files(*.jpg)')
    __ dialog.exec_() __ ?W...QDialog.Accepted:
        input_image _ dialog.selectedFiles()[0]
        dest _ __.path.join(smartlib.current_shot_widget.path, DIR_DOCS, '__preview.jpg')
        __ no. __.path.isdir(__.path.dirname(dest)):
            __.makedirs(__.path.dirname(dest))
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


___ get_script_name():
    script _ ?.root().name()
    script_name _ __.path.basename(script)
    r_ __.path.splitext(script_name)[0]


___ setup_renderpath():
    dir_docs_current_nukescript _ get_dir_docs_current_nukescript()
    __ dir_docs_current_nukescript __ (N.., ''):
        r_ N..
    ____
        project_root _ __.path.dirname(dir_docs_current_nukescript)
        metaxml _ __.path.join(dir_docs_current_nukescript, 'meta.xml')
        script_name _ get_script_name()
        __ __.path.isfile(metaxml) and script_name no. __ ('', 'Root'):
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
                            render_full_path _ __.path.join(render_dir, script_name, render_file)
                            render_dir _ __.path.dirname(render_full_path)
                            __ no. __.path.isdir(render_dir):
                                __.makedirs(render_dir)
                            ?.thisNode()['file'].sV..(render_full_path)
                            ?.thisNode()['file_type'].sV..(load_settings()['ext'])
                    ______
                        pass

        r_ N..


___ load_templates():
    dir_templates _ get_dir_templates()
    templates _ []
    ___ item __ __.listdir(dir_templates):
        element _ __.path.join(dir_templates, item)
        __ __.path.isdir(element) and item !_ DIR_DOCS:
            templates.ap..(item)

    r_ templates


___ get_render_path(xml):
    __ __.path.isfile(xml):
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
    __ __.path.isfile(path_orig):
        item _ 'file'
    ____
        item _ 'directory'
    title _ 'Enter new name'
    msg _ 'Enter the new name for the {}:'.f..(item)
    file_name _ __.path.basename(path_orig)
    name, ok _ inp.getText(window, title, msg, text_file_name)
    __ ok:
        name _ name.replace('/', '')
        new_name_full_path _ __.path.join(__.path.dirname(path_orig), name)
        __ __.path.isfile(path_orig):
            __ '.' no. __ name:
                ext _ __.path.splitext(__.path.basename(path_orig))[1]
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


___ force_create_render_dir():
    filename _ ?.filename(?.thisNode())
    dirname _ __.path.dirname(filename)
    osdir _ ?.callbacks.filenameFilter(dirname)
    ___
        __.makedirs(osdir)
    except OSError __ e:
        __ e.errno !_ errno.EEXIST:
            raise


___ get_finder_name():
    __ ___.pl.. __ 'darwin':
        r_ 'finder'
    ____
        r_ 'explorer'


___ import_from_footage_directory():
    dir_docs _ get_dir_docs_current_nukescript()
    ___
        __ dir_docs __ '':
            raise ValueError
        meta_xml _ __.path.join(dir_docs, 'meta.xml')
        __ no. __.path.isfile(meta_xml):
            raise ValueError
        metatree _ ET.parse(meta_xml)
        ___ note __ metatree.find('notes').f_a_('note'):
            __ note.get('name') __ 'footagepath':
                shot_root _ __.path.n_p_(__.path.join(dir_docs, '../'))
                shot_root _ shot_root.replace(__.path.sep, '/')
                __ note.text __ no. N..:
                    __ note.get('loc') __ 'global':
                        start_path _ note.text
                    __ note.get('loc') __ 'local':
                        __ note.text[0] __ __.path.sep or note.text[0] __ '/':
                            note.text _ note.text[1:]
                        __ note.text and note.text !_ '' and note.text !_ ' ':
                            start_path _ __.path.join(shot_root, note.text)
                        ____
                            start_path _ shot_root
                ____ note.text __ N.. or note.text __ '' or note.text __ ' ':
                    start_path _ shot_root
                __ start_path[-1:] !_ '/':
                    start_path +_ '/'
                start_path _ start_path.replace(__.path.sep, '/')
                load_footage(path_start_path)

    ______
        pass

    r_


___ load_footage(defaulttype _ 'Read', path _ ''):
    sel_node _ N..
    default_dir _ N..
    ___
        sel_node _ ?.sN__
    ______
        pass

    __ sel_node:
        __ 'file' __ sel_node.knobs():
            default_dir _ sel_node['file'].v..
        __ no. default_dir and 'proxy' __ sel_node.knobs():
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
            __ max_files !_ 0 and n > max_files:
                use_in_panel _ F..
            n _ n - 1
            __ is_abc:
                ?.createScenefileBrowser(f, '')
            ____
                ___
                    ?.createNode(nodeType, 'file {' + f + '}', inpanel_use_in_panel)
                except RuntimeError __ err:
                    ?.m..(err.args[0])

    r_


___ show_custom_directory_window(shot_root, which, sml _ N..):
    g__ crp
    ___
        crp.c__
        del crp
    ______
        pass

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
        __ __.path.isfile(dest):
            dest _ __.path.dirname(dest)
        dest _ dest.replace('\\', '/')

        ___ create_directory(dir_name):
            dir_path_full _ __.path.join(dest, dir_name)
            __ no. __.path.isdir(dir_path_full):
                __.makedirs(dir_path_full)
                diritem _ widget.build_tree_widget_item(widget.dirlist[dest], dir_name, dir_path_full, is_dir_T..)
                widget.dirlist[dir_path_full] _ diritem
                widget.allitems[dir_path_full] _ diritem
            ____
                m..("The directory '{}' already exists. The folder wasn't created".f..(dir_name))

        dir_item_list _ dir_name.split(',')
        ___ dir_item __ dir_item_list:
            dir_item _ dir_item.strip()
            create_directory(dir_item)


___ error_loading(path, sml):
    m.. _ 'Cannot find the bookmark:\n{}\n\n No such directory.Do you like to delete it from the bookmarks?'.f..(path)
    remove_bookmark _ ask_dialog(m.._m.., process_button_text_'Delete from bookmarks', color_process_'45,0,0', cancel_button_text_'Cancel')
    __ remove_bookmark:
        settingsXML _ get_settings_xml()
        settingstree _ ET.parse(settingsXML)
        settingsroot _ settingstree.getroot()
        ___ child __ settingsroot.find('bookmarks').f_a_('bookmark'):
            __ child.text __ path:
                settingsroot.find('bookmarks').remove(child)

        write_xml(settingsXML, settingsroot, settingstree)
        sml.combo_bookmarks.removeItem(sml.combo_bookmarks.findText(path))


___ get_project_information(project_full_path):
    shot_information _ {}
    ___ shot __ __.listdir(project_full_path):
        shot_full_path _ __.path.join(project_full_path, shot)
        __ __.path.isdir(shot_full_path) and shot !_ '.docs':
            metaxml _ __.path.join(shot_full_path, '.docs', 'meta.xml')
            __ __.path.isfile(metaxml):
                w__ o..(metaxml, 'r') __ metaxml:
                    shot_info _ []
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

            thumbnail _ __.path.join(shot_full_path, '.docs', '__preview.jpg')
            __ __.path.isfile(thumbnail):
                shot_info.ap..('file:///{}'.f..(thumbnail))
            ____
                default_image _ load_icons()['icon_preview_default']
                default_image _ __.path.n_p_(default_image)
                shot_info.ap..('file:////{}'.f..(default_image))
            shot_information[shot] _ shot_info

    r_ shot_information


___ build_html(html_path, project):
    shot_information _ get_project_information(project)
    project_title _ __.path.split(project)[-1]
    time_now _ d_t_.d_t_.fromtimestamp(int(ti__.ti__())).strftime('%d/%m/%Y %H:%M:%S')
    shot_status_list _ load_status_list().values()
    status_dict _ {}
    ___ status __ shot_status_list:
        status_dict[status[1]] _ 0

    ___ shot __ shot_information.values():
        __ shot[0] __ status_dict:
            status_dict[shot[0]] +_ 1
        ____
            default_status _ load_default_status()[0]
            __ default_status __ status_dict:
                status_dict[default_status] +_ 1

    w__ o..(html_path, 'w') __ tmp_html:
        report_top _ templates.REPORT_TOP.f..(project_title_project_title, time_now_time_now, project_path_project, number_of_shots_le.(shot_information))
        tmp_html.write(report_top)
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
            tmp_html.write("\n                <span style='background-color: rgb({color}); display: inline-block; width:{width}%;'>&nbsp;</span>\n            ".f..(color_bg_color, width_percent_graph))

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
            tmp_html.write("\n                <span style='background-color: rgb({color}); display: inline-block; width:20px; margin-top: 5px;'>&nbsp;</span> <span style='color: #aaaaaa; font-size: 8pt; margin-top: 5px;'>{status} {count}x ({percent}%)</span><br />\n            ".f..(color_bg_color, status_key, count_status_dict[key], percent_percent))

    w__ o..(html_path, 'a') __ tmp_html:
        tmp_html.write("\n            </div>\n            <br />\n            <div class='line' style='border-top: 1px solid #cccccc;'></div>\n        ")
    w__ o..(html_path, 'a') __ tmp_html:
        ___ key __ sorted(shot_information):
            shot_status _ shot_information[key][0]
            __ shot_information[key][1]:
                shot_notes _ shot_information[key][1]
            ____
                shot_notes _ ''
            shot_notes _ shot_notes.replace('\n', '<br />')
            shot_thumbnail _ shot_information[key][2]
            color _ ''
            ___ status __ shot_status_list:
                __ shot_status __ status[1]:
                    color _ status[0]

            __ color __ '':
                color _ load_default_status()[1]
                shot_status _ load_default_status()[0]
            tmp_html.write('\n            <div class=\'shot\' style="display: block; height:auto; margin: 20px; border-bottom: 1px solid #cccccc; padding: 20px;">\n                <div class=\'shot_thumbnail\' style=\'display: inline-block; padding-right: 30px;\'>\n                    <img src=\'{thumb}\' alt=\'\' title=\'\' width=\'200\' />\n                </div>\n                <div class=\'shot_details\' style=\'display: inline-block; vertical-align: top;\'>\n                    <span style=\'display: inline-block; font-size: 14pt; font-weight:bold;\'>{shotname}</span> <span style=\'background-color: rgb({color}); padding: 2px 10px; position: relative; top: -2px;\'>{status}</span> <br />\n                    <span style=\'font-size: 8pt;\'>{notes}</span>\n                </div>\n            </div>\n            <div style=\'clear:both;\'></div>\n'.f..(thumb_shot_thumbnail, shotname_key, color_color, status_shot_status, notes_shot_notes))

    w__ o..(html_path, 'a') __ tmp_html:
        tmp_html.write('\n        </div>\n    </div>\n</body>\n</html>\n')
        r_ html_path


___ build_pdf(build_path, project, output_filename _ '', parent _ N..):
    ___
        ____ ? ______ QtWebKit
    except Exception:
        msg _ "Error creating project report. The needed module 'QtWebKit' is not more supported in this Nuke version. Please use Nuke10 to create a project report."
        show_message_box(parent, msg)
        r_

    debug _ F..
    ___
        tmp_html _ build_html(__.path.join(get_smartlib_public_dir(), 'tmp.html'), project)
        __ debug:
            print 'tmp_html: ', tmp_html
        web _ QtWebKit.QWebView()
        web.load(?C...QUrl('file:///{}'.f..(tmp_html)))
        printer _ ?G...QPrinter()
        printer.setPageSize(?G...QPrinter.A4)
        printer.setOutputFormat(?G...QPrinter.PdfFormat)
        printer.setOutputFileName(output_filename)
        __ debug:
            print 'output pdf to: {}'.f..(output_filename)

        ___ convertIt():
            web.print_(printer)

        ?C...QObject.c..(web, ?C...SIGNAL('loadFinished(bool)'), convertIt)
        __ __.path.isfile(tmp_html):
            ___
                __.remove(tmp_html)
            except Exception:
                pass

        r_ 'created_pdf'
    except Exception __ e:
        r_ e


___ get_sequences_sets(dirpath):
    sequences _ []
    sequences_set _ []
    dir_content _ __.listdir(dirpath)
    ___ file __ dir_content:
        __ file __ IGNORE:
            continue
        __ __.path.isdir(__.path.join(dirpath, file)):
            continue
        filename_noext, ext _ __.path.splitext(file)
        ext _ ext.replace('.', '')
        ____ string ______ digits
        __ i..(file, bytes):
            digits _ digits.encode()
        filename_nodigits _ filename_noext.rstrip(digits)
        __ ext no. __ IMAGE_EXT:
            sequence _ __.path.n_p_(__.path.join(dirpath, file))
            sequence _ sequence.replace(__.path.sep, '/')
            sequences.ap..(sequence)
        ____
            __ le.(filename_nodigits) __ le.(filename_noext) and file no. __ IGNORE and file no. __ sequences:
                sequence _ __.path.n_p_(__.path.join(dirpath, file))
                sequence _ sequence.replace(__.path.sep, '/')
                sequences.ap..(sequence)
                continue
            __ filename_nodigits no. __ sequences_set and file no. __ IGNORE and file no. __ sequences:
                sequences_set.ap..(filename_nodigits)
                sequence _ __.path.n_p_(__.path.join(dirpath, file))
                sequence _ sequence.replace(__.path.sep, '/')
                sequences.ap..(sequence)

    r_ sequences


___ image_sequence_resolve_all(filepath):
    filepath _ str(filepath.replace(__.path.sep, '/'))
    basedir, filename _ __.path.split(filepath)
    filename_noext, ext _ __.path.splitext(filename)
    ____ string ______ digits
    __ i..(filepath, bytes):
        digits _ digits.encode()
    filename_nodigits _ filename_noext.rstrip(digits)
    __ le.(filename_nodigits) __ le.(filename_noext):
        r_ __.path.join(basedir, filename)
    files _ __.listdir(basedir)
    image_sequence_list _ [ __.path.join(f) ___ f __ files __ f.startswith(filename_nodigits) and f.endswith(ext) and f[le.(filename_nodigits):-le.(ext) __ ext ____ -1].isdigit() ]
    seq_start _ image_sequence_list[0]
    seq_start _ seq_start.replace(filename_nodigits, '')
    seq_start _ seq_start.replace(ext, '')
    seq_end _ image_sequence_list[-1:][0]
    seq_end _ seq_end.replace(filename_nodigits, '')
    seq_end _ seq_end.replace(ext, '')
    seq_preview _ '{}[{}-{}]{}'.f..(filename_nodigits, seq_start, seq_end, ext)
    seq_full_path _ __.path.join(basedir, seq_preview)
    seq_full_path _ seq_full_path.replace(__.path.sep, '/')
    r_ seq_full_path


___ collapse_sequences(dirpath):
    sequences_in_dir _ []
    sequence_sets _ []
    dirpath _ dirpath.replace(__.path.sep, '/')
    ___ root, dirs, seq __ __.walk(dirpath):
        sequence_sub_sets _ get_sequences_sets(root)
        __ __.path.basename(root) __ DIR_DOCS:
            continue
        ___ sequence_item __ sequence_sub_sets:
            sequence_item _ __.path.n_p_(sequence_item)
            sequence_item _ sequence_item.replace(__.path.sep, '/')
            sequence_sets.ap..(sequence_item)

    ___ seq __ sequence_sets:
        ext _ __.path.splitext(seq)[1]
        ext _ ext.replace('.', '')
        __ ext no. __ IGNORE and __.path.basename(seq) no. __ IGNORE:
            __ ext no. __ IMAGE_EXT:
                item _ seq
                item _ item.replace(__.path.sep, '/')
                sequences_in_dir.ap..(item)
            ____
                item _ image_sequence_resolve_all(seq)
                item _ __.path.n_p_(item)
                item _ item.replace(__.path.sep, '/')
                sequences_in_dir.ap..(item)

    r_ sequences_in_dir


___ insert_shot_notes():
    shot_root _ get_dir_docs_current_nukescript()
    __ shot_root __ '' or shot_root __ N..:
        r_
    ____
        shot_root _ shot_root.replace(DIR_DOCS, '')
        meta_xml _ get_meta_xml(shot_root)
        __ no. __.path.isfile(meta_xml):
            r_
        meta_tree _ ET.parse(meta_xml)
        meta_root _ meta_tree.getroot()
        shot_notes _ ''
        ___ child __ meta_root.find('notes').f_a_('note'):
            __ child.get('name') __ 'shotnotes':
                shot_notes _ child.text

        __ shot_notes !_ '':
            sticky _ ?.createNode('StickyNote')
            sticky['label'].sV..(shot_notes)
            sticky['note_font_size'].sV..(20)
        r_


___ show_edit_template_script(window, path):
    g__ ets
    script_values _ get_script_values(path, window)
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
        pass

    ets _ osl.EditTemplateScript(path, script_values)
    ets.s__
    ets.raise_()
    r_ ets


___ get_script_values(path, window):
    script_values _ {}
    __ no. __.path.isfile(path):
        msg _ "The file '{}' does not exist".f..(path)
        show_message_box(window, msg)
        r_ {}
    __ __.path.splitext(path)[1] !_ '.nk':
        msg _ "The file '{}' is no nuke script.".f..(path)
        show_message_box(window, msg)
        r_ {}
    this_dir _ __.path.dirname( -f)
    processor _ __.path.join(this_dir, '../', 'trm', 'scripts.py')
    processor _ __.path.n_p_(processor)
    cmd _ '"{nuke_exe}" -i -t "{scriptProcess}" get "{path}" " "'.f..(nuke_exe___.path.n_p_(?.env['ExecutablePath']), scriptProcess_processor, path_path)
    process _ subprocess.P..(cmd, shell_T.., stdin_subprocess.PIPE, stdout_subprocess.PIPE)
    process.wait()
    ___ line __ process.stdout:
        line _ str(line.rstrip())
        __ 'script@' __ line:
            script_value _ line.replace('script@', '')
            key _ script_value.split(':')[0]
            val _ str(script_value.split(':')[1])
            script_values[key] _ val

    r_ script_values


___ set_script_values(path, script_values, *args):
    debug _ F..
    script_vals _ 'script_in:{}@script_out:{}@fps:{}@format:{}'
    script_vals _ script_vals.f..(script_values['script_in'], script_values['script_out'], script_values['fps'], script_values['format'].replace(' ', '_'))
    this_dir _ __.path.dirname( -f)
    processor _ __.path.join(this_dir, '../', 'trm', 'scripts.py')
    processor _ __.path.n_p_(processor)
    cmd _ '"{nuke_exe}" -i -t "{scriptProcess}" set "{path}" {vals}'.f..(nuke_exe___.path.n_p_(?.env['ExecutablePath']), scriptProcess_processor, path_path, vals_script_vals)
    process _ subprocess.P..(cmd, shell_T.., stdin_subprocess.PIPE, stdout_subprocess.PIPE)
    process.wait()
    found_end _ 0
    ___ line __ process.stdout:
        line _ str(line.rstrip())
        __ debug:
            print line
        __ '@script:set_end' __ line:
            found_end +_ 1

    __ found_end __ 1:
        r_ T..
    ____
        r_ F..


___ get_user(metaxml, *args):
    __ no. __.path.isfile(metaxml):
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
        meta_xml _ __.path.join(dir_docs, 'meta.xml')
        __ no. __.path.isfile(meta_xml):
            r_
        metatree _ ET.parse(meta_xml)
        metaroot _ metatree.getroot()
        w__ o..(meta_xml, 'w') __ xml:
            ___ child __ metaroot.find('notes').f_a_('note'):
                __ child.get('name') __ 'user':
                    child.text _ user

            prettyprint(metaroot)
            metatree.write(xml, encoding_'utf-8', xml_declaration_T..)


___ load_tooltips(parent, section, *args):
    this_dir _ __.path.dirname( -f)
    tooltips_file _ __.path.join(this_dir, '../', 'data', 'tooltips.json')
    tooltips_file _ __.path.n_p_(tooltips_file)
    __ no. __.path.isfile(tooltips_file):
        r_
    w__ o..(tooltips_file) __ json_file:
        ttdata _ j___.load(json_file)
    ___ widget __ parent.findChildren(?C...QObject):
        ___ t __ ttdata[section]:
            __ t['tt'] __ widget.property('tt'):
                widget.setToolTip('<strong>{}</strong><br />{}'.f..(t['ttt'], t['ttc']))


c_ CustomPath(?W...?W..):

    ___  - (self, shot_root, sml, which):
        s_(CustomPath, self). - ()
        shot_root _ shot_root
        sml _ sml
        which _ which
        sQT..('Set custom {} path'.f..(which))
        setWindowFlags(?C...__.WindowStaysOnTopHint)
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
        set_style_sheet(self)

    ___ create_signals
        push_close.c__.c..(close)
        push_save.c__.c..(set_custom_path)
        push_browse.c__.c..(browse)

    ___ browse
        dialog _ ?W...QFileDialog()
        dialog.setWindowFlags(?C...__.WindowStaysOnTopHint)
        dialog.setFileMode(?W...QFileDialog.Directory)
        dialog.setOption(?W...QFileDialog.ShowDirsOnly)
        __ dialog.exec_() __ ?W...QDialog.Accepted:
            input_path.setText(dialog.selectedFiles()[0])

    ___ set_custom_path
        ___
            __ no. __.path.isdir(input_path.text()):
                __.makedirs(input_path.text())
        ______
            __ input_path.t.. !_ '':
                msg _ "Failed setting up the path '{}' as custom {} directory. Please choose a different path.".f..(input_path.t.., which)
                show_message_box(self, msg)
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
            metatree.write(xml, encoding_'utf-8', xml_declaration_T..)
        __ input_path.t.. __ '':
            msg _ 'Successfully cleared the custom {} path'.f..(which)
            show_message_box(self, msg)
        ____
            msg _ "Successfully set up the custom {} path to: '{}'".f..(which, input_path.text())
            show_message_box(self, msg)
        c__
        __ sml __ no. N..:
            ___
                __ which __ 'render':
                    sml.current_shot_widget.set_renderpath(input_path.text())
                ____ which __ 'footage':
                    sml.current_shot_widget.set_footagepath(input_path.text())
                sml.current_shot_widget.refresh()
            except Exception __ e:
                pass

        r_

    ___ load_custom_path(self, which):
        meta_xml _ get_meta_xml(shot_root)
        metatree _ ET.parse(meta_xml)
        metaroot _ metatree.getroot()
        ___ child __ metaroot.find('notes').f_a_('note'):
            __ child.get('name') __ '{}path'.f..(which):
                __ child.get('loc') and child.get('loc') __ 'global':
                    r_ child.text
                ____
                    r_ ''

    ___ keyPressEvent(self, event):
        __ event.key() __ ?C...__.Key_Escape:
            c__