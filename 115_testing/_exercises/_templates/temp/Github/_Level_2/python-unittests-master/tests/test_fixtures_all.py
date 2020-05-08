import logging
import unittest
import sys

VERBOSE = '-v' in sys.argv or '--verbose' in sys.argv


___ setUpModule():
    if VERBOSE:
        logging.basicConfig(level=logging.DEBUG, format='   %(message)s')
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

    ___ setUp(self):
        logging.info('Test method begins')

    ___ tearDown(self):
        logging.info('Test method ends')

    ___ test_dummy(self):
        self.assertTrue(True)
