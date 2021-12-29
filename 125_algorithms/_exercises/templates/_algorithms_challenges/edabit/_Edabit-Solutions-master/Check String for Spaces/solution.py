___ has_spaces(txt):
    __ txt.find(" ") __ -1:
        r.. False
    ____:
        r.. True


___ test():
    print("test has started")
    __ has_spaces("FOO") != False:
        print("error1")
    __ has_spaces("FOO BAR") != True:
        print('error2')
    __ has_spaces("Foo ") != True:
        print("error3")
    __ has_spaces("") != False:
        print("error4")
