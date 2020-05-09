# Filename: deleting_nodes_unittest.py
# Programmer: Marcin Czajkowski
# Purpose: The purpose of this script is test a removeNode() method
#          of the linkedlist.py 


______ sys
______ unittest
____ linkedlist ______ LinkedList

c_ NodesDeleteTest(unittest.TestCase):
    ___ setUp
        try:
            #create list
            newList _ LinkedList()
            #populate the list with data 0 to 9
            for i in range(10):
                newList.addNode(i)
        except:
            print('\nSetup failed: '+ str(sys.exc_info()[0]))
                   
        #prepare list reflecting example data in list
        dataList _ list(range(10))
        rmItemDataList _ list(range(10))
        rmItemDataList.remove(3)

    ___ testCompareNodesData
        #get all data from the list
        dataTest _ newList.getAllData()
        #compare the list data and the sample data
        assertTrue(dataTest, dataList)

    ___ testDeleteDataItem
        #delete data=3 from the list and the sample data
        newList.removeNode(3)
        dataTest _ newList.getAllData()
        #compare the list data and the sample data
        assertTrue(dataTest, rmItemDataList)

if __name__ == '__main__':
    unittest.main(verbosity_2)
