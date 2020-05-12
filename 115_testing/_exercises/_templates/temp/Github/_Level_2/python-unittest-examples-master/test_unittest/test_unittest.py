# -*- coding: utf-8 -*-

______ u__
____ sets ______ Set


c_ Widget o..

    """For running tests"""

    ___  -   widget_name
        _size _ (50, 50)
        widget_name _ widget_name

    ___ resize  x_value, y_value
        _size _ (x_value, y_value)

    ___ dispose
        print 'dispose'

    ___ size
        r_ _size

    ___ raise_exception
        r_ E..()


@u__.skipIf(3 < 2, 'This class will be executed because 3 is greater than 2, which makes the condition false.')
c_ TestUnittest?.?

    ??
    ___ setUpClass ___
        print 'setUpClass'

    ??
    ___ tearDownClass ___
        print 'tearDownClass'

    ___ setUp
        widget _ Widget('The widget')

    ___ tearDown
        widget.dispose()
        widget _ N..

    ___ test_default_size
        aE..(widget.size(), (50, 50),
                         'incorrect default size')

    ___ test_resize
        widget.resize(100, 150)
        aE..(widget.size(), (100, 150),
                         'wrong size after resize')

    @u__.skip("demonstrating skipping")
    ___ test_nothing
        fail("shouldn't happen")

    @u__.skipIf(1 < 2, 'because 1 < 2, this test case will not be executed')
    ___ test_always_be_tested
        p..

    @u__.skipUnless(1 > 2, 'This test case will be skipped. Unless the condition is true')
    ___ test_skipunless_decorator
        p..

    @u__.expectedFailure
    ___ test_fail
        aT..(false)

    ___ test_basic_usage
        aE..(1, 1)
        aNE..(1, 2)
        aT..(T..)
        aF..(F..)
        assertIs(widget, widget)
        assertIsNot(widget, Widget('new widget'))
        aIN..(N..)
        aINN..('A value')
        aI..(1, (1, 2, 3))
        assertNotIn(1, (2, 3, 4))
        AII..(widget, Widget)
        assertNotIsInstance(1, Widget)
        aAE..(2.12345678, 2.12345679)
        aAE..(2.1, 2.2, delta_0.2)
        aNAE..(2.1, 2, 2)
        aG..(3, 2)
        aGE..(2, 2)
        aL..(1, 2)
        aLE..(1, 1)
        assertRegexpMatches('a string', 'string')
        assertNotRegexpMatches('a string', 'the')
        # assertItemsEqual: sorted(a) == sorted(b)
        assertItemsEqual([1, 2, 3], [1, 3, 2])
        # assertDictContainsSubset: Deprecated since version 3.2.
        assertDictContainsSubset(expected_{
                                      'key1': 1}, actual_{'key1': 1, 'key2': 2})

        assertMultiLineEqual('test', 'test')
        """
        assertSequenceEqual: This method is not called directly by assertEqual(), but it’s used to
        implement assertListEqual() and assertTupleEqual().
        """
        assertSequenceEqual((1, 2), (1, 2))
        aLE..([1, 2], [1, 2])
        assertTupleEqual((1, 2), (1, 2))
        assertSetEqual(Set(['a', 'b', 'c']), Set(['b', 'a', 'c']))
        assertDictEqual({'key1': 1, 'key2': 2}, {'key1': 1, 'key2': 2})

    ___ test_raise_exception
        w__ aR..(E..
            widget.raise_exception()

__ _____ __ _____
    ?.?
# Do not use the following way to trigger unit testing if you wanna use
# nosetests as the test runner.

# suite = unittest.TestLoader().loadTestsFromTestCase(TestUnittest)
# unittest.TextTestRunner(verbosity=2).run(suite)
