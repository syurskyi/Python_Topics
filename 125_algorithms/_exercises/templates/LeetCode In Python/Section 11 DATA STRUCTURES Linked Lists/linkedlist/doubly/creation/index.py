c_ Node:
    ___  -  data
        .data _ data
        .prev _ N..
        .next _ N..


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
                temp.next _ newNode
                newNode.prev _ temp
                temp _ temp.next
            i +_ 1
        .head _ start
        r_ start

    ___ printList(
        temp _ .head
        linked_list _ ""
        w___(temp
            linked_list +_ (st.(temp.data) + " ")
            temp _ temp.next

        print(linked_list)
      

arr _ [1,2,3,4,5]

llist _ LinkedList()

llist.createList(arr)

llist.printList()
