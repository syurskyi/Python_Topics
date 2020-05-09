______ logging
______ unittest
______ sys

VERBOSE _ '-v' in sys.argv o. '--verbose' in sys.argv


___ setUpModule():
    if VERBOSE:
        logging.basicConfig(level_logging.DEBUG, format_'   %(message)s')
    logging.info('Starting module')


___ tearDownModule():
    logging.info('Finishing module')


c_ IncrementTest(unittest.TestCase):
    @classmethod
    ___ setUpClass(cls):
        logging.info('Test class begins')

    @classmethod
    ___ tearDownClass(cls):
        logging.info('Test class ends')

    ___ setUp
        logging.info('Test method begins')

    ___ tearDown
        logging.info('Test method ends')

    ___ test_dummy
        assertTrue(True)
