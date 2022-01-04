___ has_spaces(txt):
    __ txt.find(" ") __ -1:
        r.. F..
    ____:
        r.. T..


___ test
    print("test has started")
    __ has_spaces("FOO") != F..:
        print("error1")
    __ has_spaces("FOO BAR") != T..:
        print('error2')
    __ has_spaces("Foo ") != T..:
        print("error3")
    __ has_spaces("") != F..:
        print("error4")
