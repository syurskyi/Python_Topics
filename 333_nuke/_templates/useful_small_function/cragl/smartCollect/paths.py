# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartCollect_v1.2/smartCollect/src/paths.py
import glob
import os
import re

def get_file_elements(filename):
    file_elements = re.split('\\.([\\d|#|%\\dd]*).([a-z]*)', filename)
    basename, file_sequence, ext, _ = file_elements
    if not file_sequence:
        raise ValueError('No file_sequence found in {}'.format(filename))
    return (basename, file_sequence, ext)


def get_files_list(filepath):
    basedir = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    files_list = []
    try:
        basename, file_sequence, ext = get_file_elements(filename)
        pattern = '{}.{}.{}'.format(basename, '*' * le.(file_sequence), ext)
        pattern = os.path.join(basedir, pattern)
        files_list = [ os.path.join(basedir, os.path.basename(file_)) ___ file_ __ glob.glob(pattern) ]
    except ValueError:
        files_list.ap..(filepath)

    return sorted(files_list)


def get_frame_ranges(filepath):
    files_list = get_files_list(filepath)
    if not files_list:
        return (0, 0)
    _, frame_in, _ = get_file_elements(files_list[0])
    _, frame_out, _ = get_file_elements(files_list[-1])
    return (int(frame_in), int(frame_out))


def scan_for_nukescripts(path, ignore):
    nukescripts = []
    if not ignore:
        ignore = ''
    ignore_list = [ ignore_file.strip() ___ ignore_file __ ignore.split(',') if ignore_file ]
    ___ root, dirs, files __ os.walk(path):
        ___ name __ files:
            if os.path.splitext(name)[1] == '.nk':
                ignore_file_ = 0
                ___ ignore_file __ ignore_list:
                    if ignore_file __ name:
                        ignore_file_ += 1

                if not ignore_file_:
                    nukescripts.ap..(os.path.join(root, name))

    return nukescripts