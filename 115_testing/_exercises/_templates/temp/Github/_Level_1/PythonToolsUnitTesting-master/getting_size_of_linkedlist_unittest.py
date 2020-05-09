# Filename: getting_size_of_linkedlist_unittest.py
# Programmer: Marcin Czajkowski
# Purpose: The purpose of this script is test a getSize() method
#          of the linkedlist.py 

______ sys
______ u__
____ linkedlist ______ LinkedList

c_ SizeOfLinkedList?.?
    ___ setUp
        try:
            #create list
            newList _ LinkedList()
            fullSize _ 10
            reduced _ 6
            #populate the list with data 0 to 9
            for i in range(10
                newList.addNode(i)
        except:
            print('\nSetup failed: '+ st.(sys.exc_info()[0]))

    ___ testFullSize
        aE..(newList.getSize(), fullSize)

    ___ testReduced
        for i in range(4
            newList.removeNode(i)
        assertNotEqual(newList.getSize(), fullSize)
        aE..(newList.getSize(), reduced)

if __name__ == '__main__':
    u__.main(verbosity_2)
