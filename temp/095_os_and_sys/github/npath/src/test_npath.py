______ __
______ shutil
____ tempfile ______ mkdtemp

____ unittest ______ TestCase

____ npath.Path ______ Path

c_ TempDirectory(object):
    '''
    A directory structure to test within

    (path)
      |-- Dir 1
      |    |-- File A.exe       (blank)
      |    `-- File B.txt       (contents: "File B")
      |-- Dir 2
      |    |-- File C           (blank)
      |    |-- File D.txt       (contents: "File B")
      |    `-- Dir 3
      |         `-- test_file   (blank)
      `-- test_file             (contents: "test")

    '''
    ___  -
        __path _ mkdtemp()

        __.mkdir(__.path.j..(path, 'Dir 1'))
        __.mkdir(__.path.j..(path, 'Dir 2'))
        __.mkdir(__.path.j..(path, 'Dir 2', 'Dir 3'))

        with o..(__.path.j..(path, 'Dir 1', 'File A.exe'), 'w') __ fh:
            p..
        with o..(__.path.j..(path, 'Dir 1', 'File B.txt'), 'w') __ fh:
            fh.write("File B")
        with o..(__.path.j..(path, 'Dir 2', 'File C'), 'w') __ fh:
            p..
        with o..(__.path.j..(path, 'Dir 2', 'File D.txt'), 'w') __ fh:
            fh.write("File B")
        with o..(__.path.j..(path, 'Dir 2', 'Dir 3', 'test_file'), 'w') __ fh:
            p..
        with o..(__.path.j..(path, 'test_file'), 'w') __ fh:
            fh.write("test")

    ??
    ___ path
        r_ __path

    ??
    ___ contents
        '''List all paths in the test directory'''
        rtn _ list()
        ___ dirpath, dirnames, filenames __ __.walk(__path):
            ___ dirname __ dirnames:
                path _ __.path.j..(dirpath, dirname)[le.(__path)+1:] + __.path.sep
                rtn.ap..(path)
            ___ filename __ filenames:
                path _ __.path.j..(dirpath, filename)[le.(__path)+1:]
                size _ __.path.getsize(__.path.j..(__path, path))
                with o..(__.path.j..(__path, path), 'r') __ fh:
                    contents _ fh.read()
                rtn.ap..((path, size, contents))
        r_ rtn

    ___ clean
        __ __.path.exists(__path):
            shutil.rmtree(__path)

    ___ __del__
        clean()


c_ TestPath(TestCase):

    ___ test_equal
        assertEqual(Path('a/b/c'), Path('a/b/c'))
        assertEqual(Path('a\\b\\c'), Path('a\\b\\c'))
        assertEqual(Path('a/b/c'), 'a/b/c')


    ___ test_not_equal
        assertNotEqual(Path('a/b/c'), Path('a/b'))
        assertNotEqual(Path('a/b/c'), 'a/b')


    ___ test_str
        assertEqual(str(Path('a/b/c')), 'a/b/c')


    ___ test_dict
        d _ {
            Path('a/b/c'): 1,
            Path('a/b'): 2,
        }

        assertTrue(Path('a/b') __ d)
        assertFalse(Path('a/b/c/d') __ d)

        assertEqual(d[Path('a/b/c')], 1)
        assertEqual(d[Path('a/b')], 2)


    ___ test_set
        s _ set([
            Path('a/b/c'),
            Path('a/b'),
        ])

        assertIn(Path('a/b/c'), s)
        assertNotIn(Path('a/b/c/d'), s)


    ___ test_abs_path
        assertEqual(Path('sub').abs, __.path.abspath('sub'))


    ___ test_norm
        assertEqual(Path('a/b/c').norm, __.path.normpath('a/b/c'))
        assertEqual(Path('a\\b\\c').norm, __.path.normpath('a\\b\\c'))


    ___ test_join
        assertEqual(Path('a/b/c').j..('d', 'e'), Path('a/b/c/d/e'))
        assertEqual(Path('a/b/c').j..(Path('d/e'), Path('f')), Path('a/b/c/d/e/f'))


    ___ test_basename
        assertEqual(Path('a/b/c').basename, 'c')


    ___ test_parent
        assertEqual(Path('a/b/c').parent, Path('a/b'))


    ___ test_exists
        td _ TempDirectory()
        assertTrue(Path(td.path, 'test_file').exists)
        assertFalse(Path(td.path, 'unknown_file').exists)
        td.clean()


    ___ test_is_file
        td _ TempDirectory()
        assertTrue(Path(td.path, 'test_file').is_file)
        assertFalse(Path(td.path, 'Dir 1').is_file)
        assertFalse(Path(td.path, 'missing_file').is_file)
        td.clean()

    ___ test_is_link
        td _ TempDirectory()
        assertFalse(Path(td.path, 'Dir 1').is_link)
        td.clean()

    ___ test_is_dir
        td _ TempDirectory()
        assertFalse(Path(td.path, 'test_file').is_dir)
        assertTrue(Path(td.path, 'Dir 1').is_dir)
        assertFalse(Path(td.path, 'missing_file').is_dir)
        td.clean()


    ___ test_find
        td _ TempDirectory()

        all _ list(Path(td.path).find())

        assertIn(Path(td.path, "Dir 1"), all)
        assertIn(Path(td.path, "Dir 1", "File A.exe"), all)
        assertIn(Path(td.path, "Dir 1", "File B.txt"), all)
        assertIn(Path(td.path, "Dir 2"), all)
        assertIn(Path(td.path, "Dir 2", 'File C'), all)
        assertIn(Path(td.path, "Dir 2", 'File D.txt'), all)
        assertIn(Path(td.path, "test_file"), all)
        assertIn(Path(td.path, "Dir 2", "Dir 3"), all)
        assertIn(Path(td.path, "Dir 2", "Dir 3", "test_file"), all)

        td.clean()


    ___ test_walk
        td _ TempDirectory()

        all _ list(Path(td.path).walk())

        assertIn(Path(td.path, "Dir 1"), all)
        assertIn(Path(td.path, "Dir 1", "File A.exe"), all)
        assertIn(Path(td.path, "Dir 1", "File B.txt"), all)
        assertIn(Path(td.path, "Dir 2"), all)
        assertIn(Path(td.path, "Dir 2", 'File C'), all)
        assertIn(Path(td.path, "Dir 2", 'File D.txt'), all)
        assertIn(Path(td.path, "test_file"), all)
        assertIn(Path(td.path, "Dir 2", "Dir 3"), all)
        assertIn(Path(td.path, "Dir 2", "Dir 3", "test_file"), all)

        td.clean()


    ___ test_splitext
        prefix, ext _ Path('dir/file.txt').splitext
        assertEqual(prefix, 'dir/file')
        assertEqual(ext, 'txt')


    ___ test_prefix
        assertEqual(Path('a/b/file.txt').prefix, 'a/b/file')


    ___ test_ext
        assertEqual(Path('a/b/file.txt').ext, 'txt')


    ___ test_has_ext
        assertTrue(Path('dir/file.txt').has_ext('txt'))
        assertFalse(Path('dir/file.txt').has_ext('dat'))
        assertTrue(Path('dir/file.txt').has_ext('txt', 'dat'))
        assertFalse(Path('dir/file.txt').has_ext('csv', 'dat'))


    ___ test_split
        assertEqual(Path('a/bc/d').split(), ['a', 'bc', 'd'])
        assertEqual(Path('a\\bc\\d').split(), ['a', 'bc', 'd'])


    ___ test_files
        td _ TempDirectory()
        assertEqual(set(Path(td.path, 'Dir 2').files),
                         set([Path(td.path, 'Dir 2', 'File C'),
                              Path(td.path, 'Dir 2', 'File D.txt'),
                              ]))
        td.clean()


    ___ test_dirs
        td _ TempDirectory()
        assertEqual(set(Path(td.path, 'Dir 2').dirs),
                         set([Path(td.path, 'Dir 2', 'Dir 3'),
                              ]))
        td.clean()


    ___ test_all
        td _ TempDirectory()
        assertEqual(set(Path(td.path, 'Dir 2').all),
                         set([Path(td.path, 'Dir 2', 'File C'),
                              Path(td.path, 'Dir 2', 'File D.txt'),
                              Path(td.path, 'Dir 2', 'Dir 3'),
                              ]))
        td.clean()


    ___ test_samefile
        __ hasattr(__.path, 'samefile'):
            td _ TempDirectory()
            assertTrue(Path(td.path, 'test_file').samefile(Path(td.path, 'test_file')))
            assertFalse(Path(td.path, 'test_file').samefile(Path(td.path, 'Dir 2', 'Dir 3', 'test_file')))
            assertFalse(Path(td.path, 'test_file').samefile(Path(td.path, 'unknown_file.txt')))
            td.clean()


    ___ test_is_relative
        assertTrue(Path('a/b/c').is_relative)
        assertFalse(Path('C:\\test').is_relative)
        assertFalse(Path('/a/b/c').is_relative)


    ___ test_is_absolute
        assertFalse(Path('a/b/c').is_absolute)
        assertTrue(Path('C:\\test').is_absolute)
        assertTrue(Path('/a/b/c').is_absolute)


    ___ test_rel_root
        assertEqual(Path('a/b/c').rel_root,
                          __.path.abspath(__.curdir))
        assertIsNone(Path('/a/b/c').rel_root)
        assertIsNone(Path('c:\\a\\b\\c').rel_root)


    ___ test_rel_path

        p _ Path('site', relative_to_'/var/www')
        assertEqual(str(p), 'site')
        assertEqual(p.abs, '/var/www/site')
        assertEqual(p.rel_root, '/var/www')

        p2 _ p.j..('drupal')
        assertEqual(__.path.normpath(str(p2)),
                          __.path.normpath('site/drupal'))
        assertEqual(p2.abs, __.path.normpath('/var/www/site/drupal'))
        assertEqual(p2.rel_root, '/var/www')

        p3 _ Path(p, 'files')
        assertEqual(str(p3), __.path.normpath('site/files'))
        assertEqual(p3.abs, '/var/www/site/files')
        assertEqual(p3.rel_root, '/var/www')

    ___ test_make_relative

        p _ Path('/var/www/site').make_relative_to('/var/www')
        assertEqual(str(p), 'site')
        assertEqual(p.abs, '/var/www/site')
        assertEqual(p.rel_root, '/var/www')

