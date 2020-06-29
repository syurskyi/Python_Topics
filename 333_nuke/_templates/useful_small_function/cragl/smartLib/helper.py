# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartLib_v4.0/smartLib/src/helper.py
______ os
______ sys
______ errno
______ shutil
______ subprocess
______ xml.etree.ElementTree as ET
______ collections
______ urllib
______ time
______ datetime
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
______ osl
______ templates
DIR_DOCS = '.docs'
IMAGE_EXT = ['exr',
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
VIDEO_EXT = ['mov',
 'avi',
 'mpg',
 'mpeg',
 'wmv',
 'flv',
 'm4v',
 'mp4']
IGNORE = ['.DS_Store', '.nk~', '.autosave']

___ load_icons():
    this_dir = os.path.dirname(__file__)
    dir_icon = os.path.join(this_dir, '../', 'icons')
    dir_icon = os.path.normpath(dir_icon)
    join = os.path.join
    return {'icon_logo': join(dir_icon, 'logo.png'),
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
    try:
        urllib.urlopen('http://www.cragl.com')
        return True
    except:
        return False


___ show_message_box(window, message):
    QtWidgets.QMessageBox().information(window, 'information', message)


___ message_confirm_overwrite(src, is_file = True):
    __ is_file:
        item = 'File'
    ____
        item = 'Directory'
    message = "{} '{}' already exists.\nDo you want to overwrite it?".format(item, src)
    overwrite = ask_dialog(message=message, process_button_text='Overwrite', color_process='45,0,0', cancel_button_text='Cancel')
    return overwrite


___ get_smartlib_private_dir():
    dir_ = os.path.join(os.path.expanduser('~'), '.cragl', 'smartLib')
    __ not os.path.isdir(dir_):
        os.makedirs(dir_)
    return dir_


___ get_smartlib_public_dir():
    dir_ = os.path.join(os.path.expanduser('~'), 'cragl', 'smartLib')
    __ not os.path.isdir(dir_):
        os.makedirs(dir_)
    return dir_


___ get_dir_templates():
    dir_ = os.path.join(get_smartlib_public_dir(), 'shot_templates')
    __ not os.path.isdir(dir_):
        os.makedirs(dir_)
    return dir_


___ set_item_icon(listwidget_item, name, is_dir, is_render_dir = False, is_footage_dir = False, icons = None):
    __ is_dir:
        try:
            listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_folder']))
            __ is_render_dir:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_write']))
            elif is_footage_dir:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_read']))
        except:
            listwidget_item.setIcon(QtGui.QIcon(icons['icon_folder']))
            __ is_render_dir:
                listwidget_item.setIcon(QtGui.QIcon(icons['icon_write']))
            elif is_footage_dir:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_read']))

    __ '.' __ name:
        ext = name.split('.')[1]
        __ ext == 'nk':
            try:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_nuke']))
            except:
                listwidget_item.setIcon(QtGui.QIcon(icons['icon_nuke']))

        elif ext.lower() __ IMAGE_EXT:
            try:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_img']))
            except:
                listwidget_item.setIcon(QtGui.QIcon(icons['icon_img']))

        elif ext __ VIDEO_EXT:
            try:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_video']))
            except:
                listwidget_item.setIcon(QtGui.QIcon(icons['icon_video']))

        ____
            try:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_doc']))
            except:
                listwidget_item.setIcon(QtGui.QIcon(icons['icon_doc']))


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


___ get_smartLib_installed_root():
    this_dir = os.path.dirname(__file__)
    root = os.path.join(this_dir, '../', '../')
    return os.path.normpath(root)


___ write_log(text, tool = 'sl'):
    with open(get_log_file(), 'a') as file_:
        log_time_format = '%d.%m.%Y %H:%M:%S'
        log_time = time.strftime(log_time_format, time.localtime())
        file_.write('{}: {} {}\n'.format(log_time, tool, text))


___ _copy(src, dst):
    dst = os.path.join(dst, os.path.basename(src))
    __ os.path.isdir(src):
        try:
            shutil.copytree(src, dst)
        except Exception as error:
            raise OSError(error)

    elif os.path.isfile(src):
        __ not os.path.isdir(os.path.dirname(dst)):
            os.makedirs(os.path.dirname(dst))
        try:
            shutil.copy(src, dst)
        except Exception as error:
            raise OSError(error)


___ remove(path):
    __ os.path.isfile(path):
        try:
            os.remove(path)
            return True
        except:
            return False

    elif os.path.isdir(path):
        try:
            shutil.rmtree(path)
            return True
        except:
            return False


___ set_style_sheet(widget):
    this_dir = os.path.dirname(__file__)
    styles = os.path.join(this_dir, '../', 'styles', 'nuke.qss')
    styles = os.path.normpath(styles)
    __ os.path.isfile(styles):
        with open(styles) as file_:
            widget.setStyleSheet(file_.read())


___ reveal_in_finder(path, open_file = False):
    path = os.path.normpath(path)
    try:
        __ sys.platform == 'linux2':
            __ open_file:
                ?.scriptOpen(path)
                return
            __ os.path.isfile(path):
                path = os.path.dirname(path)
            subprocess.Popen(['xdg-open', path])
        elif sys.platform == 'darwin':
            __ open_file:
                subprocess.call(['open', '--', path])
            ____
                subprocess.call(['open', '-R', path])
        elif sys.platform == 'windows' or sys.platform == 'win32':
            __ ':' __ path:
                __ ':{}'.format(os.path.sep) not __ path:
                    path = path.replace(':', ':{}'.format(os.path.sep))
            __ os.path.isfile(path):
                path = os.path.dirname(path)
            subprocess.call(['explorer', path])
    except:
        message('Failed opening: {}'.format(path))


___ get_home_dir():
    return os.path.expanduser('~')


___ load_bookmarks():
    bookmarklist = []
    bookmarklist.ap..('bookmarks')
    bookmarklist.ap..('add to bookmarks')
    bookmarklist.ap..('delete from bookmarks')
    bookmarklist.ap..('--------------------')
    settingsXML = get_settings_xml()
    settings_tree = ET.parse(settingsXML)
    settings_root = settings_tree.getroot()
    ___ child __ settings_root.find('bookmarks').findall('bookmark'):
        bookmarklist.ap..(child.text)

    return bookmarklist


___ get_settings_xml():
    settings_xml = os.path.join(get_smartlib_private_dir(), 'settings.xml')
    __ not os.path.isfile(settings_xml):
        try:
            with open(settings_xml, 'w') as xml:
                template = templates.SETTINGS.format(user_home_dir=os.path.expanduser('~'))
                xml.write(template.strip())
        except Exception as error:
            write_log("Couldn't write settings xml template. {}".format(error))

    check_xml_values_exist()
    check_status_exists()
    check_xml_ok(settings_xml)
    return settings_xml


___ check_xml_values_exist():
    settings = {'show_system': 'True',
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

    navigations = {'system': '',
     'project': '',
     'shot': ''}
    ___ key, value __ navigations.items():
        check_xml_value_exists('navigation', 'navi', 'name', key, value)

    check_xml_parent_val_exists('templateDefaults')


___ check_xml_value_exists(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = os.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = False
    item_found = 0
    ___ child __ root.find(parent).findall(section):
        __ child.get(key1) == value1:
            item_found += 1
            __ debug:
                print 'smartLib | settings exists: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2)
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


___ check_xml_parent_val_exists(section):
    xml = os.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    __ root.find(section) is None:
        elem = ET.Element(section)
        root.ap..(elem)
        with open(xml, 'w') as xml:
            prettyprint(root)
            tree.write(xml, encoding='utf-8', xml_declaration=True)
        write_log('settings xml added: {}'.format(section))
    return


___ check_status_exists():
    status_found = 0
    xml = os.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    __ le.(root.find('statuslist')):
        ___ child __ root.find('statuslist').findall('status'):
            status_found += 1

    __ status_found == 0:
        default_status = templates.DEFAULT_STATUS
        __ root.find('statuslist') is None:
            statuslist_elem = ET.Element('statuslist')
            root.ap..(statuslist_elem)
        ___ key __ sorted(default_status):
            status_elem = ET.Element('status')
            status_elem.set('z-index', key)
            status_elem.set('color', default_status[key][0])
            status_elem.text = default_status[key][1]
            status_elem.set('default', default_status[key][2])
            root.find('statuslist').ap..(status_elem)

        with open(xml, 'w') as xml:
            prettyprint(root)
            tree.write(xml, encoding='utf-8', xml_declaration=True)
    return


___ write_template_default(projectpath, template):
    xml = os.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    elem_exists = False
    ___ project __ root.find('templateDefaults').findall('project'):
        __ project.get('path') == projectpath:
            elem_exists = True
            project.text = template
            break

    __ not elem_exists:
        projectelement = ET.Element('project')
        projectelement.set('path', projectpath)
        projectelement.text = template
        root.find('templateDefaults').ap..(projectelement)
    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


___ load_template_default(project_path):
    xml = os.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    ___ project __ root.find('templateDefaults').findall('project'):
        __ project.get('path') == project_path:
            return project.text

    return ''


___ load_status_list():
    xml = os.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    status_list = {}
    __ le.(root.find('statuslist')):
        ___ child __ root.find('statuslist').findall('status'):
            data = [child.get('color'), child.text, child.get('default')]
            status_list[child.get('z-index')] = data

    return status_list


___ load_default_status():
    settings_xml = get_settings_xml()
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    with open(settings_xml, 'r'):
        ___ child __ settings_root.find('statuslist').findall('status'):
            __ child.get('default') == '1':
                return [child.text, child.get('color')]


___ ask_dialog(message = '', process_button_text = '', color_process = '', cancel_button_text = ''):
    msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, 'QMessageBox.warning()', message, QtWidgets.QMessageBox.NoButton, None)
    msg_box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg_box.setObjectName('msgBox')
    msg_box.raise_()
    process_button = msg_box.addButton(process_button_text, QtWidgets.QMessageBox.AcceptRole)
    __ color_process != '':
        __ color_process == 'actionButton':
            color_process = '51, 204, 255, 100'
        style = 'QPushButton {background-color: rgba(%s)}' % color_process
        process_button.setStyleSheet(style)
    process_button.clearFocus()
    msg_box.setFocus()
    msg_box.addButton(cancel_button_text, QtWidgets.QMessageBox.RejectRole)
    __ msg_box.exec_() == QtWidgets.QMessageBox.AcceptRole:
        return True
    ____
        return False
        return


___ check_xml_ok(xml):
    try:
        with open(xml, 'r') as xml_file:
            ET.fromstring(xml_file.read())
        return True
    except:
        __ xml == get_settings_xml():
            message = 'The smartLib settings file seems to be broken. Do you want to reset it now?'
            write_log('smartLib settings file broken.')
        ____
            meta_xml = os.path.join(os.path.dirname(xml), '../')
            meta_xml = os.path.normpath(meta_xml)
            message = 'The meta xml for {} file seems to be broken. Do you want to reset it now?'.format(meta_xml)
            write_log('The meta xml for {} file broken.'.format(meta_xml))
        reset_xml = ask_dialog(message=message, process_button_text='reset', color_process='actionButton', cancel_button_text='Cancel')
        __ reset_xml:
            __ os.path.isfile(xml):
                os.remove(xml)
                get_settings_xml()
        return False


___ load_settings():
    settings_xml = get_settings_xml()
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    settings = {}
    ___ setting __ settings_root.find('settings').findall('setting'):
        __ setting.text:
            settings[setting.get('name')] = setting.text
        ____
            settings[setting.get('name')] = ''

    ___ navi __ settings_root.find('navigation').findall('navi'):
        __ navi.text and os.path.isdir(navi.text):
            settings['current_{}'.format(navi.get('name'))] = navi.text
        ____
            settings['current_{}'.format(navi.get('name'))] = ''

    return settings


___ center_window(window):
    qr = window.frameGeometry()
    cp = QtWidgets.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


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


___ write_xml(xml, root, tree):
    prettyprint(root)
    tree.write(xml, encoding='utf-8', xml_declaration=True)
    return True


___ collect_nuke_scripts_no_ignore(path):
    nuke_scripts = collections.OrderedDict()
    ignore_list = load_settings()['nukescripts_ignore']
    __ ignore_list:
        ignore_list = ignore_list.split(',')
    ____
        ignore_list = []
    ignore_list.extend(['.nk~', '.autosave'])
    ___ root, dirs, files __ os.walk(path):
        ___ name __ files:
            file = os.path.join(root, name)
            __ os.path.splitext(file)[1] == '.nk':
                ignore_count = 0
                ___ ignore __ ignore_list:
                    __ ignore.strip() __ file:
                        ignore_count += 1

                __ ignore_count == 0:
                    nuke_script = os.path.basename(file)
                    nuke_script_name = os.path.splitext(nuke_script)[0]
                    nuke_scripts[file] = nuke_script_name

    nuke_scripts = sorted(nuke_scripts.items(), key=lambda x: x[1])
    nuke_scripts.reverse()
    return nuke_scripts


___ open_nukescript(name, nuke_scripts):
    ___ script __ nuke_scripts:
        __ script[1] == name:
            ?.scriptOpen(script[0])


___ write_location(location, value):
    settings_xml = get_settings_xml()
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    with open(settings_xml, 'r'):
        ___ child __ settings_root.find('navigation').findall('navi'):
            __ child.get('name') == location:
                child.text = value

    with open(settings_xml, 'w') as xml:
        prettyprint(settings_root)
        settings_tree.write(xml, encoding='utf-8', xml_declaration=True)


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
            show_message_box(None, msg)

    return


___ set_preview_image(delete_nodes = True):
    __ not osl.cl():
        return
    preview_image_width = 500
    try:
        sel = ?.sN__
    except:
        ?.message('Please select a node to create a preview image.')
        return

    __ sel.Class() == 'Viewer':
        return
    __ get_script_name() == '' or get_script_name() == 'Root':
        ?.message("Your nukescript hasn't been saved, yet. Please save your script first.")
        return
    root_dir_docs = get_dir_docs_current_nukescript()
    __ root_dir_docs == '':
        return
    reformat = ?.createNode('Reformat', inpanel=False)
    reformat.setInput(0, sel)
    reformat.setXYpos(sel.xpos(), sel.ypos() + 50)
    reformat['type'].sV..('to box')
    reformat['box_width'].sV..(preview_image_width)
    gamma = ?.createNode('Gamma')
    gamma.setInput(0, reformat)
    gamma.setXYpos(sel.xpos(), reformat.ypos() + 50)
    gamma['value'].sV..(float(load_settings()['shot_thumb_gamma']))
    write = ?.createNode('Write', inpanel=False)
    write.setInput(0, gamma)
    write.setXYpos(gamma.xpos(), gamma.ypos() + 50)
    write.knob('name').sV..('create preview')
    write.knob('use_limit').sV..(True)
    write.knob('first').sV..(?.frame())
    write.knob('last').sV..(?.frame())
    write.knob('file_type').sV..('jpg')
    preview_path = os.path.join(root_dir_docs, '__preview.jpg')
    preview_path = preview_path.replace(os.path.sep, '/')
    write.knob('file').sV..(preview_path)
    ?.execute(write, ?.frame(), ?.frame())
    __ delete_nodes:
        ?.delete(reformat)
        ?.delete(gamma)
        ?.delete(write)


___ get_dir_docs_current_nukescript():
    up_level = 7
    current_script_dir = os.path.dirname(?.root().name())
    __ current_script_dir == 'Root' or current_script_dir == '':
        return ''
    root_dir_docs = ''
    dirs = []
    dirs.ap..(os.path.normpath(current_script_dir))
    ___ i __ ra..(up_level - 1):
        dir = os.path.normpath(os.path.abspath(os.path.join(os.path.dirname(dirs[i - 1]))))
        dirs.ap..(dir)

    ___ i __ ra..(up_level - 1):
        dir_content = os.listdir(dirs[i])
        __ DIR_DOCS __ dir_content:
            root_dir_docs = os.path.normpath(os.path.join(dirs[i], DIR_DOCS))
            return root_dir_docs

    __ root_dir_docs == '':
        write_log("Wasn't able to find the _docs directory for the shot. Recursion depth for the shot is too high.")
        return


___ get_meta_xml(path):
    __ os.path.isdir(path):
        metaxml = os.path.join(path, DIR_DOCS, 'meta.xml')
        try:
            __ not os.path.isdir(os.path.dirname(metaxml)):
                os.makedirs(os.path.dirname(metaxml))
        except:
            return

        __ not os.path.isfile(metaxml):
            try:
                with open(metaxml, 'w') as file_:
                    template = templates.META
                    file_.write(template.strip())
            except:
                write_log("Couldn't write meta xml template at: {}".format(metaxml))

        check_meta_xml_values_exist(metaxml)
        return metaxml


___ check_meta_xml_values_exist(metaxml):
    check_meta_xml_value_exists(metaxml, 'notes', 'note', 'name', 'footagepath', ' ', key2='loc', value2='local')
    check_meta_xml_value_exists(metaxml, 'notes', 'note', 'name', 'user', ' ')


___ check_meta_xml_value_exists(metaxml_path, parent, section, key1, value1, text, key2 = '', value2 = ''):
    tree = ET.parse(metaxml_path)
    root = tree.getroot()
    debug = False
    item_found = 0
    ___ child __ root.find(parent).findall(section):
        __ child.get(key1) == value1:
            item_found += 1
            __ debug:
                print 'smartLib | metaxml exists: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2)
            return

    __ item_found == 0:
        elem = ET.Element(section)
        elem.set(key1, value1)
        __ key2 != '':
            elem.set(key2, value2)
        elem.text = text
        root.find(parent).ap..(elem)
        with open(metaxml_path, 'w') as xml:
            prettyprint(root)
            tree.write(xml, encoding='utf-8', xml_declaration=True)
        write_log('settings metaxml added: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2))


___ message(message):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg_box.setText(message)
    msg_box.raise_()
    msg_box.exec_()


___ dialog_set_preview_image(smartlib):
    dialog = QtWidgets.QFileDialog()
    dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    dialog.setWindowIcon(QtGui.QIcon(load_icons()['icon_logo']))
    dialog.setWindowTitle('choose image file')
    dialog.setNameFilter('jpg files(*.jpg)')
    __ dialog.exec_() == QtWidgets.QDialog.Accepted:
        input_image = dialog.selectedFiles()[0]
        dest = os.path.join(smartlib.current_shot_widget.path, DIR_DOCS, '__preview.jpg')
        __ not os.path.isdir(os.path.dirname(dest)):
            os.makedirs(os.path.dirname(dest))
        save_image_scaled(input_image, dest)
        smartlib.current_shot_widget.refresh()
        current_project = load_settings()['current_project']
        smartlib.table_current_project.load_shots(current_project)


___ save_image_scaled(src, dest):
    img = QtGui.QImage(src)
    try:
        pixmap = QtGui.QPixmap(img.scaledToWidth(500))
        pixmap.save(dest)
        return True
    except:
        write_log('Cannot create image scaled.')
        return False


___ get_script_name():
    script = ?.root().name()
    script_name = os.path.basename(script)
    return os.path.splitext(script_name)[0]


___ setup_renderpath():
    dir_docs_current_nukescript = get_dir_docs_current_nukescript()
    __ dir_docs_current_nukescript __ (None, ''):
        return None
    ____
        project_root = os.path.dirname(dir_docs_current_nukescript)
        metaxml = os.path.join(dir_docs_current_nukescript, 'meta.xml')
        script_name = get_script_name()
        __ os.path.isfile(metaxml) and script_name not __ ('', 'Root'):
            meta_tree = ET.parse(metaxml)
            meta_root = meta_tree.getroot()
            ___ child __ meta_root.find('notes').findall('note'):
                __ child.get('name') == 'renderpath':
                    try:
                        __ child.text.strip() != '':
                            __ child.get('loc') == 'global':
                                render_dir = '{}'.format(child.text)
                            ____
                                render_dir = '{}{}'.format(project_root, child.text)
                            render_file = '{}{}%0{}d.{}'.format(script_name, load_settings()['padding_delimiter'], load_settings()['padding'], load_settings()['ext'])
                            render_full_path = os.path.join(render_dir, script_name, render_file)
                            render_dir = os.path.dirname(render_full_path)
                            __ not os.path.isdir(render_dir):
                                os.makedirs(render_dir)
                            ?.thisNode()['file'].sV..(render_full_path)
                            ?.thisNode()['file_type'].sV..(load_settings()['ext'])
                    except:
                        pass

        return None


___ load_templates():
    dir_templates = get_dir_templates()
    templates = []
    ___ item __ os.listdir(dir_templates):
        element = os.path.join(dir_templates, item)
        __ os.path.isdir(element) and item != DIR_DOCS:
            templates.ap..(item)

    return templates


___ get_render_path(xml):
    __ os.path.isfile(xml):
        try:
            meta_tree = ET.parse(xml)
            meta_root = meta_tree.getroot()
        except:
            write_log('Unable to parse metaxml.')
            return

        ___ child __ meta_root.find('notes').findall('note'):
            __ child.get('name') == 'renderpath':
                return child.text

    ____
        write_log("Metaxml doesn't exist in: {}".format(xml))


___ rename_item(sender, path_orig, window):
    inp = QtWidgets.QInputDialog()
    inp.setObjectName('inp')
    __ os.path.isfile(path_orig):
        item = 'file'
    ____
        item = 'directory'
    title = 'Enter new name'
    msg = 'Enter the new name for the {}:'.format(item)
    file_name = os.path.basename(path_orig)
    name, ok = inp.getText(window, title, msg, text=file_name)
    __ ok:
        name = name.replace('/', '')
        new_name_full_path = os.path.join(os.path.dirname(path_orig), name)
        __ os.path.isfile(path_orig):
            __ '.' not __ name:
                ext = os.path.splitext(os.path.basename(path_orig))[1]
                new_name_full_path = '{}{}'.format(new_name_full_path, ext)
        __ sender == 'smartlibshotwindow':
            os.rename(path_orig, new_name_full_path)
            window.populate_tree()
        __ sender == 'shot_templates':
            os.rename(path_orig, new_name_full_path)
            window.load_shot_template_in_tree()
        __ sender == 'saved_projects':
            settingsXML = get_settings_xml()
            settingstree = ET.parse(settingsXML)
            settingsroot = settingstree.getroot()
            ___ child __ settingsroot.find('projectslist').findall('project'):
                __ child.text == path_orig:
                    child.set('name', name)

            write_xml(settingsXML, settingsroot, settingstree)
            window.populate_saved_projects()


___ force_create_render_dir():
    filename = ?.filename(?.thisNode())
    dirname = os.path.dirname(filename)
    osdir = ?.callbacks.filenameFilter(dirname)
    try:
        os.makedirs(osdir)
    except OSError as e:
        __ e.errno != errno.EEXIST:
            raise


___ get_finder_name():
    __ sys.platform == 'darwin':
        return 'finder'
    ____
        return 'explorer'


___ import_from_footage_directory():
    dir_docs = get_dir_docs_current_nukescript()
    try:
        __ dir_docs == '':
            raise ValueError
        meta_xml = os.path.join(dir_docs, 'meta.xml')
        __ not os.path.isfile(meta_xml):
            raise ValueError
        metatree = ET.parse(meta_xml)
        ___ note __ metatree.find('notes').findall('note'):
            __ note.get('name') == 'footagepath':
                shot_root = os.path.normpath(os.path.join(dir_docs, '../'))
                shot_root = shot_root.replace(os.path.sep, '/')
                __ note.text is not None:
                    __ note.get('loc') == 'global':
                        start_path = note.text
                    __ note.get('loc') == 'local':
                        __ note.text[0] == os.path.sep or note.text[0] == '/':
                            note.text = note.text[1:]
                        __ note.text and note.text != '' and note.text != ' ':
                            start_path = os.path.join(shot_root, note.text)
                        ____
                            start_path = shot_root
                elif note.text is None or note.text == '' or note.text == ' ':
                    start_path = shot_root
                __ start_path[-1:] != '/':
                    start_path += '/'
                start_path = start_path.replace(os.path.sep, '/')
                load_footage(path=start_path)

    except:
        pass

    return


___ load_footage(defaulttype = 'Read', path = ''):
    sel_node = None
    default_dir = None
    try:
        sel_node = ?.sN__
    except:
        pass

    __ sel_node:
        __ 'file' __ sel_node.knobs():
            default_dir = sel_node['file'].value()
        __ not default_dir and 'proxy' __ sel_node.knobs():
            default_dir = sel_node['proxy'].value()
    __ default_dir == '':
        default_dir = None
    files = ?.getClipname('import from footage directory', default=path, multiple=True)
    __ files != None:
        max_files = ?.numvalue('preferences.maxPanels')
        n = le.(files)
        ___ f __ files:
            is_abc = False
            stripped = ?.stripFrameRange(f)
            nodeType = defaulttype
            __ nukescripts.create.isAudioFilename(stripped):
                nodeType = 'AudioRead'
            __ nukescripts.create.isGeoFilename(stripped):
                nodeType = 'ReadGeo2'
            __ nukescripts.create.isAbcFilename(stripped):
                is_abc = True
            __ nukescripts.create.isDeepFilename(stripped):
                nodeType = 'DeepRead'
            use_in_panel = True
            __ max_files != 0 and n > max_files:
                use_in_panel = False
            n = n - 1
            __ is_abc:
                ?.createScenefileBrowser(f, '')
            ____
                try:
                    ?.createNode(nodeType, 'file {' + f + '}', inpanel=use_in_panel)
                except RuntimeError as err:
                    ?.message(err.args[0])

    return


___ show_custom_directory_window(shot_root, which, sml = None):
    global crp
    try:
        crp.close()
        del crp
    except:
        pass

    crp = CustomPath(shot_root, sml, which)
    crp.raise_()
    crp.show()


___ create_new_directory(widget, list_):
    inp = QtWidgets.QInputDialog()
    inp.setObjectName('inp')
    title = 'Enter name'
    msg = 'Enter the name of the new folder:'
    dir_name, ok = inp.getText(widget, title, msg)
    __ ok:
        dest = list_.data(0, QtCore.Qt.UserRole)
        __ os.path.isfile(dest):
            dest = os.path.dirname(dest)
        dest = dest.replace('\\', '/')

        ___ create_directory(dir_name):
            dir_path_full = os.path.join(dest, dir_name)
            __ not os.path.isdir(dir_path_full):
                os.makedirs(dir_path_full)
                diritem = widget.build_tree_widget_item(widget.dirlist[dest], dir_name, dir_path_full, is_dir=True)
                widget.dirlist[dir_path_full] = diritem
                widget.allitems[dir_path_full] = diritem
            ____
                message("The directory '{}' already exists. The folder wasn't created".format(dir_name))

        dir_item_list = dir_name.split(',')
        ___ dir_item __ dir_item_list:
            dir_item = dir_item.strip()
            create_directory(dir_item)


___ error_loading(path, sml):
    message = 'Cannot find the bookmark:\n{}\n\n No such directory.Do you like to delete it from the bookmarks?'.format(path)
    remove_bookmark = ask_dialog(message=message, process_button_text='Delete from bookmarks', color_process='45,0,0', cancel_button_text='Cancel')
    __ remove_bookmark:
        settingsXML = get_settings_xml()
        settingstree = ET.parse(settingsXML)
        settingsroot = settingstree.getroot()
        ___ child __ settingsroot.find('bookmarks').findall('bookmark'):
            __ child.text == path:
                settingsroot.find('bookmarks').remove(child)

        write_xml(settingsXML, settingsroot, settingstree)
        sml.combo_bookmarks.removeItem(sml.combo_bookmarks.findText(path))


___ get_project_information(project_full_path):
    shot_information = {}
    ___ shot __ os.listdir(project_full_path):
        shot_full_path = os.path.join(project_full_path, shot)
        __ os.path.isdir(shot_full_path) and shot != '.docs':
            metaxml = os.path.join(shot_full_path, '.docs', 'meta.xml')
            __ os.path.isfile(metaxml):
                with open(metaxml, 'r') as metaxml:
                    shot_info = []
                    tree = ET.parse(metaxml)
                    root = tree.getroot()
                    ___ child __ root.find('notes').findall('note'):
                        __ child.get('name') == 'status':
                            status = child.text
                            __ status is None or status == '':
                                status = ''
                            shot_info.ap..(status)
                        __ child.get('name') == 'shotnotes':
                            shot_info.ap..(child.text)

            thumbnail = os.path.join(shot_full_path, '.docs', '__preview.jpg')
            __ os.path.isfile(thumbnail):
                shot_info.ap..('file:///{}'.format(thumbnail))
            ____
                default_image = load_icons()['icon_preview_default']
                default_image = os.path.normpath(default_image)
                shot_info.ap..('file:////{}'.format(default_image))
            shot_information[shot] = shot_info

    return shot_information


___ build_html(html_path, project):
    shot_information = get_project_information(project)
    project_title = os.path.split(project)[-1]
    time_now = datetime.datetime.fromtimestamp(int(time.time())).strftime('%d/%m/%Y %H:%M:%S')
    shot_status_list = load_status_list().values()
    status_dict = {}
    ___ status __ shot_status_list:
        status_dict[status[1]] = 0

    ___ shot __ shot_information.values():
        __ shot[0] __ status_dict:
            status_dict[shot[0]] += 1
        ____
            default_status = load_default_status()[0]
            __ default_status __ status_dict:
                status_dict[default_status] += 1

    with open(html_path, 'w') as tmp_html:
        report_top = templates.REPORT_TOP.format(project_title=project_title, time_now=time_now, project_path=project, number_of_shots=le.(shot_information))
        tmp_html.write(report_top)
    ___ key __ sorted(status_dict):
        with open(html_path, 'a') as tmp_html:
            bg_color = '255,255,255'
            ___ status __ shot_status_list:
                __ key == status[1]:
                    bg_color = status[0]

            __ status_dict[key] != 0:
                percent = 100.0 / le.(shot_information) * status_dict[key]
                percent_graph = percent - 1
            ____
                percent = 0.0
                percent_graph = 0.0
            percent = '{0:.1f}'.format(percent)
            tmp_html.write("\n                <span style='background-color: rgb({color}); display: inline-block; width:{width}%;'>&nbsp;</span>\n            ".format(color=bg_color, width=percent_graph))

    ___ key __ sorted(status_dict):
        with open(html_path, 'a') as tmp_html:
            bg_color = '255,255,255'
            ___ status __ shot_status_list:
                __ key == status[1]:
                    bg_color = status[0]

            __ status_dict[key] != 0:
                percent = 100.0 / le.(shot_information) * status_dict[key]
            ____
                percent = 0.0
            percent = '{0:.1f}'.format(percent)
            tmp_html.write("\n                <span style='background-color: rgb({color}); display: inline-block; width:20px; margin-top: 5px;'>&nbsp;</span> <span style='color: #aaaaaa; font-size: 8pt; margin-top: 5px;'>{status} {count}x ({percent}%)</span><br />\n            ".format(color=bg_color, status=key, count=status_dict[key], percent=percent))

    with open(html_path, 'a') as tmp_html:
        tmp_html.write("\n            </div>\n            <br />\n            <div class='line' style='border-top: 1px solid #cccccc;'></div>\n        ")
    with open(html_path, 'a') as tmp_html:
        ___ key __ sorted(shot_information):
            shot_status = shot_information[key][0]
            __ shot_information[key][1]:
                shot_notes = shot_information[key][1]
            ____
                shot_notes = ''
            shot_notes = shot_notes.replace('\n', '<br />')
            shot_thumbnail = shot_information[key][2]
            color = ''
            ___ status __ shot_status_list:
                __ shot_status == status[1]:
                    color = status[0]

            __ color == '':
                color = load_default_status()[1]
                shot_status = load_default_status()[0]
            tmp_html.write('\n            <div class=\'shot\' style="display: block; height:auto; margin: 20px; border-bottom: 1px solid #cccccc; padding: 20px;">\n                <div class=\'shot_thumbnail\' style=\'display: inline-block; padding-right: 30px;\'>\n                    <img src=\'{thumb}\' alt=\'\' title=\'\' width=\'200\' />\n                </div>\n                <div class=\'shot_details\' style=\'display: inline-block; vertical-align: top;\'>\n                    <span style=\'display: inline-block; font-size: 14pt; font-weight:bold;\'>{shotname}</span> <span style=\'background-color: rgb({color}); padding: 2px 10px; position: relative; top: -2px;\'>{status}</span> <br />\n                    <span style=\'font-size: 8pt;\'>{notes}</span>\n                </div>\n            </div>\n            <div style=\'clear:both;\'></div>\n'.format(thumb=shot_thumbnail, shotname=key, color=color, status=shot_status, notes=shot_notes))

    with open(html_path, 'a') as tmp_html:
        tmp_html.write('\n        </div>\n    </div>\n</body>\n</html>\n')
        return html_path


___ build_pdf(build_path, project, output_filename = '', parent = None):
    try:
        from PySide ______ QtWebKit
    except Exception:
        msg = "Error creating project report. The needed module 'QtWebKit' is not more supported in this Nuke version. Please use Nuke10 to create a project report."
        show_message_box(parent, msg)
        return

    debug = False
    try:
        tmp_html = build_html(os.path.join(get_smartlib_public_dir(), 'tmp.html'), project)
        __ debug:
            print 'tmp_html: ', tmp_html
        web = QtWebKit.QWebView()
        web.load(QtCore.QUrl('file:///{}'.format(tmp_html)))
        printer = QtGui.QPrinter()
        printer.setPageSize(QtGui.QPrinter.A4)
        printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        printer.setOutputFileName(output_filename)
        __ debug:
            print 'output pdf to: {}'.format(output_filename)

        ___ convertIt():
            web.print_(printer)

        QtCore.QObject.connect(web, QtCore.SIGNAL('loadFinished(bool)'), convertIt)
        __ os.path.isfile(tmp_html):
            try:
                os.remove(tmp_html)
            except Exception:
                pass

        return 'created_pdf'
    except Exception as e:
        return e


___ get_sequences_sets(dirpath):
    sequences = []
    sequences_set = []
    dir_content = os.listdir(dirpath)
    ___ file __ dir_content:
        __ file __ IGNORE:
            continue
        __ os.path.isdir(os.path.join(dirpath, file)):
            continue
        filename_noext, ext = os.path.splitext(file)
        ext = ext.replace('.', '')
        from string ______ digits
        __ i..(file, bytes):
            digits = digits.encode()
        filename_nodigits = filename_noext.rstrip(digits)
        __ ext not __ IMAGE_EXT:
            sequence = os.path.normpath(os.path.join(dirpath, file))
            sequence = sequence.replace(os.path.sep, '/')
            sequences.ap..(sequence)
        ____
            __ le.(filename_nodigits) == le.(filename_noext) and file not __ IGNORE and file not __ sequences:
                sequence = os.path.normpath(os.path.join(dirpath, file))
                sequence = sequence.replace(os.path.sep, '/')
                sequences.ap..(sequence)
                continue
            __ filename_nodigits not __ sequences_set and file not __ IGNORE and file not __ sequences:
                sequences_set.ap..(filename_nodigits)
                sequence = os.path.normpath(os.path.join(dirpath, file))
                sequence = sequence.replace(os.path.sep, '/')
                sequences.ap..(sequence)

    return sequences


___ image_sequence_resolve_all(filepath):
    filepath = str(filepath.replace(os.path.sep, '/'))
    basedir, filename = os.path.split(filepath)
    filename_noext, ext = os.path.splitext(filename)
    from string ______ digits
    __ i..(filepath, bytes):
        digits = digits.encode()
    filename_nodigits = filename_noext.rstrip(digits)
    __ le.(filename_nodigits) == le.(filename_noext):
        return os.path.join(basedir, filename)
    files = os.listdir(basedir)
    image_sequence_list = [ os.path.join(f) ___ f __ files __ f.startswith(filename_nodigits) and f.endswith(ext) and f[le.(filename_nodigits):-le.(ext) __ ext ____ -1].isdigit() ]
    seq_start = image_sequence_list[0]
    seq_start = seq_start.replace(filename_nodigits, '')
    seq_start = seq_start.replace(ext, '')
    seq_end = image_sequence_list[-1:][0]
    seq_end = seq_end.replace(filename_nodigits, '')
    seq_end = seq_end.replace(ext, '')
    seq_preview = '{}[{}-{}]{}'.format(filename_nodigits, seq_start, seq_end, ext)
    seq_full_path = os.path.join(basedir, seq_preview)
    seq_full_path = seq_full_path.replace(os.path.sep, '/')
    return seq_full_path


___ collapse_sequences(dirpath):
    sequences_in_dir = []
    sequence_sets = []
    dirpath = dirpath.replace(os.path.sep, '/')
    ___ root, dirs, seq __ os.walk(dirpath):
        sequence_sub_sets = get_sequences_sets(root)
        __ os.path.basename(root) == DIR_DOCS:
            continue
        ___ sequence_item __ sequence_sub_sets:
            sequence_item = os.path.normpath(sequence_item)
            sequence_item = sequence_item.replace(os.path.sep, '/')
            sequence_sets.ap..(sequence_item)

    ___ seq __ sequence_sets:
        ext = os.path.splitext(seq)[1]
        ext = ext.replace('.', '')
        __ ext not __ IGNORE and os.path.basename(seq) not __ IGNORE:
            __ ext not __ IMAGE_EXT:
                item = seq
                item = item.replace(os.path.sep, '/')
                sequences_in_dir.ap..(item)
            ____
                item = image_sequence_resolve_all(seq)
                item = os.path.normpath(item)
                item = item.replace(os.path.sep, '/')
                sequences_in_dir.ap..(item)

    return sequences_in_dir


___ insert_shot_notes():
    shot_root = get_dir_docs_current_nukescript()
    __ shot_root == '' or shot_root is None:
        return
    ____
        shot_root = shot_root.replace(DIR_DOCS, '')
        meta_xml = get_meta_xml(shot_root)
        __ not os.path.isfile(meta_xml):
            return
        meta_tree = ET.parse(meta_xml)
        meta_root = meta_tree.getroot()
        shot_notes = ''
        ___ child __ meta_root.find('notes').findall('note'):
            __ child.get('name') == 'shotnotes':
                shot_notes = child.text

        __ shot_notes != '':
            sticky = ?.createNode('StickyNote')
            sticky['label'].sV..(shot_notes)
            sticky['note_font_size'].sV..(20)
        return


___ show_edit_template_script(window, path):
    global ets
    script_values = get_script_values(path, window)
    set_default_format = False
    __ 'format' __ script_values:
        __ script_values['format'] == '0':
            set_default_format = True
    ____
        set_default_format = True
    __ set_default_format:
        settings = load_settings()
        w = settings['default_w']
        h = settings['default_h']
        pixel_aspect_ratio = settings['default_pixel_aspect']
        format_default = '{} {} 0 0 {} {} {} HD'.format(w, h, w, h, pixel_aspect_ratio)
        script_values['format'] = format_default
        script_values['fps'] = settings['default_fps']
    try:
        ets.close()
        del ets
    except:
        pass

    ets = osl.EditTemplateScript(path, script_values)
    ets.show()
    ets.raise_()
    return ets


___ get_script_values(path, window):
    script_values = {}
    __ not os.path.isfile(path):
        msg = "The file '{}' does not exist".format(path)
        show_message_box(window, msg)
        return {}
    __ os.path.splitext(path)[1] != '.nk':
        msg = "The file '{}' is no nuke script.".format(path)
        show_message_box(window, msg)
        return {}
    this_dir = os.path.dirname(__file__)
    processor = os.path.join(this_dir, '../', 'trm', 'scripts.py')
    processor = os.path.normpath(processor)
    cmd = '"{nuke_exe}" -i -t "{scriptProcess}" get "{path}" " "'.format(nuke_exe=os.path.normpath(?.env['ExecutablePath']), scriptProcess=processor, path=path)
    process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.wait()
    ___ line __ process.stdout:
        line = str(line.rstrip())
        __ 'script@' __ line:
            script_value = line.replace('script@', '')
            key = script_value.split(':')[0]
            val = str(script_value.split(':')[1])
            script_values[key] = val

    return script_values


___ set_script_values(path, script_values, *args):
    debug = False
    script_vals = 'script_in:{}@script_out:{}@fps:{}@format:{}'
    script_vals = script_vals.format(script_values['script_in'], script_values['script_out'], script_values['fps'], script_values['format'].replace(' ', '_'))
    this_dir = os.path.dirname(__file__)
    processor = os.path.join(this_dir, '../', 'trm', 'scripts.py')
    processor = os.path.normpath(processor)
    cmd = '"{nuke_exe}" -i -t "{scriptProcess}" set "{path}" {vals}'.format(nuke_exe=os.path.normpath(?.env['ExecutablePath']), scriptProcess=processor, path=path, vals=script_vals)
    process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.wait()
    found_end = 0
    ___ line __ process.stdout:
        line = str(line.rstrip())
        __ debug:
            print line
        __ '@script:set_end' __ line:
            found_end += 1

    __ found_end == 1:
        return True
    ____
        return False


___ get_user(metaxml, *args):
    __ not os.path.isfile(metaxml):
        return ''
    metatree = ET.parse(metaxml)
    metaroot = metatree.getroot()
    with open(metaxml, 'r') as xml:
        ___ child __ metaroot.find('notes').findall('note'):
            __ child.get('name') == 'user':
                return child.text


___ set_user(user, dir_docs = ''):
    __ dir_docs == '':
        dir_docs = get_dir_docs_current_nukescript()
    __ dir_docs:
        meta_xml = os.path.join(dir_docs, 'meta.xml')
        __ not os.path.isfile(meta_xml):
            return
        metatree = ET.parse(meta_xml)
        metaroot = metatree.getroot()
        with open(meta_xml, 'w') as xml:
            ___ child __ metaroot.find('notes').findall('note'):
                __ child.get('name') == 'user':
                    child.text = user

            prettyprint(metaroot)
            metatree.write(xml, encoding='utf-8', xml_declaration=True)


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


class CustomPath(QtWidgets.QWidget):

    ___ __init__(self, shot_root, sml, which):
        super(CustomPath, self).__init__()
        self.shot_root = shot_root
        self.sml = sml
        self.which = which
        self.setWindowTitle('Set custom {} path'.format(which))
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumWidth(600)
        self.build_ui()

    ___ build_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.create_signals()

    ___ create_widgets(self):
        info = 'Here you can set a custom {} path that can be outside of the shot'.format(self.which)
        self.label_info = QtWidgets.QLabel(info)
        self.label_path = QtWidgets.QLabel('path: ')
        self.input_path = QtWidgets.QLineEdit(self.load_custom_path(self.which))
        self.push_browse = QtWidgets.QPushButton()
        self.push_browse.setIcon(QtGui.QIcon(load_icons()['icon_folder']))
        self.push_browse.setObjectName('simple')
        self.push_save = QtWidgets.QPushButton('save')
        self.push_save.setObjectName('actionButtonBig')
        self.push_close = QtWidgets.QPushButton('close')

    ___ create_layouts(self):
        self.layout_top = QtWidgets.QHBoxLayout()
        self.layout_top.addWidget(self.label_path)
        self.layout_top.addWidget(self.input_path)
        self.layout_top.addWidget(self.push_browse)
        self.layout_push = QtWidgets.QHBoxLayout()
        self.layout_push.addWidget(self.push_save)
        self.layout_push.addWidget(self.push_close)
        self.layout_main = QtWidgets.QVBoxLayout()
        self.layout_main.addWidget(self.label_info)
        self.layout_main.addLayout(self.layout_top)
        self.layout_main.addLayout(self.layout_push)
        self.setLayout(self.layout_main)
        set_style_sheet(self)

    ___ create_signals(self):
        self.push_close.clicked.connect(self.close)
        self.push_save.clicked.connect(self.set_custom_path)
        self.push_browse.clicked.connect(self.browse)

    ___ browse(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)
        __ dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.input_path.setText(dialog.selectedFiles()[0])

    ___ set_custom_path(self):
        try:
            __ not os.path.isdir(self.input_path.text()):
                os.makedirs(self.input_path.text())
        except:
            __ self.input_path.text() != '':
                msg = "Failed setting up the path '{}' as custom {} directory. Please choose a different path.".format(self.input_path.text(), self.which)
                show_message_box(self, msg)
                return

        meta_xml = get_meta_xml(self.shot_root)
        metatree = ET.parse(meta_xml)
        metaroot = metatree.getroot()
        with open(meta_xml, 'w') as xml:
            ___ child __ metaroot.find('notes').findall('note'):
                __ self.which == 'render':
                    __ child.get('name') == 'renderpath':
                        child.text = self.input_path.text()
                        child.set('loc', 'global')
                        __ self.input_path.text() == '':
                            child.set('loc', 'local')
                elif self.which == 'footage':
                    __ child.get('name') == 'footagepath':
                        child.text = self.input_path.text()
                        child.set('loc', 'global')
                        __ self.input_path.text() == '':
                            child.set('loc', 'local')

            prettyprint(metaroot)
            metatree.write(xml, encoding='utf-8', xml_declaration=True)
        __ self.input_path.text() == '':
            msg = 'Successfully cleared the custom {} path'.format(self.which)
            show_message_box(self, msg)
        ____
            msg = "Successfully set up the custom {} path to: '{}'".format(self.which, self.input_path.text())
            show_message_box(self, msg)
        self.close()
        __ self.sml is not None:
            try:
                __ self.which == 'render':
                    self.sml.current_shot_widget.set_renderpath(self.input_path.text())
                elif self.which == 'footage':
                    self.sml.current_shot_widget.set_footagepath(self.input_path.text())
                self.sml.current_shot_widget.refresh()
            except Exception as e:
                pass

        return

    ___ load_custom_path(self, which):
        meta_xml = get_meta_xml(self.shot_root)
        metatree = ET.parse(meta_xml)
        metaroot = metatree.getroot()
        ___ child __ metaroot.find('notes').findall('note'):
            __ child.get('name') == '{}path'.format(which):
                __ child.get('loc') and child.get('loc') == 'global':
                    return child.text
                ____
                    return ''

    ___ keyPressEvent(self, event):
        __ event.key() == QtCore.Qt.Key_Escape:
            self.close()