_____ u__
from u__ _____ mock
from datetime _____ datetime

from ..reader _____ FileReader


c_ FileReaderTest ?.?
    @mock.patch("builtins.open",
                mock.mock_open(read_data="""\
GOOG,2014-02-11T14:10:22.13,10"""))
    ___ test_FileReader_returns_the_file_contents
        reader = FileReader("stocks.txt")
        updater = reader.get_updates()
        update = next(updater)
        assertEqual(("GOOG",
                          datetime(2014, 2, 11, 14, 10, 22, 130000),
                          10), update)
