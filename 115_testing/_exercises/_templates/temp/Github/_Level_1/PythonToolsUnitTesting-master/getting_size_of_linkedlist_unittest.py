# Filename: getting_size_of_linkedlist_unittest.py
# Programmer: Marcin Czajkowski
# Purpose: The purpose of this script is test a getSize() method
#          of the linkedlist.py 

______ sys
______ unittest
____ linkedlist ______ LinkedList

c_ SizeOfLinkedList(unittest.TestCase):
    ___ setUp
        try:
            #create list
            newList _ LinkedList()
            fullSize _ 10
            reduced _ 6
            #populate the list with data 0 to 9
            for i in range(10):
                newList.addNode(i)
        except:
            print('\nSetup failed: '+ str(sys.exc_info()[0]))

    ___ testFullSize
        assertEqual(newList.getSize(), fullSize)

    ___ testReduced
        for i in range(4):
            newList.removeNode(i)
        assertNotEqual(newList.getSize(), fullSize)
        assertEqual(newList.getSize(), reduced)

if __name__ == '__main__':
    unittest.main(verbosity_2)
