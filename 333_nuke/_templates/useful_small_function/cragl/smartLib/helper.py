# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartLib_v4.0/smartLib/src/helper.py
______ __
______ ___
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
______ ?
__ ?.NUKE_VERSION_MAJOR < 11:
    ____ PySide ______ QtGui as ?W..
    ____ PySide ______ QtGui
    ____ PySide ______ QtCore
____
    ____ ? ______ ?W..
    ____ ? ______ QtGui
    ____ ? ______ QtCore
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
    this_dir = __.path.dirname(__file__)
    dir_icon = __.path.join(this_dir, '../', 'icons')
    dir_icon = __.path.normpath(dir_icon)
    join = __.path.join
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
        r_ True
    ______
        r_ False


___ show_message_box(window, m..):
    ?W...QMessageBox().information(window, 'information', m..)


___ message_confirm_overwrite(src, is_file = True):
    __ is_file:
        item = 'File'
    ____
        item = 'Directory'
    m.. = "{} '{}' already exists.\nDo you want to overwrite it?".format(item, src)
    overwrite = ask_dialog(m..=m.., process_button_text='Overwrite', color_process='45,0,0', cancel_button_text='Cancel')
    r_ overwrite


___ get_smartlib_private_dir():
    dir_ = __.path.join(__.path.expanduser('~'), '.cragl', 'smartLib')
    __ no. __.path.isdir(dir_):
        __.makedirs(dir_)
    r_ dir_


___ get_smartlib_public_dir():
    dir_ = __.path.join(__.path.expanduser('~'), 'cragl', 'smartLib')
    __ no. __.path.isdir(dir_):
        __.makedirs(dir_)
    r_ dir_


___ get_dir_templates():
    dir_ = __.path.join(get_smartlib_public_dir(), 'shot_templates')
    __ no. __.path.isdir(dir_):
        __.makedirs(dir_)
    r_ dir_


___ set_item_icon(listwidget_item, name, is_dir, is_render_dir = False, is_footage_dir = False, icons = N..):
    __ is_dir:
        ___
            listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_folder']))
            __ is_render_dir:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_write']))
            ____ is_footage_dir:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_read']))
        ______
            listwidget_item.setIcon(QtGui.QIcon(icons['icon_folder']))
            __ is_render_dir:
                listwidget_item.setIcon(QtGui.QIcon(icons['icon_write']))
            ____ is_footage_dir:
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_read']))

    __ '.' __ name:
        ext = name.split('.')[1]
        __ ext __ 'nk':
            ___
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_nuke']))
            ______
                listwidget_item.setIcon(QtGui.QIcon(icons['icon_nuke']))

        ____ ext.lower() __ IMAGE_EXT:
            ___
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_img']))
            ______
                listwidget_item.setIcon(QtGui.QIcon(icons['icon_img']))

        ____ ext __ VIDEO_EXT:
            ___
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_video']))
            ______
                listwidget_item.setIcon(QtGui.QIcon(icons['icon_video']))

        ____
            ___
                listwidget_item.setIcon(0, QtGui.QIcon(icons['icon_doc']))
            ______
                listwidget_item.setIcon(QtGui.QIcon(icons['icon_doc']))


___ get_log_file():
    connect_dir = __.path.join(__.path.expanduser('~'), '.cragl', 'connect')
    __ no. __.path.isdir(connect_dir):
        __.makedirs(connect_dir)
    log_file = __.path.join(connect_dir, 'connectlog.txt')
    __ no. __.path.isfile(log_file):
        with open(log_file, 'w') as lf:
            log_template = 'connect log\n{}\n'.format('-' * 50)
            lf.write(log_template)
    r_ log_file


___ get_smartLib_installed_root():
    this_dir = __.path.dirname(__file__)
    root = __.path.join(this_dir, '../', '../')
    r_ __.path.normpath(root)


___ write_log(text, tool = 'sl'):
    with open(get_log_file(), 'a') as file_:
        log_time_format = '%d.%m.%Y %H:%M:%S'
        log_time = time.strftime(log_time_format, time.localtime())
        file_.write('{}: {} {}\n'.format(log_time, tool, text))


___ _copy(src, dst):
    dst = __.path.join(dst, __.path.basename(src))
    __ __.path.isdir(src):
        ___
            shutil.copytree(src, dst)
        except Exception as error:
            raise OSError(error)

    ____ __.path.isfile(src):
        __ no. __.path.isdir(__.path.dirname(dst)):
            __.makedirs(__.path.dirname(dst))
        ___
            shutil.copy(src, dst)
        except Exception as error:
            raise OSError(error)


___ remove(path):
    __ __.path.isfile(path):
        ___
            __.remove(path)
            r_ True
        ______
            r_ False

    ____ __.path.isdir(path):
        ___
            shutil.rmtree(path)
            r_ True
        ______
            r_ False


___ set_style_sheet(widget):
    this_dir = __.path.dirname(__file__)
    styles = __.path.join(this_dir, '../', 'styles', 'nuke.qss')
    styles = __.path.normpath(styles)
    __ __.path.isfile(styles):
        with open(styles) as file_:
            widget.setStyleSheet(file_.read())


___ reveal_in_finder(path, open_file = False):
    path = __.path.normpath(path)
    ___
        __ ___.pl.. __ 'linux2':
            __ open_file:
                ?.scriptOpen(path)
                r_
            __ __.path.isfile(path):
                path = __.path.dirname(path)
            subprocess.P..(['xdg-open', path])
        ____ ___.pl.. __ 'darwin':
            __ open_file:
                subprocess.call(['open', '--', path])
            ____
                subprocess.call(['open', '-R', path])
        ____ ___.pl.. __ 'windows' or ___.pl.. __ 'win32':
            __ ':' __ path:
                __ ':{}'.format(__.path.sep) no. __ path:
                    path = path.replace(':', ':{}'.format(__.path.sep))
            __ __.path.isfile(path):
                path = __.path.dirname(path)
            subprocess.call(['explorer', path])
    ______
        m..('Failed opening: {}'.format(path))


___ get_home_dir():
    r_ __.path.expanduser('~')


___ load_bookmarks():
    bookmarklist = []
    bookmarklist.ap..('bookmarks')
    bookmarklist.ap..('add to bookmarks')
    bookmarklist.ap..('delete from bookmarks')
    bookmarklist.ap..('--------------------')
    settingsXML = get_settings_xml()
    settings_tree = ET.parse(settingsXML)
    settings_root = settings_tree.getroot()
    ___ child __ settings_root.find('bookmarks').f_a_('bookmark'):
        bookmarklist.ap..(child.text)

    r_ bookmarklist


___ get_settings_xml():
    settings_xml = __.path.join(get_smartlib_private_dir(), 'settings.xml')
    __ no. __.path.isfile(settings_xml):
        ___
            with open(settings_xml, 'w') as xml:
                template = templates.SETTINGS.format(user_home_dir=__.path.expanduser('~'))
                xml.write(template.strip())
        except Exception as error:
            write_log("Couldn't write settings xml template. {}".format(error))

    check_xml_values_exist()
    check_status_exists()
    check_xml_ok(settings_xml)
    r_ settings_xml


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
    xml = __.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = False
    item_found = 0
    ___ child __ root.find(parent).f_a_(section):
        __ child.get(key1) __ value1:
            item_found += 1
            __ debug:
                print 'smartLib | settings exists: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2)
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


___ check_xml_parent_val_exists(section):
    xml = __.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    __ root.find(section) is N..:
        elem = ET.Element(section)
        root.ap..(elem)
        with open(xml, 'w') as xml:
            prettyprint(root)
            tree.write(xml, encoding='utf-8', xml_declaration=True)
        write_log('settings xml added: {}'.format(section))
    r_


___ check_status_exists():
    status_found = 0
    xml = __.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    __ le.(root.find('statuslist')):
        ___ child __ root.find('statuslist').f_a_('status'):
            status_found += 1

    __ status_found __ 0:
        default_status = templates.DEFAULT_STATUS
        __ root.find('statuslist') is N..:
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
    r_


___ write_template_default(projectpath, template):
    xml = __.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    elem_exists = False
    ___ project __ root.find('templateDefaults').f_a_('project'):
        __ project.get('path') __ projectpath:
            elem_exists = True
            project.text = template
            break

    __ no. elem_exists:
        projectelement = ET.Element('project')
        projectelement.set('path', projectpath)
        projectelement.text = template
        root.find('templateDefaults').ap..(projectelement)
    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


___ load_template_default(project_path):
    xml = __.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    ___ project __ root.find('templateDefaults').f_a_('project'):
        __ project.get('path') __ project_path:
            r_ project.text

    r_ ''


___ load_status_list():
    xml = __.path.join(get_smartlib_private_dir(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    status_list = {}
    __ le.(root.find('statuslist')):
        ___ child __ root.find('statuslist').f_a_('status'):
            data = [child.get('color'), child.text, child.get('default')]
            status_list[child.get('z-index')] = data

    r_ status_list


___ load_default_status():
    settings_xml = get_settings_xml()
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    with open(settings_xml, 'r'):
        ___ child __ settings_root.find('statuslist').f_a_('status'):
            __ child.get('default') __ '1':
                r_ [child.text, child.get('color')]


___ ask_dialog(m.. = '', process_button_text = '', color_process = '', cancel_button_text = ''):
    msg_box = ?W...QMessageBox(?W...QMessageBox.Warning, 'QMessageBox.warning()', m.., ?W...QMessageBox.NoButton, N..)
    msg_box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg_box.setObjectName('msgBox')
    msg_box.raise_()
    process_button = msg_box.addButton(process_button_text, ?W...QMessageBox.AcceptRole)
    __ color_process != '':
        __ color_process __ 'actionButton':
            color_process = '51, 204, 255, 100'
        style = 'QPushButton {background-color: rgba(%s)}' % color_process
        process_button.setStyleSheet(style)
    process_button.clearFocus()
    msg_box.setFocus()
    msg_box.addButton(cancel_button_text, ?W...QMessageBox.RejectRole)
    __ msg_box.exec_() __ ?W...QMessageBox.AcceptRole:
        r_ True
    ____
        r_ False
        r_


___ check_xml_ok(xml):
    ___
        with open(xml, 'r') as xml_file:
            ET.fromstring(xml_file.read())
        r_ True
    ______
        __ xml __ get_settings_xml():
            m.. = 'The smartLib settings file seems to be broken. Do you want to reset it now?'
            write_log('smartLib settings file broken.')
        ____
            meta_xml = __.path.join(__.path.dirname(xml), '../')
            meta_xml = __.path.normpath(meta_xml)
            m.. = 'The meta xml for {} file seems to be broken. Do you want to reset it now?'.format(meta_xml)
            write_log('The meta xml for {} file broken.'.format(meta_xml))
        reset_xml = ask_dialog(m..=m.., process_button_text='reset', color_process='actionButton', cancel_button_text='Cancel')
        __ reset_xml:
            __ __.path.isfile(xml):
                __.remove(xml)
                get_settings_xml()
        r_ False


___ load_settings():
    settings_xml = get_settings_xml()
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    settings = {}
    ___ setting __ settings_root.find('settings').f_a_('setting'):
        __ setting.text:
            settings[setting.get('name')] = setting.text
        ____
            settings[setting.get('name')] = ''

    ___ navi __ settings_root.find('navigation').f_a_('navi'):
        __ navi.text and __.path.isdir(navi.text):
            settings['current_{}'.format(navi.get('name'))] = navi.text
        ____
            settings['current_{}'.format(navi.get('name'))] = ''

    r_ settings


___ center_window(window):
    qr = window.frameGeometry()
    cp = ?W...QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


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


___ write_xml(xml, root, tree):
    prettyprint(root)
    tree.write(xml, encoding='utf-8', xml_declaration=True)
    r_ True


___ collect_nuke_scripts_no_ignore(path):
    nuke_scripts = collections.OrderedDict()
    ignore_list = load_settings()['nukescripts_ignore']
    __ ignore_list:
        ignore_list = ignore_list.split(',')
    ____
        ignore_list = []
    ignore_list.extend(['.nk~', '.autosave'])
    ___ root, dirs, files __ __.walk(path):
        ___ name __ files:
            file = __.path.join(root, name)
            __ __.path.splitext(file)[1] __ '.nk':
                ignore_count = 0
                ___ ignore __ ignore_list:
                    __ ignore.strip() __ file:
                        ignore_count += 1

                __ ignore_count __ 0:
                    nuke_script = __.path.basename(file)
                    nuke_script_name = __.path.splitext(nuke_script)[0]
                    nuke_scripts[file] = nuke_script_name

    nuke_scripts = sorted(nuke_scripts.items(), key=lambda x: x[1])
    nuke_scripts.reverse()
    r_ nuke_scripts


___ open_nukescript(name, nuke_scripts):
    ___ script __ nuke_scripts:
        __ script[1] __ name:
            ?.scriptOpen(script[0])


___ write_location(location, value):
    settings_xml = get_settings_xml()
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    with open(settings_xml, 'r'):
        ___ child __ settings_root.find('navigation').f_a_('navi'):
            __ child.get('name') __ location:
                child.text = value

    with open(settings_xml, 'w') as xml:
        prettyprint(settings_root)
        settings_tree.write(xml, encoding='utf-8', xml_declaration=True)


___ open_website(url):
    __ ___.pl.. __ 'win32':
        __.startfile(url)
    ____ ___.pl.. __ 'darwin':
        subprocess.P..(['open', url])
    ____
        ___
            subprocess.P..(['xdg-open', url])
        except OSError:
            msg = 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.format(url)
            show_message_box(N.., msg)

    r_


___ set_preview_image(delete_nodes = True):
    __ no. osl.cl():
        r_
    preview_image_width = 500
    ___
        sel = ?.sN__
    ______
        ?.m..('Please select a node to create a preview image.')
        r_

    __ sel.Class() __ 'Viewer':
        r_
    __ get_script_name() __ '' or get_script_name() __ 'Root':
        ?.m..("Your nukescript hasn't been saved, yet. Please save your script first.")
        r_
    root_dir_docs = get_dir_docs_current_nukescript()
    __ root_dir_docs __ '':
        r_
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
    preview_path = __.path.join(root_dir_docs, '__preview.jpg')
    preview_path = preview_path.replace(__.path.sep, '/')
    write.knob('file').sV..(preview_path)
    ?.execute(write, ?.frame(), ?.frame())
    __ delete_nodes:
        ?.delete(reformat)
        ?.delete(gamma)
        ?.delete(write)


___ get_dir_docs_current_nukescript():
    up_level = 7
    current_script_dir = __.path.dirname(?.root().name())
    __ current_script_dir __ 'Root' or current_script_dir __ '':
        r_ ''
    root_dir_docs = ''
    dirs = []
    dirs.ap..(__.path.normpath(current_script_dir))
    ___ i __ ra..(up_level - 1):
        dir = __.path.normpath(__.path.abspath(__.path.join(__.path.dirname(dirs[i - 1]))))
        dirs.ap..(dir)

    ___ i __ ra..(up_level - 1):
        dir_content = __.listdir(dirs[i])
        __ DIR_DOCS __ dir_content:
            root_dir_docs = __.path.normpath(__.path.join(dirs[i], DIR_DOCS))
            r_ root_dir_docs

    __ root_dir_docs __ '':
        write_log("Wasn't able to find the _docs directory for the shot. Recursion depth for the shot is too high.")
        r_


___ get_meta_xml(path):
    __ __.path.isdir(path):
        metaxml = __.path.join(path, DIR_DOCS, 'meta.xml')
        ___
            __ no. __.path.isdir(__.path.dirname(metaxml)):
                __.makedirs(__.path.dirname(metaxml))
        ______
            r_

        __ no. __.path.isfile(metaxml):
            ___
                with open(metaxml, 'w') as file_:
                    template = templates.META
                    file_.write(template.strip())
            ______
                write_log("Couldn't write meta xml template at: {}".format(metaxml))

        check_meta_xml_values_exist(metaxml)
        r_ metaxml


___ check_meta_xml_values_exist(metaxml):
    check_meta_xml_value_exists(metaxml, 'notes', 'note', 'name', 'footagepath', ' ', key2='loc', value2='local')
    check_meta_xml_value_exists(metaxml, 'notes', 'note', 'name', 'user', ' ')


___ check_meta_xml_value_exists(metaxml_path, parent, section, key1, value1, text, key2 = '', value2 = ''):
    tree = ET.parse(metaxml_path)
    root = tree.getroot()
    debug = False
    item_found = 0
    ___ child __ root.find(parent).f_a_(section):
        __ child.get(key1) __ value1:
            item_found += 1
            __ debug:
                print 'smartLib | metaxml exists: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2)
            r_

    __ item_found __ 0:
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


___ m..(m..):
    msg_box = ?W...QMessageBox()
    msg_box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg_box.setText(m..)
    msg_box.raise_()
    msg_box.exec_()


___ dialog_set_preview_image(smartlib):
    dialog = ?W...QFileDialog()
    dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    dialog.setWindowIcon(QtGui.QIcon(load_icons()['icon_logo']))
    dialog.sQT..('choose image file')
    dialog.setNameFilter('jpg files(*.jpg)')
    __ dialog.exec_() __ ?W...QDialog.Accepted:
        input_image = dialog.selectedFiles()[0]
        dest = __.path.join(smartlib.current_shot_widget.path, DIR_DOCS, '__preview.jpg')
        __ no. __.path.isdir(__.path.dirname(dest)):
            __.makedirs(__.path.dirname(dest))
        save_image_scaled(input_image, dest)
        smartlib.current_shot_widget.refresh()
        current_project = load_settings()['current_project']
        smartlib.table_current_project.load_shots(current_project)


___ save_image_scaled(src, dest):
    img = QtGui.QImage(src)
    ___
        pixmap = QtGui.QPixmap(img.scaledToWidth(500))
        pixmap.save(dest)
        r_ True
    ______
        write_log('Cannot create image scaled.')
        r_ False


___ get_script_name():
    script = ?.root().name()
    script_name = __.path.basename(script)
    r_ __.path.splitext(script_name)[0]


___ setup_renderpath():
    dir_docs_current_nukescript = get_dir_docs_current_nukescript()
    __ dir_docs_current_nukescript __ (N.., ''):
        r_ N..
    ____
        project_root = __.path.dirname(dir_docs_current_nukescript)
        metaxml = __.path.join(dir_docs_current_nukescript, 'meta.xml')
        script_name = get_script_name()
        __ __.path.isfile(metaxml) and script_name no. __ ('', 'Root'):
            meta_tree = ET.parse(metaxml)
            meta_root = meta_tree.getroot()
            ___ child __ meta_root.find('notes').f_a_('note'):
                __ child.get('name') __ 'renderpath':
                    ___
                        __ child.text.strip() != '':
                            __ child.get('loc') __ 'global':
                                render_dir = '{}'.format(child.text)
                            ____
                                render_dir = '{}{}'.format(project_root, child.text)
                            render_file = '{}{}%0{}d.{}'.format(script_name, load_settings()['padding_delimiter'], load_settings()['padding'], load_settings()['ext'])
                            render_full_path = __.path.join(render_dir, script_name, render_file)
                            render_dir = __.path.dirname(render_full_path)
                            __ no. __.path.isdir(render_dir):
                                __.makedirs(render_dir)
                            ?.thisNode()['file'].sV..(render_full_path)
                            ?.thisNode()['file_type'].sV..(load_settings()['ext'])
                    ______
                        pass

        r_ N..


___ load_templates():
    dir_templates = get_dir_templates()
    templates = []
    ___ item __ __.listdir(dir_templates):
        element = __.path.join(dir_templates, item)
        __ __.path.isdir(element) and item != DIR_DOCS:
            templates.ap..(item)

    r_ templates


___ get_render_path(xml):
    __ __.path.isfile(xml):
        ___
            meta_tree = ET.parse(xml)
            meta_root = meta_tree.getroot()
        ______
            write_log('Unable to parse metaxml.')
            r_

        ___ child __ meta_root.find('notes').f_a_('note'):
            __ child.get('name') __ 'renderpath':
                r_ child.text

    ____
        write_log("Metaxml doesn't exist in: {}".format(xml))


___ rename_item(sender, path_orig, window):
    inp = ?W...QInputDialog()
    inp.setObjectName('inp')
    __ __.path.isfile(path_orig):
        item = 'file'
    ____
        item = 'directory'
    title = 'Enter new name'
    msg = 'Enter the new name for the {}:'.format(item)
    file_name = __.path.basename(path_orig)
    name, ok = inp.getText(window, title, msg, text=file_name)
    __ ok:
        name = name.replace('/', '')
        new_name_full_path = __.path.join(__.path.dirname(path_orig), name)
        __ __.path.isfile(path_orig):
            __ '.' no. __ name:
                ext = __.path.splitext(__.path.basename(path_orig))[1]
                new_name_full_path = '{}{}'.format(new_name_full_path, ext)
        __ sender __ 'smartlibshotwindow':
            __.rename(path_orig, new_name_full_path)
            window.populate_tree()
        __ sender __ 'shot_templates':
            __.rename(path_orig, new_name_full_path)
            window.load_shot_template_in_tree()
        __ sender __ 'saved_projects':
            settingsXML = get_settings_xml()
            settingstree = ET.parse(settingsXML)
            settingsroot = settingstree.getroot()
            ___ child __ settingsroot.find('projectslist').f_a_('project'):
                __ child.text __ path_orig:
                    child.set('name', name)

            write_xml(settingsXML, settingsroot, settingstree)
            window.populate_saved_projects()


___ force_create_render_dir():
    filename = ?.filename(?.thisNode())
    dirname = __.path.dirname(filename)
    osdir = ?.callbacks.filenameFilter(dirname)
    ___
        __.makedirs(osdir)
    except OSError as e:
        __ e.errno != errno.EEXIST:
            raise


___ get_finder_name():
    __ ___.pl.. __ 'darwin':
        r_ 'finder'
    ____
        r_ 'explorer'


___ import_from_footage_directory():
    dir_docs = get_dir_docs_current_nukescript()
    ___
        __ dir_docs __ '':
            raise ValueError
        meta_xml = __.path.join(dir_docs, 'meta.xml')
        __ no. __.path.isfile(meta_xml):
            raise ValueError
        metatree = ET.parse(meta_xml)
        ___ note __ metatree.find('notes').f_a_('note'):
            __ note.get('name') __ 'footagepath':
                shot_root = __.path.normpath(__.path.join(dir_docs, '../'))
                shot_root = shot_root.replace(__.path.sep, '/')
                __ note.text is no. N..:
                    __ note.get('loc') __ 'global':
                        start_path = note.text
                    __ note.get('loc') __ 'local':
                        __ note.text[0] __ __.path.sep or note.text[0] __ '/':
                            note.text = note.text[1:]
                        __ note.text and note.text != '' and note.text != ' ':
                            start_path = __.path.join(shot_root, note.text)
                        ____
                            start_path = shot_root
                ____ note.text is N.. or note.text __ '' or note.text __ ' ':
                    start_path = shot_root
                __ start_path[-1:] != '/':
                    start_path += '/'
                start_path = start_path.replace(__.path.sep, '/')
                load_footage(path=start_path)

    ______
        pass

    r_


___ load_footage(defaulttype = 'Read', path = ''):
    sel_node = N..
    default_dir = N..
    ___
        sel_node = ?.sN__
    ______
        pass

    __ sel_node:
        __ 'file' __ sel_node.knobs():
            default_dir = sel_node['file'].value()
        __ no. default_dir and 'proxy' __ sel_node.knobs():
            default_dir = sel_node['proxy'].value()
    __ default_dir __ '':
        default_dir = N..
    files = ?.getClipname('______ from footage directory', default=path, multiple=True)
    __ files != N..:
        max_files = ?.numvalue('preferences.maxPanels')
        n = le.(files)
        ___ f __ files:
            is_abc = False
            stripped = ?.stripFrameRange(f)
            nodeType = defaulttype
            __ ?.create.isAudioFilename(stripped):
                nodeType = 'AudioRead'
            __ ?.create.isGeoFilename(stripped):
                nodeType = 'ReadGeo2'
            __ ?.create.isAbcFilename(stripped):
                is_abc = True
            __ ?.create.isDeepFilename(stripped):
                nodeType = 'DeepRead'
            use_in_panel = True
            __ max_files != 0 and n > max_files:
                use_in_panel = False
            n = n - 1
            __ is_abc:
                ?.createScenefileBrowser(f, '')
            ____
                ___
                    ?.createNode(nodeType, 'file {' + f + '}', inpanel=use_in_panel)
                except RuntimeError as err:
                    ?.m..(err.args[0])

    r_


___ show_custom_directory_window(shot_root, which, sml = N..):
    g__ crp
    ___
        crp.c__
        del crp
    ______
        pass

    crp = CustomPath(shot_root, sml, which)
    crp.raise_()
    crp.s__


___ create_new_directory(widget, list_):
    inp = ?W...QInputDialog()
    inp.setObjectName('inp')
    title = 'Enter name'
    msg = 'Enter the name of the new folder:'
    dir_name, ok = inp.getText(widget, title, msg)
    __ ok:
        dest = list_.data(0, QtCore.Qt.UserRole)
        __ __.path.isfile(dest):
            dest = __.path.dirname(dest)
        dest = dest.replace('\\', '/')

        ___ create_directory(dir_name):
            dir_path_full = __.path.join(dest, dir_name)
            __ no. __.path.isdir(dir_path_full):
                __.makedirs(dir_path_full)
                diritem = widget.build_tree_widget_item(widget.dirlist[dest], dir_name, dir_path_full, is_dir=True)
                widget.dirlist[dir_path_full] = diritem
                widget.allitems[dir_path_full] = diritem
            ____
                m..("The directory '{}' already exists. The folder wasn't created".format(dir_name))

        dir_item_list = dir_name.split(',')
        ___ dir_item __ dir_item_list:
            dir_item = dir_item.strip()
            create_directory(dir_item)


___ error_loading(path, sml):
    m.. = 'Cannot find the bookmark:\n{}\n\n No such directory.Do you like to delete it from the bookmarks?'.format(path)
    remove_bookmark = ask_dialog(m..=m.., process_button_text='Delete from bookmarks', color_process='45,0,0', cancel_button_text='Cancel')
    __ remove_bookmark:
        settingsXML = get_settings_xml()
        settingstree = ET.parse(settingsXML)
        settingsroot = settingstree.getroot()
        ___ child __ settingsroot.find('bookmarks').f_a_('bookmark'):
            __ child.text __ path:
                settingsroot.find('bookmarks').remove(child)

        write_xml(settingsXML, settingsroot, settingstree)
        sml.combo_bookmarks.removeItem(sml.combo_bookmarks.findText(path))


___ get_project_information(project_full_path):
    shot_information = {}
    ___ shot __ __.listdir(project_full_path):
        shot_full_path = __.path.join(project_full_path, shot)
        __ __.path.isdir(shot_full_path) and shot != '.docs':
            metaxml = __.path.join(shot_full_path, '.docs', 'meta.xml')
            __ __.path.isfile(metaxml):
                with open(metaxml, 'r') as metaxml:
                    shot_info = []
                    tree = ET.parse(metaxml)
                    root = tree.getroot()
                    ___ child __ root.find('notes').f_a_('note'):
                        __ child.get('name') __ 'status':
                            status = child.text
                            __ status is N.. or status __ '':
                                status = ''
                            shot_info.ap..(status)
                        __ child.get('name') __ 'shotnotes':
                            shot_info.ap..(child.text)

            thumbnail = __.path.join(shot_full_path, '.docs', '__preview.jpg')
            __ __.path.isfile(thumbnail):
                shot_info.ap..('file:///{}'.format(thumbnail))
            ____
                default_image = load_icons()['icon_preview_default']
                default_image = __.path.normpath(default_image)
                shot_info.ap..('file:////{}'.format(default_image))
            shot_information[shot] = shot_info

    r_ shot_information


___ build_html(html_path, project):
    shot_information = get_project_information(project)
    project_title = __.path.split(project)[-1]
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
                __ key __ status[1]:
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
                __ key __ status[1]:
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
                __ shot_status __ status[1]:
                    color = status[0]

            __ color __ '':
                color = load_default_status()[1]
                shot_status = load_default_status()[0]
            tmp_html.write('\n            <div class=\'shot\' style="display: block; height:auto; margin: 20px; border-bottom: 1px solid #cccccc; padding: 20px;">\n                <div class=\'shot_thumbnail\' style=\'display: inline-block; padding-right: 30px;\'>\n                    <img src=\'{thumb}\' alt=\'\' title=\'\' width=\'200\' />\n                </div>\n                <div class=\'shot_details\' style=\'display: inline-block; vertical-align: top;\'>\n                    <span style=\'display: inline-block; font-size: 14pt; font-weight:bold;\'>{shotname}</span> <span style=\'background-color: rgb({color}); padding: 2px 10px; position: relative; top: -2px;\'>{status}</span> <br />\n                    <span style=\'font-size: 8pt;\'>{notes}</span>\n                </div>\n            </div>\n            <div style=\'clear:both;\'></div>\n'.format(thumb=shot_thumbnail, shotname=key, color=color, status=shot_status, notes=shot_notes))

    with open(html_path, 'a') as tmp_html:
        tmp_html.write('\n        </div>\n    </div>\n</body>\n</html>\n')
        r_ html_path


___ build_pdf(build_path, project, output_filename = '', parent = N..):
    ___
        ____ PySide ______ QtWebKit
    except Exception:
        msg = "Error creating project report. The needed module 'QtWebKit' is not more supported in this Nuke version. Please use Nuke10 to create a project report."
        show_message_box(parent, msg)
        r_

    debug = False
    ___
        tmp_html = build_html(__.path.join(get_smartlib_public_dir(), 'tmp.html'), project)
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

        QtCore.QObject.c..(web, QtCore.SIGNAL('loadFinished(bool)'), convertIt)
        __ __.path.isfile(tmp_html):
            ___
                __.remove(tmp_html)
            except Exception:
                pass

        r_ 'created_pdf'
    except Exception as e:
        r_ e


___ get_sequences_sets(dirpath):
    sequences = []
    sequences_set = []
    dir_content = __.listdir(dirpath)
    ___ file __ dir_content:
        __ file __ IGNORE:
            continue
        __ __.path.isdir(__.path.join(dirpath, file)):
            continue
        filename_noext, ext = __.path.splitext(file)
        ext = ext.replace('.', '')
        ____ string ______ digits
        __ i..(file, bytes):
            digits = digits.encode()
        filename_nodigits = filename_noext.rstrip(digits)
        __ ext no. __ IMAGE_EXT:
            sequence = __.path.normpath(__.path.join(dirpath, file))
            sequence = sequence.replace(__.path.sep, '/')
            sequences.ap..(sequence)
        ____
            __ le.(filename_nodigits) __ le.(filename_noext) and file no. __ IGNORE and file no. __ sequences:
                sequence = __.path.normpath(__.path.join(dirpath, file))
                sequence = sequence.replace(__.path.sep, '/')
                sequences.ap..(sequence)
                continue
            __ filename_nodigits no. __ sequences_set and file no. __ IGNORE and file no. __ sequences:
                sequences_set.ap..(filename_nodigits)
                sequence = __.path.normpath(__.path.join(dirpath, file))
                sequence = sequence.replace(__.path.sep, '/')
                sequences.ap..(sequence)

    r_ sequences


___ image_sequence_resolve_all(filepath):
    filepath = str(filepath.replace(__.path.sep, '/'))
    basedir, filename = __.path.split(filepath)
    filename_noext, ext = __.path.splitext(filename)
    ____ string ______ digits
    __ i..(filepath, bytes):
        digits = digits.encode()
    filename_nodigits = filename_noext.rstrip(digits)
    __ le.(filename_nodigits) __ le.(filename_noext):
        r_ __.path.join(basedir, filename)
    files = __.listdir(basedir)
    image_sequence_list = [ __.path.join(f) ___ f __ files __ f.startswith(filename_nodigits) and f.endswith(ext) and f[le.(filename_nodigits):-le.(ext) __ ext ____ -1].isdigit() ]
    seq_start = image_sequence_list[0]
    seq_start = seq_start.replace(filename_nodigits, '')
    seq_start = seq_start.replace(ext, '')
    seq_end = image_sequence_list[-1:][0]
    seq_end = seq_end.replace(filename_nodigits, '')
    seq_end = seq_end.replace(ext, '')
    seq_preview = '{}[{}-{}]{}'.format(filename_nodigits, seq_start, seq_end, ext)
    seq_full_path = __.path.join(basedir, seq_preview)
    seq_full_path = seq_full_path.replace(__.path.sep, '/')
    r_ seq_full_path


___ collapse_sequences(dirpath):
    sequences_in_dir = []
    sequence_sets = []
    dirpath = dirpath.replace(__.path.sep, '/')
    ___ root, dirs, seq __ __.walk(dirpath):
        sequence_sub_sets = get_sequences_sets(root)
        __ __.path.basename(root) __ DIR_DOCS:
            continue
        ___ sequence_item __ sequence_sub_sets:
            sequence_item = __.path.normpath(sequence_item)
            sequence_item = sequence_item.replace(__.path.sep, '/')
            sequence_sets.ap..(sequence_item)

    ___ seq __ sequence_sets:
        ext = __.path.splitext(seq)[1]
        ext = ext.replace('.', '')
        __ ext no. __ IGNORE and __.path.basename(seq) no. __ IGNORE:
            __ ext no. __ IMAGE_EXT:
                item = seq
                item = item.replace(__.path.sep, '/')
                sequences_in_dir.ap..(item)
            ____
                item = image_sequence_resolve_all(seq)
                item = __.path.normpath(item)
                item = item.replace(__.path.sep, '/')
                sequences_in_dir.ap..(item)

    r_ sequences_in_dir


___ insert_shot_notes():
    shot_root = get_dir_docs_current_nukescript()
    __ shot_root __ '' or shot_root is N..:
        r_
    ____
        shot_root = shot_root.replace(DIR_DOCS, '')
        meta_xml = get_meta_xml(shot_root)
        __ no. __.path.isfile(meta_xml):
            r_
        meta_tree = ET.parse(meta_xml)
        meta_root = meta_tree.getroot()
        shot_notes = ''
        ___ child __ meta_root.find('notes').f_a_('note'):
            __ child.get('name') __ 'shotnotes':
                shot_notes = child.text

        __ shot_notes != '':
            sticky = ?.createNode('StickyNote')
            sticky['label'].sV..(shot_notes)
            sticky['note_font_size'].sV..(20)
        r_


___ show_edit_template_script(window, path):
    g__ ets
    script_values = get_script_values(path, window)
    set_default_format = False
    __ 'format' __ script_values:
        __ script_values['format'] __ '0':
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
    ___
        ets.c__
        del ets
    ______
        pass

    ets = osl.EditTemplateScript(path, script_values)
    ets.s__
    ets.raise_()
    r_ ets


___ get_script_values(path, window):
    script_values = {}
    __ no. __.path.isfile(path):
        msg = "The file '{}' does not exist".format(path)
        show_message_box(window, msg)
        r_ {}
    __ __.path.splitext(path)[1] != '.nk':
        msg = "The file '{}' is no nuke script.".format(path)
        show_message_box(window, msg)
        r_ {}
    this_dir = __.path.dirname(__file__)
    processor = __.path.join(this_dir, '../', 'trm', 'scripts.py')
    processor = __.path.normpath(processor)
    cmd = '"{nuke_exe}" -i -t "{scriptProcess}" get "{path}" " "'.format(nuke_exe=__.path.normpath(?.env['ExecutablePath']), scriptProcess=processor, path=path)
    process = subprocess.P..(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.wait()
    ___ line __ process.stdout:
        line = str(line.rstrip())
        __ 'script@' __ line:
            script_value = line.replace('script@', '')
            key = script_value.split(':')[0]
            val = str(script_value.split(':')[1])
            script_values[key] = val

    r_ script_values


___ set_script_values(path, script_values, *args):
    debug = False
    script_vals = 'script_in:{}@script_out:{}@fps:{}@format:{}'
    script_vals = script_vals.format(script_values['script_in'], script_values['script_out'], script_values['fps'], script_values['format'].replace(' ', '_'))
    this_dir = __.path.dirname(__file__)
    processor = __.path.join(this_dir, '../', 'trm', 'scripts.py')
    processor = __.path.normpath(processor)
    cmd = '"{nuke_exe}" -i -t "{scriptProcess}" set "{path}" {vals}'.format(nuke_exe=__.path.normpath(?.env['ExecutablePath']), scriptProcess=processor, path=path, vals=script_vals)
    process = subprocess.P..(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.wait()
    found_end = 0
    ___ line __ process.stdout:
        line = str(line.rstrip())
        __ debug:
            print line
        __ '@script:set_end' __ line:
            found_end += 1

    __ found_end __ 1:
        r_ True
    ____
        r_ False


___ get_user(metaxml, *args):
    __ no. __.path.isfile(metaxml):
        r_ ''
    metatree = ET.parse(metaxml)
    metaroot = metatree.getroot()
    with open(metaxml, 'r') as xml:
        ___ child __ metaroot.find('notes').f_a_('note'):
            __ child.get('name') __ 'user':
                r_ child.text


___ set_user(user, dir_docs = ''):
    __ dir_docs __ '':
        dir_docs = get_dir_docs_current_nukescript()
    __ dir_docs:
        meta_xml = __.path.join(dir_docs, 'meta.xml')
        __ no. __.path.isfile(meta_xml):
            r_
        metatree = ET.parse(meta_xml)
        metaroot = metatree.getroot()
        with open(meta_xml, 'w') as xml:
            ___ child __ metaroot.find('notes').f_a_('note'):
                __ child.get('name') __ 'user':
                    child.text = user

            prettyprint(metaroot)
            metatree.write(xml, encoding='utf-8', xml_declaration=True)


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


c_ CustomPath(?W...?W..):

    ___  - (self, shot_root, sml, which):
        s_(CustomPath, self). - ()
        shot_root = shot_root
        sml = sml
        which = which
        sQT..('Set custom {} path'.format(which))
        setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        setMinimumWidth(600)
        build_ui()

    ___ build_ui
        create_widgets()
        create_layouts()
        create_signals()

    ___ create_widgets
        info = 'Here you can set a custom {} path that can be outside of the shot'.format(which)
        label_info = ?W...?L..(info)
        label_path = ?W...?L..('path: ')
        input_path = ?W...QLineEdit(load_custom_path(which))
        push_browse = ?W...?PB..()
        push_browse.setIcon(QtGui.QIcon(load_icons()['icon_folder']))
        push_browse.setObjectName('simple')
        push_save = ?W...?PB..('save')
        push_save.setObjectName('actionButtonBig')
        push_close = ?W...?PB..('close')

    ___ create_layouts
        layout_top = ?W...QHBoxLayout()
        layout_top.aW..(label_path)
        layout_top.aW..(input_path)
        layout_top.aW..(push_browse)
        layout_push = ?W...QHBoxLayout()
        layout_push.aW..(push_save)
        layout_push.aW..(push_close)
        layout_main = ?W...?VB..
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
        dialog = ?W...QFileDialog()
        dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        dialog.setFileMode(?W...QFileDialog.Directory)
        dialog.setOption(?W...QFileDialog.ShowDirsOnly)
        __ dialog.exec_() __ ?W...QDialog.Accepted:
            input_path.setText(dialog.selectedFiles()[0])

    ___ set_custom_path
        ___
            __ no. __.path.isdir(input_path.text()):
                __.makedirs(input_path.text())
        ______
            __ input_path.t.. != '':
                msg = "Failed setting up the path '{}' as custom {} directory. Please choose a different path.".format(input_path.t.., which)
                show_message_box(self, msg)
                r_

        meta_xml = get_meta_xml(shot_root)
        metatree = ET.parse(meta_xml)
        metaroot = metatree.getroot()
        with open(meta_xml, 'w') as xml:
            ___ child __ metaroot.find('notes').f_a_('note'):
                __ which __ 'render':
                    __ child.get('name') __ 'renderpath':
                        child.text = input_path.t..
                        child.set('loc', 'global')
                        __ input_path.t.. __ '':
                            child.set('loc', 'local')
                ____ which __ 'footage':
                    __ child.get('name') __ 'footagepath':
                        child.text = input_path.t..
                        child.set('loc', 'global')
                        __ input_path.t.. __ '':
                            child.set('loc', 'local')

            prettyprint(metaroot)
            metatree.write(xml, encoding='utf-8', xml_declaration=True)
        __ input_path.t.. __ '':
            msg = 'Successfully cleared the custom {} path'.format(which)
            show_message_box(self, msg)
        ____
            msg = "Successfully set up the custom {} path to: '{}'".format(which, input_path.text())
            show_message_box(self, msg)
        c__
        __ sml is no. N..:
            ___
                __ which __ 'render':
                    sml.current_shot_widget.set_renderpath(input_path.text())
                ____ which __ 'footage':
                    sml.current_shot_widget.set_footagepath(input_path.text())
                sml.current_shot_widget.refresh()
            except Exception as e:
                pass

        r_

    ___ load_custom_path(self, which):
        meta_xml = get_meta_xml(shot_root)
        metatree = ET.parse(meta_xml)
        metaroot = metatree.getroot()
        ___ child __ metaroot.find('notes').f_a_('note'):
            __ child.get('name') __ '{}path'.format(which):
                __ child.get('loc') and child.get('loc') __ 'global':
                    r_ child.text
                ____
                    r_ ''

    ___ keyPressEvent(self, event):
        __ event.key() __ QtCore.Qt.Key_Escape:
            c__