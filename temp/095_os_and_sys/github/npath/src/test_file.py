from unittest ______ TestCase

from test_npath ______ TempDirectory
from npath ______ Path, File

c_ TestFile(TestCase):

    ___ test_open
        td _ TempDirectory()

        # Test read
        fh _ File(td.path, 'test_file').open('r')
        assertEqual(fh.read(), "test")
        fh.close()

        # Test write
        fh _ File(td.path, 'test_file_2.txt').open('w')
        fh.write("test")
        fh.close()
        assertIn(("test_file_2.txt", 4, "test"), td.contents)

        td.clean()


    ___ test_touch
        td _ TempDirectory()
        File(td.path, 'new_file').touch()
        assertIn(("new_file", 0, ""), td.contents)
        td.clean()


    ___ test_md5
        td _ TempDirectory()
        assertEqual(File(td.path, 'test_file').md5.lower(),
                         '098f6bcd4621d373cade4e832627b4f6')


    ___ test_unlink
        td _ TempDirectory()
        File(td.path, 'test_file').unlink()
        assertNotIn(("test_file", 4, "test"), td.contents)
        td.clean()


    ___ test_size
        td _ TempDirectory()
        assertEqual(File(td.path, 'test_file').size, 4)
        td.clean()
