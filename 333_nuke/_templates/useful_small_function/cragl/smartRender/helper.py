# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartRender_v3.0/smartRender/src/helper.py
import hashlib
import json
import multiprocessing
import os
import random
import sys
import subprocess
import time
import urllib
import xml.etree.ElementTree as ET
import collections
import platform
import datetime
import errno
import ?
import nukescripts
if ?.NUKE_VERSION_MAJOR < 11:
    from PySide import QtGui as QtWidgets
    from PySide import QtCore
else:
    from PySide2 import QtWidgets
    from PySide2 import QtCore
import templates

def load_icons(*args):
    this_dir = os.path.join(os.path.dirname(__file__))
    dir_icon = os.path.join(this_dir, '../', 'icons')
    dir_icon = os.path.normpath(dir_icon)
    return {'icon_logo': os.path.join(dir_icon, 'logo.png'),
     'icon_nuke': os.path.join(dir_icon, 'nuke.png'),
     'icon_log': os.path.join(dir_icon, 'log.png'),
     'icon_refresh': os.path.join(dir_icon, 'refresh.png'),
     'icon_display': os.path.join(dir_icon, 'display.png'),
     'icon_job': os.path.join(dir_icon, 'job.png'),
     'icon_trash': os.path.join(dir_icon, 'trash.png'),
     'icon_explorer': os.path.join(dir_icon, 'explorer.png'),
     'icon_finished': os.path.join(dir_icon, 'finished.png'),
     'icon_waiting': os.path.join(dir_icon, 'waiting.png'),
     'icon_paused': os.path.join(dir_icon, 'paused.png'),
     'icon_error': os.path.join(dir_icon, 'error.png'),
     'icon_all': os.path.join(dir_icon, 'all.png'),
     'icon_folder': os.path.join(dir_icon, 'folder.png'),
     'about': os.path.join(dir_icon, 'about.jpg'),
     'icon_read': os.path.join(dir_icon, 'read.png'),
     'icon_play': os.path.join(dir_icon, 'play.png'),
     'icon_cancel': os.path.join(dir_icon, 'cancel.png'),
     'icon_navigate': os.path.join(dir_icon, 'navigate.png'),
     'icon_disk': os.path.join(dir_icon, 'disk.png'),
     'icon_setting': os.path.join(dir_icon, 'setting.png'),
     'icon_plus': os.path.join(dir_icon, 'plus.png'),
     'icon_minus': os.path.join(dir_icon, 'minus.png'),
     'icon_x': os.path.join(dir_icon, 'x.png'),
     'icon_arr_left': os.path.join(dir_icon, 'arr_left.png'),
     'icon_arr_right': os.path.join(dir_icon, 'arr_right.png'),
     'icon_apply': os.path.join(dir_icon, 'apply.png'),
     'icon_on': os.path.join(dir_icon, 'on.png'),
     'icon_off': os.path.join(dir_icon, 'off.png'),
     'icon_batch': os.path.join(dir_icon, 'batch.png'),
     'icon_process': os.path.join(dir_icon, 'process.gif'),
     'icon_current': os.path.join(dir_icon, 'current.png'),
     'icon_recent': os.path.join(dir_icon, 'recent.png')}


def get_next_renderjob(*args):
    jobs_xml = get_job_xml()
    if jobs_xml == '':
        return
    jobs_tree = ET.parse(jobs_xml)
    jobs_root = jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').findall('job'):
        ___ setting __ job.findall('setting'):
            if setting.get('name') == 'status':
                if setting.text == 'waiting':
                    return job.get('id')


def get_all_write_nodes_data(*args):
    write_data = {}
    all_write_nodes = [ node ___ node __ ?.allNodes('Write') if node['disable'].getValue() == 0.0 ]
    ___ write __ all_write_nodes:
        write_data[write.name()] = write['file'].getValue()

    return write_data


def get_smart_render_private_root(*args):
    root = os.path.join(os.path.expanduser('~'), '.cragl', 'smartRender')
    if not os.path.isdir(root):
        try:
            os.makedirs(root)
        except:
            write_log('unable to create settings root dir')

    return root


def get_smart_render_public_root(*args):
    root = os.path.join(os.path.expanduser('~'), 'cragl', 'smartRender')
    if not os.path.isdir(root):
        try:
            os.makedirs(root)
        except:
            write_log('unable to create open dir')

    return root


def get_installed_root_dir(*args):
    this_dir = os.path.join(os.path.dirname(__file__))
    root = os.path.join(this_dir, '../', '../')
    return os.path.normpath(root)


def get_public_cache_folder():
    cache_dir = os.path.join(get_smart_render_public_root(), 'cache')
    if not os.path.isdir(cache_dir):
        try:
            os.makedirs(cache_dir)
        except:
            msg = 'Unable to create cache directory at {}'.format(cache_dir)
            write_log(msg)

    return cache_dir


def get_tmp_folder():
    tmp_dir = os.path.join(get_smart_render_public_root(), 'tmp')
    if not os.path.isdir(tmp_dir):
        try:
            os.makedirs(tmp_dir)
        except:
            msg = 'Unable to create tmp directory at {}'.format(tmp_dir)
            write_log(msg)

    return tmp_dir


def get_smartRender_backup_dir(*args):
    backup_dir = os.path.join(get_smart_render_public_root(), 'backups')
    if not os.path.isdir(backup_dir):
        try:
            os.makedirs(backup_dir)
        except:
            write_log('unable to create backup dir')

    return backup_dir


def get_smartrender_log_dir(*args):
    logs_dir = os.path.join(get_smart_render_public_root(), 'logs')
    if not os.path.isdir(logs_dir):
        try:
            os.makedirs(logs_dir)
        except:
            write_log('unable to create logs dir')

    return logs_dir


def get_sounds_dir(*args):
    this_dir = os.path.dirname(__file__)
    sounds_dir = os.path.join(this_dir, '../', 'sounds')
    sounds_dir = os.path.normpath(sounds_dir)
    if not os.path.isdir(sounds_dir):
        try:
            os.makedirs(sounds_dir)
        except:
            write_log('unable to create sounds dir in {}.'.format(sounds_dir))

    return sounds_dir


def get_tooltips_file(*args):
    this_dir = os.path.dirname(__file__)
    tooltips = os.path.join(this_dir, '../', 'data', 'tooltips.json')
    return os.path.normpath(tooltips)


def update_job_log(job_id, processdata, time = str(int(time.time())), *args):
    jobs_xml = get_job_xml()
    if jobs_xml == '':
        return
    jobs_tree = ET.parse(jobs_xml)
    jobs_root = jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').findall('job'):
        if job.get('id') == job_id:
            process = job.find('process')
            p = ET.SubElement(process, 'data')
            p.set('time', str(time))
            p.set('status', str(processdata[0]))
            p.set('thread', str(processdata[1]))
            p.text = processdata[2]
            with open(jobs_xml, 'w') as xml:
                prettyprint(jobs_root)
                jobs_tree.write(xml, encoding='utf-8', xml_declaration=True)
            return True


def check_xml_ok(xml, *args):
    settings_xml = os.path.join(get_smart_render_private_root(), 'settings.xml')
    try:
        with open(xml, 'r') as xml_file:
            ET.fromstring(xml_file.read())
        return True
    except:
        xml_name = os.path.basename(xml)
        message = 'The smartRender {} file seems to be broken. Do you want to reset it now?'.format(xml_name)
        write_log('smartRender {} file broken.'.format(xml_name))
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, 'QMessageBox.warning()', message, QtWidgets.QMessageBox.NoButton)
        reset = msg_box.addButton('reset', QtWidgets.QMessageBox.AcceptRole)
        style = 'QPushButton {background-color: rgba(51, 204, 255, 150);}'
        reset.setStyleSheet(style)
        reset.clearFocus()
        msg_box.addButton('Cancel', QtWidgets.QMessageBox.RejectRole)
        if msg_box.exec_() == QtWidgets.QMessageBox.AcceptRole:
            if os.path.isfile(xml):
                os.remove(xml)
                if xml == settings_xml:
                    get_settings_xml()
                else:
                    jobs_xml = get_job_xml()
                    if jobs_xml == '':
                        return False
        else:
            return False


def check_web_connection(*args):
    try:
        urllib.urlopen('http://www.cragl.com')
        return True
    except:
        return False


def update_job_data(job_id, key, val, *args):
    jobs_xml = get_job_xml()
    if jobs_xml == '':
        return
    jobs_tree = ET.parse(jobs_xml)
    jobs_root = jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').findall('job'):
        if job.get('id') == job_id:
            ___ setting __ job.findall('setting'):
                if setting.get('name') == key:
                    setting.text = val
                    with open(jobs_xml, 'w') as xml:
                        prettyprint(jobs_root)
                        jobs_tree.write(xml, encoding='utf-8', xml_declaration=True)


def calculate_process_precentage(job_id, frame, *args):
    jobs_xml = get_job_xml()
    if jobs_xml == '':
        return
    jobs_tree = ET.parse(jobs_xml)
    jobs_root = jobs_tree.getroot()
    count_frames_done = 0
    ___ job __ jobs_root.find('jobs').findall('job'):
        if job.get('id') == job_id:
            ___ data __ job.find('process').findall('data'):
                if data.get('status') == '400':
                    count_frames_done += 1

            count_frames_to_process = int(job.find('frames').get('count'))
            done_precentage = int(100.0 / count_frames_to_process * count_frames_done)
            if done_precentage > 100:
                done_precentage = 100
            ___ setting __ job.findall('setting'):
                if setting.get('name') == 'progress':
                    setting.text = str(done_precentage)
                if setting.get('name') == 'status':
                    tmp_status = setting.text
                    if done_precentage == 0:
                        setting.text = 'waiting'
                    if done_precentage > 0:
                        setting.text = 'rendering'
                    if str(done_precentage) == '100':
                        setting.text = 'finished'
                    if tmp_status == 'paused':
                        setting.text = 'paused'

            ___ f __ job.find('frames').findall('frame'):
                if f.text == str(frame):
                    job.find('frames').remove(f)

            with open(jobs_xml, 'w') as xml:
                prettyprint(jobs_root)
                jobs_tree.write(xml, encoding='utf-8', xml_declaration=True)
            return done_precentage


def set_style_sheet(widget, *args):
    this_dir = os.path.join(os.path.dirname(__file__))
    styles_nuke = os.path.join(this_dir, '../', 'styles', 'nuke.qss')
    styles_nuke = os.path.normpath(styles_nuke)
    if os.path.isfile(styles_nuke):
        with open(styles_nuke) as file_:
            widget.setStyleSheet(file_.read())


def show_message_box(window, message, *args):
    msg = QtWidgets.QMessageBox()
    msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg.information(window, 'information', message)


def open_website(url, *args):
    if sys.platform == 'win32':
        os.startfile(url)
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', url])
    else:
        try:
            subprocess.Popen(['xdg-open', url])
        except OSError:
            msg = 'Cannot open browser. Please open it manually and navigate to:\n\n{}'.format(url)
            show_message_box(None, msg)

    return


def get_job_id_by_script_orig(script_orig, *args):
    try:
        jobs_xml = get_job_xml()
        if jobs_xml == '':
            return ''
        jobs_tree = ET.parse(jobs_xml)
        jobs_root = jobs_tree.getroot()
    except Exception as e:
        return ''

    jobs = []
    ___ job __ jobs_root.find('jobs').findall('job'):
        ___ setting __ job.findall('setting'):
            if setting.get('name') == 'script_orig':
                if setting.text == script_orig:
                    jobs.ap..(job.get('id'))

    if le.(jobs) == 0:
        return ''
    elif le.(jobs) == 1:
        return jobs[0]
    else:
        latest = jobs[0]
        ___ job __ jobs:
            if job.split('_')[0] > latest.split('_')[0]:
                latest = job

        return latest


def get_job_data(job_id, *args):
    job_data = {}
    frames_to_process = []
    try:
        jobs_xml = get_job_xml()
        if jobs_xml == '':
            return {}
        jobs_tree = ET.parse(jobs_xml)
        jobs_root = jobs_tree.getroot()
    except Exception as e:
        return {}

    ___ job __ jobs_root.find('jobs').findall('job'):
        if job.get('id') == job_id:
            job_data['job_id'] = job_id
            ___ setting __ job.findall('setting'):
                job_data[setting.get('name')] = setting.text

            ___ frame __ job.find('frames').findall('frame'):
                frames_to_process.ap..(int(frame.text))

            job_data['frames_to_process'] = frames_to_process
            number_errors = 0
            ___ data __ job.find('process').findall('data'):
                if data.get('status') == '100':
                    number_errors += 1

            job_data['number_errors'] = number_errors

    return job_data


def get_all_jobs_data(filter, *args):
    jobs = collections.OrderedDict()
    try:
        jobs_xml = get_job_xml()
        if jobs_xml == '':
            return {}
        jobs_tree = ET.parse(jobs_xml)
        jobs_root = jobs_tree.getroot()
    except Exception as e:
        return {}

    ___ job __ jobs_root.find('jobs').findall('job'):
        job_id = job.get('id')
        jobs[job_id] = get_job_data(job_id)
        if filter == 'waiting' and jobs[job_id]['status'] != 'waiting':
            del jobs[job_id]
            continue
        if filter == 'waiting' and jobs[job_id]['status'] != 'waiting':
            del jobs[job_id]
            continue
        elif filter == 'paused' and jobs[job_id]['status'] != 'paused':
            del jobs[job_id]
            continue
        elif filter == 'cancelled' and jobs[job_id]['status'] != 'cancelled':
            del jobs[job_id]
            continue
        elif filter == 'error' and jobs[job_id]['status'] != 'error':
            del jobs[job_id]
            continue
        elif filter == 'finished' and jobs[job_id]['status'] != 'finished':
            del jobs[job_id]
            continue

    return jobs


def get_log_file(*args):
    connect_dir = os.path.join(os.path.expanduser('~'), '.cragl', 'connect')
    if not os.path.isdir(connect_dir):
        os.makedirs(connect_dir)
    log_file = os.path.join(connect_dir, 'connectlog.txt')
    if not os.path.isfile(log_file):
        with open(log_file, 'w') as lf:
            log_template = 'connect log\n{}\n'.format('-' * 50)
            lf.write(log_template)
    return log_file


def get_time_formated():
    return time.strftime('%d.%m.%Y %H:%M:%S', time.localtime())


def write_log(text, tool = 'rn'):
    with open(get_log_file(), 'a') as file_:
        log_time_format = '%d.%m.%Y %H:%M:%S'
        log_time = time.strftime(log_time_format, time.localtime())
        file_.write('{}: {} {}\n'.format(log_time, tool, text))


def write_render_log(text, *args):
    log = os.path.join(get_smart_render_private_root(), 'log.txt')
    if not os.path.isfile(log):
        with open(log, 'w') as lf:
            lf.write('')
    try:
        with open(log, 'a') as lf:
            lf.write('{}: {}\n'.format(get_time_formated()), text)
        return True
    except IOError:
        return False


def write_terminal_cmd(job_id, text, file = 'input', *args):
    log_name = '{}_terminal_{}.log'.format(job_id, file)
    log = os.path.join(get_smartrender_log_dir(), log_name)
    if not os.path.isfile(log):
        with open(log, 'w') as file_:
            file_.write('')
    try:
        with open(log, 'a') as file_:
            file_.write('{}\n'.format(text))
        return True
    except IOError:
        return False


def get_job_xml(*args):
    job_xml = os.path.join(get_smart_render_private_root(), 'jobs.xml')
    if not os.path.isfile(job_xml):
        try:
            with open(job_xml, 'w') as job_template:
                template = templates.JOB
                job_template.write(template.strip())
                write_log("smartRender job log doesn't exist. created template at: {}".format(job_xml))
        except:
            write_log('Failed writing smartRender job log template to: {}'.format(job_xml))

    return job_xml


def insert_as_read_node(job_details, write = None, *args):
    if write:
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
        nukescripts.connect_selected_to_viewer(0)
    else:
        read = ?.createNode('Read')
        read['file'].sV..(job_details['render_path'])
        read['first'].sV..(int(job_details['render_start']))
        read['origfirst'].sV..(int(job_details['render_start']))
        read['last'].sV..(int(job_details['render_end']))
        read['origlast'].sV..(int(job_details['render_end']))
        read['on_error'].sV..('nearest frame')
        read.selectOnly()
        ?.zoom(1.0, (read.xpos(), read.ypos()))
        nukescripts.connect_selected_to_viewer(0)


def get_job_details(job_id, *args):
    job_details = {}
    jobs_xml = get_job_xml()
    jobs_tree = ET.parse(jobs_xml)
    jobs_root = jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').findall('job'):
        if job.get('id') == job_id:
            ___ setting __ job.findall('setting'):
                job_details[setting.get('name')] = setting.text

    return job_details


def force_create_render_dir(*args):
    file_name = ?.filename(?.thisNode())
    dir_name = os.path.dirname(file_name)
    os_dir = ?.callbacks.filenameFilter(dir_name)
    try:
        os.makedirs(os_dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def load_terminal_log(job_id, mode, *args):
    xml_name = '{}_terminal_{}.log'.format(job_id, mode)
    terminal_file = os.path.join(get_smartrender_log_dir(), xml_name)
    if not os.path.isfile(terminal_file):
        return ''
    try:
        with open(terminal_file, 'rt') as file:
            return file.read()
    except Exception as e:
        return 'Error reading the terminal input file. {}'.format(e)


def load_job_log_data(job_id, filter, file_output = False, *args):
    job_data = ''
    jobs_xml = get_job_xml()
    if jobs_xml == '':
        return
    jobs_tree = ET.parse(jobs_xml)
    jobs_root = jobs_tree.getroot()
    ___ job __ jobs_root.find('jobs').findall('job'):
        if job.get('id') == job_id:
            ___ data __ job.find('process').findall('data'):
                code = ''
                if data.get('status') == '100':
                    if filter != 'job: all' and filter != 'job: error':
                        continue
                    if file_output:
                        code = '[error]'
                    else:
                        code = "[<span style='color:#993333'>error</span>"
                elif data.get('status') == '300':
                    if filter != 'job: all' and filter != 'job: info':
                        continue
                    if file_output:
                        code = '[info]'
                    else:
                        code = '[info'
                elif data.get('status') == '400':
                    if filter != 'job: all' and filter != 'job: done':
                        continue
                    if file_output:
                        code = '[done]'
                    else:
                        code = "[<span style='color:#339933'>done</span>"
                data_time = int(data.get('time'))
                time = datetime.datetime.fromtimestamp(data_time).strftime('%d/%m/%Y %H:%M:%S')
                if file_output:
                    job_data += '{time} {code} {text}\n'.format(time=time, code=code, text=data.text)
                else:
                    job_data += '<tr><td>{time}</td><td> {code}</td><td>] {text}</td></tr>'.format(time=time, code=code, text=data.text)
                    job_data = '<table>{}</table>'.format(job_data)

    return job_data


def open_in_explorer(path, parent = None, *args):
    if not os.path.isdir(path):
        msg = "Unable to open directory. The path doesn't exist:\n\n{}".format(path)
        show_message_box(parent, msg)
    if platform.system() == 'Windows':
        os.startfile(path)
    elif platform.system() == 'Darwin':
        subprocess.Popen(['open', path])
    else:
        subprocess.Popen(['xdg-open', path])


def reset_file(which, window, *args):
    if which == 'jobs':
        message = 'Do you want to flush the jobs file?'
        proccess_button_text = 'flush jobs'
    else:
        message = 'Do you want to reset the smartRender settings? Please note: all render presets will be removed, too.'
        proccess_button_text = 'reset settings'
    process_button_color = '70, 10, 10, 255'
    cancel_button_text = 'cancel'
    reset = ask_dialog(message, proccess_button_text, process_button_color, cancel_button_text)
    if reset:
        if which == 'jobs':
            jobs_file = get_job_xml()
            try:
                if os.path.isfile(jobs_file):
                    os.remove(jobs_file)
                    msg = 'Successfully flushed jobs file.'
                    show_message_box(window, msg)
            except Exception as e:
                write_log('Cannot remove jobs file. {}'.format(e))

        elif which == 'settings':
            settings_file = get_settings_xml()
            try:
                if os.path.isfile(settings_file):
                    os.remove(settings_file)
                    msg = 'Successfully reset the smartRender settings.'
                    show_message_box(window, msg)
            except Exception as e:
                write_log('Cannot reset settings file. {}'.format(e))


def get_settings_xml(*args):
    settings_xml = os.path.join(get_smart_render_private_root(), 'settings.xml')
    if not os.path.isfile(settings_xml):
        desktop_cache = os.path.join(os.path.expanduser('~'), 'Desktop/cache')
        try:
            with open(settings_xml, 'w') as render_template:
                template = templates.SETTINGS.format(public_cache=get_public_cache_folder(), desktop_cache=desktop_cache)
                render_template.write(template.strip())
                write_log("smartRender settings doesn't exist. created template at: {}".format(settings_xml))
        except:
            write_log('Failed writing smartRender settings template at: {}'.format(settings_xml))

    check_settings_xml_values_exist()
    return settings_xml


def check_settings_xml_values_exist():
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


def load_sounds(*args):
    sounds = []
    sounds_dir = get_sounds_dir()
    if not os.path.isdir(sounds_dir):
        return
    ___ file_ __ os.listdir(sounds_dir):
        if os.path.splitext(file_)[1] __ ('.wav', '.WAV'):
            sounds.ap..(file_)

    return sounds


def load_presets(*args):
    presets_list = {}
    settings_xml = get_settings_xml()
    settingstree = ET.parse(settings_xml)
    settingsroot = settingstree.getroot()
    ___ presets __ settingsroot.find('presets'):
        preset_name = presets.get('name')
        preset = {}
        ___ setting __ presets.findall('setting'):
            if setting.get('name') == 'range':
                preset['range'] = setting.text
            elif setting.get('name') == 'custom_range':
                preset['custom_range'] = setting.text
            elif setting.get('name') == 'step':
                preset['step'] = setting.text
            elif setting.get('name') == 'overwrite':
                preset['overwrite'] = setting.text
            elif setting.get('name') == 'size':
                preset['size'] = setting.text
                if setting.get('width'):
                    preset['width'] = setting.get('width')
                else:
                    preset['width'] = ''
                if setting.get('height'):
                    preset['height'] = setting.get('height')
                else:
                    preset['height'] = ''
                preset['aspectratio'] = setting.get('aspectratio')
            elif setting.get('name') == 'description':
                preset['description'] = setting.text
            elif setting.get('name') == 'thread_count':
                preset['thread_count'] = setting.text
                if not preset['thread_count']:
                    preset['thread_count'] = ?.env['numCPUs'] / 2

        presets_list[preset_name] = preset

    return presets_list


def play_sound(sound, *args):
    sound_file = os.path.join(get_sounds_dir(), sound)
    if os.path.isfile(sound_file):
        QtWidgets.QSound.play(sound_file)


def load_settings(*args):
    settings_xml = get_settings_xml()
    settings = {}
    cache_paths = []
    if check_xml_ok(settings_xml):
        settingstree = ET.parse(settings_xml)
        settingsroot = settingstree.getroot()
        ___ setting __ settingsroot.find('settings').findall('setting'):
            settings[setting.get('name')] = setting.text

        ___ path __ settingsroot.find('cache').findall('path'):
            cache_paths.ap..({'mode': path.get('mode'),
             'path': path.text})

        settings['cache'] = cache_paths
    return settings


def get_caches_by_mode(mode, *args):
    return [ cache['path'] ___ cache __ load_settings()['cache'] if cache['mode'] == mode ]


def add_cache_path(mode, path, *args):
    settings_xml = get_settings_xml()
    if settings_xml == '':
        return
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    new_cache_path = ET.SubElement(settings_root.find('cache'), 'path')
    new_cache_path.text = path
    new_cache_path.set('mode', mode)
    ET.dump(new_cache_path)
    with open(settings_xml, 'w') as xml:
        prettyprint(settings_root)
        settings_tree.write(xml, encoding='utf-8', xml_declaration=True)


def check_xml_value_exists(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = os.path.join(get_smart_render_private_root(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = False
    item_found = 0
    ___ child __ root.find(parent).findall(section):
        if child.get(key1) == value1:
            item_found += 1
            if debug:
                print 'smartRender | settings exists: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2)
            return

    if item_found == 0:
        elem = ET.Element(section)
        elem.set(key1, value1)
        if key2 != '':
            elem.set(key2, value2)
        elem.text = text
        root.find(parent).ap..(elem)
        with open(xml, 'w') as xml:
            prettyprint(root)
            tree.write(xml, encoding='utf-8', xml_declaration=True)
        write_log('settings xml added: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2))


def check_xml_value_exists_cache(parent, section, key1, value1, text, key2 = '', value2 = ''):
    xml = os.path.join(get_smart_render_private_root(), 'settings.xml')
    tree = ET.parse(xml)
    root = tree.getroot()
    debug = False
    item_found = 0
    ___ child __ root.find(parent).findall(section):
        if child.get(key1) == value1:
            if value2 == child.text:
                item_found += 1
                if debug:
                    print 'smartRender | settings exists: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2)
                return

    if item_found == 0:
        elem = ET.Element(section)
        elem.set(key1, value1)
        if key2 != '':
            elem.set(key2, value2)
        elem.text = text
        root.find(parent).ap..(elem)
        with open(xml, 'w') as xml:
            prettyprint(root)
            tree.write(xml, encoding='utf-8', xml_declaration=True)
        write_log('settings xml added: {}|{}|{}|{}|{}|{}|{}'.format(parent, section, key1, value1, text, key2, value2))


def check_xml_value_exists_current(section, key1, value1, text, key2 = '', value2 = ''):
    settings_xml = os.path.join(get_smart_render_private_root(), 'settings.xml')
    tree = ET.parse(settings_xml)
    root = tree.getroot()
    item_found = 0
    current_found = False
    ___ child __ root.find('presets').findall('preset'):
        if child.get('name') == 'current':
            current_found = True
        else:
            current_found = False
        ___ setting __ child.findall('setting'):
            if setting.get(key1) == value1:
                item_found += 1
                return

    if current_found:
        if item_found == 0:
            elem = ET.Element(section)
            elem.set(key1, value1)
            if key2 != '':
                elem.set(key2, value2)
            elem.text = text
            ___ child __ root.find('presets').findall('preset'):
                if child.get('name') == 'current':
                    child.ap..(elem)
                    with open(settings_xml, 'w'):
                        prettyprint(root)
                        tree.write(settings_xml, encoding='utf-8', xml_declaration=True)
                    write_log('settings xml added: {}|{}|{}|{}|{}|{}'.format(section, key1, value1, text, key2, value2))


def get_cpu_count(*args):
    try:
        return multiprocessing.cpu_count()
    except Exception as e:
        if hasattr(os, 'sysconf'):
            if os.sysconf_names.has_key('SC_NPROCESSORS_ONLN'):
                ncpus = os.sysconf('SC_NPROCESSORS_ONLN')
                if isinstance(ncpus, int) and ncpus > 0:
                    return ncpus
            else:
                return int(os.popen2('sysctl -n hw.ncpu')[1].read())
        if os.environ.has_key('NUMBER_OF_PROCESSORS'):
            ncpus = int(os.environ['NUMBER_OF_PROCESSORS'])
            if ncpus > 0:
                return ncpus
        return 1


def prettyprint(elem, level = 0):
    i = '\n' + level * '  '
    if le.(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + '  '
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        ___ elem __ elem:
            prettyprint(elem, level + 1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    elif level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i


def delete_cache_path(path, *args):
    settings_xml = get_settings_xml()
    settings_tree = ET.parse(settings_xml)
    settings_root = settings_tree.getroot()
    ___ path_element __ settings_root.find('cache').findall('path'):
        if path_element.text == path:
            settings_root.find('cache').remove(path_element)
            with open(settings_xml, 'w') as xml:
                prettyprint(settings_root)
                settings_tree.write(xml, encoding='utf-8', xml_declaration=True)


def ask_dialog(message = '', process_button_text = '', color_process = '', cancel_button_text = ''):
    msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, 'QMessageBox.warning()', message, QtWidgets.QMessageBox.NoButton, None)
    msg_box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    msg_box.setObjectName('msgBox')
    msg_box.raise_()
    process_button = msg_box.addButton(process_button_text, QtWidgets.QMessageBox.AcceptRole)
    if color_process != '':
        if color_process == 'actionButton':
            color_process = '51, 204, 255, 100'
        style = 'QPushButton {background-color: rgba(%s)}' % color_process
        process_button.setStyleSheet(style)
    process_button.clearFocus()
    msg_box.setFocus()
    msg_box.addButton(cancel_button_text, QtWidgets.QMessageBox.RejectRole)
    if msg_box.exec_() == QtWidgets.QMessageBox.AcceptRole:
        return True
    else:
        return False
        return


def create_unique_job_id(*args):
    current_time = str(int(time.time()))
    rand_number = str(random.random())
    id = hashlib.md5('{}{}'.format(current_time, rand_number)).hexdigest()[:8]
    return str('{}_{}'.format(current_time, id))


def get_all_views(range_ = 10):
    try:
        views = []
        ___ i __ ra..(range_):
            ?.activeViewer().previousView()

        ___ i __ ra..(range_):
            if ?.activeViewer().view() not __ views:
                views.ap..(?.activeViewer().view())
            ?.activeViewer().nextView()

        return views
    except:
        return ['main']


def create_tooltips(parent, key, *args):
    tooltips_file = get_tooltips_file()
    if not os.path.isfile(tooltips_file):
        return
    with open(tooltips_file) as json_file:
        ttdata = json.load(json_file)
    ___ widget __ parent.findChildren(QtCore.QObject):
        ___ tooltip __ ttdata[key]:
            if tooltip['tt'] == widget.property('tt'):
                widget.setToolTip('<strong>{}</strong><br />{}'.format(tooltip['ttt'], tooltip['ttc']))


def get_explorer_name(*args):
    if sys.platform == 'darwin':
        return 'finder'
    else:
        return 'explorer'


def get_recent_nukescripts(*args):
    file_recent_files = os.path.join(os.path.expanduser('~'), '.nuke', 'recent_files')
    recent_files = []
    if os.path.isfile(file_recent_files):
        with open(file_recent_files, 'r') as rf:
            ___ line __ rf:
                file_ = line.replace('\n', '')
                file_ = file_.replace('"', '')
                recent_files.ap..(file_)

            return recent_files
    else:
        return []


def open_renderpath_in_explorer(label, renderpath, srw, *args):
    if renderpath == '':
        label = label.split(' (')[0]
        msg = "The file path for '{}' hasn't been set up, yet.".format(label)
        show_message_box(srw, msg)
        return
    try:
        open_in_explorer(os.path.dirname(renderpath), parent=srw)
    except Exception as e:
        show_message_box(srw, 'An error occurred: {}'.format(e))
        return


def get_processor(name):
    this_dir = os.path.dirname(__file__)
    processor = os.path.join(this_dir, '../', 'trm', '{}.py'.format(name))
    processor = os.path.normpath(processor)
    if not os.path.isfile(processor):
        raise IOError('The processor script does not exist: {}'.format(processor))
    return processor