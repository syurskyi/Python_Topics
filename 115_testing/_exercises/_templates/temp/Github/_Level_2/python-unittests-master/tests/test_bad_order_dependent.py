______ u__


# You can skip a whole test class

@u__.skip(reason_"May fail intermittently")
c_ OrderDependentExample?.?
    ___ test_foo
        # this is a bad idea anyway, you should use randomized names for temporary files
        w__ o..('/tmp/bla', _ __ f:
            f.write('bla')

    ___ test_bar
        w__ o..('/tmp/bla') __ f:
            f.read()

    # you can also skip a test method
    @u__.skip(reason_"Fails work for some reason ;)"
                          "Tracked in https://github.com/stardust85/python-unittests/issues/1")
    ___ test_baz
        # Yes, we can use pytest's assertions even in unttest-like TestCase :)
        a.. 1 __ 2
