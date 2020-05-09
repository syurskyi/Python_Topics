# Filename: add_siglenode_unittest.py
# Programmer: Marcin Czajkowski
# Purpose: The purpose of this script is test a addNode() method
#          of the linkedlist.py 

______ sys
______ unittest
____ linkedlist ______ LinkedList

c_ SingleNodeInsertionTest(unittest.TestCase):
    ___ setUp
        try:
            newList _ LinkedList()
        except:
            print('\nSetup failed: '+ str(sys.exc_info()[0]))

    ___ testNodeInsertion
        #insert new node
        newList.addNode(10)
        #check if node exists
        assertEqual(newList.findNode(10), 10)

if __name__ == '__main__':
    unittest.main(verbosity_2)

