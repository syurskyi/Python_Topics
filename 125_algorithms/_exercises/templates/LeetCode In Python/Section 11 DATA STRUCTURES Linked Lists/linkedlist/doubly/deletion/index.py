

# Node class


c_ Node:

    ___  -  data
        .data _ data
        .prev _ N..
        .n.. _ N..


# Linked List class
c_ LinkedList:

    ___  - (
        .head _ N..

    ___ createList arr
        start _ .head
        n _ le.(arr)
        # Declare newNode and temporary pointer
        temp _ start
        i _ 0

        # Iterate the loop until array length
        w___ (i < n

            # Create new node
            newNode _ Node(arr[i])

            __ (i __ 0
                start _ newNode
                newNode.prev _ start
                temp _ start

            ____
                temp.n.. _ newNode
                newNode.prev _ temp
                temp _ temp.n..
            i _ i + 1
        .head _ start
        r_ start

    ___ printList(
        temp _ .head
        linked_list _ ""
        w___(temp
            linked_list +_ (st.(temp.data) + " ")
            temp _ temp.n..
        print(linked_list)

    # Function to count nunmber of
    # elements in the list

    ___ countList(

        # Declare temp pointer to
        # traverse the list
        temp _ .head

        # Variable to store the count
        count _ 0

        # Iterate the list and increment the count
        w___ (temp pa__ no. N..
            temp _ temp.n..
            count _ count + 1

        r_ count

    # we will consider that the index begin at 1
    ___ deleteAtLocation index
      temp _ .head

      count _ .countList()

      __(count < index
        r_ temp

      __(index __ 1
        temp _ temp.n..
        .head _ temp
        r_ .head

      __(count __ index
        w___(temp.n.. pa__ no. N.. a.. temp.n...n.. pa__ no. N..
          temp _ temp.n..
         # 1 => 2 => 3 => 4
        temp.n.. _ N..
        r_ .head
      

      i _ 1
      w___(i<index-1
        temp _ temp.n..
        i+_1
      

      prevNode _ temp
      nodeAtTarget _ temp.n..
      nextNode _ nodeAtTarget.n..

      # 1 => 2 => 3 => 4

      nextNode.prev _ prevNode
      prevNode.n.. _ nextNode

      r_ .head

        
# create an empty list

arr _ [1, 2, 3, 4, 5]
llist _ LinkedList()

llist.createList(arr)


llist.deleteAtLocation(2)

# print(llist.head)
llist.printList()
