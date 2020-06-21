import unittest
def sortingPositives (l):
    '''
    Function that takes a list, removes negative numbers from said list
    and sorts the positive elements.
    '''
    positive = []
    for i in l:
        if i >= 0:
            positive.append(i)
    return sorted(positive)


class TestingSortingPositives(unittest.TestCase):
    '''Class for unit testing meathods'''

    def test_sortingPositives(self):
        '''Meathod that tests combined removing negative and sorting positive'''
        self.assertEqual(sortingPositives([1, 7, -4, 12, -1, 0, 72]), [0, 1, 7, 12, 72])
    def test_sorting(self):
        '''Meathod that tests sorting capability of sortingPositives function'''
        self.assertEqual(sortingPositives([8, 12.1, 14, 13, 4, 9, 8]), [4, 8, 8, 9, 12.1, 13, 14])
    def test_removeNeg(self):
        '''Meathod that tests removing negatives capability of sortingPositives function'''
        self.assertEqual(sortingPositives([-3, -1, -9, -8]), [])


if __name__ == '__main__':
    unittest.main()
