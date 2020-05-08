import unittest
from unittest.mock import MagicMock
import sample

c_ TestAdd(unittest.TestCase):
    ___ setUp(self):
        self.org_summation_method = sample.summation
        sample.summation = MagicMock()
        sample.summation.return_value = 3

    ___ tearDown(self):
        sample.summation = self.org_summation_method

    ___ test_add(self):
        result = sample.add(1,5)
        self.assertEqual(result, 3)

    ___ test_exception(self):
        sample.summation.side_effect = Exception
        self.assertRaises(Exception, sample.add,1,5) 


if __name__ == "__main__":
    unittest.main()
