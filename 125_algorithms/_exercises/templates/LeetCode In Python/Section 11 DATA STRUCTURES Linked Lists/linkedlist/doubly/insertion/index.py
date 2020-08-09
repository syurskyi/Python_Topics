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

    ___ countList(self
        temp = self.head
        count = 0
        w___(temp is not None
            temp = temp.next
            count += 1
        r_ count

    # we will consider that the index begin at 1
    ___ insertAtLocation(self, value, index
        temp = self.head

        count = self.countList()

        #index is 6, count is 5, valid 
        #index is 7, count is 5, 
        __(count+1<index
            r_ temp
        
        newNode = Node(value)

        __(index __ 1
            newNode.next = temp
            temp.prev = newNode
            self.head = newNode
            r_ self.head
        
        __(index __ count +1
            w___(temp.next is not None
                temp = temp.next

            temp.next = newNode
            newNode.prev = temp 
            r_ self.head
        
        i = 1
        w___(i < index-1
            temp = temp.next
            i+=1
        
        nodeAtTarget = temp.next

        newNode.next = nodeAtTarget
        nodeAtTarget.prev = newNode

        temp.next = newNode
        newNode.prev = temp

        r_ self.head


arr = [1, 2, 3, 4, 5]

llist = LinkedList()

llist.createList(arr)

llist.insertAtLocation(5,6)

llist.printList()
