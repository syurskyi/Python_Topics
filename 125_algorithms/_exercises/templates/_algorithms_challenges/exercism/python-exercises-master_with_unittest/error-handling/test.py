_______ unittest

_______ error_handling __ er


c_ FileLike(o..):
    ___ - , fail_something=T..):
        is_open = F..
        was_open = F..
        did_something = F..
        fail_something = fail_something

    ___ open
        was_open = F..
        is_open = T..

    ___ close
        is_open = F..
        was_open = T..

    ___ __enter__
        open()
        r.. self

    ___ __exit__  *args):
        close()

    ___ do_something
        did_something = T..
        __ fail_something:
            r.. E..("Failed while doing something")


c_ ErrorHandlingTest(unittest.TestCase):
    ___ test_throw_exception
        w__ assertRaisesWithMessage(E..):
            er.handle_error_by_throwing_exception()

    ___ test_return_none
        assertEqual(er.handle_error_by_returning_none('1'), 1,
                         'Result of valid input should not be None')
        assertIsNone(er.handle_error_by_returning_none('a'),
                          'Result of invalid input should be None')

    ___ test_return_tuple
        successful_result, result = er.handle_error_by_returning_tuple('1')
        assertIs(successful_result, T..,
                      'Valid input should be successful')
        assertEqual(result, 1, 'Result of valid input should not be None')

        failure_result, result = er.handle_error_by_returning_tuple('a')
        assertIs(failure_result, F..,
                      'Invalid input should not be successful')

    ___ test_filelike_objects_are_closed_on_exception
        filelike_object = FileLike(fail_something=T..)
        w__ assertRaisesWithMessage(E..):
            er.filelike_objects_are_closed_on_exception(filelike_object)
        assertIs(filelike_object.is_open, F..,
                      'filelike_object should be closed')
        assertIs(filelike_object.was_open, T..,
                      'filelike_object should have been opened')
        assertIs(filelike_object.did_something, T..,
                      'filelike_object should call do_something()')

    ___ test_filelike_objects_are_closed_without_exception
        filelike_object = FileLike(fail_something=F..)
        er.filelike_objects_are_closed_on_exception(filelike_object)
        assertIs(filelike_object.is_open, F..,
                      'filelike_object should be closed')
        assertIs(filelike_object.was_open, T..,
                      'filelike_object should have been opened')
        assertIs(filelike_object.did_something, T..,
                      'filelike_object should call do_something()')

    # Utility functions
    ___ setUp
        ___
            assertRaisesRegex
        ______ AttributeError:
            assertRaisesRegex = assertRaisesRegexp

    ___ assertRaisesWithMessage  exception):
        r.. assertRaisesRegex(exception, r".+")


__ _____ __ _____
    unittest.main()
