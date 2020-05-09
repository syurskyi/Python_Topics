# Filename: add_siglenode_unittest.py
# Programmer: Marcin Czajkowski
# Purpose: The purpose of this script is test a addNode() method
#          of the linkedlist.py 

______ sys
______ u__
____ linkedlist ______ LinkedList

c_ SingleNodeInsertionTest?.?
    ___ setUp
        try:
            newList _ LinkedList()
        except:
            print('\nSetup failed: '+ st.(sys.exc_info()[0]))

    ___ testNodeInsertion
        #insert new node
        newList.addNode(10)
        #check if node exists
        aE..(newList.findNode(10), 10)

__ __name__ __ '__main__':
    u__.main(verbosity_2)

