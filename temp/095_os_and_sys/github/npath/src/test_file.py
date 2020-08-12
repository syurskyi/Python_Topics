from unittest ______ TestCase

from test_npath ______ TempDirectory
from npath ______ Path, File

class TestFile(TestCase):

    def test_open(self):
        td _ TempDirectory()

        # Test read
        fh _ File(td.path, 'test_file').open('r')
        self.assertEqual(fh.read(), "test")
        fh.close()

        # Test write
        fh _ File(td.path, 'test_file_2.txt').open('w')
        fh.write("test")
        fh.close()
        self.assertIn(("test_file_2.txt", 4, "test"), td.contents)

        td.clean()


    def test_touch(self):
        td _ TempDirectory()
        File(td.path, 'new_file').touch()
        self.assertIn(("new_file", 0, ""), td.contents)
        td.clean()


    def test_md5(self):
        td _ TempDirectory()
        self.assertEqual(File(td.path, 'test_file').md5.lower(),
                         '098f6bcd4621d373cade4e832627b4f6')


    def test_unlink(self):
        td _ TempDirectory()
        File(td.path, 'test_file').unlink()
        self.assertNotIn(("test_file", 4, "test"), td.contents)
        td.clean()


    def test_size(self):
        td _ TempDirectory()
        self.assertEqual(File(td.path, 'test_file').size, 4)
        td.clean()
