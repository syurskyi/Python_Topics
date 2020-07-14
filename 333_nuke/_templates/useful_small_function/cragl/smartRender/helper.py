# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartRender_v3.0/smartRender/src/helper.py
______ hashlib
______ j___
______ multiprocessing
______ __
______ random
______ ___
______ subprocess
______ ti__
______ urllib
______ xml.etree.ElementTree __ ET
______ collections
______ pl..
______ d_t_
______ errno
______ ?
______ ?
__ ?.NUKE_VERSION_MAJOR < 11:
    ____ ? ______ ?G.. __ ?W..
    ____ ? ______ ?C..
____
    ____ ? ______ ?W..
    ____ ? ______ ?C..
______ templates

___ load_icons(*args):
    this_dir _ __.pa__.j..(__.pa__.d_n_( -f))
    dir_icon _ __.pa__.j..(this_dir, '../', 'icons')
    dir_icon _ __.pa__.n_p_(dir_icon)
    r_ {'icon_logo': __.pa__.j..(dir_icon, 'logo.png'),
     'icon_nuke': __.pa__.j..(dir_icon, 'nuke.png'),
     'icon_log': __.pa__.j..(dir_icon, 'log.png'),
     'icon_refresh': __.pa__.j..(dir_icon, 'refresh.png'),
     'icon_display': __.pa__.j..(dir_icon, 'display.png'),
     'icon_job': __.pa__.j..(dir_icon, 'job.png'),
     'icon_trash': __.pa__.j..(dir_icon, 'trash.png'),
     'icon_explorer': __.pa__.j..(dir_icon, 'explorer.png'),
     'icon_finished': __.pa__.j..(dir_icon, 'finished.png'),
     'icon_waiting': __.pa__.j..(dir_icon, 'waiting.png'),
     'icon_paused': __.pa__.j..(dir_icon, 'paused.png'),
     'icon_error': __.pa__.j..(dir_icon, 'error.png'),
     'icon_all': __.pa__.j..(dir_icon, 'all.png'),
     'icon_folder': __.pa__.j..(dir_icon, 'folder.png'),
     'about': __.pa__.j..(dir_icon, 'about.jpg'),
     'icon_read': __.pa__.j..(dir_icon, 'read.png'),
     'icon_play': __.pa__.j..(dir_icon, 'play.png'),
     'icon_cancel': __.pa__.j..(dir_icon, 'cancel.png'),
     'icon_navigate': __.pa__.j..(dir_icon, 'navigate.png'),
     'icon_disk': __.pa__.j..(dir_icon, 'disk.png'),
     'icon_setting': __.pa__.j..(dir_icon, 'setting.png'),
     'icon_plus': __.pa__.j..(dir_icon, 'plus.png'),
     'icon_minus': __.pa__.j..(dir_icon, 'minus.png'),
     'icon_x': __.pa__.j..(dir_icon, 'x.png'),
     'icon_arr_left': __.pa__.j..(dir_icon, 'arr_left.png'),
     'icon_arr_right': __.pa__.j..(dir_icon, 'arr_right.png'),
     'icon_apply': __.pa__.j..(dir_icon, 'apply.png'),
     'icon_on': __.pa__.j..(dir_icon, 'on.png'),
     'icon_off': __.pa__.j..(dir_icon, 'off.png'),
     'icon_batch': __.pa__.j..(dir_icon, 'batch.png'),
     'icon_process': __.pa__.j..(dir_icon, 'process.gif'),
     'icon_current': __.pa__.j..(dir_icon, 'current.png'),
     'icon_recent': __.pa__.j..(dir_icon, 'recent.png')}


___ get_next_renderjob(*args):
    jobs_xml _ get_job_xml()
    __ jobs_xml __ '':
        r_
    jobs_tree _ ET.parse(jobs_xml)
    jobs_root _ jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').f_a_('job'):
        ___ setting __ job.f_a_('setting'):
            __ setting.get('name') __ 'status':
                __ setting.text __ 'waiting':
                    r_ job.get('id')


___ get_all_write_nodes_data(*args):
    write_data _ {}
    all_write_nodes _ [ node ___ node __ ?.allNodes('Write') __ node['disable'].gV.. __ 0.0 ]
    ___ w.. __ all_write_nodes:
        write_data[w...n.. ] _ w..['file'].gV..

    r_ write_data


___ get_smart_render_private_root(*args):
    root _ __.pa__.j..(__.pa__.expanduser('~'), '.cragl', 'smartRender')
    __ no. __.pa__.isd..(root):
        ___
            __.m_d_(root)
        ______
            write_log('unable to create settings root dir')

    r_ root


___ get_smart_render_public_root(*args):
    root _ __.pa__.j..(__.pa__.expanduser('~'), 'cragl', 'smartRender')
    __ no. __.pa__.isd..(root):
        ___
            __.m_d_(root)
        ______
            write_log('unable to create open dir')

    r_ root


___ get_installed_root_dir(*args):
    this_dir _ __.pa__.j..(__.pa__.d_n_( -f))
    root _ __.pa__.j..(this_dir, '../', '../')
    r_ __.pa__.n_p_(root)


___ get_public_cache_folder():
    cache_dir _ __.pa__.j..(get_smart_render_public_root(), 'cache')
    __ no. __.pa__.isd..(cache_dir):
        ___
            __.m_d_(cache_dir)
        ______
            msg _ 'Unable to create cache directory at {}'.f..(cache_dir)
            write_log(msg)

    r_ cache_dir


___ get_tmp_folder():
    tmp_dir _ __.pa__.j..(get_smart_render_public_root(), 'tmp')
    __ no. __.pa__.isd..(tmp_dir):
        ___
            __.m_d_(tmp_dir)
        ______
            msg _ 'Unable to create tmp directory at {}'.f..(tmp_dir)
            write_log(msg)

    r_ tmp_dir


___ get_smartRender_backup_dir(*args):
    backup_dir _ __.pa__.j..(get_smart_render_public_root(), 'backups')
    __ no. __.pa__.isd..(backup_dir):
        ___
            __.m_d_(backup_dir)
        ______
            write_log('unable to create backup dir')

    r_ backup_dir


___ get_smartrender_log_dir(*args):
    logs_dir _ __.pa__.j..(get_smart_render_public_root(), 'logs')
    __ no. __.pa__.isd..(logs_dir):
        ___
            __.m_d_(logs_dir)
        ______
            write_log('unable to create logs dir')

    r_ logs_dir


___ get_sounds_dir(*args):
    this_dir _ __.pa__.d_n_( -f)
    sounds_dir _ __.pa__.j..(this_dir, '../', 'sounds')
    sounds_dir _ __.pa__.n_p_(sounds_dir)
    __ no. __.pa__.isd..(sounds_dir):
        ___
            __.m_d_(sounds_dir)
        ______
            write_log('unable to create sounds dir in {}.'.f..(sounds_dir))

    r_ sounds_dir


___ get_tooltips_file(*args):
    this_dir _ __.pa__.d_n_( -f)
    tooltips _ __.pa__.j..(this_dir, '../', 'data', 'tooltips.json')
    r_ __.pa__.n_p_(tooltips)


___ update_job_log(job_id, processdata, ti__ _ st.(__.(ti__.ti__())), *args):
    jobs_xml _ get_job_xml()
    __ jobs_xml __ '':
        r_
    jobs_tree _ ET.parse(jobs_xml)
    jobs_root _ jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').f_a_('job'):
        __ job.get('id') __ job_id:
            process _ job.find('process')
            p _ ET.SubElement(process, 'data')
            p.set('time', st.(ti__))
            p.set('status', st.(processdata[0]))
            p.set('thread', st.(processdata[1]))
            p.text _ processdata[2]
            w__ o..(jobs_xml, 'w') __ xml:
                prettyprint(jobs_root)
                jobs_tree.w..(xml, encoding_'utf-8', xml_declaration_T..)
            r_ T..


___ check_xml_ok(xml, *args):
    settings_xml _ __.pa__.j..(get_smart_render_private_root(), 'settings.xml')
    ___
        w__ o..(xml, 'r') __ xml_file:
            ET.fromstring(xml_file.read())
        r_ T..
    ______
        xml_name _ __.pa__.b_n_(xml)
        m.. _ 'The smartRender {} file seems to be broken. Do you want to reset it now?'.f..(xml_name)
        write_log('smartRender {} file broken.'.f..(xml_name))
        msg_box _ ?W...QMessageBox(?W...QMessageBox.Warning, 'QMessageBox.warning()', m.., ?W...QMessageBox.NoButton)
        reset _ msg_box.addButton('reset', ?W...QMessageBox.AcceptRole)
        style _ 'QPushButton {background-color: rgba(51, 204, 255, 150);}'
        reset.setStyleSheet(style)
        reset.clearFocus()
        msg_box.addButton('Cancel', ?W...QMessageBox.RejectRole)
        __ msg_box.exec_() __ ?W...QMessageBox.AcceptRole:
            __ __.pa__.isf..(xml):
                __.remove(xml)
                __ xml __ settings_xml:
                    get_settings_xml()
                ____
                    jobs_xml _ get_job_xml()
                    __ jobs_xml __ '':
                        r_ F..
        ____
            r_ F..


___ check_web_connection(*args):
    ___
        urllib.urlopen('http://www.cragl.com')
        r_ T..
    ______
        r_ F..


___ update_job_data(job_id, key, val, *args):
    jobs_xml _ get_job_xml()
    __ jobs_xml __ '':
        r_
    jobs_tree _ ET.parse(jobs_xml)
    jobs_root _ jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').f_a_('job'):
        __ job.get('id') __ job_id:
            ___ setting __ job.f_a_('setting'):
                __ setting.get('name') __ key:
                    setting.text _ val
                    w__ o..(jobs_xml, 'w') __ xml:
                        prettyprint(jobs_root)
                        jobs_tree.w..(xml, encoding_'utf-8', xml_declaration_T..)


___ calculate_process_precentage(job_id, frame, *args):
    jobs_xml _ get_job_xml()
    __ jobs_xml __ '':
        r_
    jobs_tree _ ET.parse(jobs_xml)
    jobs_root _ jobs_tree.getroot()
    count_frames_done _ 0
    ___ job __ jobs_root.find('jobs').f_a_('job'):
        __ job.get('id') __ job_id:
            ___ data __ job.find('process').f_a_('data'):
                __ data.get('status') __ '400':
                    count_frames_done +_ 1

            count_frames_to_process _ __.(job.find('frames').get('count'))
            done_precentage _ __.(100.0 / count_frames_to_process * count_frames_done)
            __ done_precentage > 100:
                done_precentage _ 100
            ___ setting __ job.f_a_('setting'):
                __ setting.get('name') __ 'progress':
                    setting.text _ st.(done_precentage)
                __ setting.get('name') __ 'status':
                    tmp_status _ setting.text
                    __ done_precentage __ 0:
                        setting.text _ 'waiting'
                    __ done_precentage > 0:
                        setting.text _ 'rendering'
                    __ st.(done_precentage) __ '100':
                        setting.text _ 'finished'
                    __ tmp_status __ 'paused':
                        setting.text _ 'paused'

            ___ f __ job.find('frames').f_a_('frame'):
                __ f.text __ st.(frame):
                    job.find('frames').remove(f)

            w__ o..(jobs_xml, 'w') __ xml:
                prettyprint(jobs_root)
                jobs_tree.w..(xml, encoding_'utf-8', xml_declaration_T..)
            r_ done_precentage


___ set_style_sheet(widget, *args):
    this_dir _ __.pa__.j..(__.pa__.d_n_( -f))
    styles_nuke _ __.pa__.j..(this_dir, '../', 'styles', 'nuke.qss')
    styles_nuke _ __.pa__.n_p_(styles_nuke)
    __ __.pa__.isf..(styles_nuke):
        w__ o..(styles_nuke) __ file_:
            widget.setStyleSheet(file_.read())


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
        ______ OSError:
            msg _ 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.f..(url)
            show_message_box(N.., msg)

    r_


___ get_job_id_by_script_orig(script_orig, *args):
    ___
        jobs_xml _ get_job_xml()
        __ jobs_xml __ '':
            r_ ''
        jobs_tree _ ET.parse(jobs_xml)
        jobs_root _ jobs_tree.getroot()
    ______ E.. __ e:
        r_ ''

    jobs _ # list
    ___ job __ jobs_root.find('jobs').f_a_('job'):
        ___ setting __ job.f_a_('setting'):
            __ setting.get('name') __ 'script_orig':
                __ setting.text __ script_orig:
                    jobs.ap..(job.get('id'))

    __ le.(jobs) __ 0:
        r_ ''
    ____ le.(jobs) __ 1:
        r_ jobs[0]
    ____
        latest _ jobs[0]
        ___ job __ jobs:
            __ job.s..('_')[0] > latest.s..('_')[0]:
                latest _ job

        r_ latest


___ get_job_data(job_id, *args):
    job_data _ {}
    frames_to_process _ # list
    ___
        jobs_xml _ get_job_xml()
        __ jobs_xml __ '':
            r_ {}
        jobs_tree _ ET.parse(jobs_xml)
        jobs_root _ jobs_tree.getroot()
    ______ E.. __ e:
        r_ {}

    ___ job __ jobs_root.find('jobs').f_a_('job'):
        __ job.get('id') __ job_id:
            job_data['job_id'] _ job_id
            ___ setting __ job.f_a_('setting'):
                job_data[setting.get('name')] _ setting.text

            ___ frame __ job.find('frames').f_a_('frame'):
                frames_to_process.ap..(__.(frame.text))

            job_data['frames_to_process'] _ frames_to_process
            number_errors _ 0
            ___ data __ job.find('process').f_a_('data'):
                __ data.get('status') __ '100':
                    number_errors +_ 1

            job_data['number_errors'] _ number_errors

    r_ job_data


___ get_all_jobs_data(filter, *args):
    jobs _ collections.OrderedDict()
    ___
        jobs_xml _ get_job_xml()
        __ jobs_xml __ '':
            r_ {}
        jobs_tree _ ET.parse(jobs_xml)
        jobs_root _ jobs_tree.getroot()
    ______ E.. __ e:
        r_ {}

    ___ job __ jobs_root.find('jobs').f_a_('job'):
        job_id _ job.get('id')
        jobs[job_id] _ get_job_data(job_id)
        __ filter __ 'waiting' an. jobs[job_id]['status'] !_ 'waiting':
            del jobs[job_id]
            c___
        __ filter __ 'waiting' an. jobs[job_id]['status'] !_ 'waiting':
            del jobs[job_id]
            c___
        ____ filter __ 'paused' an. jobs[job_id]['status'] !_ 'paused':
            del jobs[job_id]
            c___
        ____ filter __ 'cancelled' an. jobs[job_id]['status'] !_ 'cancelled':
            del jobs[job_id]
            c___
        ____ filter __ 'error' an. jobs[job_id]['status'] !_ 'error':
            del jobs[job_id]
            c___
        ____ filter __ 'finished' an. jobs[job_id]['status'] !_ 'finished':
            del jobs[job_id]
            c___

    r_ jobs


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


___ get_time_formated():
    r_ ti__.strftime('%d.%m.%Y %H:%M:%S', ti__.localtime())


___ write_log(text, tool _ 'rn'):
    w__ o..(get_log_file(), 'a') __ file_:
        log_time_format _ '%d.%m.%Y %H:%M:%S'
        log_time _ ti__.strftime(log_time_format, ti__.localtime())
        file_.w..('{}: {} {}\n'.f..(log_time, tool, text))


___ write_render_log(text, *args):
    log _ __.pa__.j..(get_smart_render_private_root(), 'log.txt')
    __ no. __.pa__.isf..(log):
        w__ o..(log, 'w') __ lf:
            lf.w..('')
    ___
        w__ o..(log, 'a') __ lf:
            lf.w..('{}: {}\n'.f..(get_time_formated()), text)
        r_ T..
    ______ IOError:
        r_ F..


___ write_terminal_cmd(job_id, text, file _ 'input', *args):
    log_name _ '{}_terminal_{}.log'.f..(job_id, file)
    log _ __.pa__.j..(get_smartrender_log_dir(), log_name)
    __ no. __.pa__.isf..(log):
        w__ o..(log, 'w') __ file_:
            file_.w..('')
    ___
        w__ o..(log, 'a') __ file_:
            file_.w..('{}\n'.f..(text))
        r_ T..
    ______ IOError:
        r_ F..


___ get_job_xml(*args):
    job_xml _ __.pa__.j..(get_smart_render_private_root(), 'jobs.xml')
    __ no. __.pa__.isf..(job_xml):
        ___
            w__ o..(job_xml, 'w') __ job_template:
                template _ templates.JOB
                job_template.w..(template.strip())
                write_log("smartRender job log doesn't exist. created template at: {}".f..(job_xml))
        ______
            write_log('Failed writing smartRender job log template to: {}'.f..(job_xml))

    r_ job_xml


___ insert_as_read_node(job_details, w.. _ N.., *args):
    __ w..:
        read _ ?.createNode('Read')
        read['file'].sV..(w..['file'].getValue())
        read['first'].sV..(__.(?.r.. ['first_frame'].getValue()))
        read['origfirst'].sV..(__.(?.r.. ['first_frame'].getValue()))
        read['last'].sV..(__.(?.r.. ['last_frame'].getValue()))
        read['origlast'].sV..(__.(?.r.. ['last_frame'].getValue()))
        read['on_error'].sV..('nearest frame')
        read.selectOnly()
        read.setXYpos(__.(w..['xpos'].getValue()), __.(w..['ypos'].getValue()) + 70)
        ?.zoom(1.0, (w...xpos(), w...ypos()))
        ?.connect_selected_to_viewer(0)
    ____
        read _ ?.createNode('Read')
        read['file'].sV..(job_details['render_path'])
        read['first'].sV..(__.(job_details['render_start']))
        read['origfirst'].sV..(__.(job_details['render_start']))
        read['last'].sV..(__.(job_details['render_end']))
        read['origlast'].sV..(__.(job_details['render_end']))
        read['on_error'].sV..('nearest frame')
        read.selectOnly()
        ?.zoom(1.0, (read.xpos(), read.ypos()))
        ?.connect_selected_to_viewer(0)


___ get_job_details(job_id, *args):
    job_details _ {}
    jobs_xml _ get_job_xml()
    jobs_tree _ ET.parse(jobs_xml)
    jobs_root _ jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').f_a_('job'):
        __ job.get('id') __ job_id:
            ___ setting __ job.f_a_('setting'):
                job_details[setting.get('name')] _ setting.text

    r_ job_details


___ force_create_render_dir(*args):
    file_name _ ?.filename(?.tN..())
    dir_name _ __.pa__.d_n_(file_name)
    os_dir _ ?.callbacks.filenameFilter(dir_name)
    ___
        __.m_d_(os_dir)
    ______ OSError __ e:
        __ e.errno !_ errno.EEXIST:
            raise


___ load_terminal_log(job_id, mode, *args):
    xml_name _ '{}_terminal_{}.log'.f..(job_id, mode)
    terminal_file _ __.pa__.j..(get_smartrender_log_dir(), xml_name)
    __ no. __.pa__.isf..(terminal_file):
        r_ ''
    ___
        w__ o..(terminal_file, 'rt') __ file:
            r_ file.read()
    ______ E.. __ e:
        r_ 'Error reading the terminal input file. {}'.f..(e)


___ load_job_log_data(job_id, filter, file_output _ F.., *args):
    job_data _ ''
    jobs_xml _ get_job_xml()
    __ jobs_xml __ '':
        r_
    jobs_tree _ ET.parse(jobs_xml)
    jobs_root _ jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').f_a_('job'):
        __ job.get('id') __ job_id:
            ___ data __ job.find('process').f_a_('data'):
                code _ ''
                __ data.get('status') __ '100':
                    __ filter !_ 'job: all' an. filter !_ 'job: error':
                        c___
                    __ file_output:
                        code _ '[error]'
                    ____
                        code _ "[<span style='color:#993333'>error</span>"
                ____ data.get('status') __ '300':
                    __ filter !_ 'job: all' an. filter !_ 'job: info':
                        c___
                    __ file_output:
                        code _ '[info]'
                    ____
                        code _ '[info'
                ____ data.get('status') __ '400':
                    __ filter !_ 'job: all' an. filter !_ 'job: done':
                        c___
                    __ file_output:
                        code _ '[done]'
                    ____
                        code _ "[<span style='color:#339933'>done</span>"
                data_time _ __.(data.get('time'))
                ti__ _ d_t_.d_t_.fromtimestamp(data_time).strftime('%d/%m/%Y %H:%M:%S')
                __ file_output:
                    job_data +_ '{time} {code} {text}\n'.f..(ti___ti__, code_code, text_data.text)
                ____
                    job_data +_ '<tr><td>{time}</td><td> {code}</td><td>] {text}</td></tr>'.f..(ti___ti__, code_code, text_data.text)
                    job_data _ '<table>{}</table>'.f..(job_data)

    r_ job_data


___ open_in_explorer(pa__, parent _ N.., *args):
    __ no. __.pa__.isd..(pa__):
        msg _ "Unable to open directory. The path doesn't exist:\n\n{}".f..(pa__)
        show_message_box(parent, msg)
    __ pl...system() __ 'Windows':
        __.startfile(pa__)
    ____ pl...system() __ 'Darwin':
        subprocess.P..(['open', pa__])
    ____
        subprocess.P..(['xdg-open', pa__])


___ reset_file(which, window, *args):
    __ which __ 'jobs':
        m.. _ 'Do you want to flush the jobs file?'
        proccess_button_text _ 'flush jobs'
    ____
        m.. _ 'Do you want to reset the smartRender settings? Please note: all render presets will be removed, too.'
        proccess_button_text _ 'reset settings'
    process_button_color _ '70, 10, 10, 255'
    cancel_button_text _ 'cancel'
    reset _ ask_dialog(m.., proccess_button_text, process_button_color, cancel_button_text)
    __ reset:
        __ which __ 'jobs':
            jobs_file _ get_job_xml()
            ___
                __ __.pa__.isf..(jobs_file):
                    __.remove(jobs_file)
                    msg _ 'Successfully flushed jobs file.'
                    show_message_box(window, msg)
            ______ E.. __ e:
                write_log('Cannot remove jobs file. {}'.f..(e))

        ____ which __ 'settings':
            settings_file _ get_settings_xml()
            ___
                __ __.pa__.isf..(settings_file):
                    __.remove(settings_file)
                    msg _ 'Successfully reset the smartRender settings.'
                    show_message_box(window, msg)
            ______ E.. __ e:
                write_log('Cannot reset settings file. {}'.f..(e))


___ get_settings_xml(*args):
    settings_xml _ __.pa__.j..(get_smart_render_private_root(), 'settings.xml')
    __ no. __.pa__.isf..(settings_xml):
        desktop_cache _ __.pa__.j..(__.pa__.expanduser('~'), 'Desktop/cache')
        ___
            w__ o..(settings_xml, 'w') __ render_template:
                template _ templates.SETTINGS.f..(public_cache_get_public_cache_folder(), desktop_cache_desktop_cache)
                render_template.w..(template.strip())
                write_log("smartRender settings doesn't exist. created template at: {}".f..(settings_xml))
        ______
            write_log('Failed writing smartRender settings template at: {}'.f..(settings_xml))

    check_settings_xml_values_exist()
    r_ settings_xml


___ check_settings_xml_values_exist():
    settings _ {'current_tab': '1',
     'timer_log_update': '1000',
     'timer_job_log_update': '5000',
     'show_cmd': 'True',
     'notification': 'True',
     'sound': '01.wav',
     'auto_dir': 'True',
     'auto_insert_render': 'False',
     'enable_backup': 'True',
     'after_submit': '0',
     'cache_padding_delimiter': '_',
     'cache_padding': '4',
     'cache_extension': 'exr',
     'enable_node_addons_read': 'True',
     'enable_node_addons_write': 'True',
     'gnc_change_nodes': '0',
     'gnc_change_knobs': '0',
     'show_renderinfo': 'True',
     'info_pos': '0:0',
     'info_resume': 'True',
     'info_pause': 'True',
     'info_delete': 'True',
     'info_job_log': 'True',
     'info_render_into_dag': 'True',
     'info_open_renderdir': 'True',
     'auto_close_renderinfo': 'True',
     'show_render_file_name': 'True',
     'tooltips': 'True'}
    ___ key, v..  __ settings.i..():
        check_xml_value_exists('settings', 'setting', 'name', key, v.. )

    settings_current _ {'range': 'global',
     'custom_range': '',
     'step': '1',
     'overwrite': 'True',
     'size': 'full',
     'thread_count': st.(__.(get_cpu_count() / 2))}
    ___ key, v..  __ settings_current.i..():
        check_xml_value_exists_current('setting', 'name', key, v.. )


___ load_sounds(*args):
    sounds _ # list
    sounds_dir _ get_sounds_dir()
    __ no. __.pa__.isd..(sounds_dir):
        r_
    ___ file_ __ __.l_d_(sounds_dir):
        __ __.pa__.s_t_(file_)[1] __ ('.wav', '.WAV'):
            sounds.ap..(file_)

    r_ sounds


___ load_presets(*args):
    presets_list _ {}
    settings_xml _ get_settings_xml()
    settingstree _ ET.parse(settings_xml)
    settingsroot _ settingstree.getroot()
    ___ presets __ settingsroot.find('presets'):
        preset_name _ presets.get('name')
        preset _ {}
        ___ setting __ presets.f_a_('setting'):
            __ setting.get('name') __ 'range':
                preset['range'] _ setting.text
            ____ setting.get('name') __ 'custom_range':
                preset['custom_range'] _ setting.text
            ____ setting.get('name') __ 'step':
                preset['step'] _ setting.text
            ____ setting.get('name') __ 'overwrite':
                preset['overwrite'] _ setting.text
            ____ setting.get('name') __ 'size':
                preset['size'] _ setting.text
                __ setting.get('width'):
                    preset['width'] _ setting.get('width')
                ____
                    preset['width'] _ ''
                __ setting.get('height'):
                    preset['height'] _ setting.get('height')
                ____
                    preset['height'] _ ''
                preset['aspectratio'] _ setting.get('aspectratio')
            ____ setting.get('name') __ 'description':
                preset['description'] _ setting.text
            ____ setting.get('name') __ 'thread_count':
                preset['thread_count'] _ setting.text
                __ no. preset['thread_count']:
                    preset['thread_count'] _ ?.env['numCPUs'] / 2

        presets_list[preset_name] _ preset

    r_ presets_list


___ play_sound(sound, *args):
    sound_file _ __.pa__.j..(get_sounds_dir(), sound)
    __ __.pa__.isf..(sound_file):
        ?W...QSound.play(sound_file)


___ load_settings(*args):
    settings_xml _ get_settings_xml()
    settings _ {}
    cache_paths _ # list
    __ check_xml_ok(settings_xml):
        settingstree _ ET.parse(settings_xml)
        settingsroot _ settingstree.getroot()
        ___ setting __ settingsroot.find('settings').f_a_('setting'):
            settings[setting.get('name')] _ setting.text

        ___ pa__ __ settingsroot.find('cache').f_a_('path'):
            cache_paths.ap..({'mode': pa__.get('mode'),
             'path': pa__.text})

        settings['cache'] _ cache_paths
    r_ settings


___ get_caches_by_mode(mode, *args):
    r_ [ cache['path'] ___ cache __ load_settings()['cache'] __ cache['mode'] __ mode ]


___ add_cache_path(mode, pa__, *args):
    settings_xml _ get_settings_xml()
    __ settings_xml __ '':
        r_
    settings_tree _ ET.parse(settings_xml)
    settings_root _ settings_tree.getroot()
    new_cache_path _ ET.SubElement(settings_root.find('cache'), 'path')
    new_cache_path.text _ pa__
    new_cache_path.set('mode', mode)
    ET.dump(new_cache_path)
    w__ o..(settings_xml, 'w') __ xml:
        prettyprint(settings_root)
        settings_tree.w..(xml, encoding_'utf-8', xml_declaration_T..)


___ check_xml_value_exists(parent, section, key1, value1, text, key2 _ '', value2 _ ''):
    xml _ __.pa__.j..(get_smart_render_private_root(), 'settings.xml')
    tree _ ET.parse(xml)
    root _ tree.getroot()
    debug _ F..
    item_found _ 0
    ___ child __ root.find(parent).f_a_(section):
        __ child.get(key1) __ value1:
            item_found +_ 1
            __ debug:
                print 'smartRender | settings exists: {}|{}|{}|{}|{}|{}|{}'.f..(parent, section, key1, value1, text, key2, value2)
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


___ check_xml_value_exists_cache(parent, section, key1, value1, text, key2 _ '', value2 _ ''):
    xml _ __.pa__.j..(get_smart_render_private_root(), 'settings.xml')
    tree _ ET.parse(xml)
    root _ tree.getroot()
    debug _ F..
    item_found _ 0
    ___ child __ root.find(parent).f_a_(section):
        __ child.get(key1) __ value1:
            __ value2 __ child.text:
                item_found +_ 1
                __ debug:
                    print 'smartRender | settings exists: {}|{}|{}|{}|{}|{}|{}'.f..(parent, section, key1, value1, text, key2, value2)
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


___ check_xml_value_exists_current(section, key1, value1, text, key2 _ '', value2 _ ''):
    settings_xml _ __.pa__.j..(get_smart_render_private_root(), 'settings.xml')
    tree _ ET.parse(settings_xml)
    root _ tree.getroot()
    item_found _ 0
    current_found _ F..
    ___ child __ root.find('presets').f_a_('preset'):
        __ child.get('name') __ 'current':
            current_found _ T..
        ____
            current_found _ F..
        ___ setting __ child.f_a_('setting'):
            __ setting.get(key1) __ value1:
                item_found +_ 1
                r_

    __ current_found:
        __ item_found __ 0:
            elem _ ET.Element(section)
            elem.set(key1, value1)
            __ key2 !_ '':
                elem.set(key2, value2)
            elem.text _ text
            ___ child __ root.find('presets').f_a_('preset'):
                __ child.get('name') __ 'current':
                    child.ap..(elem)
                    w__ o..(settings_xml, 'w'):
                        prettyprint(root)
                        tree.w..(settings_xml, encoding_'utf-8', xml_declaration_T..)
                    write_log('settings xml added: {}|{}|{}|{}|{}|{}'.f..(section, key1, value1, text, key2, value2))


___ get_cpu_count(*args):
    ___
        r_ multiprocessing.cpu_count()
    ______ E.. __ e:
        __ hasattr(__, 'sysconf'):
            __ __.sysconf_names.has_key('SC_NPROCESSORS_ONLN'):
                ncpus _ __.sysconf('SC_NPROCESSORS_ONLN')
                __ i..(ncpus, __.) an. ncpus > 0:
                    r_ ncpus
            ____
                r_ __.(__.popen2('sysctl -n hw.ncpu')[1].read())
        __ __.en__.has_key('NUMBER_OF_PROCESSORS'):
            ncpus _ __.(__.en__['NUMBER_OF_PROCESSORS'])
            __ ncpus > 0:
                r_ ncpus
        r_ 1


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


___ delete_cache_path(pa__, *args):
    settings_xml _ get_settings_xml()
    settings_tree _ ET.parse(settings_xml)
    settings_root _ settings_tree.getroot()
    ___ path_element __ settings_root.find('cache').f_a_('path'):
        __ path_element.text __ pa__:
            settings_root.find('cache').remove(path_element)
            w__ o..(settings_xml, 'w') __ xml:
                prettyprint(settings_root)
                settings_tree.w..(xml, encoding_'utf-8', xml_declaration_T..)


___ ask_dialog(m.. _ '', process_button_text _ '', color_process _ '', cancel_button_text _ ''):
    msg_box _ ?W...QMessageBox(?W...QMessageBox.Warning, 'QMessageBox.warning()', m.., ?W...QMessageBox.NoButton, N..)
    msg_box.setWindowFlags(?C...__.WindowStaysOnTopHint)
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


___ create_unique_job_id(*args):
    current_time _ st.(__.(ti__.ti__()))
    rand_number _ st.(random.random())
    id _ hashlib.md5('{}{}'.f..(current_time, rand_number)).hexdigest()[:8]
    r_ st.('{}_{}'.f..(current_time, id))


___ get_all_views(range_ _ 10):
    ___
        views _ # list
        ___ i __ ra..(range_):
            ?.activeViewer().previousView()

        ___ i __ ra..(range_):
            __ ?.activeViewer().view() no. __ views:
                views.ap..(?.activeViewer().view())
            ?.activeViewer().nextView()

        r_ views
    ______
        r_ ['main']


___ create_tooltips(parent, key, *args):
    tooltips_file _ get_tooltips_file()
    __ no. __.pa__.isf..(tooltips_file):
        r_
    w__ o..(tooltips_file) __ json_file:
        ttdata _ j___.l..(json_file)
    ___ widget __ parent.findChildren(?C...QObject):
        ___ tooltip __ ttdata[key]:
            __ tooltip['tt'] __ widget.property('tt'):
                widget.setToolTip('<strong>{}</strong><br />{}'.f..(tooltip['ttt'], tooltip['ttc']))


___ get_explorer_name(*args):
    __ ___.pl.. __ 'darwin':
        r_ 'finder'
    ____
        r_ 'explorer'


___ get_recent_nukescripts(*args):
    file_recent_files _ __.pa__.j..(__.pa__.expanduser('~'), '.nuke', 'recent_files')
    recent_files _ # list
    __ __.pa__.isf..(file_recent_files):
        w__ o..(file_recent_files, 'r') __ rf:
            ___ line __ rf:
                file_ _ line.r..('\n', '')
                file_ _ file_.r..('"', '')
                recent_files.ap..(file_)

            r_ recent_files
    ____
        r_ # list


___ open_renderpath_in_explorer(label, renderpath, srw, *args):
    __ renderpath __ '':
        label _ label.s..(' (')[0]
        msg _ "The file path for '{}' hasn't been set up, yet.".f..(label)
        show_message_box(srw, msg)
        r_
    ___
        open_in_explorer(__.pa__.d_n_(renderpath), parent_srw)
    ______ E.. __ e:
        show_message_box(srw, 'An error occurred: {}'.f..(e))
        r_


___ get_processor(name):
    this_dir _ __.pa__.d_n_( -f)
    processor _ __.pa__.j..(this_dir, '../', 'trm', '{}.py'.f..(name))
    processor _ __.pa__.n_p_(processor)
    __ no. __.pa__.isf..(processor):
        raise IOError('The processor script does not exist: {}'.f..(processor))
    r_ processor