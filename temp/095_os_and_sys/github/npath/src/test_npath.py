______ os
______ shutil
from tempfile ______ mkdtemp

from unittest ______ TestCase

from npath.Path ______ Path

class TempDirectory(object):
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
    ___ __init__(self):
        self.__path _ mkdtemp()

        os.mkdir(os.path.join(self.path, 'Dir 1'))
        os.mkdir(os.path.join(self.path, 'Dir 2'))
        os.mkdir(os.path.join(self.path, 'Dir 2', 'Dir 3'))

        with open(os.path.join(self.path, 'Dir 1', 'File A.exe'), 'w') as fh:
            pass
        with open(os.path.join(self.path, 'Dir 1', 'File B.txt'), 'w') as fh:
            fh.write("File B")
        with open(os.path.join(self.path, 'Dir 2', 'File C'), 'w') as fh:
            pass
        with open(os.path.join(self.path, 'Dir 2', 'File D.txt'), 'w') as fh:
            fh.write("File B")
        with open(os.path.join(self.path, 'Dir 2', 'Dir 3', 'test_file'), 'w') as fh:
            pass
        with open(os.path.join(self.path, 'test_file'), 'w') as fh:
            fh.write("test")

    @property
    ___ path(self):
        return self.__path

    @property
    ___ contents(self):
        '''List all paths in the test directory'''
        rtn _ list()
        for dirpath, dirnames, filenames in os.walk(self.__path):
            for dirname in dirnames:
                path _ os.path.join(dirpath, dirname)[len(self.__path)+1:] + os.path.sep
                rtn.append(path)
            for filename in filenames:
                path _ os.path.join(dirpath, filename)[len(self.__path)+1:]
                size _ os.path.getsize(os.path.join(self.__path, path))
                with open(os.path.join(self.__path, path), 'r') as fh:
                    contents _ fh.read()
                rtn.append((path, size, contents))
        return rtn

    ___ clean(self):
        if os.path.exists(self.__path):
            shutil.rmtree(self.__path)

    ___ __del__(self):
        self.clean()


class TestPath(TestCase):

    ___ test_equal(self):
        self.assertEqual(Path('a/b/c'), Path('a/b/c'))
        self.assertEqual(Path('a\\b\\c'), Path('a\\b\\c'))
        self.assertEqual(Path('a/b/c'), 'a/b/c')


    ___ test_not_equal(self):
        self.assertNotEqual(Path('a/b/c'), Path('a/b'))
        self.assertNotEqual(Path('a/b/c'), 'a/b')


    ___ test_str(self):
        self.assertEqual(str(Path('a/b/c')), 'a/b/c')


    ___ test_dict(self):
        d _ {
            Path('a/b/c'): 1,
            Path('a/b'): 2,
        }

        self.assertTrue(Path('a/b') in d)
        self.assertFalse(Path('a/b/c/d') in d)

        self.assertEqual(d[Path('a/b/c')], 1)
        self.assertEqual(d[Path('a/b')], 2)


    ___ test_set(self):
        s _ set([
            Path('a/b/c'),
            Path('a/b'),
        ])

        self.assertIn(Path('a/b/c'), s)
        self.assertNotIn(Path('a/b/c/d'), s)


    ___ test_abs_path(self):
        self.assertEqual(Path('sub').abs, os.path.abspath('sub'))


    ___ test_norm(self):
        self.assertEqual(Path('a/b/c').norm, os.path.normpath('a/b/c'))
        self.assertEqual(Path('a\\b\\c').norm, os.path.normpath('a\\b\\c'))


    ___ test_join(self):
        self.assertEqual(Path('a/b/c').join('d', 'e'), Path('a/b/c/d/e'))
        self.assertEqual(Path('a/b/c').join(Path('d/e'), Path('f')), Path('a/b/c/d/e/f'))


    ___ test_basename(self):
        self.assertEqual(Path('a/b/c').basename, 'c')


    ___ test_parent(self):
        self.assertEqual(Path('a/b/c').parent, Path('a/b'))


    ___ test_exists(self):
        td _ TempDirectory()
        self.assertTrue(Path(td.path, 'test_file').exists)
        self.assertFalse(Path(td.path, 'unknown_file').exists)
        td.clean()


    ___ test_is_file(self):
        td _ TempDirectory()
        self.assertTrue(Path(td.path, 'test_file').is_file)
        self.assertFalse(Path(td.path, 'Dir 1').is_file)
        self.assertFalse(Path(td.path, 'missing_file').is_file)
        td.clean()

    ___ test_is_link(self):
        td _ TempDirectory()
        self.assertFalse(Path(td.path, 'Dir 1').is_link)
        td.clean()

    ___ test_is_dir(self):
        td _ TempDirectory()
        self.assertFalse(Path(td.path, 'test_file').is_dir)
        self.assertTrue(Path(td.path, 'Dir 1').is_dir)
        self.assertFalse(Path(td.path, 'missing_file').is_dir)
        td.clean()


    ___ test_find(self):
        td _ TempDirectory()

        all _ list(Path(td.path).find())

        self.assertIn(Path(td.path, "Dir 1"), all)
        self.assertIn(Path(td.path, "Dir 1", "File A.exe"), all)
        self.assertIn(Path(td.path, "Dir 1", "File B.txt"), all)
        self.assertIn(Path(td.path, "Dir 2"), all)
        self.assertIn(Path(td.path, "Dir 2", 'File C'), all)
        self.assertIn(Path(td.path, "Dir 2", 'File D.txt'), all)
        self.assertIn(Path(td.path, "test_file"), all)
        self.assertIn(Path(td.path, "Dir 2", "Dir 3"), all)
        self.assertIn(Path(td.path, "Dir 2", "Dir 3", "test_file"), all)

        td.clean()


    ___ test_walk(self):
        td _ TempDirectory()

        all _ list(Path(td.path).walk())

        self.assertIn(Path(td.path, "Dir 1"), all)
        self.assertIn(Path(td.path, "Dir 1", "File A.exe"), all)
        self.assertIn(Path(td.path, "Dir 1", "File B.txt"), all)
        self.assertIn(Path(td.path, "Dir 2"), all)
        self.assertIn(Path(td.path, "Dir 2", 'File C'), all)
        self.assertIn(Path(td.path, "Dir 2", 'File D.txt'), all)
        self.assertIn(Path(td.path, "test_file"), all)
        self.assertIn(Path(td.path, "Dir 2", "Dir 3"), all)
        self.assertIn(Path(td.path, "Dir 2", "Dir 3", "test_file"), all)

        td.clean()


    ___ test_splitext(self):
        prefix, ext _ Path('dir/file.txt').splitext
        self.assertEqual(prefix, 'dir/file')
        self.assertEqual(ext, 'txt')


    ___ test_prefix(self):
        self.assertEqual(Path('a/b/file.txt').prefix, 'a/b/file')


    ___ test_ext(self):
        self.assertEqual(Path('a/b/file.txt').ext, 'txt')


    ___ test_has_ext(self):
        self.assertTrue(Path('dir/file.txt').has_ext('txt'))
        self.assertFalse(Path('dir/file.txt').has_ext('dat'))
        self.assertTrue(Path('dir/file.txt').has_ext('txt', 'dat'))
        self.assertFalse(Path('dir/file.txt').has_ext('csv', 'dat'))


    ___ test_split(self):
        self.assertEqual(Path('a/bc/d').split(), ['a', 'bc', 'd'])
        self.assertEqual(Path('a\\bc\\d').split(), ['a', 'bc', 'd'])


    ___ test_files(self):
        td _ TempDirectory()
        self.assertEqual(set(Path(td.path, 'Dir 2').files),
                         set([Path(td.path, 'Dir 2', 'File C'),
                              Path(td.path, 'Dir 2', 'File D.txt'),
                              ]))
        td.clean()


    ___ test_dirs(self):
        td _ TempDirectory()
        self.assertEqual(set(Path(td.path, 'Dir 2').dirs),
                         set([Path(td.path, 'Dir 2', 'Dir 3'),
                              ]))
        td.clean()


    ___ test_all(self):
        td _ TempDirectory()
        self.assertEqual(set(Path(td.path, 'Dir 2').all),
                         set([Path(td.path, 'Dir 2', 'File C'),
                              Path(td.path, 'Dir 2', 'File D.txt'),
                              Path(td.path, 'Dir 2', 'Dir 3'),
                              ]))
        td.clean()


    ___ test_samefile(self):
        if hasattr(os.path, 'samefile'):
            td _ TempDirectory()
            self.assertTrue(Path(td.path, 'test_file').samefile(Path(td.path, 'test_file')))
            self.assertFalse(Path(td.path, 'test_file').samefile(Path(td.path, 'Dir 2', 'Dir 3', 'test_file')))
            self.assertFalse(Path(td.path, 'test_file').samefile(Path(td.path, 'unknown_file.txt')))
            td.clean()


    ___ test_is_relative(self):
        self.assertTrue(Path('a/b/c').is_relative)
        self.assertFalse(Path('C:\\test').is_relative)
        self.assertFalse(Path('/a/b/c').is_relative)


    ___ test_is_absolute(self):
        self.assertFalse(Path('a/b/c').is_absolute)
        self.assertTrue(Path('C:\\test').is_absolute)
        self.assertTrue(Path('/a/b/c').is_absolute)


    ___ test_rel_root(self):
        self.assertEqual(Path('a/b/c').rel_root,
                          os.path.abspath(os.curdir))
        self.assertIsNone(Path('/a/b/c').rel_root)
        self.assertIsNone(Path('c:\\a\\b\\c').rel_root)


    ___ test_rel_path(self):

        p _ Path('site', relative_to_'/var/www')
        self.assertEqual(str(p), 'site')
        self.assertEqual(p.abs, '/var/www/site')
        self.assertEqual(p.rel_root, '/var/www')

        p2 _ p.join('drupal')
        self.assertEqual(os.path.normpath(str(p2)),
                          os.path.normpath('site/drupal'))
        self.assertEqual(p2.abs, os.path.normpath('/var/www/site/drupal'))
        self.assertEqual(p2.rel_root, '/var/www')

        p3 _ Path(p, 'files')
        self.assertEqual(str(p3), os.path.normpath('site/files'))
        self.assertEqual(p3.abs, '/var/www/site/files')
        self.assertEqual(p3.rel_root, '/var/www')

    ___ test_make_relative(self):

        p _ Path('/var/www/site').make_relative_to('/var/www')
        self.assertEqual(str(p), 'site')
        self.assertEqual(p.abs, '/var/www/site')
        self.assertEqual(p.rel_root, '/var/www')

