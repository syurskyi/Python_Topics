# Filename: getting_size_of_linkedlist_unittest.py
# Programmer: Marcin Czajkowski
# Purpose: The purpose of this script is test a getSize() method
#          of the linkedlist.py 

______ sys
______ u__
____ linkedlist ______ LinkedList

c_ SizeOfLinkedList?.?
    ___ setUp
        ___
            #create list
            newList _ LinkedList()
            fullSize _ 10
            reduced _ 6
            #populate the list with data 0 to 9
            ___ i __ ra..(10
                newList.addNode(i)
        _____:
            print('\nSetup failed: '+ st.(sys.exc_info()[0]))

    ___ testFullSize
        aE..(newList.getSize(), fullSize)

    ___ testReduced
        ___ i __ ra..(4
            newList.removeNode(i)
        assertNotEqual(newList.getSize(), fullSize)
        aE..(newList.getSize(), reduced)

__ _____ __ _____
    u__.main(verbosity_2)
