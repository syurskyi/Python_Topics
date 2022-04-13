___ has_spaces(txt
    __ txt.f.. " ") __ -1:
        r.. F..
    ____
        r.. T..


___ test
    print("test has started")
    __ has_spaces("FOO") !_ F..:
        print("error1")
    __ has_spaces("FOO BAR") !_ T..
        print('error2')
    __ has_spaces("Foo ") !_ T..
        print("error3")
    __ has_spaces("") !_ F..:
        print("error4")
