# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartCollect_v1.2/smartCollect/src/helper.py
______ __
______ ___
______ ti__
______ xml.etree.ElementTree __ ET
______ subprocess
______ pl..
______ j___
______ hashlib
______ random
______ tempfile
______ cPickle
___
    ______ ?
except ImportError:
    ____ smartCollect.src ______ autosearch
    sitepackages = autosearch.scan_for_pyside()
    __ sitepackages no. __ ___.path:
        ___.path.insert(0, sitepackages)

___
    ____ ? ______ ?G.. __ ?W..
    ____ ? ______ ?G..
    ____ ? ______ ?C..
except ImportError:
    ____ ? ______ ?W..
    ____ ? ______ ?G..
    ____ ? ______ ?C..

____ smartCollect.src ______ templates

___ load_icons(*args):
    this_dir = __.path.dirname( -f)
    dir_icon = __.path.join(this_dir, '../', 'icons')
    dir_icon = __.path.n_p_(dir_icon)
    icons = {}
    ___ file_ __ __.listdir(dir_icon):
        name = __.path.splitext(file_)[0]
        path = __.path.join(dir_icon, file_)
        icons[name] = path

    r_ icons


___ get_tool_public_root(*args):
    root = __.path.join(__.path.expanduser('~'), 'cragl', 'smartCollect')
    __ no. __.path.isdir(root):
        ___
            __.makedirs(root)
        ______
            write_log('unable to create open tool dir at: {}'.f..(root))

    r_ root


___ get_tool_private_root(*args):
    root = __.path.join(__.path.expanduser('~'), '.cragl', 'smartCollect')
    __ no. __.path.isdir(root):
        ___
            __.makedirs(root)
        ______
            write_log('unable to create private tool dir at: {}'.f..(root))

    r_ root


___ get_logs_root():
    root = __.path.join(get_tool_public_root(), 'logs')
    __ no. __.path.isdir(root):
        ___
            __.makedirs(root)
        ______
            write_log('unable to create logs dir at: {}'.f..(root))

    r_ root


___ get_log_file(*args):
    connect_dir = __.path.join(__.path.expanduser('~'), '.cragl', 'connect')
    __ no. __.path.isdir(connect_dir):
        __.makedirs(connect_dir)
    log_file = __.path.join(connect_dir, 'connectlog.txt')
    __ no. __.path.isfile(log_file):
        w__ o..(log_file, 'w') __ lf:
            log_template = 'connect log\n{}\n'.f..('-' * 50)
            lf.write(log_template)
    r_ log_file


___ write_log(text, tool = 'sc'):
    w__ o..(get_log_file(), 'a') __ file_:
        log_time_format = '%d.%m.%Y %H:%M:%S'
        log_time = ti__.strftime(log_time_format, ti__.localtime())
        file_.write('{}: {} {}\n'.f..(log_time, tool, text))


___ get_trm_file(name):
    this_dir = __.path.dirname( -f)
    file_ = __.path.join(this_dir, 'trm_{}.py'.f..(name))
    file_ = __.path.n_p_(file_)
    __ no. __.path.isfile(file_):
        raise IOError('The terminal file does not exist: {}'.f..(file_))
    r_ file_


___ load_settings(*args):
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
                value = False
            settings[setting.get('name')] = value

    r_ settings


___ get_xml_elements():
    xml = get_settings_xml()
    tree = ET.parse(xml)
    root = tree.getroot()
    r_ (xml, root, tree)


___ get_settings_xml(*args):
    settings_xml = __.path.join(get_tool_private_root(), 'settings.xml')
    __ no. __.path.isfile(settings_xml):
        ___
            w__ o..(settings_xml, 'w') __ look_template:
                template = templates.SETTINGS
                look_template.write(template.strip())
                msg = "smartCollect settings doesn't exist. created template at: {}".f..(settings_xml)
                write_log(msg)
        ______
            msg = 'Failed writing smartCollect settings template at: {}'.f..(settings_xml)
            write_log(msg)

    check_xml_ok(settings_xml)
    check_xml_values_exist()
    r_ settings_xml


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
    ___ child __ root.find(parent).f_a_(section):
        __ child.get(key1) __ value1:
            item_found += 1
            __ debug:
                print 'smartCollect | settings exists: {}|{}|{}|{}|{}|{}|{}'.f..(parent, section, key1, value1, text, key2, value2)
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


___ check_xml_ok(xml, *args):
    ___
        w__ o..(xml, 'r') __ xml_file:
            ET.fromstring(xml_file.read())
        r_ T..
    ______
        m.. = 'The smartCollect settings file seems to be broken. Do you want to reset it now?'
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
        r_ False
        r_


___ center_window(window):
    qr = window.frameGeometry()
    cp = ?W...QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


___ set_style_sheet(widget, *args):
    this_dir = __.path.join(__.path.dirname( -f))
    styles_nuke = __.path.join(this_dir, '../', 'styles', 'styles.qss')
    styles_nuke = __.path.n_p_(styles_nuke)
    __ __.path.isfile(styles_nuke):
        w__ o..(styles_nuke) __ file_:
            widget.setStyleSheet(file_.read())


___ open_in_explorer(path, parent = N.., *args):
    __ pl...system() __ 'Windows':
        __.startfile(path)
    ____ pl...system() __ 'Darwin':
        subprocess.P..(['open', path])
    ____
        subprocess.P..(['xdg-open', path])


___ show_message_box(window, m.., *args):
    msg = ?W...QMessageBox()
    msg.setWindowFlags(?C...__.WindowStaysOnTopHint)
    msg.information(window, 'information', m..)


___ load_nukescripts_settings(section):
    xml, root, tree = get_xml_elements()
    ? = []
    ___ nukescript __ root.find(section).f_a_('nukescript'):
        ?.ap..(nukescript.text)

    r_ ?


___ load_nukescripts_progress(path):
    _, root, _ = get_xml_elements()
    ___ nukescript __ root.find('archive').f_a_('nukescript'):
        __ nukescript.text __ path:
            r_ int(nukescript.get('progress'))

    r_ 0


___ add_nukescript_settings(path, section):
    xml, root, tree = get_xml_elements()
    nukescript = ET.SubElement(root.find(section), 'nukescript')
    nukescript.text = path
    __ section __ 'archive':
        nukescript.set('progress', '0')
        nukescript.set('comment', '')
        nukescript.set('output_path', '')
        nukescript.set('job_id', '')
    w__ o..(xml, 'w') __ xml_:
        prettyprint(root)
        tree.write(xml_, encoding='utf-8', xml_declaration=T..)


___ update_nukescript_section(path, section, tag, value):
    xml, root, tree = get_xml_elements()
    ___ nukescript __ root.find(section).f_a_('nukescript'):
        __ nukescript.text __ path:
            nukescript.set(tag, value)

    w__ o..(xml, 'w') __ xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=T..)


___ load_nukescript_section(path, section, tag):
    xml, root, tree = get_xml_elements()
    ___ nukescript __ root.find(section).f_a_('nukescript'):
        __ nukescript.text __ path:
            r_ nukescript.get(tag)


___ remove_nukescript_settings(path, section):
    xml, root, tree = get_xml_elements()
    ___ nukescript __ root.find(section).f_a_('nukescript'):
        __ nukescript.text __ path:
            root.find(section).remove(nukescript)

    w__ o..(xml, 'w') __ xml:
        prettyprint(root)
        tree.write(xml, encoding='utf-8', xml_declaration=T..)


___ update_statusbar_added(smart_collector, source, count_dropped_elements):
    plural = 's' __ count_dropped_elements > 1 ____ ''
    status_msg = '{}: Added {} nukescript{}'.f..(source.capitalize(), count_dropped_elements, plural)
    update_statusbar(smart_collector, status_msg, delay=2)


___ add_this_nukescript(smart_collector, source):
    ______ nk_utils
    path = nk_utils.get_nukescript_path()
    __ path __ ('', 'Root', N..):
        show_message_box(smart_collector, 'Please save your script first in order to proceed.')
        r_
    ____ path __ smart_collector.table_nukescripts.?:
        show_message_box(smart_collector, 'The Nuke script exists already in the Nukescripts list.')
        r_
    ____
        smart_collector.dropped_elements(([path], source))
        update_statusbar_added(smart_collector, source, 1)
        r_


___ show_path_browser(title):
    dialog = ?W...QFileDialog()
    dialog.setWindowFlags(?C...__.WindowStaysOnTopHint)
    dialog.sQT..(title)
    dialog.setFileMode(?W...QFileDialog.Directory)
    dialog.setOption(?W...QFileDialog.ShowDirsOnly)
    __ dialog.exec_() __ ?W...QDialog.Accepted:
        r_ dialog.selectedFiles()[0]


___ get_filename(path):
    r_ __.path.splitext(__.path.basename(path))[0]


___ load_tooltips(parent, section, *args):
    this_dir = __.path.dirname( -f)
    tooltips_file = __.path.join(this_dir, '../', 'data', 'tooltips.json')
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


___ create_job_id(*args):
    current_time = str(int(ti__.ti__()))
    rand_number = str(random.random())
    id_ = hashlib.md5('{}{}'.f..(current_time, rand_number)).hexdigest()[:8]
    r_ str('{}_{}'.f..(current_time, id_))


___ update_statusbar(smart_collector, text, delay = 0):
    data = {'text': text,
     'delay': delay}
    smart_collector.statusbar_data_received.emit(data)


___ write_pickle_data(data):
    tmp_dir = tempfile.mkdtemp()
    path = __.path.join(tmp_dir, 'smartcollect_data.pickle')
    w__ o..(path, 'w') __ file_:
        cPickle.dump(data, file_)
    r_ path


___ get_selected_widgets(table):
    selected_elements = []
    ___ row __ table.selectedIndexes():
        selected_elements.ap..(table.cellWidget(row.row(), 0))

    r_ selected_elements


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
            show_message_box(N.., msg)

    r_


___ clear_statusbar(statusbar, delay):
    ti__.sleep(delay)
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
    human_fmt = '%.{}f %s'.f..(decimals)
    ___ unit __ units[:-1]:
        __ bytes_size < human_radix:
            r_ human_fmt % (bytes_size, unit)
        bytes_size /= human_radix

    r_ human_fmt % (bytes_size, units[-1])


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

    r_ bytesize_to_human(total_size)