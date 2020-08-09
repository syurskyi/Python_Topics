class Node:
    ___ __init__(self, data
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    ___ __init__(self
        self.head = None

    ___ createList(self, arr
        start = self.head
        n = le.(arr)

        temp = start
        i = 0

        w___(i < n
            newNode = Node(arr[i])
            __(i __ 0
                start = newNode
                temp = start
            ____
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next
            i += 1
        self.head = start
        r_ start

    ___ printList(self
        temp = self.head
        linked_list = ""
        w___(temp
            linked_list += (str(temp.data) + " ")
            temp = temp.next

        print(linked_list)
      

arr = [1,2,3,4,5]

llist = LinkedList()

llist.createList(arr)

llist.printList()
