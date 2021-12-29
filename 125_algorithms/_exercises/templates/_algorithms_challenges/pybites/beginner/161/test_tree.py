from tree import count_dirs_and_files


___ test_only_files(tmp_path):
    for i in range(1, 6):
        path = tmp_path / f'{i}.txt'
        with open(path, 'w') as f:
            f.write('hello')
    assert count_dirs_and_files(tmp_path) == (0, 5)


___ test_only_dirs(tmp_path):
    for i in range(5):
        (tmp_path / str(i)).mkdir()
    assert count_dirs_and_files(tmp_path) == (5, 0)


___ test_files_and_dirs(tmp_path):
    for i in range(10):
        __ i % 2 == 0:
            target_dir = tmp_path / str(i)
            target_dir.mkdir()
            for j in range(5):
                path = target_dir / f'{j}.txt'
                with open(path, 'w') as f:
                    f.write('hello')
    assert count_dirs_and_files(tmp_path) == (5, 25)