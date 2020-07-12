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
    this_dir _ __.path.join(__.path.dirname( -f))
    dir_icon _ __.path.join(this_dir, '../', 'icons')
    dir_icon _ __.path.n_p_(dir_icon)
    r_ {'icon_logo': __.path.join(dir_icon, 'logo.png'),
     'icon_nuke': __.path.join(dir_icon, 'nuke.png'),
     'icon_log': __.path.join(dir_icon, 'log.png'),
     'icon_refresh': __.path.join(dir_icon, 'refresh.png'),
     'icon_display': __.path.join(dir_icon, 'display.png'),
     'icon_job': __.path.join(dir_icon, 'job.png'),
     'icon_trash': __.path.join(dir_icon, 'trash.png'),
     'icon_explorer': __.path.join(dir_icon, 'explorer.png'),
     'icon_finished': __.path.join(dir_icon, 'finished.png'),
     'icon_waiting': __.path.join(dir_icon, 'waiting.png'),
     'icon_paused': __.path.join(dir_icon, 'paused.png'),
     'icon_error': __.path.join(dir_icon, 'error.png'),
     'icon_all': __.path.join(dir_icon, 'all.png'),
     'icon_folder': __.path.join(dir_icon, 'folder.png'),
     'about': __.path.join(dir_icon, 'about.jpg'),
     'icon_read': __.path.join(dir_icon, 'read.png'),
     'icon_play': __.path.join(dir_icon, 'play.png'),
     'icon_cancel': __.path.join(dir_icon, 'cancel.png'),
     'icon_navigate': __.path.join(dir_icon, 'navigate.png'),
     'icon_disk': __.path.join(dir_icon, 'disk.png'),
     'icon_setting': __.path.join(dir_icon, 'setting.png'),
     'icon_plus': __.path.join(dir_icon, 'plus.png'),
     'icon_minus': __.path.join(dir_icon, 'minus.png'),
     'icon_x': __.path.join(dir_icon, 'x.png'),
     'icon_arr_left': __.path.join(dir_icon, 'arr_left.png'),
     'icon_arr_right': __.path.join(dir_icon, 'arr_right.png'),
     'icon_apply': __.path.join(dir_icon, 'apply.png'),
     'icon_on': __.path.join(dir_icon, 'on.png'),
     'icon_off': __.path.join(dir_icon, 'off.png'),
     'icon_batch': __.path.join(dir_icon, 'batch.png'),
     'icon_process': __.path.join(dir_icon, 'process.gif'),
     'icon_current': __.path.join(dir_icon, 'current.png'),
     'icon_recent': __.path.join(dir_icon, 'recent.png')}


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
    ___ write __ all_write_nodes:
        write_data[write.name()] _ write['file'].gV..

    r_ write_data


___ get_smart_render_private_root(*args):
    root _ __.path.join(__.path.expanduser('~'), '.cragl', 'smartRender')
    __ no. __.path.isdir(root):
        ___
            __.makedirs(root)
        ______
            write_log('unable to create settings root dir')

    r_ root


___ get_smart_render_public_root(*args):
    root _ __.path.join(__.path.expanduser('~'), 'cragl', 'smartRender')
    __ no. __.path.isdir(root):
        ___
            __.makedirs(root)
        ______
            write_log('unable to create open dir')

    r_ root


___ get_installed_root_dir(*args):
    this_dir _ __.path.join(__.path.dirname( -f))
    root _ __.path.join(this_dir, '../', '../')
    r_ __.path.n_p_(root)


___ get_public_cache_folder():
    cache_dir _ __.path.join(get_smart_render_public_root(), 'cache')
    __ no. __.path.isdir(cache_dir):
        ___
            __.makedirs(cache_dir)
        ______
            msg _ 'Unable to create cache directory at {}'.f..(cache_dir)
            write_log(msg)

    r_ cache_dir


___ get_tmp_folder():
    tmp_dir _ __.path.join(get_smart_render_public_root(), 'tmp')
    __ no. __.path.isdir(tmp_dir):
        ___
            __.makedirs(tmp_dir)
        ______
            msg _ 'Unable to create tmp directory at {}'.f..(tmp_dir)
            write_log(msg)

    r_ tmp_dir


___ get_smartRender_backup_dir(*args):
    backup_dir _ __.path.join(get_smart_render_public_root(), 'backups')
    __ no. __.path.isdir(backup_dir):
        ___
            __.makedirs(backup_dir)
        ______
            write_log('unable to create backup dir')

    r_ backup_dir


___ get_smartrender_log_dir(*args):
    logs_dir _ __.path.join(get_smart_render_public_root(), 'logs')
    __ no. __.path.isdir(logs_dir):
        ___
            __.makedirs(logs_dir)
        ______
            write_log('unable to create logs dir')

    r_ logs_dir


___ get_sounds_dir(*args):
    this_dir _ __.path.dirname( -f)
    sounds_dir _ __.path.join(this_dir, '../', 'sounds')
    sounds_dir _ __.path.n_p_(sounds_dir)
    __ no. __.path.isdir(sounds_dir):
        ___
            __.makedirs(sounds_dir)
        ______
            write_log('unable to create sounds dir in {}.'.f..(sounds_dir))

    r_ sounds_dir


___ get_tooltips_file(*args):
    this_dir _ __.path.dirname( -f)
    tooltips _ __.path.join(this_dir, '../', 'data', 'tooltips.json')
    r_ __.path.n_p_(tooltips)


___ update_job_log(job_id, processdata, ti__ _ str(in.(ti__.ti__())), *args):
    jobs_xml _ get_job_xml()
    __ jobs_xml __ '':
        r_
    jobs_tree _ ET.parse(jobs_xml)
    jobs_root _ jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').f_a_('job'):
        __ job.get('id') __ job_id:
            process _ job.find('process')
            p _ ET.SubElement(process, 'data')
            p.set('time', str(ti__))
            p.set('status', str(processdata[0]))
            p.set('thread', str(processdata[1]))
            p.text _ processdata[2]
            w__ o..(jobs_xml, 'w') __ xml:
                prettyprint(jobs_root)
                jobs_tree.write(xml, encoding_'utf-8', xml_declaration_T..)
            r_ T..


___ check_xml_ok(xml, *args):
    settings_xml _ __.path.join(get_smart_render_private_root(), 'settings.xml')
    ___
        w__ o..(xml, 'r') __ xml_file:
            ET.fromstring(xml_file.read())
        r_ T..
    ______
        xml_name _ __.path.basename(xml)
        m.. _ 'The smartRender {} file seems to be broken. Do you want to reset it now?'.f..(xml_name)
        write_log('smartRender {} file broken.'.f..(xml_name))
        msg_box _ ?W...QMessageBox(?W...QMessageBox.Warning, 'QMessageBox.warning()', m.., ?W...QMessageBox.NoButton)
        reset _ msg_box.addButton('reset', ?W...QMessageBox.AcceptRole)
        style _ 'QPushButton {background-color: rgba(51, 204, 255, 150);}'
        reset.setStyleSheet(style)
        reset.clearFocus()
        msg_box.addButton('Cancel', ?W...QMessageBox.RejectRole)
        __ msg_box.exec_() __ ?W...QMessageBox.AcceptRole:
            __ __.path.isfile(xml):
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
                        jobs_tree.write(xml, encoding_'utf-8', xml_declaration_T..)


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

            count_frames_to_process _ in.(job.find('frames').get('count'))
            done_precentage _ in.(100.0 / count_frames_to_process * count_frames_done)
            __ done_precentage > 100:
                done_precentage _ 100
            ___ setting __ job.f_a_('setting'):
                __ setting.get('name') __ 'progress':
                    setting.text _ str(done_precentage)
                __ setting.get('name') __ 'status':
                    tmp_status _ setting.text
                    __ done_precentage __ 0:
                        setting.text _ 'waiting'
                    __ done_precentage > 0:
                        setting.text _ 'rendering'
                    __ str(done_precentage) __ '100':
                        setting.text _ 'finished'
                    __ tmp_status __ 'paused':
                        setting.text _ 'paused'

            ___ f __ job.find('frames').f_a_('frame'):
                __ f.text __ str(frame):
                    job.find('frames').remove(f)

            w__ o..(jobs_xml, 'w') __ xml:
                prettyprint(jobs_root)
                jobs_tree.write(xml, encoding_'utf-8', xml_declaration_T..)
            r_ done_precentage


___ set_style_sheet(widget, *args):
    this_dir _ __.path.join(__.path.dirname( -f))
    styles_nuke _ __.path.join(this_dir, '../', 'styles', 'nuke.qss')
    styles_nuke _ __.path.n_p_(styles_nuke)
    __ __.path.isfile(styles_nuke):
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
        except OSError:
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
    except Exception __ e:
        r_ ''

    jobs _ []
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
            __ job.split('_')[0] > latest.split('_')[0]:
                latest _ job

        r_ latest


___ get_job_data(job_id, *args):
    job_data _ {}
    frames_to_process _ []
    ___
        jobs_xml _ get_job_xml()
        __ jobs_xml __ '':
            r_ {}
        jobs_tree _ ET.parse(jobs_xml)
        jobs_root _ jobs_tree.getroot()
    except Exception __ e:
        r_ {}

    ___ job __ jobs_root.find('jobs').f_a_('job'):
        __ job.get('id') __ job_id:
            job_data['job_id'] _ job_id
            ___ setting __ job.f_a_('setting'):
                job_data[setting.get('name')] _ setting.text

            ___ frame __ job.find('frames').f_a_('frame'):
                frames_to_process.ap..(in.(frame.text))

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
    except Exception __ e:
        r_ {}

    ___ job __ jobs_root.find('jobs').f_a_('job'):
        job_id _ job.get('id')
        jobs[job_id] _ get_job_data(job_id)
        __ filter __ 'waiting' an. jobs[job_id]['status'] !_ 'waiting':
            del jobs[job_id]
            continue
        __ filter __ 'waiting' an. jobs[job_id]['status'] !_ 'waiting':
            del jobs[job_id]
            continue
        ____ filter __ 'paused' an. jobs[job_id]['status'] !_ 'paused':
            del jobs[job_id]
            continue
        ____ filter __ 'cancelled' an. jobs[job_id]['status'] !_ 'cancelled':
            del jobs[job_id]
            continue
        ____ filter __ 'error' an. jobs[job_id]['status'] !_ 'error':
            del jobs[job_id]
            continue
        ____ filter __ 'finished' an. jobs[job_id]['status'] !_ 'finished':
            del jobs[job_id]
            continue

    r_ jobs


___ get_log_file(*args):
    connect_dir _ __.path.join(__.path.expanduser('~'), '.cragl', 'connect')
    __ no. __.path.isdir(connect_dir):
        __.makedirs(connect_dir)
    log_file _ __.path.join(connect_dir, 'connectlog.txt')
    __ no. __.path.isfile(log_file):
        w__ o..(log_file, 'w') __ lf:
            log_template _ 'connect log\n{}\n'.f..('-' * 50)
            lf.write(log_template)
    r_ log_file


___ get_time_formated():
    r_ ti__.strftime('%d.%m.%Y %H:%M:%S', ti__.localtime())


___ write_log(text, tool _ 'rn'):
    w__ o..(get_log_file(), 'a') __ file_:
        log_time_format _ '%d.%m.%Y %H:%M:%S'
        log_time _ ti__.strftime(log_time_format, ti__.localtime())
        file_.write('{}: {} {}\n'.f..(log_time, tool, text))


___ write_render_log(text, *args):
    log _ __.path.join(get_smart_render_private_root(), 'log.txt')
    __ no. __.path.isfile(log):
        w__ o..(log, 'w') __ lf:
            lf.write('')
    ___
        w__ o..(log, 'a') __ lf:
            lf.write('{}: {}\n'.f..(get_time_formated()), text)
        r_ T..
    except IOError:
        r_ F..


___ write_terminal_cmd(job_id, text, file _ 'input', *args):
    log_name _ '{}_terminal_{}.log'.f..(job_id, file)
    log _ __.path.join(get_smartrender_log_dir(), log_name)
    __ no. __.path.isfile(log):
        w__ o..(log, 'w') __ file_:
            file_.write('')
    ___
        w__ o..(log, 'a') __ file_:
            file_.write('{}\n'.f..(text))
        r_ T..
    except IOError:
        r_ F..


___ get_job_xml(*args):
    job_xml _ __.path.join(get_smart_render_private_root(), 'jobs.xml')
    __ no. __.path.isfile(job_xml):
        ___
            w__ o..(job_xml, 'w') __ job_template:
                template _ templates.JOB
                job_template.write(template.strip())
                write_log("smartRender job log doesn't exist. created template at: {}".f..(job_xml))
        ______
            write_log('Failed writing smartRender job log template to: {}'.f..(job_xml))

    r_ job_xml


___ insert_as_read_node(job_details, write _ N.., *args):
    __ write:
        read _ ?.createNode('Read')
        read['file'].sV..(write['file'].getValue())
        read['first'].sV..(in.(?.root()['first_frame'].getValue()))
        read['origfirst'].sV..(in.(?.root()['first_frame'].getValue()))
        read['last'].sV..(in.(?.root()['last_frame'].getValue()))
        read['origlast'].sV..(in.(?.root()['last_frame'].getValue()))
        read['on_error'].sV..('nearest frame')
        read.selectOnly()
        read.setXYpos(in.(write['xpos'].getValue()), in.(write['ypos'].getValue()) + 70)
        ?.zoom(1.0, (write.xpos(), write.ypos()))
        ?.connect_selected_to_viewer(0)
    ____
        read _ ?.createNode('Read')
        read['file'].sV..(job_details['render_path'])
        read['first'].sV..(in.(job_details['render_start']))
        read['origfirst'].sV..(in.(job_details['render_start']))
        read['last'].sV..(in.(job_details['render_end']))
        read['origlast'].sV..(in.(job_details['render_end']))
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
    file_name _ ?.filename(?.thisNode())
    dir_name _ __.path.dirname(file_name)
    os_dir _ ?.callbacks.filenameFilter(dir_name)
    ___
        __.makedirs(os_dir)
    except OSError __ e:
        __ e.errno !_ errno.EEXIST:
            raise


___ load_terminal_log(job_id, mode, *args):
    xml_name _ '{}_terminal_{}.log'.f..(job_id, mode)
    terminal_file _ __.path.join(get_smartrender_log_dir(), xml_name)
    __ no. __.path.isfile(terminal_file):
        r_ ''
    ___
        w__ o..(terminal_file, 'rt') __ file:
            r_ file.read()
    except Exception __ e:
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
                        continue
                    __ file_output:
                        code _ '[error]'
                    ____
                        code _ "[<span style='color:#993333'>error</span>"
                ____ data.get('status') __ '300':
                    __ filter !_ 'job: all' an. filter !_ 'job: info':
                        continue
                    __ file_output:
                        code _ '[info]'
                    ____
                        code _ '[info'
                ____ data.get('status') __ '400':
                    __ filter !_ 'job: all' an. filter !_ 'job: done':
                        continue
                    __ file_output:
                        code _ '[done]'
                    ____
                        code _ "[<span style='color:#339933'>done</span>"
                data_time _ in.(data.get('time'))
                ti__ _ d_t_.d_t_.fromtimestamp(data_time).strftime('%d/%m/%Y %H:%M:%S')
                __ file_output:
                    job_data +_ '{time} {code} {text}\n'.f..(ti___ti__, code_code, text_data.text)
                ____
                    job_data +_ '<tr><td>{time}</td><td> {code}</td><td>] {text}</td></tr>'.f..(ti___ti__, code_code, text_data.text)
                    job_data _ '<table>{}</table>'.f..(job_data)

    r_ job_data


___ open_in_explorer(path, parent _ N.., *args):
    __ no. __.path.isdir(path):
        msg _ "Unable to open directory. The path doesn't exist:\n\n{}".f..(path)
        show_message_box(parent, msg)
    __ pl...system() __ 'Windows':
        __.startfile(path)
    ____ pl...system() __ 'Darwin':
        subprocess.P..(['open', path])
    ____
        subprocess.P..(['xdg-open', path])


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
                __ __.path.isfile(jobs_file):
                    __.remove(jobs_file)
                    msg _ 'Successfully flushed jobs file.'
                    show_message_box(window, msg)
            except Exception __ e:
                write_log('Cannot remove jobs file. {}'.f..(e))

        ____ which __ 'settings':
            settings_file _ get_settings_xml()
            ___
                __ __.path.isfile(settings_file):
                    __.remove(settings_file)
                    msg _ 'Successfully reset the smartRender settings.'
                    show_message_box(window, msg)
            except Exception __ e:
                write_log('Cannot reset settings file. {}'.f..(e))


___ get_settings_xml(*args):
    settings_xml _ __.path.join(get_smart_render_private_root(), 'settings.xml')
    __ no. __.path.isfile(settings_xml):
        desktop_cache _ __.path.join(__.path.expanduser('~'), 'Desktop/cache')
        ___
            w__ o..(settings_xml, 'w') __ render_template:
                template _ templates.SETTINGS.f..(public_cache_get_public_cache_folder(), desktop_cache_desktop_cache)
                render_template.write(template.strip())
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
    ___ key, value __ settings.items():
        check_xml_value_exists('settings', 'setting', 'name', key, value)

    settings_current _ {'range': 'global',
     'custom_range': '',
     'step': '1',
     'overwrite': 'True',
     'size': 'full',
     'thread_count': str(in.(get_cpu_count() / 2))}
    ___ key, value __ settings_current.items():
        check_xml_value_exists_current('setting', 'name', key, value)


___ load_sounds(*args):
    sounds _ []
    sounds_dir _ get_sounds_dir()
    __ no. __.path.isdir(sounds_dir):
        r_
    ___ file_ __ __.listdir(sounds_dir):
        __ __.path.splitext(file_)[1] __ ('.wav', '.WAV'):
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
    sound_file _ __.path.join(get_sounds_dir(), sound)
    __ __.path.isfile(sound_file):
        ?W...QSound.play(sound_file)


___ load_settings(*args):
    settings_xml _ get_settings_xml()
    settings _ {}
    cache_paths _ []
    __ check_xml_ok(settings_xml):
        settingstree _ ET.parse(settings_xml)
        settingsroot _ settingstree.getroot()
        ___ setting __ settingsroot.find('settings').f_a_('setting'):
            settings[setting.get('name')] _ setting.text

        ___ path __ settingsroot.find('cache').f_a_('path'):
            cache_paths.ap..({'mode': path.get('mode'),
             'path': path.text})

        settings['cache'] _ cache_paths
    r_ settings


___ get_caches_by_mode(mode, *args):
    r_ [ cache['path'] ___ cache __ load_settings()['cache'] __ cache['mode'] __ mode ]


___ add_cache_path(mode, path, *args):
    settings_xml _ get_settings_xml()
    __ settings_xml __ '':
        r_
    settings_tree _ ET.parse(settings_xml)
    settings_root _ settings_tree.getroot()
    new_cache_path _ ET.SubElement(settings_root.find('cache'), 'path')
    new_cache_path.text _ path
    new_cache_path.set('mode', mode)
    ET.dump(new_cache_path)
    w__ o..(settings_xml, 'w') __ xml:
        prettyprint(settings_root)
        settings_tree.write(xml, encoding_'utf-8', xml_declaration_T..)


___ check_xml_value_exists(parent, section, key1, value1, text, key2 _ '', value2 _ ''):
    xml _ __.path.join(get_smart_render_private_root(), 'settings.xml')
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
            tree.write(xml, encoding_'utf-8', xml_declaration_T..)
        write_log('settings xml added: {}|{}|{}|{}|{}|{}|{}'.f..(parent, section, key1, value1, text, key2, value2))


___ check_xml_value_exists_cache(parent, section, key1, value1, text, key2 _ '', value2 _ ''):
    xml _ __.path.join(get_smart_render_private_root(), 'settings.xml')
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
            tree.write(xml, encoding_'utf-8', xml_declaration_T..)
        write_log('settings xml added: {}|{}|{}|{}|{}|{}|{}'.f..(parent, section, key1, value1, text, key2, value2))


___ check_xml_value_exists_current(section, key1, value1, text, key2 _ '', value2 _ ''):
    settings_xml _ __.path.join(get_smart_render_private_root(), 'settings.xml')
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
                        tree.write(settings_xml, encoding_'utf-8', xml_declaration_T..)
                    write_log('settings xml added: {}|{}|{}|{}|{}|{}'.f..(section, key1, value1, text, key2, value2))


___ get_cpu_count(*args):
    ___
        r_ multiprocessing.cpu_count()
    except Exception __ e:
        __ hasattr(__, 'sysconf'):
            __ __.sysconf_names.has_key('SC_NPROCESSORS_ONLN'):
                ncpus _ __.sysconf('SC_NPROCESSORS_ONLN')
                __ i..(ncpus, in.) an. ncpus > 0:
                    r_ ncpus
            ____
                r_ in.(__.popen2('sysctl -n hw.ncpu')[1].read())
        __ __.en__.has_key('NUMBER_OF_PROCESSORS'):
            ncpus _ in.(__.en__['NUMBER_OF_PROCESSORS'])
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


___ delete_cache_path(path, *args):
    settings_xml _ get_settings_xml()
    settings_tree _ ET.parse(settings_xml)
    settings_root _ settings_tree.getroot()
    ___ path_element __ settings_root.find('cache').f_a_('path'):
        __ path_element.text __ path:
            settings_root.find('cache').remove(path_element)
            w__ o..(settings_xml, 'w') __ xml:
                prettyprint(settings_root)
                settings_tree.write(xml, encoding_'utf-8', xml_declaration_T..)


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
    current_time _ str(in.(ti__.ti__()))
    rand_number _ str(random.random())
    id _ hashlib.md5('{}{}'.f..(current_time, rand_number)).hexdigest()[:8]
    r_ str('{}_{}'.f..(current_time, id))


___ get_all_views(range_ _ 10):
    ___
        views _ []
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
    __ no. __.path.isfile(tooltips_file):
        r_
    w__ o..(tooltips_file) __ json_file:
        ttdata _ j___.load(json_file)
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
    file_recent_files _ __.path.join(__.path.expanduser('~'), '.nuke', 'recent_files')
    recent_files _ []
    __ __.path.isfile(file_recent_files):
        w__ o..(file_recent_files, 'r') __ rf:
            ___ line __ rf:
                file_ _ line.r..('\n', '')
                file_ _ file_.r..('"', '')
                recent_files.ap..(file_)

            r_ recent_files
    ____
        r_ []


___ open_renderpath_in_explorer(label, renderpath, srw, *args):
    __ renderpath __ '':
        label _ label.split(' (')[0]
        msg _ "The file path for '{}' hasn't been set up, yet.".f..(label)
        show_message_box(srw, msg)
        r_
    ___
        open_in_explorer(__.path.dirname(renderpath), parent_srw)
    except Exception __ e:
        show_message_box(srw, 'An error occurred: {}'.f..(e))
        r_


___ get_processor(name):
    this_dir _ __.path.dirname( -f)
    processor _ __.path.join(this_dir, '../', 'trm', '{}.py'.f..(name))
    processor _ __.path.n_p_(processor)
    __ no. __.path.isfile(processor):
        raise IOError('The processor script does not exist: {}'.f..(processor))
    r_ processor