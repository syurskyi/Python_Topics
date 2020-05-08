import logging
import unittest
import sys

VERBOSE = '-v' in sys.argv or '--verbose' in sys.argv


def setUpModule():
    if VERBOSE:
        logging.basicConfig(level=logging.DEBUG, format='   %(message)s')
    logging.info('Starting module')


def tearDownModule():
    logging.info('Finishing module')


class IncrementTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.info('Test class begins')

    @classmethod
    def tearDownClass(cls):
        logging.info('Test class ends')

    def setUp(self):
        logging.info('Test method begins')

    def tearDown(self):
        logging.info('Test method ends')

    def test_dummy(self):
        self.assertTrue(True)
