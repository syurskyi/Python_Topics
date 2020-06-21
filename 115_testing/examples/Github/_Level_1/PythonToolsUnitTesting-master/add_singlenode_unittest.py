# Filename: add_siglenode_unittest.py
# Programmer: Marcin Czajkowski
# Purpose: The purpose of this script is test a addNode() method
#          of the linkedlist.py 

import sys
import unittest
from linkedlist import LinkedList

class SingleNodeInsertionTest(unittest.TestCase):
    def setUp(self):
        try:
            self.newList = LinkedList()
        except:
            print('\nSetup failed: '+ str(sys.exc_info()[0]))

    def testNodeInsertion(self):
        #insert new node
        self.newList.addNode(10)
        #check if node exists
        self.assertEqual(self.newList.findNode(10), 10)

if __name__ == '__main__':
    unittest.main(verbosity=2)

