# Filename: deleting_nodes_unittest.py
# Programmer: Marcin Czajkowski
# Purpose: The purpose of this script is test a removeNode() method
#          of the linkedlist.py 


import sys
import unittest
from linkedlist import LinkedList

class NodesDeleteTest(unittest.TestCase):
    def setUp(self):
        try:
            #create list
            self.newList = LinkedList()
            #populate the list with data 0 to 9
            for i in range(10):
                self.newList.addNode(i)
        except:
            print('\nSetup failed: '+ str(sys.exc_info()[0]))
                   
        #prepare list reflecting example data in list
        self.dataList = list(range(10))
        self.rmItemDataList = list(range(10))
        self.rmItemDataList.remove(3)

    def testCompareNodesData(self):
        #get all data from the list
        self.dataTest = self.newList.getAllData()
        #compare the list data and the sample data
        self.assertTrue(self.dataTest, self.dataList)

    def testDeleteDataItem(self):
        #delete data=3 from the list and the sample data
        self.newList.removeNode(3)
        self.dataTest = self.newList.getAllData()
        #compare the list data and the sample data
        self.assertTrue(self.dataTest, self.rmItemDataList)

if __name__ == '__main__':
    unittest.main(verbosity=2)
