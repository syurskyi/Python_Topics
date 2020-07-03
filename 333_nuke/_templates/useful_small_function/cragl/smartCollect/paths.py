# Embedded file name: /Volumes/Secomba/cragl/Boxcryptor/Dropbox/crypto/_GLOBALS/NUKE/python/cragl/PREPAREFORRELEASE/smartCollect_v1.2/smartCollect/src/paths.py
______ glob
______ __
______ re

___ get_file_elements(filename):
    file_elements = re.split('\\.([\\d|#|%\\dd]*).([a-z]*)', filename)
    basename, file_sequence, ext, _ = file_elements
    __ no. file_sequence:
        raise ValueError('No file_sequence found in {}'.f..(filename))
    r_ (basename, file_sequence, ext)


___ get_files_list(filepath):
    basedir = __.path.dirname(filepath)
    filename = __.path.basename(filepath)
    files_list = []
    ___
        basename, file_sequence, ext = get_file_elements(filename)
        pattern = '{}.{}.{}'.f..(basename, '*' * le.(file_sequence), ext)
        pattern = __.path.join(basedir, pattern)
        files_list = [ __.path.join(basedir, __.path.basename(file_)) ___ file_ __ glob.glob(pattern) ]
    except ValueError:
        files_list.ap..(filepath)

    r_ sorted(files_list)


___ get_frame_ranges(filepath):
    files_list = get_files_list(filepath)
    __ no. files_list:
        r_ (0, 0)
    _, frame_in, _ = get_file_elements(files_list[0])
    _, frame_out, _ = get_file_elements(files_list[-1])
    r_ (int(frame_in), int(frame_out))


___ scan_for_nukescripts(path, ignore):
    ? = []
    __ no. ignore:
        ignore = ''
    ignore_list = [ ignore_file.strip() ___ ignore_file __ ignore.split(',') __ ignore_file ]
    ___ root, dirs, files __ __.walk(path):
        ___ name __ files:
            __ __.path.splitext(name)[1] __ '.nk':
                ignore_file_ = 0
                ___ ignore_file __ ignore_list:
                    __ ignore_file __ name:
                        ignore_file_ += 1

                __ no. ignore_file_:
                    ?.ap..(__.path.join(root, name))

    r_ ?