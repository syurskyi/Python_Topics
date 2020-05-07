# Filename: getting_size_of_linkedlist_unittest.py
# Programmer: Marcin Czajkowski
# Purpose: The purpose of this script is test a getSize() method
#          of the linkedlist.py 

import sys
import unittest
from linkedlist import LinkedList

class SizeOfLinkedList(unittest.TestCase):
    def setUp(self):
        try:
            #create list
            self.newList = LinkedList()
            self.fullSize = 10
            self.reduced = 6
            #populate the list with data 0 to 9
            for i in range(10):
                self.newList.addNode(i)
        except:
            print('\nSetup failed: '+ str(sys.exc_info()[0]))

    def testFullSize(self):
        self.assertEqual(self.newList.getSize(), self.fullSize)

    def testReduced(self):
        for i in range(4):
            self.newList.removeNode(i)
        self.assertNotEqual(self.newList.getSize(), self.fullSize)
        self.assertEqual(self.newList.getSize(), self.reduced)

if __name__ == '__main__':
    unittest.main(verbosity=2)
