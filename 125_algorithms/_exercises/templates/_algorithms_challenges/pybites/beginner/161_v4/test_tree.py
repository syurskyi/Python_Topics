_______ os
____ tempfile _______ TemporaryDirectory

____ tree _______ count_dirs_and_files

TMP = '/tmp'


___ test_only_files
    w__ TemporaryDirectory(dir=TMP) __ dirname:
        ___ i __ r..(5):
            filename = f'{i}.txt'
            path = os.path.j..(dirname, filename)
            w__ open(path, 'w') __ f:
                f.write('hello')

        ... count_dirs_and_files(dirname) __ (0, 5)


___ test_only_dirs
    w__ TemporaryDirectory(dir=TMP) __ dirname:
        ___ i __ r..(5):
            os.makedirs(os.path.j..(dirname, s..(i)))

        ... count_dirs_and_files(dirname) __ (5, 0)


___ test_files_and_dirs
    w__ TemporaryDirectory(dir=TMP) __ dirname:
        ___ i __ r..(10):
            __ i % 2 __ 0:
                target_dir = os.path.j..(dirname, s..(i))
                os.makedirs(target_dir)
                ___ j __ r..(5):
                    filename = f'{j}.txt'
                    path = os.path.j..(target_dir, filename)
                    w__ open(path, 'w') __ f:
                        f.write('hello')

        ... count_dirs_and_files(dirname) __ (5, 25)