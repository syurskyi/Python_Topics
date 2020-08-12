# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartCollect_v1.2/smartCollect/src/paths.py
______ glob
______ os
______ re

___ get_file_elements(filename):
    file_elements _ re.split('\\.([\\d|#|%\\dd]*).([a-z]*)', filename)
    basename, file_sequence, ext, _ _ file_elements
    __ no. file_sequence:
        r_ ValueError('No file_sequence found in {}'.f..(filename))
    r_ (basename, file_sequence, ext)


___ get_files_list(filepath):
    basedir _ os.path.dirname(filepath)
    filename _ os.path.basename(filepath)
    files_list _ []
    ___
        basename, file_sequence, ext _ get_file_elements(filename)
        pattern _ '{}.{}.{}'.f..(basename, '*' * len(file_sequence), ext)
        pattern _ os.path.join(basedir, pattern)
        files_list _ [ os.path.join(basedir, os.path.basename(file_)) for file_ __ glob.glob(pattern) ]
    _____ ValueError:
        files_list.append(filepath)

    r_ sorted(files_list)


___ get_frame_ranges(filepath):
    files_list _ get_files_list(filepath)
    __ no. files_list:
        r_ (0, 0)
    _, frame_in, _ _ get_file_elements(files_list[0])
    _, frame_out, _ _ get_file_elements(files_list[-1])
    r_ (int(frame_in), int(frame_out))


___ scan_for_nukescripts(path, ignore):
    nukescripts _ []
    __ no. ignore:
        ignore _ ''
    ignore_list _ [ ignore_file.strip() for ignore_file __ ignore.split(',') __ ignore_file ]
    for root, dirs, files __ os.walk(path):
        for name __ files:
            __ os.path.splitext(name)[1] __ '.nk':
                ignore_file_ _ 0
                for ignore_file __ ignore_list:
                    __ ignore_file __ name:
                        ignore_file_ +_ 1

                __ no. ignore_file_:
                    nukescripts.append(os.path.join(root, name))

    r_ nukescripts