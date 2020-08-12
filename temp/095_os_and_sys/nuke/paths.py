# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartCollect_v1.2/smartCollect/src/paths.py
______ glob
______ os
______ re

def get_file_elements(filename):
    file_elements _ re.split('\\.([\\d|#|%\\dd]*).([a-z]*)', filename)
    basename, file_sequence, ext, _ _ file_elements
    if not file_sequence:
        raise ValueError('No file_sequence found in {}'.format(filename))
    return (basename, file_sequence, ext)


def get_files_list(filepath):
    basedir _ os.path.dirname(filepath)
    filename _ os.path.basename(filepath)
    files_list _ []
    try:
        basename, file_sequence, ext _ get_file_elements(filename)
        pattern _ '{}.{}.{}'.format(basename, '*' * len(file_sequence), ext)
        pattern _ os.path.join(basedir, pattern)
        files_list _ [ os.path.join(basedir, os.path.basename(file_)) for file_ in glob.glob(pattern) ]
    except ValueError:
        files_list.append(filepath)

    return sorted(files_list)


def get_frame_ranges(filepath):
    files_list _ get_files_list(filepath)
    if not files_list:
        return (0, 0)
    _, frame_in, _ _ get_file_elements(files_list[0])
    _, frame_out, _ _ get_file_elements(files_list[-1])
    return (int(frame_in), int(frame_out))


def scan_for_nukescripts(path, ignore):
    nukescripts _ []
    if not ignore:
        ignore _ ''
    ignore_list _ [ ignore_file.strip() for ignore_file in ignore.split(',') if ignore_file ]
    for root, dirs, files in os.walk(path):
        for name in files:
            if os.path.splitext(name)[1] == '.nk':
                ignore_file_ _ 0
                for ignore_file in ignore_list:
                    if ignore_file in name:
                        ignore_file_ +_ 1

                if not ignore_file_:
                    nukescripts.append(os.path.join(root, name))

    return nukescripts