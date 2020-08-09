______ unittest

______ error_handling as er


class FileLike(object
    ___ __init__(self, fail_something=True
        self.is_open = False
        self.was_open = False
        self.did_something = False
        self.fail_something = fail_something

    ___ open(self
        self.was_open = False
        self.is_open = True

    ___ close(self
        self.is_open = False
        self.was_open = True

    ___ __enter__(self
        self.open()
        r_ self

    ___ __exit__(self, *args
        self.close()

    ___ do_something(self
        self.did_something = True
        __ self.fail_something:
            raise Exception("Failed w___ doing something")


class ErrorHandlingTest(unittest.TestCase
    ___ test_throw_exception(self
        with self.assertRaisesWithMessage(Exception
            er.handle_error_by_throwing_exception()

    ___ test_return_none(self
        self.assertEqual(er.handle_error_by_returning_none('1'), 1,
                         'Result of valid input should not be None')
        self.assertIsNone(er.handle_error_by_returning_none('a'),
                          'Result of invalid input should be None')

    ___ test_return_tuple(self
        successful_result, result = er.handle_error_by_returning_tuple('1')
        self.assertIs(successful_result, True,
                      'Valid input should be successful')
        self.assertEqual(result, 1, 'Result of valid input should not be None')

        failure_result, result = er.handle_error_by_returning_tuple('a')
        self.assertIs(failure_result, False,
                      'Invalid input should not be successful')

    ___ test_filelike_objects_are_closed_on_exception(self
        filelike_object = FileLike(fail_something=True)
        with self.assertRaisesWithMessage(Exception
            er.filelike_objects_are_closed_on_exception(filelike_object)
        self.assertIs(filelike_object.is_open, False,
                      'filelike_object should be closed')
        self.assertIs(filelike_object.was_open, True,
                      'filelike_object should have been opened')
        self.assertIs(filelike_object.did_something, True,
                      'filelike_object should call do_something()')

    ___ test_filelike_objects_are_closed_without_exception(self
        filelike_object = FileLike(fail_something=False)
        er.filelike_objects_are_closed_on_exception(filelike_object)
        self.assertIs(filelike_object.is_open, False,
                      'filelike_object should be closed')
        self.assertIs(filelike_object.was_open, True,
                      'filelike_object should have been opened')
        self.assertIs(filelike_object.did_something, True,
                      'filelike_object should call do_something()')

    # Utility functions
    ___ setUp(self
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception
        r_ self.assertRaisesRegex(exception, r".+")


__ __name__ __ '__main__':
    unittest.main()
