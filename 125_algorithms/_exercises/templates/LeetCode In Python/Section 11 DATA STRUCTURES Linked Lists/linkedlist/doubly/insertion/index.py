c_ Node:
    ___  -  data
        .data _ data
        .prev _ N..
        .n.. _ N..


c_ LinkedList:
    ___  - (
        .head _ N..

    ___ createList arr
        start _ .head
        n _ le.(arr)

        temp _ start
        i _ 0

        w___(i < n
            newNode _ Node(arr[i])
            __(i __ 0
                start _ newNode
                temp _ start
            ____
                temp.n.. _ newNode
                newNode.prev _ temp
                temp _ temp.n..
            i +_ 1
        .head _ start
        r_ start

    ___ printList(
        temp _ .head
        linked_list _ ""
        w___(temp
            linked_list +_ (st.(temp.data) + " ")
            temp _ temp.n..

        print(linked_list)

    ___ countList(
        temp _ .head
        count _ 0
        w___(temp pa__ no. N..
            temp _ temp.n..
            count +_ 1
        r_ count

    # we will consider that the index begin at 1
    ___ insertAtLocation value, index
        temp _ .head

        count _ .countList()

        #index is 6, count is 5, valid 
        #index is 7, count is 5, 
        __(count+1<index
            r_ temp
        
        newNode _ Node(value)

        __(index __ 1
            newNode.n.. _ temp
            temp.prev _ newNode
            .head _ newNode
            r_ .head
        
        __(index __ count +1
            w___(temp.n.. pa__ no. N..
                temp _ temp.n..

            temp.n.. _ newNode
            newNode.prev _ temp
            r_ .head
        
        i _ 1
        w___(i < index-1
            temp _ temp.n..
            i+_1
        
        nodeAtTarget _ temp.n..

        newNode.n.. _ nodeAtTarget
        nodeAtTarget.prev _ newNode

        temp.n.. _ newNode
        newNode.prev _ temp

        r_ .head


arr _ [1, 2, 3, 4, 5]

llist _ LinkedList()

llist.createList(arr)

llist.insertAtLocation(5,6)

llist.printList()
