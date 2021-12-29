____ tree _______ count_dirs_and_files


___ test_only_files(tmp_path):
    ___ i __ r..(1, 6):
        path = tmp_path / f'{i}.txt'
        with open(path, 'w') as f:
            f.write('hello')
    ... count_dirs_and_files(tmp_path) __ (0, 5)


___ test_only_dirs(tmp_path):
    ___ i __ r..(5):
        (tmp_path / s..(i)).mkdir()
    ... count_dirs_and_files(tmp_path) __ (5, 0)


___ test_files_and_dirs(tmp_path):
    ___ i __ r..(10):
        __ i % 2 __ 0:
            target_dir = tmp_path / s..(i)
            target_dir.mkdir()
            ___ j __ r..(5):
                path = target_dir / f'{j}.txt'
                with open(path, 'w') as f:
                    f.write('hello')
    ... count_dirs_and_files(tmp_path) __ (5, 25)