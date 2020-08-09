

# Node class


c_ Node:

    ___ __init__(, data
        .data _ data
        .prev _ None
        .next _ None


# Linked List class
c_ LinkedList:

    ___ __init__(
        .head _ None

    ___ createList(, arr
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
                temp.next _ newNode
                newNode.prev _ temp
                temp _ temp.next
            i _ i + 1
        .head _ start
        r_ start

    ___ printList(
        temp _ .head
        linked_list _ ""
        w___(temp
            linked_list +_ (st.(temp.data) + " ")
            temp _ temp.next
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
        w___ (temp is no. None
            temp _ temp.next
            count _ count + 1

        r_ count

    # we will consider that the index begin at 1
    ___ deleteAtLocation(, index
      temp _ .head

      count _ .countList()

      __(count < index
        r_ temp

      __(index __ 1
        temp _ temp.next
        .head _ temp
        r_ .head

      __(count __ index
        w___(temp.next is no. None and temp.next.next is no. None
          temp _ temp.next
         # 1 => 2 => 3 => 4
        temp.next _ None
        r_ .head
      

      i _ 1
      w___(i<index-1
        temp _ temp.next
        i+_1
      

      prevNode _ temp
      nodeAtTarget _ temp.next
      nextNode _ nodeAtTarget.next

      # 1 => 2 => 3 => 4

      nextNode.prev _ prevNode
      prevNode.next _ nextNode

      r_ .head

        
# create an empty list

arr _ [1, 2, 3, 4, 5]
llist _ LinkedList()

llist.createList(arr)


llist.deleteAtLocation(2)

# print(llist.head)
llist.printList()
