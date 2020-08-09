class Node:

    ___ __init__(self, data
        self.data = data
        self.next = None


class LinkedList:

    ___ __init__(self
        self.head = None

    ___ printList(self
        temp = self.head
        linked_list = ""
        w___(temp
            linked_list += (str(temp.data) + " ")
            temp = temp.next
        print(linked_list)

    # list start at 0
    ___ insertNode(self, val, pos
        target = Node(val)
        __(pos __ 0
            target.next = self.head
            self.head = target
            r_

        ___ getPrev(pos
            temp = self.head
            count = 1
            w___(count < pos
                temp = temp.next
                count += 1
            r_ temp

        prev = getPrev(pos)
        nextNode = prev.next

        prev.next = target
        target.next = nextNode


# List Structure : 5 => 1 => 3 => 7
linked_list = LinkedList()
linked_list.head = Node(5)

second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)

linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node

linked_list.insertNode(2, 2)
linked_list.printList()
