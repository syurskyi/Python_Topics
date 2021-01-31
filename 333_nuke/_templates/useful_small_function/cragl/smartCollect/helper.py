# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartCollect_v1.2/smartCollect/src/helper.py
______ __
______ ___
______ ti__
______ xml.etree.ElementTree __ ET
______ su__
______ pl..
______ j___
______ hashlib
______ random
______ tempfile
______ cPickle
___
    ______ ?
______ ImportError:
    ____ smartCollect.src ______ autosearch
    sitepackages _ autosearch.scan_for_pyside()
    __ sitepackages no. __ ___.pa__:
        ___.pa__.insert(0, sitepackages)

___
    ____ ? ______ ?G.. __ ?W..
    ____ ? ______ ?G..
    ____ ? ______ ?C..
______ ImportError:
    ____ ? ______ ?W..
    ____ ? ______ ?G..
    ____ ? ______ ?C..

____ smartCollect.src ______ templates

___ load_icons(*args):
    this_dir _ __.pa__.d_n_( -f)
    dir_icon _ __.pa__.j..(this_dir, '../', 'icons')
    dir_icon _ __.pa__.n_p_(dir_icon)
    icons _ {}
    ___ file_ __ __.l_d_(dir_icon):
        name _ __.pa__.s_t_(file_)[0]
        pa__ _ __.pa__.j..(dir_icon, file_)
        icons[name] _ pa__

    r_ icons


___ get_tool_public_root(*args):
    root _ __.pa__.j..(__.pa__.e__('~'), 'cragl', 'smartCollect')
    __ no. __.pa__.isd..(root):
        ___
            __.m_d_(root)
        ______
            write_log('unable to create open tool dir at: {}'.f..(root))

    r_ root


___ get_tool_private_root(*args):
    root _ __.pa__.j..(__.pa__.e__('~'), '.cragl', 'smartCollect')
    __ no. __.pa__.isd..(root):
        ___
            __.m_d_(root)
        ______
            write_log('unable to create private tool dir at: {}'.f..(root))

    r_ root


___ get_logs_root
    root _ __.pa__.j..(get_tool_public_root(), 'logs')
    __ no. __.pa__.isd..(root):
        ___
            __.m_d_(root)
        ______
            write_log('unable to create logs dir at: {}'.f..(root))

    r_ root


___ get_log_file(*args):
    connect_dir _ __.pa__.j..(__.pa__.e__('~'), '.cragl', 'connect')
    __ no. __.pa__.isd..(connect_dir):
        __.m_d_(connect_dir)
    log_file _ __.pa__.j..(connect_dir, 'connectlog.txt')
    __ no. __.pa__.isf..(log_file):
        w__ o..(log_file, 'w') __ lf:
            log_template _ 'connect log\n{}\n'.f..('-' * 50)
            lf.w..(log_template)
    r_ log_file


___ write_log(text, tool _ 'sc'):
    w__ o..(get_log_file(), 'a') __ file_:
        log_time_format _ '%d.%m.%Y %H:%M:%S'
        log_time _ ti__.s_t_(log_time_format, ti__.localtime())
        file_.w..('{}: {} {}\n'.f..(log_time, tool, text))


___ get_trm_file(name):
    this_dir _ __.pa__.d_n_( -f)
    file_ _ __.pa__.j..(this_dir, 'trm_{}.py'.f..(name))
    file_ _ __.pa__.n_p_(file_)
    __ no. __.pa__.isf..(file_):
        raise IOError('The terminal file does not exist: {}'.f..(file_))
    r_ file_


___ load_settings(*args):
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


___ get_xml_elements
    xml _ get_settings_xml()
    tree _ ET.parse(xml)
    root _ tree.getroot()
    r_ (xml, root, tree)


___ get_settings_xml(*args):
    settings_xml _ __.pa__.j..(get_tool_private_root(), 'settings.xml')
    __ no. __.pa__.isf..(settings_xml):
        ___
            w__ o..(settings_xml, 'w') __ look_template:
                template _ templates.SETTINGS
                look_template.w..(template.strip())
                msg _ "smartCollect settings doesn't exist. created template at: {}".f..(settings_xml)
                write_log(msg)
        ______
            msg _ 'Failed writing smartCollect settings template at: {}'.f..(settings_xml)
            write_log(msg)

    check_xml_ok(settings_xml)
    check_xml_values_exist()
    r_ settings_xml


___ check_xml_values_exist
    settings _ {'always_on_top': 'True',
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
    ___ key, v..  __ settings.i..
        check_xml_value_exists('settings', 'setting', 'name', key, v.. )


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
                print 'smartCollect | settings exists: {}|{}|{}|{}|{}|{}|{}'.f..(parent, section, key1, value1, text, key2, value2)
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


___ check_xml_ok(xml, *args):
    ___
        w__ o..(xml, 'r') __ xml_file:
            ET.fromstring(xml_file.read())
        r_ T..
    ______
        m.. _ 'The smartCollect settings file seems to be broken. Do you want to reset it now?'
        reset_settings_xml _ ask_dialog(m.., process_label_'reset', color_process_'actionButton')
        __ reset_settings_xml:
            __ __.pa__.isf..(xml):
                __.r__(xml)
                get_settings_xml()


___ ask_dialog(m.., process_label _ 'ok', color_process _ 'actionButton', cancel_label _ 'cancel'):
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
    msg_box.addButton(cancel_label, ?W...QMessageBox.RejectRole)
    __ msg_box.exec_() __ ?W...QMessageBox.AcceptRole:
        r_ T..
    ____
        r_ F..
        r_


___ center_window(window):
    qr _ window.frameGeometry()
    cp _ ?W...QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


___ set_style_sheet(widget, *args):
    this_dir _ __.pa__.j..(__.pa__.d_n_( -f))
    styles_nuke _ __.pa__.j..(this_dir, '../', 'styles', 'styles.qss')
    styles_nuke _ __.pa__.n_p_(styles_nuke)
    __ __.pa__.isf..(styles_nuke):
        w__ o..(styles_nuke) __ file_:
            widget.setStyleSheet(file_.read())


___ open_in_explorer(pa__, parent _ N.., *args):
    __ pl...system() __ 'Windows':
        __.startfile(pa__)
    ____ pl...system() __ 'Darwin':
        su__.P..(['open', pa__])
    ____
        su__.P..(['xdg-open', pa__])


___ show_message_box(window, m.., *args):
    msg _ ?W...QMessageBox()
    msg.setWindowFlags(?C...__.WindowStaysOnTopHint)
    msg.information(window, 'information', m..)


___ load_nukescripts_settings(section):
    xml, root, tree _ get_xml_elements()
    ? _ # list
    ___ nukescript __ root.find(section).f_a_('nukescript'):
        ?.ap..(nukescript.text)

    r_ ?


___ load_nukescripts_progress(pa__):
    _, root, _ _ get_xml_elements()
    ___ nukescript __ root.find('archive').f_a_('nukescript'):
        __ nukescript.text __ pa__:
            r_ __.(nukescript.get('progress'))

    r_ 0


___ add_nukescript_settings(pa__, section):
    xml, root, tree _ get_xml_elements()
    nukescript _ ET.SubElement(root.find(section), 'nukescript')
    nukescript.text _ pa__
    __ section __ 'archive':
        nukescript.set('progress', '0')
        nukescript.set('comment', '')
        nukescript.set('output_path', '')
        nukescript.set('job_id', '')
    w__ o..(xml, 'w') __ xml_:
        prettyprint(root)
        tree.w..(xml_, encoding_'utf-8', xml_declaration_T..)


___ update_nukescript_section(pa__, section, tag, v.. ):
    xml, root, tree _ get_xml_elements()
    ___ nukescript __ root.find(section).f_a_('nukescript'):
        __ nukescript.text __ pa__:
            nukescript.set(tag, v.. )

    w__ o..(xml, 'w') __ xml:
        prettyprint(root)
        tree.w..(xml, encoding_'utf-8', xml_declaration_T..)


___ load_nukescript_section(pa__, section, tag):
    xml, root, tree _ get_xml_elements()
    ___ nukescript __ root.find(section).f_a_('nukescript'):
        __ nukescript.text __ pa__:
            r_ nukescript.get(tag)


___ remove_nukescript_settings(pa__, section):
    xml, root, tree _ get_xml_elements()
    ___ nukescript __ root.find(section).f_a_('nukescript'):
        __ nukescript.text __ pa__:
            root.find(section).r__(nukescript)

    w__ o..(xml, 'w') __ xml:
        prettyprint(root)
        tree.w..(xml, encoding_'utf-8', xml_declaration_T..)


___ update_statusbar_added(smart_collector, source, count_dropped_elements):
    plural _ 's' __ count_dropped_elements > 1 ____ ''
    status_msg _ '{}: Added {} nukescript{}'.f..(source.capitalize(), count_dropped_elements, plural)
    update_statusbar(smart_collector, status_msg, delay_2)


___ add_this_nukescript(smart_collector, source):
    ______ nk_utils
    pa__ _ nk_utils.get_nukescript_path()
    __ pa__ __ ('', 'Root', N..):
        show_message_box(smart_collector, 'Please save your script first in order to proceed.')
        r_
    ____ pa__ __ smart_collector.table_nukescripts.?:
        show_message_box(smart_collector, 'The Nuke script exists already in the Nukescripts list.')
        r_
    ____
        smart_collector.dropped_elements(([pa__], source))
        update_statusbar_added(smart_collector, source, 1)
        r_


___ show_path_browser(title):
    dialog _ ?W...QFileDialog()
    dialog.setWindowFlags(?C...__.WindowStaysOnTopHint)
    dialog.sQT..(title)
    dialog.setFileMode(?W...QFileDialog.Directory)
    dialog.setOption(?W...QFileDialog.ShowDirsOnly)
    __ dialog.exec_() __ ?W...QDialog.Accepted:
        r_ dialog.selectedFiles()[0]


___ get_filename(pa__):
    r_ __.pa__.s_t_(__.pa__.b_n_(pa__))[0]


___ load_tooltips(parent, section, *args):
    this_dir _ __.pa__.d_n_( -f)
    tooltips_file _ __.pa__.j..(this_dir, '../', 'data', 'tooltips.json')
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


___ create_job_id(*args):
    current_time _ st.(__.(ti__.ti__()))
    rand_number _ st.(random.random())
    id_ _ hashlib.md5('{}{}'.f..(current_time, rand_number)).hexdigest()[:8]
    r_ st.('{}_{}'.f..(current_time, id_))


___ update_statusbar(smart_collector, text, delay _ 0):
    data _ {'text': text,
     'delay': delay}
    smart_collector.statusbar_data_received.emit(data)


___ write_pickle_data(data):
    tmp_dir _ tempfile.mkdtemp()
    pa__ _ __.pa__.j..(tmp_dir, 'smartcollect_data.pickle')
    w__ o..(pa__, 'w') __ file_:
        cPickle.dump(data, file_)
    r_ pa__


___ get_selected_widgets(table):
    selected_elements _ # list
    ___ row __ table.selectedIndexes
        selected_elements.ap..(table.cellWidget(row.row(), 0))

    r_ selected_elements


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


___ clear_statusbar(statusbar, delay):
    ti__.sleep(delay)
    statusbar.showMessage('')


___ bytesize_to_human(bytes_size, decimals _ 2, human_radix _ 1000.0):
    byte _ 'B'
    kilobyte _ 'KB'
    megabyte _ 'MB'
    gigabyte _ 'GB'
    terabyte _ 'TB'
    units _ [byte,
     kilobyte,
     megabyte,
     gigabyte,
     terabyte]
    human_fmt _ '%.{}f @'.f..(decimals)
    ___ unit __ units[:-1]:
        __ bytes_size < human_radix:
            r_ human_fmt % (bytes_size, unit)
        bytes_size /_ human_radix

    r_ human_fmt % (bytes_size, units[-1])


___ get_dir_size(pa__):
    total_size _ 0
    seen _ set()
    ___ dirpath, dirnames, filenames __ __.walk(pa__):
        ___ f __ filenames:
            fp _ __.pa__.j..(dirpath, f)
            ___
                stat _ __.stat(fp)
            ______ OSError:
                c___

            __ stat.st_ino __ seen:
                c___
            seen.add(stat.st_ino)
            total_size +_ stat.st_size

    r_ bytesize_to_human(total_size)