import os
import shutil
from tempfile import mkdtemp

from unittest import TestCase

from npath.Path import Path

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
    def __init__(self):
        self.__path = mkdtemp()

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
    def path(self):
        return self.__path

    @property
    def contents(self):
        '''List all paths in the test directory'''
        rtn = list()
        for dirpath, dirnames, filenames in os.walk(self.__path):
            for dirname in dirnames:
                path = os.path.join(dirpath, dirname)[len(self.__path)+1:] + os.path.sep
                rtn.append(path)
            for filename in filenames:
                path = os.path.join(dirpath, filename)[len(self.__path)+1:]
                size = os.path.getsize(os.path.join(self.__path, path))
                with open(os.path.join(self.__path, path), 'r') as fh:
                    contents = fh.read()
                rtn.append((path, size, contents))
        return rtn

    def clean(self):
        if os.path.exists(self.__path):
            shutil.rmtree(self.__path)

    def __del__(self):
        self.clean()


class TestPath(TestCase):

    def test_equal(self):
        self.assertEqual(Path('a/b/c'), Path('a/b/c'))
        self.assertEqual(Path('a\\b\\c'), Path('a\\b\\c'))
        self.assertEqual(Path('a/b/c'), 'a/b/c')


    def test_not_equal(self):
        self.assertNotEqual(Path('a/b/c'), Path('a/b'))
        self.assertNotEqual(Path('a/b/c'), 'a/b')


    def test_str(self):
        self.assertEqual(str(Path('a/b/c')), 'a/b/c')


    def test_dict(self):
        d = {
            Path('a/b/c'): 1,
            Path('a/b'): 2,
        }

        self.assertTrue(Path('a/b') in d)
        self.assertFalse(Path('a/b/c/d') in d)

        self.assertEqual(d[Path('a/b/c')], 1)
        self.assertEqual(d[Path('a/b')], 2)


    def test_set(self):
        s = set([
            Path('a/b/c'),
            Path('a/b'),
        ])

        self.assertIn(Path('a/b/c'), s)
        self.assertNotIn(Path('a/b/c/d'), s)


    def test_abs_path(self):
        self.assertEqual(Path('sub').abs, os.path.abspath('sub'))


    def test_norm(self):
        self.assertEqual(Path('a/b/c').norm, os.path.normpath('a/b/c'))
        self.assertEqual(Path('a\\b\\c').norm, os.path.normpath('a\\b\\c'))


    def test_join(self):
        self.assertEqual(Path('a/b/c').join('d', 'e'), Path('a/b/c/d/e'))
        self.assertEqual(Path('a/b/c').join(Path('d/e'), Path('f')), Path('a/b/c/d/e/f'))


    def test_basename(self):
        self.assertEqual(Path('a/b/c').basename, 'c')


    def test_parent(self):
        self.assertEqual(Path('a/b/c').parent, Path('a/b'))


    def test_exists(self):
        td = TempDirectory()
        self.assertTrue(Path(td.path, 'test_file').exists)
        self.assertFalse(Path(td.path, 'unknown_file').exists)
        td.clean()


    def test_is_file(self):
        td = TempDirectory()
        self.assertTrue(Path(td.path, 'test_file').is_file)
        self.assertFalse(Path(td.path, 'Dir 1').is_file)
        self.assertFalse(Path(td.path, 'missing_file').is_file)
        td.clean()

    def test_is_link(self):
        td = TempDirectory()
        self.assertFalse(Path(td.path, 'Dir 1').is_link)
        td.clean()

    def test_is_dir(self):
        td = TempDirectory()
        self.assertFalse(Path(td.path, 'test_file').is_dir)
        self.assertTrue(Path(td.path, 'Dir 1').is_dir)
        self.assertFalse(Path(td.path, 'missing_file').is_dir)
        td.clean()


    def test_find(self):
        td = TempDirectory()

        all = list(Path(td.path).find())

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


    def test_walk(self):
        td = TempDirectory()

        all = list(Path(td.path).walk())

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


    def test_splitext(self):
        prefix, ext = Path('dir/file.txt').splitext
        self.assertEqual(prefix, 'dir/file')
        self.assertEqual(ext, 'txt')


    def test_prefix(self):
        self.assertEqual(Path('a/b/file.txt').prefix, 'a/b/file')


    def test_ext(self):
        self.assertEqual(Path('a/b/file.txt').ext, 'txt')


    def test_has_ext(self):
        self.assertTrue(Path('dir/file.txt').has_ext('txt'))
        self.assertFalse(Path('dir/file.txt').has_ext('dat'))
        self.assertTrue(Path('dir/file.txt').has_ext('txt', 'dat'))
        self.assertFalse(Path('dir/file.txt').has_ext('csv', 'dat'))


    def test_split(self):
        self.assertEqual(Path('a/bc/d').split(), ['a', 'bc', 'd'])
        self.assertEqual(Path('a\\bc\\d').split(), ['a', 'bc', 'd'])


    def test_files(self):
        td = TempDirectory()
        self.assertEqual(set(Path(td.path, 'Dir 2').files),
                         set([Path(td.path, 'Dir 2', 'File C'),
                              Path(td.path, 'Dir 2', 'File D.txt'),
                              ]))
        td.clean()


    def test_dirs(self):
        td = TempDirectory()
        self.assertEqual(set(Path(td.path, 'Dir 2').dirs),
                         set([Path(td.path, 'Dir 2', 'Dir 3'),
                              ]))
        td.clean()


    def test_all(self):
        td = TempDirectory()
        self.assertEqual(set(Path(td.path, 'Dir 2').all),
                         set([Path(td.path, 'Dir 2', 'File C'),
                              Path(td.path, 'Dir 2', 'File D.txt'),
                              Path(td.path, 'Dir 2', 'Dir 3'),
                              ]))
        td.clean()


    def test_samefile(self):
        if hasattr(os.path, 'samefile'):
            td = TempDirectory()
            self.assertTrue(Path(td.path, 'test_file').samefile(Path(td.path, 'test_file')))
            self.assertFalse(Path(td.path, 'test_file').samefile(Path(td.path, 'Dir 2', 'Dir 3', 'test_file')))
            self.assertFalse(Path(td.path, 'test_file').samefile(Path(td.path, 'unknown_file.txt')))
            td.clean()


    def test_is_relative(self):
        self.assertTrue(Path('a/b/c').is_relative)
        self.assertFalse(Path('C:\\test').is_relative)
        self.assertFalse(Path('/a/b/c').is_relative)


    def test_is_absolute(self):
        self.assertFalse(Path('a/b/c').is_absolute)
        self.assertTrue(Path('C:\\test').is_absolute)
        self.assertTrue(Path('/a/b/c').is_absolute)


    def test_rel_root(self):
        self.assertEqual(Path('a/b/c').rel_root,
                          os.path.abspath(os.curdir))
        self.assertIsNone(Path('/a/b/c').rel_root)
        self.assertIsNone(Path('c:\\a\\b\\c').rel_root)


    def test_rel_path(self):

        p = Path('site', relative_to='/var/www')
        self.assertEqual(str(p), 'site')
        self.assertEqual(p.abs, '/var/www/site')
        self.assertEqual(p.rel_root, '/var/www')

        p2 = p.join('drupal')
        self.assertEqual(os.path.normpath(str(p2)),
                          os.path.normpath('site/drupal'))
        self.assertEqual(p2.abs, os.path.normpath('/var/www/site/drupal'))
        self.assertEqual(p2.rel_root, '/var/www')

        p3 = Path(p, 'files')
        self.assertEqual(str(p3), os.path.normpath('site/files'))
        self.assertEqual(p3.abs, '/var/www/site/files')
        self.assertEqual(p3.rel_root, '/var/www')

    def test_make_relative(self):

        p = Path('/var/www/site').make_relative_to('/var/www')
        self.assertEqual(str(p), 'site')
        self.assertEqual(p.abs, '/var/www/site')
        self.assertEqual(p.rel_root, '/var/www')

