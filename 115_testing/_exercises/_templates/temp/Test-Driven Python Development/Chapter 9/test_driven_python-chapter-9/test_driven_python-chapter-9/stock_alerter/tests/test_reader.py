_____ u__
____ u__ _____ mock
____ d_t_ _____ d_t_

____ ..reader _____ FileReader


c_ FileReaderTest ?.?
    @mock.patch("builtins.open",
                mock.mock_open(read_data="""\
GOOG,2014-02-11T14:10:22.13,10"""))
    ___ test_FileReader_returns_the_file_contents
        reader = FileReader("stocks.txt")
        updater = reader.get_updates()
        u.. = next(updater)
        aE..(("GOOG",
                          d_t_(2014, 2, 11, 14, 10, 22, 130000),
                          10), u..)
