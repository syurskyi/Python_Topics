

# Node class


class Node:

    ___ __init__(self, data
        self.data = data
        self.prev = None
        self.next = None


# Linked List class
class LinkedList:

    ___ __init__(self
        self.head = None

    ___ createList(self, arr
        start = self.head
        n = le.(arr)
        # Declare newNode and temporary pointer
        temp = start
        i = 0

        # Iterate the loop until array length
        w___ (i < n

            # Create new node
            newNode = Node(arr[i])

            __ (i __ 0
                start = newNode
                newNode.prev = start
                temp = start

            ____
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next
            i = i + 1
        self.head = start
        r_ start

    ___ printList(self
        temp = self.head
        linked_list = ""
        w___(temp
            linked_list += (str(temp.data) + " ")
            temp = temp.next
        print(linked_list)

    # Function to count nunmber of
    # elements in the list

    ___ countList(self

        # Declare temp pointer to
        # traverse the list
        temp = self.head

        # Variable to store the count
        count = 0

        # Iterate the list and increment the count
        w___ (temp is not None
            temp = temp.next
            count = count + 1

        r_ count

    # we will consider that the index begin at 1
    ___ deleteAtLocation(self, index
      temp = self.head

      count = self.countList()

      __(count < index
        r_ temp

      __(index __ 1
        temp = temp.next
        self.head = temp
        r_ self.head

      __(count __ index
        w___(temp.next is not None and temp.next.next is not None
          temp = temp.next
         # 1 => 2 => 3 => 4
        temp.next = None
        r_ self.head
      

      i = 1 
      w___(i<index-1
        temp = temp.next
        i+=1
      

      prevNode = temp
      nodeAtTarget = temp.next
      nextNode = nodeAtTarget.next

      # 1 => 2 => 3 => 4

      nextNode.prev = prevNode
      prevNode.next = nextNode

      r_ self.head

        
# create an empty list

arr = [1, 2, 3, 4, 5]
llist = LinkedList()

llist.createList(arr)


llist.deleteAtLocation(2)

# print(llist.head)
llist.printList()
