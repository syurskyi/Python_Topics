# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartRender_v3.0/smartRender/src/helper.py
______ hashlib
______ json
______ multiprocessing
______ __
______ random
______ ___
______ subprocess
______ time
______ urllib
______ xml.etree.ElementTree as ET
______ collections
______ pl..
______ datetime
______ errno
______ ?
______ ?
__ ?.NUKE_VERSION_MAJOR < 11:
    ____ PySide ______ QtGui as ?W..
    ____ PySide ______ QtCore
____
    ____ ? ______ ?W..
    ____ ? ______ QtCore
______ templates

___ load_icons(*args):
    this_dir = __.path.join(__.path.dirname(__file__))
    dir_icon = __.path.join(this_dir, '../', 'icons')
    dir_icon = __.path.normpath(dir_icon)
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
    jobs_xml = get_job_xml()
    __ jobs_xml __ '':
        r_
    jobs_tree = ET.parse(jobs_xml)
    jobs_root = jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').f_a_('job'):
        ___ setting __ job.f_a_('setting'):
            __ setting.get('name') __ 'status':
                __ setting.text __ 'waiting':
                    r_ job.get('id')


___ get_all_write_nodes_data(*args):
    write_data = {}
    all_write_nodes = [ node ___ node __ ?.allNodes('Write') __ node['disable'].getValue() __ 0.0 ]
    ___ write __ all_write_nodes:
        write_data[write.name()] = write['file'].getValue()

    r_ write_data


___ get_smart_render_private_root(*args):
    root = __.path.join(__.path.expanduser('~'), '.cragl', 'smartRender')
    __ no. __.path.isdir(root):
        ___
            __.makedirs(root)
        ______
            write_log('unable to create settings root dir')

    r_ root


___ get_smart_render_public_root(*args):
    root = __.path.join(__.path.expanduser('~'), 'cragl', 'smartRender')
    __ no. __.path.isdir(root):
        ___
            __.makedirs(root)
        ______
            write_log('unable to create open dir')

    r_ root


___ get_installed_root_dir(*args):
    this_dir = __.path.join(__.path.dirname(__file__))
    root = __.path.join(this_dir, '../', '../')
    r_ __.path.normpath(root)


___ get_public_cache_folder():
    cache_dir = __.path.join(get_smart_render_public_root(), 'cache')
    __ no. __.path.isdir(cache_dir):
        ___
            __.makedirs(cache_dir)
        ______
            msg = 'Unable to create cache directory at {}'.format(cache_dir)
            write_log(msg)

    r_ cache_dir


___ get_tmp_folder():
    tmp_dir = __.path.join(get_smart_render_public_root(), 'tmp')
    __ no. __.path.isdir(tmp_dir):
        ___
            __.makedirs(tmp_dir)
        ______
            msg = 'Unable to create tmp directory at {}'.format(tmp_dir)
            write_log(msg)

    r_ tmp_dir


___ get_smartRender_backup_dir(*args):
    backup_dir = __.path.join(get_smart_render_public_root(), 'backups')
    __ no. __.path.isdir(backup_dir):
        ___
            __.makedirs(backup_dir)
        ______
            write_log('unable to create backup dir')

    r_ backup_dir


___ get_smartrender_log_dir(*args):
    logs_dir = __.path.join(get_smart_render_public_root(), 'logs')
    __ no. __.path.isdir(logs_dir):
        ___
            __.makedirs(logs_dir)
        ______
            write_log('unable to create logs dir')

    r_ logs_dir


___ get_sounds_dir(*args):
    this_dir = __.path.dirname(__file__)
    sounds_dir = __.path.join(this_dir, '../', 'sounds')
    sounds_dir = __.path.normpath(sounds_dir)
    __ no. __.path.isdir(sounds_dir):
        ___
            __.makedirs(sounds_dir)
        ______
            write_log('unable to create sounds dir in {}.'.format(sounds_dir))

    r_ sounds_dir


___ get_tooltips_file(*args):
    this_dir = __.path.dirname(__file__)
    tooltips = __.path.join(this_dir, '../', 'data', 'tooltips.json')
    r_ __.path.normpath(tooltips)


___ update_job_log(job_id, processdata, time = str(int(time.time())), *args):
    jobs_xml = get_job_xml()
    __ jobs_xml __ '':
        r_
    jobs_tree = ET.parse(jobs_xml)
    jobs_root = jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').f_a_('job'):
        __ job.get('id') __ job_id:
            process = job.find('process')
            p = ET.SubElement(process, 'data')
            p.set('time', str(time))
            p.set('status', str(processdata[0]))
            p.set('thread', str(processdata[1]))
            p.text = processdata[2]
            with open(jobs_xml, 'w') as xml:
                prettyprint(jobs_root)
                jobs_tree.write(xml, encoding='utf-8', xml_declaration=True)
            r_ True


___ check_xml_ok(xml, *args):
    settings_xml = __.path.join(get_smart_render_private_root(), 'settings.xml')
    ___
        with open(xml, 'r') as xml_file:
            ET.fromstring(xml_file.read())
        r_ True
    ______
        xml_name = __.path.basename(xml)
        m.. = 'The smartRender {} file seems to be broken. Do you want to reset it now?'.format(xml_name)
        write_log('smartRender {} file broken.'.format(xml_name))
        msg_box = ?W...QMessageBox(?W...QMessageBox.Warning, 'QMessageBox.warning()', m.., ?W...QMessageBox.NoButton)
        reset = msg_box.addButton('reset', ?W...QMessageBox.AcceptRole)
        style = 'QPushButton {background-color: rgba(51, 204, 255, 150);}'
        reset.setStyleSheet(style)
        reset.clearFocus()
        msg_box.addButton('Cancel', ?W...QMessageBox.RejectRole)
        __ msg_box.exec_() __ ?W...QMessageBox.AcceptRole:
            __ __.path.isfile(xml):
                __.remove(xml)
                __ xml __ settings_xml:
                    get_settings_xml()
                ____
                    jobs_xml = get_job_xml()
                    __ jobs_xml __ '':
                        r_ False
        ____
            r_ False


___ check_web_connection(*args):
    ___
        urllib.urlopen('http://www.cragl.com')
        r_ True
    ______
        r_ False


___ update_job_data(job_id, key, val, *args):
    jobs_xml = get_job_xml()
    __ jobs_xml __ '':
        r_
    jobs_tree = ET.parse(jobs_xml)
    jobs_root = jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').f_a_('job'):
        __ job.get('id') __ job_id:
            ___ setting __ job.f_a_('setting'):
                __ setting.get('name') __ key:
                    setting.text = val
                    with open(jobs_xml, 'w') as xml:
                        prettyprint(jobs_root)
                        jobs_tree.write(xml, encoding='utf-8', xml_declaration=True)


___ calculate_process_precentage(job_id, frame, *args):
    jobs_xml = get_job_xml()
    __ jobs_xml __ '':
        r_
    jobs_tree = ET.parse(jobs_xml)
    jobs_root = jobs_tree.getroot()
    count_frames_done = 0
    ___ job __ jobs_root.find('jobs').f_a_('job'):
        __ job.get('id') __ job_id:
            ___ data __ job.find('process').f_a_('data'):
                __ data.get('status') __ '400':
                    count_frames_done += 1

            count_frames_to_process = int(job.find('frames').get('count'))
            done_precentage = int(100.0 / count_frames_to_process * count_frames_done)
            __ done_precentage > 100:
                done_precentage = 100
            ___ setting __ job.f_a_('setting'):
                __ setting.get('name') __ 'progress':
                    setting.text = str(done_precentage)
                __ setting.get('name') __ 'status':
                    tmp_status = setting.text
                    __ done_precentage __ 0:
                        setting.text = 'waiting'
                    __ done_precentage > 0:
                        setting.text = 'rendering'
                    __ str(done_precentage) __ '100':
                        setting.text = 'finished'
                    __ tmp_status __ 'paused':
                        setting.text = 'paused'

            ___ f __ job.find('frames').f_a_('frame'):
                __ f.text __ str(frame):
                    job.find('frames').remove(f)

            with open(jobs_xml, 'w') as xml:
                prettyprint(jobs_root)
                jobs_tree.write(xml, encoding='utf-8', xml_declaration=True)
            r_ done_precentage


___ set_style_sheet(widget, *args):
    this_dir = __.path.join(__.path.dirname(__file__))
    styles_nuke = __.path.join(this_dir, '../', 'styles', 'nuke.qss')
    styles_nuke = __.path.normpath(styles_nuke)
    __ __.path.isfile(styles_nuke):
        with open(styles_nuke) as file_:
            widget.setStyleSheet(file_.read())


___ show_message_box(window, m.., *args):
    msg = ?W...QMessageBox()
    msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
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
            msg = 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.format(url)
            show_message_box(N.., msg)

    r_


___ get_job_id_by_script_orig(script_orig, *args):
    ___
        jobs_xml = get_job_xml()
        __ jobs_xml __ '':
            r_ ''
        jobs_tree = ET.parse(jobs_xml)
        jobs_root = jobs_tree.getroot()
    except Exception as e:
        r_ ''

    jobs = []
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
        latest = jobs[0]
        ___ job __ jobs:
            __ job.split('_')[0] > latest.split('_')[0]:
                latest = job

        r_ latest


___ get_job_data(job_id, *args):
    job_data = {}
    frames_to_process = []
    ___
        jobs_xml = get_job_xml()
        __ jobs_xml __ '':
            r_ {}
        jobs_tree = ET.parse(jobs_xml)
        jobs_root = jobs_tree.getroot()
    except Exception as e:
        r_ {}

    ___ job __ jobs_root.find('jobs').f_a_('job'):
        __ job.get('id') __ job_id:
            job_data['job_id'] = job_id
            ___ setting __ job.f_a_('setting'):
                job_data[setting.get('name')] = setting.text

            ___ frame __ job.find('frames').f_a_('frame'):
                frames_to_process.ap..(int(frame.text))

            job_data['frames_to_process'] = frames_to_process
            number_errors = 0
            ___ data __ job.find('process').f_a_('data'):
                __ data.get('status') __ '100':
                    number_errors += 1

            job_data['number_errors'] = number_errors

    r_ job_data


___ get_all_jobs_data(filter, *args):
    jobs = collections.OrderedDict()
    ___
        jobs_xml = get_job_xml()
        __ jobs_xml __ '':
            r_ {}
        jobs_tree = ET.parse(jobs_xml)
        jobs_root = jobs_tree.getroot()
    except Exception as e:
        r_ {}

    ___ job __ jobs_root.find('jobs').f_a_('job'):
        job_id = job.get('id')
        jobs[job_id] = get_job_data(job_id)
        __ filter __ 'waiting' and jobs[job_id]['status'] != 'waiting':
            del jobs[job_id]
            continue
        __ filter __ 'waiting' and jobs[job_id]['status'] != 'waiting':
            del jobs[job_id]
            continue
        ____ filter __ 'paused' and jobs[job_id]['status'] != 'paused':
            del jobs[job_id]
            continue
        ____ filter __ 'cancelled' and jobs[job_id]['status'] != 'cancelled':
            del jobs[job_id]
            continue
        ____ filter __ 'error' and jobs[job_id]['status'] != 'error':
            del jobs[job_id]
            continue
        ____ filter __ 'finished' and jobs[job_id]['status'] != 'finished':
            del jobs[job_id]
            continue

    r_ jobs


___ get_log_file(*args):
    connect_dir = __.path.join(__.path.expanduser('~'), '.cragl', 'connect')
    __ no. __.path.isdir(connect_dir):
        __.makedirs(connect_dir)
    log_file = __.path.join(connect_dir, 'connectlog.txt')
    __ no. __.path.isfile(log_file):
        with open(log_file, 'w') as lf:
            log_template = 'connect log\n{}\n'.format('-' * 50)
            lf.write(log_template)
    r_ log_file


___ get_time_formated():
    r_ time.strftime('%d.%m.%Y %H:%M:%S', time.localtime())


___ write_log(text, tool = 'rn'):
    with open(get_log_file(), 'a') as file_:
        log_time_format = '%d.%m.%Y %H:%M:%S'
        log_time = time.strftime(log_time_format, time.localtime())
        file_.write('{}: {} {}\n'.format(log_time, tool, text))


___ write_render_log(text, *args):
    log = __.path.join(get_smart_render_private_root(), 'log.txt')
    __ no. __.path.isfile(log):
        with open(log, 'w') as lf:
            lf.write('')
    ___
        with open(log, 'a') as lf:
            lf.write('{}: {}\n'.format(get_time_formated()), text)
        r_ True
    except IOError:
        r_ False


___ write_terminal_cmd(job_id, text, file = 'input', *args):
    log_name = '{}_terminal_{}.log'.format(job_id, file)
    log = __.path.join(get_smartrender_log_dir(), log_name)
    __ no. __.path.isfile(log):
        with open(log, 'w') as file_:
            file_.write('')
    ___
        with open(log, 'a') as file_:
            file_.write('{}\n'.format(text))
        r_ True
    except IOError:
        r_ False


___ get_job_xml(*args):
    job_xml = __.path.join(get_smart_render_private_root(), 'jobs.xml')
    __ no. __.path.isfile(job_xml):
        ___
            with open(job_xml, 'w') as job_template:
                template = templates.JOB
                job_template.write(template.strip())
                write_log("smartRender job log doesn't exist. created template at: {}".format(job_xml))
        ______
            write_log('Failed writing smartRender job log template to: {}'.format(job_xml))

    r_ job_xml


___ insert_as_read_node(job_details, write = N.., *args):
    __ write:
        read = ?.createNode('Read')
        read['file'].sV..(write['file'].getValue())
        read['first'].sV..(int(?.root()['first_frame'].getValue()))
        read['origfirst'].sV..(int(?.root()['first_frame'].getValue()))
        read['last'].sV..(int(?.root()['last_frame'].getValue()))
        read['origlast'].sV..(int(?.root()['last_frame'].getValue()))
        read['on_error'].sV..('nearest frame')
        read.selectOnly()
        read.setXYpos(int(write['xpos'].getValue()), int(write['ypos'].getValue()) + 70)
        ?.zoom(1.0, (write.xpos(), write.ypos()))
        ?.connect_selected_to_viewer(0)
    ____
        read = ?.createNode('Read')
        read['file'].sV..(job_details['render_path'])
        read['first'].sV..(int(job_details['render_start']))
        read['origfirst'].sV..(int(job_details['render_start']))
        read['last'].sV..(int(job_details['render_end']))
        read['origlast'].sV..(int(job_details['render_end']))
        read['on_error'].sV..('nearest frame')
        read.selectOnly()
        ?.zoom(1.0, (read.xpos(), read.ypos()))
        ?.connect_selected_to_viewer(0)


___ get_job_details(job_id, *args):
    job_details = {}
    jobs_xml = get_job_xml()
    jobs_tree = ET.parse(jobs_xml)
    jobs_root = jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').f_a_('job'):
        __ job.get('id') __ job_id:
            ___ setting __ job.f_a_('setting'):
                job_details[setting.get('name')] = setting.text

    r_ job_details


___ force_create_render_dir(*args):
    file_name = ?.filename(?.thisNode())
    dir_name = __.path.dirname(file_name)
    os_dir = ?.callbacks.filenameFilter(dir_name)
    ___
        __.makedirs(os_dir)
    except OSError as e:
        __ e.errno != errno.EEXIST:
            raise


___ load_terminal_log(job_id, mode, *args):
    xml_name = '{}_terminal_{}.log'.format(job_id, mode)
    terminal_file = __.path.join(get_smartrender_log_dir(), xml_name)
    __ no. __.path.isfile(terminal_file):
        r_ ''
    ___
        with open(terminal_file, 'rt') as file:
            r_ file.read()
    except Exception as e:
        r_ 'Error reading the terminal input file. {}'.format(e)


___ load_job_log_data(job_id, filter, file_output = False, *args):
    job_data = ''
    jobs_xml = get_job_xml()
    __ jobs_xml __ '':
        r_
    jobs_tree = ET.parse(jobs_xml)
    jobs_root = jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').f_a_('job'):
        __ job.get('id') __ job_id:
            ___ data __ job.find('process').f_a_('data'):
                code = ''
                __ data.get('status') __ '100':
                    __ filter != 'job: all' and filter != 'job: error':
                        continue
                    __ file_output:
                        code = '[error]'
                    ____
                        code = "[<span style='color:#993333'>error</span>"
                ____ data.get('status') __ '300':
                    __ filter != 'job: all' and filter != 'job: info':
                        continue
                    __ file_output:
                        code = '[info]'
                    ____
                        code = '[info'
                ____ data.get('status') __ '400':
                    __ filter != 'job: all' and filter != 'job: done':
                        continue
                    __ file_output:
                        code = '[done]'
                    ____
                        code = "[<span style='color:#339933'>done</span>"
                data_time = int(data.get('time'))
                time = datetime.datetime.fromtimestamp(data_time).strftime('%d/%m/%Y %H:%M:%S')
                __ file_output:
                    job_data += '{time} {code} {text}\n'.format(time=time, code=code, text=data.text)
                ____
                    job_data += '<tr><td>{time}</td><td> {code}</td><td>] {text}</td></tr>'.format(time=time, code=code, text=data.text)
                    job_data = '<table>{}</table>'.format(job_data)

    r_ job_data


___ open_in_explorer(path, parent = N.., *args):
    __ no. __.path.isdir(path):
        msg = "Unable to open directory. The path doesn't exist:\n\n{}".format(path)
        show_message_box(parent, msg)
    __ pl...system() __ 'Windows':
        __.startfile(path)
    ____ pl...system() __ 'Darwin':
        subprocess.P..(['open', path])
    ____
        subprocess.P..(['xdg-open', path])


___ reset_file(which, window, *args):
    __ which __ 'jobs':
        m.. = 'Do you want to flush the jobs file?'
        proccess_button_text = 'flush jobs'
    ____
        m.. = 'Do you want to reset the smartRender settings? Please note: all render presets will be removed, too.'
        proccess_button_text = 'reset settings'
    process_button_color = '70, 10, 10, 255'
    cancel_button_text = 'cancel'
    reset = ask_dialog(m.., proccess_button_text, process_button_color, cancel_button_text)
    __ reset:
        __ which __ 'jobs':
            jobs_file = get_job_xml()
            ___
                __ __.path.isfile(jobs_file):
                    __.remove(jobs_file)
                    msg = 'Successfully flushed jobs file.'
                    show_message_box(window, msg)
            except Exception as e:
                write_log('Cannot remove jobs file. {}'.format(e))

        ____ which __ 'settings':
            settings_file = get_settings_xml()
            ___
                __ __.path.isfile(settings_file):
                    __.remove(settings_file)
                    msg = 'Successfully reset the smartRender settings.'
                    show_message_box(window, msg)
            except Exception as e:
                write_log('Cannot reset settings file. {}'.format(e))


___ get_settings_xml(*args):
    settings_xml = __.path.join(get_smart_render_private_root(), 'settings.xml')
    __ no. __.path.isfile(settings_xml):
        desktop_cache = __.path.join(__.path.expanduser('~'), 'Desktop/cache')
        ___
            with open(settings_xml, 'w') as render_template:
                template = templates.SETTINGS.format(public_cache=get_public_cache_folder(), desktop_cache=desktop_cache)
                render_template.write(template.strip())
                write_log("smartRender settings doesn't exist. created template at: {}".format(settings_xml))
        ______
            write_log('Failed writing smartRender settings template at: {}'.format(settings_xml))

    check_settings_xml_values_exist()
    r_ settings_xml


___ check_settings_xml_values_exist():
    settings = {'current_tab': '1',
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

    settings_current = {'range': 'global',
     'custom_range': '',
     'step': '1',
     'overwrite': 'True',
     'size': 'full',
     'thread_count': str(int(get_cpu_count() / 2))}
    ___ key, value __ settings_current.items():
        check_xml_value_exists_current('setting', 'name', key, value)


___ load_sounds(*args):
    sounds = []
    sounds_dir = get_sounds_dir()
    __ no. __.path.isdir(sounds_dir):
        r_
    ___ file_ __ __.listdir(sounds_dir):
        __ __.path.splitext(file_)[1] __ ('.wav', '.WAV'):
            sounds.ap..(file_)

    r_ sounds


___ load_presets(*args):
    presets_list = {}
    settings_xml = get_settings_xml()
    settingstree = ET.parse(settings_xml)
    settingsroot = settingstree.getroot()
    ___ presets __ settingsroot.find('presets'):
        preset_name = presets.get('name')
        preset = {}
        ___ setting __ presets.f_a_('setting'):
            __ setting.get('name') __ 'range':
                preset['range'] = setting.text
            ____ setting.get('name') __ 'custom_range':
                preset['custom_range'] = setting.text
            ____ setting.get('name') __ 'step':
                preset['step'] = setting.text
            ____ setting.get('name') __ 'overwrite':
                preset['overwrite'] = setting.text
            ____ setting.get('name') __ 'size':
                preset['size'] = setting.text
                __ setting.get('width'):
                    preset['width'] = setting.get('width')
                ____
                    preset['width'] = ''
                __ setting.get('height'):
                    preset['height'] = setting.get('height')
                ____
                    preset['height'] = ''
                preset['aspectratio'] = setting.get('aspectratio')
            ____ setting.get('name') __ 'description':
                preset['description'] = setting.text
            ____ setting.get('name') __ 'thread_count':
                preset['thread_count'] = setting.text
                __ no. preset['thread_count']:
                    preset['thread_count'] = ?.env['numCPUs'] / 2

        presets_list[preset_name] = preset

    r_ presets_list


___ play_sound(sound, *args):
    sound_file = __.path.join(get_sounds_dir(), sound)
    __ __.path.isfile(sound_file):
        ?W...QSound.play(sound_file)


___ load_settings(*args):
    settings_xml = get_settings_xml()
    settings = {}
    cache_paths = []
    __ check_xml_ok(settings_xml):
        settingstree = ET.parse(settings_xml)
        settingsroot = settingstree.getroot()
        ___ setting __ settingsroot.find('settings').f_a_('setting'):
            settings[setting.get('name')] = setting.text

        ___ path __ settingsroot.find('cache').f_a_('path'):
            cache_paths.ap..({'mode': path.get('mode'),
             'path': path.text})

        settings['cache'] = cache_paths
    r_ settings


___ get_caches_by_mode(mode, *args):
    r_ [ cache['path'] ___ cache __ load_settings()['cache'] __ cache['mode'] __ mode ]


___ add_cache_path(mode, path, *args):
    settings_xml = get_settings_xml()
    __ settings_xml __ '':
        r_
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    new_cache_path = ET.SubElement(settings_root.find('cache'), 'path')
    new_cache_path.text = path
    new_cache_path.set('mode', mode)
    ET.dump(new_cache_path)
    with open(settings_xml, 'w') as xml:
        prettyprint(settings_root)
        settings_tree.write(xml, encoding='utf-8', xml_declaration=True)


___ check_xml_value_exists(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = __.path.join(get_smart_render_private_root(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = False
    item_found = 0
    ___ child __ root.find(parent).f_a_(section):
        __ child.get(key1) __ value1:
            item_found += 1
            __ debug:
                print 'smartRender | settings exists: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2)
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


___ check_xml_value_exists_cache(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = __.path.join(get_smart_render_private_root(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = False
    item_found = 0
    ___ child __ root.find(parent).f_a_(section):
        __ child.get(key1) __ value1:
            __ value2 __ child.text:
                item_found += 1
                __ debug:
                    print 'smartRender | settings exists: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2)
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


___ check_xml_value_exists_current(section, key1, value1, text, key2 = '', value2 = ''):
    settings_xml = __.path.join(get_smart_render_private_root(), 'settings.xml')
    tree = ET.parse(settings_xml)
    root = tree.getroot()
    item_found = 0
    current_found = False
    ___ child __ root.find('presets').f_a_('preset'):
        __ child.get('name') __ 'current':
            current_found = True
        ____
            current_found = False
        ___ setting __ child.f_a_('setting'):
            __ setting.get(key1) __ value1:
                item_found += 1
                r_

    __ current_found:
        __ item_found __ 0:
            elem = ET.Element(section)
            elem.set(key1, value1)
            __ key2 != '':
                elem.set(key2, value2)
            elem.text = text
            ___ child __ root.find('presets').f_a_('preset'):
                __ child.get('name') __ 'current':
                    child.ap..(elem)
                    with open(settings_xml, 'w'):
                        prettyprint(root)
                        tree.write(settings_xml, encoding='utf-8', xml_declaration=True)
                    write_log('settings xml added: {}|{}|{}|{}|{}|{}'.format(section, key1, value1, text, key2, value2))


___ get_cpu_count(*args):
    ___
        r_ multiprocessing.cpu_count()
    except Exception as e:
        __ hasattr(__, 'sysconf'):
            __ __.sysconf_names.has_key('SC_NPROCESSORS_ONLN'):
                ncpus = __.sysconf('SC_NPROCESSORS_ONLN')
                __ i..(ncpus, int) and ncpus > 0:
                    r_ ncpus
            ____
                r_ int(__.popen2('sysctl -n hw.ncpu')[1].read())
        __ __.environ.has_key('NUMBER_OF_PROCESSORS'):
            ncpus = int(__.environ['NUMBER_OF_PROCESSORS'])
            __ ncpus > 0:
                r_ ncpus
        r_ 1


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


___ delete_cache_path(path, *args):
    settings_xml = get_settings_xml()
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    ___ path_element __ settings_root.find('cache').f_a_('path'):
        __ path_element.text __ path:
            settings_root.find('cache').remove(path_element)
            with open(settings_xml, 'w') as xml:
                prettyprint(settings_root)
                settings_tree.write(xml, encoding='utf-8', xml_declaration=True)


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


___ create_unique_job_id(*args):
    current_time = str(int(time.time()))
    rand_number = str(random.random())
    id = hashlib.md5('{}{}'.format(current_time, rand_number)).hexdigest()[:8]
    r_ str('{}_{}'.format(current_time, id))


___ get_all_views(range_ = 10):
    ___
        views = []
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
    tooltips_file = get_tooltips_file()
    __ no. __.path.isfile(tooltips_file):
        r_
    with open(tooltips_file) as json_file:
        ttdata = json.load(json_file)
    ___ widget __ parent.findChildren(QtCore.QObject):
        ___ tooltip __ ttdata[key]:
            __ tooltip['tt'] __ widget.property('tt'):
                widget.setToolTip('<strong>{}</strong><br />{}'.format(tooltip['ttt'], tooltip['ttc']))


___ get_explorer_name(*args):
    __ ___.pl.. __ 'darwin':
        r_ 'finder'
    ____
        r_ 'explorer'


___ get_recent_nukescripts(*args):
    file_recent_files = __.path.join(__.path.expanduser('~'), '.nuke', 'recent_files')
    recent_files = []
    __ __.path.isfile(file_recent_files):
        with open(file_recent_files, 'r') as rf:
            ___ line __ rf:
                file_ = line.replace('\n', '')
                file_ = file_.replace('"', '')
                recent_files.ap..(file_)

            r_ recent_files
    ____
        r_ []


___ open_renderpath_in_explorer(label, renderpath, srw, *args):
    __ renderpath __ '':
        label = label.split(' (')[0]
        msg = "The file path for '{}' hasn't been set up, yet.".format(label)
        show_message_box(srw, msg)
        r_
    ___
        open_in_explorer(__.path.dirname(renderpath), parent=srw)
    except Exception as e:
        show_message_box(srw, 'An error occurred: {}'.format(e))
        r_


___ get_processor(name):
    this_dir = __.path.dirname(__file__)
    processor = __.path.join(this_dir, '../', 'trm', '{}.py'.format(name))
    processor = __.path.normpath(processor)
    __ no. __.path.isfile(processor):
        raise IOError('The processor script does not exist: {}'.format(processor))
    r_ processor