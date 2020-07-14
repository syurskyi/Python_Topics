# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartCollect_v1.2/smartCollect/src/paths.py
______ glob
______ __
______ re

___ get_file_elements(filename):
    file_elements _ re.s..('\\.([\\d|#|%\\dd]*).([a-z]*)', filename)
    b_n_, file_sequence, ext, _ _ file_elements
    __ no. file_sequence:
        raise ValueError('No file_sequence found in {}'.f..(filename))
    r_ (b_n_, file_sequence, ext)


___ get_files_list(filepath):
    basedir _ __.pa__.d_n_(filepath)
    filename _ __.pa__.b_n_(filepath)
    files_list _ # list
    ___
        b_n_, file_sequence, ext _ get_file_elements(filename)
        pattern _ '{}.{}.{}'.f..(b_n_, '*' * le.(file_sequence), ext)
        pattern _ __.pa__.j..(basedir, pattern)
        files_list _ [ __.pa__.j..(basedir, __.pa__.b_n_(file_)) ___ file_ __ glob.glob(pattern) ]
    ______ ValueError:
        files_list.ap..(filepath)

    r_ sorted(files_list)


___ get_frame_ranges(filepath):
    files_list _ get_files_list(filepath)
    __ no. files_list:
        r_ (0, 0)
    _, frame_in, _ _ get_file_elements(files_list[0])
    _, frame_out, _ _ get_file_elements(files_list[-1])
    r_ (__.(frame_in), __.(frame_out))


___ scan_for_nukescripts(pa__, ignore):
    ? _ # list
    __ no. ignore:
        ignore _ ''
    ignore_list _ [ ignore_file.strip() ___ ignore_file __ ignore.s..(',') __ ignore_file ]
    ___ root, dirs, files __ __.walk(pa__):
        ___ name __ files:
            __ __.pa__.s_t_(name)[1] __ '.nk':
                ignore_file_ _ 0
                ___ ignore_file __ ignore_list:
                    __ ignore_file __ name:
                        ignore_file_ +_ 1

                __ no. ignore_file_:
                    ?.ap..(__.pa__.j..(root, name))

    r_ ?