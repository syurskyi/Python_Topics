# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartCollect_v1.2/smartCollect/src/helper.py
______ __
______ sys
______ time
______ xml.etree.ElementTree as ET
______ subprocess
______ platform
______ json
______ hashlib
______ random
______ tempfile
______ cPickle
___
    ______ ?
except ImportError:
    ____ smartCollect.src ______ autosearch
    sitepackages = autosearch.scan_for_pyside()
    __ sitepackages not __ sys.path:
        sys.path.insert(0, sitepackages)

___
    ____ PySide ______ QtGui as ?W..
    ____ PySide ______ QtGui
    ____ PySide ______ QtCore
except ImportError:
    ____ ? ______ ?W..
    ____ ? ______ QtGui
    ____ ? ______ QtCore

____ smartCollect.src ______ templates

___ load_icons(*args):
    this_dir = __.path.dirname(__file__)
    dir_icon = __.path.join(this_dir, '../', 'icons')
    dir_icon = __.path.normpath(dir_icon)
    icons = {}
    ___ file_ __ __.listdir(dir_icon):
        name = __.path.splitext(file_)[0]
        path = __.path.join(dir_icon, file_)
        icons[name] = path

    return icons


___ get_tool_public_root(*args):
    root = __.path.join(__.path.expanduser('~'), 'cragl', 'smartCollect')
    __ not __.path.isdir(root):
        ___
            __.makedirs(root)
        ______
            write_log('unable to create open tool dir at: {}'.format(root))

    return root


___ get_tool_private_root(*args):
    root = __.path.join(__.path.expanduser('~'), '.cragl', 'smartCollect')
    __ not __.path.isdir(root):
        ___
            __.makedirs(root)
        ______
            write_log('unable to create private tool dir at: {}'.format(root))

    return root


___ get_logs_root():
    root = __.path.join(get_tool_public_root(), 'logs')
    __ not __.path.isdir(root):
        ___
            __.makedirs(root)
        ______
            write_log('unable to create logs dir at: {}'.format(root))

    return root


___ get_log_file(*args):
    connect_dir = __.path.join(__.path.expanduser('~'), '.cragl', 'connect')
    __ not __.path.isdir(connect_dir):
        __.makedirs(connect_dir)
    log_file = __.path.join(connect_dir, 'connectlog.txt')
    __ not __.path.isfile(log_file):
        with open(log_file, 'w') as lf:
            log_template = 'connect log\n{}\n'.format('-' * 50)
            lf.write(log_template)
    return log_file


___ write_log(text, tool = 'sc'):
    with open(get_log_file(), 'a') as file_:
        log_time_format = '%d.%m.%Y %H:%M:%S'
        log_time = time.strftime(log_time_format, time.localtime())
        file_.write('{}: {} {}\n'.format(log_time, tool, text))


___ get_trm_file(name):
    this_dir = __.path.dirname(__file__)
    file_ = __.path.join(this_dir, 'trm_{}.py'.format(name))
    file_ = __.path.normpath(file_)
    __ not __.path.isfile(file_):
        raise IOError('The terminal file does not exist: {}'.format(file_))
    return file_


___ load_settings(*args):
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


___ get_xml_elements():
    xml = get_settings_xml()
    tree = ET.parse(xml)
    root = tree.getroot()
    return (xml, root, tree)


___ get_settings_xml(*args):
    settings_xml = __.path.join(get_tool_private_root(), 'settings.xml')
    __ not __.path.isfile(settings_xml):
        ___
            with open(settings_xml, 'w') as look_template:
                template = templates.SETTINGS
                look_template.write(template.strip())
                msg = "smartCollect settings doesn't exist. created template at: {}".format(settings_xml)
                write_log(msg)
        ______
            msg = 'Failed writing smartCollect settings template at: {}'.format(settings_xml)
            write_log(msg)

    check_xml_ok(settings_xml)
    check_xml_values_exist()
    return settings_xml


___ check_xml_values_exist():
    settings = {'always_on_top': 'True',
     'tooltips': 'True',
     'convert_gizmos': 'False',
     'recreate_source_path': 'True',
     'src_path_mode': 'relative',
     'output_path': 'next-to-script',
     'ignore_nukescripts': 'backup, bckp, annotation',
     'logging_mode': 'Log file',
     'logging_level': '1',
     'nuke_exe_fixed': ' ',
     'archive_threads': '2'}
    ___ key, value __ settings.items():
        check_xml_value_exists('settings', 'setting', 'name', key, value)


___ check_xml_value_exists(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = __.path.join(get_tool_private_root(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = False
    item_found = 0
    ___ child __ root.find(parent).findall(section):
        __ child.get(key1) == value1:
            item_found += 1
            __ debug:
                print 'smartCollect | settings exists: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2)
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


___ check_xml_ok(xml, *args):
    ___
        with open(xml, 'r') as xml_file:
            ET.fromstring(xml_file.read())
        return True
    ______
        message = 'The smartCollect settings file seems to be broken. Do you want to reset it now?'
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


___ center_window(window):
    qr = window.frameGeometry()
    cp = ?W...QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


___ set_style_sheet(widget, *args):
    this_dir = __.path.join(__.path.dirname(__file__))
    styles_nuke = __.path.join(this_dir, '../', 'styles', 'styles.qss')
    styles_nuke = __.path.normpath(styles_nuke)
    __ __.path.isfile(styles_nuke):
        with open(styles_nuke) as file_:
            widget.setStyleSheet(file_.read())


___ open_in_explorer(path, parent = None, *args):
    __ platform.system() == 'Windows':
        __.startfile(path)
    elif platform.system() == 'Darwin':
        subprocess.Popen(['open', path])
    ____
        subprocess.Popen(['xdg-open', path])


___ show_message_box(window, message, *args):
    msg = ?W...QMessageBox()
    msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg.information(window, 'information', message)


___ load_nukescripts_settings(section):
    xml, root, tree = get_xml_elements()
    ? = []
    ___ nukescript __ root.find(section).findall('nukescript'):
        ?.ap..(nukescript.text)

    return ?


___ load_nukescripts_progress(path):
    _, root, _ = get_xml_elements()
    ___ nukescript __ root.find('archive').findall('nukescript'):
        __ nukescript.text == path:
            return int(nukescript.get('progress'))

    return 0


___ add_nukescript_settings(path, section):
    xml, root, tree = get_xml_elements()
    nukescript = ET.SubElement(root.find(section), 'nukescript')
    nukescript.text = path
    __ section == 'archive':
        nukescript.set('progress', '0')
        nukescript.set('comment', '')
        nukescript.set('output_path', '')
        nukescript.set('job_id', '')
    with open(xml, 'w') as xml_:
        prettyprint(root)
        tree.write(xml_, encoding='utf-8', xml_declaration=True)


___ update_nukescript_section(path, section, tag, value):
    xml, root, tree = get_xml_elements()
    ___ nukescript __ root.find(section).findall('nukescript'):
        __ nukescript.text == path:
            nukescript.set(tag, value)

    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


___ load_nukescript_section(path, section, tag):
    xml, root, tree = get_xml_elements()
    ___ nukescript __ root.find(section).findall('nukescript'):
        __ nukescript.text == path:
            return nukescript.get(tag)


___ remove_nukescript_settings(path, section):
    xml, root, tree = get_xml_elements()
    ___ nukescript __ root.find(section).findall('nukescript'):
        __ nukescript.text == path:
            root.find(section).remove(nukescript)

    with open(xml, 'w') as xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=True)


___ update_statusbar_added(smart_collector, source, count_dropped_elements):
    plural = 's' __ count_dropped_elements > 1 ____ ''
    status_msg = '{}: Added {} nukescript{}'.format(source.capitalize(), count_dropped_elements, plural)
    update_statusbar(smart_collector, status_msg, delay=2)


___ add_this_nukescript(smart_collector, source):
    ______ nk_utils
    path = nk_utils.get_nukescript_path()
    __ path __ ('', 'Root', None):
        show_message_box(smart_collector, 'Please save your script first in order to proceed.')
        return
    elif path __ smart_collector.table_nukescripts.?:
        show_message_box(smart_collector, 'The Nuke script exists already in the Nukescripts list.')
        return
    ____
        smart_collector.dropped_elements(([path], source))
        update_statusbar_added(smart_collector, source, 1)
        return


___ show_path_browser(title):
    dialog = ?W...QFileDialog()
    dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    dialog.setWindowTitle(title)
    dialog.setFileMode(?W...QFileDialog.Directory)
    dialog.setOption(?W...QFileDialog.ShowDirsOnly)
    __ dialog.exec_() == ?W...QDialog.Accepted:
        return dialog.selectedFiles()[0]


___ get_filename(path):
    return __.path.splitext(__.path.basename(path))[0]


___ load_tooltips(parent, section, *args):
    this_dir = __.path.dirname(__file__)
    tooltips_file = __.path.join(this_dir, '../', 'data', 'tooltips.json')
    tooltips_file = __.path.normpath(tooltips_file)
    __ not __.path.isfile(tooltips_file):
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


___ create_job_id(*args):
    current_time = str(int(time.time()))
    rand_number = str(random.random())
    id_ = hashlib.md5('{}{}'.format(current_time, rand_number)).hexdigest()[:8]
    return str('{}_{}'.format(current_time, id_))


___ update_statusbar(smart_collector, text, delay = 0):
    data = {'text': text,
     'delay': delay}
    smart_collector.statusbar_data_received.emit(data)


___ write_pickle_data(data):
    tmp_dir = tempfile.mkdtemp()
    path = __.path.join(tmp_dir, 'smartcollect_data.pickle')
    with open(path, 'w') as file_:
        cPickle.dump(data, file_)
    return path


___ get_selected_widgets(table):
    selected_elements = []
    ___ row __ table.selectedIndexes():
        selected_elements.ap..(table.cellWidget(row.row(), 0))

    return selected_elements


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
            show_message_box(None, msg)

    return


___ clear_statusbar(statusbar, delay):
    time.sleep(delay)
    statusbar.showMessage('')


___ bytesize_to_human(bytes_size, decimals = 2, human_radix = 1000.0):
    byte = 'B'
    kilobyte = 'KB'
    megabyte = 'MB'
    gigabyte = 'GB'
    terabyte = 'TB'
    units = [byte,
     kilobyte,
     megabyte,
     gigabyte,
     terabyte]
    human_fmt = '%.{}f %s'.format(decimals)
    ___ unit __ units[:-1]:
        __ bytes_size < human_radix:
            return human_fmt % (bytes_size, unit)
        bytes_size /= human_radix

    return human_fmt % (bytes_size, units[-1])


___ get_dir_size(path):
    total_size = 0
    seen = set()
    ___ dirpath, dirnames, filenames __ __.walk(path):
        ___ f __ filenames:
            fp = __.path.join(dirpath, f)
            ___
                stat = __.stat(fp)
            except OSError:
                continue

            __ stat.st_ino __ seen:
                continue
            seen.add(stat.st_ino)
            total_size += stat.st_size

    return bytesize_to_human(total_size)