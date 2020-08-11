from unittest import TestCase

from test_npath import TempDirectory
from npath import Path, File

class TestFile(TestCase):

    def test_open(self):
        td = TempDirectory()

        # Test read
        fh = File(td.path, 'test_file').open('r')
        self.assertEqual(fh.read(), "test")
        fh.close()

        # Test write
        fh = File(td.path, 'test_file_2.txt').open('w')
        fh.write("test")
        fh.close()
        self.assertIn(("test_file_2.txt", 4, "test"), td.contents)

        td.clean()


    def test_touch(self):
        td = TempDirectory()
        File(td.path, 'new_file').touch()
        self.assertIn(("new_file", 0, ""), td.contents)
        td.clean()


    def test_md5(self):
        td = TempDirectory()
        self.assertEqual(File(td.path, 'test_file').md5.lower(),
                         '098f6bcd4621d373cade4e832627b4f6')


    def test_unlink(self):
        td = TempDirectory()
        File(td.path, 'test_file').unlink()
        self.assertNotIn(("test_file", 4, "test"), td.contents)
        td.clean()


    def test_size(self):
        td = TempDirectory()
        self.assertEqual(File(td.path, 'test_file').size, 4)
        td.clean()
