______ unittest
____ unittest ______ TestCase


c_ TestSetUpAndTearDown(TestCase):
    """Showcase for a test with setUp and tearDown methods"""

    important_value _ None

    # Is run before each test. Should be used to create clean condition for each test.
    ___ setUp
        important_value _ 1337

    # Is run after each test. Mostly used for closing connections/files or clean up stuff.
    ___ tearDown
        important_value _ None

    ___ test_value_after_setup
        assertEqual(1337, important_value)


# build in main method to run all tests in this class
if __name__ == '__main__':
    unittest.main()
