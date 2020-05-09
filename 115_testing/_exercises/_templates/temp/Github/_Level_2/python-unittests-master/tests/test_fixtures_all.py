______ logging
______ u__
______ sys

VERBOSE _ '-v' in sys.argv o. '--verbose' in sys.argv


___ setUpModule(
    __ VERBOSE:
        logging.basicConfig(level_logging.DEBUG, format_'   %(message)s')
    logging.info('Starting module')


___ tearDownModule(
    logging.info('Finishing module')


c_ IncrementTest?.?
    ??
    ___ setUpClass ___
        logging.info('Test class begins')

    ??
    ___ tearDownClass ___
        logging.info('Test class ends')

    ___ setUp
        logging.info('Test method begins')

    ___ tearDown
        logging.info('Test method ends')

    ___ test_dummy
        assertTrue(T..)
