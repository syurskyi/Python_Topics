_______ __
____ tempfile _______ TemporaryDirectory

____ tree _______ count_dirs_and_files

TMP = '/tmp'


___ test_only_files
    w__ TemporaryDirectory(dir=TMP) __ dirname:
        ___ i __ r..(5
            filename = f'{i}.txt'
            p.. = __.p...j..(dirname, filename)
            w__ o.. p.., 'w') __ f:
                f.w.. 'hello')

        ... count_dirs_and_files(dirname) __ (0, 5)


___ test_only_dirs
    w__ TemporaryDirectory(dir=TMP) __ dirname:
        ___ i __ r..(5
            __.makedirs(__.p...j..(dirname, s..(i)))

        ... count_dirs_and_files(dirname) __ (5, 0)


___ test_files_and_dirs
    w__ TemporaryDirectory(dir=TMP) __ dirname:
        ___ i __ r..(10
            __ i % 2 __ 0:
                target_dir = __.p...j..(dirname, s..(i
                __.makedirs(target_dir)
                ___ j __ r..(5
                    filename = f'{j}.txt'
                    p.. = __.p...j..(target_dir, filename)
                    w__ o.. p.., 'w') __ f:
                        f.w.. 'hello')

        ... count_dirs_and_files(dirname) __ (5, 25)