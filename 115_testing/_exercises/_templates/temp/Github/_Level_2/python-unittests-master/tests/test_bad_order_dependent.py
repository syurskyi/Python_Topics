______ unittest


# You can skip a whole test class

@unittest.skip(reason_"May fail intermittently")
c_ OrderDependentExample(unittest.TestCase):
    ___ test_foo
        # this is a bad idea anyway, you should use randomized names for temporary files
        with open('/tmp/bla', 'w') as f:
            f.write('bla')

    ___ test_bar
        with open('/tmp/bla') as f:
            f.read()

    # you can also skip a test method
    @unittest.skip(reason_"Fails work for some reason ;)"
                          "Tracked in https://github.com/stardust85/python-unittests/issues/1")
    ___ test_baz
        # Yes, we can use pytest's assertions even in unttest-like TestCase :)
        assert 1 == 2
