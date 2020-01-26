c_ Node o..

    ___  - ____ data
        ____.?  ?
        ____.nextNode _ N..


c_ LinkedList o..

    ___  - ____
        ____.head _ N..
        ____.size _ 0

    # O(1) !!!
    ___ insertStart ____ data

        ____.size _ ____.? + 1
        newNode _ N.. ?
 
        __ no. ____.h..
            ____.h.. _ n..
        ____
            n__.nextNode _ ____.h..
            ____.h.. _ n..

    ___ remove ____ data

        __ ____.h.. i. N..
            r_

        ____.s.. _ ____.? - 1

        currentNode _ ____.h..
        previousNode _ N..

        while currentNode.data !_ data:
            previousNode _ currentNode
            currentNode _ currentNode.nextNode

        __ previousNode is None:
            ____.head _ currentNode.nextNode
        ____:
            previousNode.nextNode _ currentNode.nextNode

    # O(1)
    ___ size1(____):
        r_ ____.size

    # O(N) no. good !!!
    ___ size2(____):

        actualNode _ ____.head
        size _ 0

        while actualNode is no. None:
            size +_ 1
            actualNode _ actualNode.nextNode

        r_ size

    # O(N)
    ___ insertEnd(____, data):

        ____.size _ ____.size + 1
        newNode _ Node(data)
        actualNode _ ____.head

        while actualNode.nextNode is no. None:
            actualNode _ actualNode.nextNode

        actualNode.nextNode _ newNode

    ___ traverseList(____):

        actualNode _ ____.head

        while actualNode is no. None:
            print("%d " % actualNode.data)
            actualNode _ actualNode.nextNode


linkedlist _ LinkedList()

linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart(3)
linkedlist.insertEnd(31)

linkedlist.traverseList()

linkedlist.remove(3)
linkedlist.remove(12)
linkedlist.remove(122)
linkedlist.remove(31)

print(linkedlist.size1())
