_______ __
____ pathlib _______ Path
____ tempfile _______ TemporaryDirectory

_______ p__

____ files _______ get_files

TMP = Path(__.getenv("TMP", "/tmp"))


?p__.m__.p.("byte_sizes, size_in_kb, expected", [
    ([800, 1000, 1200], 1,  '1200' ),
    ([1024, 1025], 1,  '1024', '1025' ),
    ([1024, 1025], 1.026, []),
    ([1000, 1300, 1777, 900], 1.25,  '1300', '1777' ),
    ([1024, 2047, 2048, 2500], 2,  '2048', '2500' ),
])
___ test_get_files(byte_sizes, size_in_kb, expected
    w__ TemporaryDirectory(dir=TMP) __ dirname:
        ___ size __ byte_sizes:
            w__ o.. __.p...j..(dirname, s..(size)), 'wb') __ f:
                f.w.. __.urandom(size))

        actual = [__.p...basename(fi) ___ fi __
                  get_files(dirname, size_in_kb)]
        ... s..(actual) __ s..(expected)