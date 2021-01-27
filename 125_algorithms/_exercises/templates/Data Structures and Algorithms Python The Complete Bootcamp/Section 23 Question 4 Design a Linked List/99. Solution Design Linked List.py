class ListNode:
    ___ __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    ___ __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    ___ get(self, index):
        __ index < 0 or index >= self.size:
            r_ -1

        cur = self.head

        w__ index != 0:
            cur = cur.next
            index = index - 1

        r_ cur.val

    ___ addAtHead(self, val):
        new_node = ListNode(val)

        __ self.head is None:
            self.head = new_node
            self.tail = new_node
        ____
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    ___ addAtTail(self, val):
        new_node = ListNode(val)

        __ self.head is None:
            self.head = new_node
            self.tail = new_node
        ____
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    ___ addAtIndex(self, index, val):
        __ index < 0 or index > self.size:
            r_
        elif index __ 0:
            self.addAtHead(val)
        elif index __ self.size:
            self.addAtTail(val)
        ____
            cur = self.head
            w__ index - 1 != 0:
                cur = cur.next
                index -= 1

            new_node = ListNode(val)

            new_node.next = cur.next
            cur.next.prev = new_node
            cur.next = new_node
            new_node.prev = cur

            self.size += 1

    ___ deleteAtIndex(self, index):
        __ index < 0 or index >= self.size:
            r_
        elif index __ 0:
            cur = self.head.next
            __ cur:
                cur.prev = None

            self.head = self.head.next
            self.size -= 1

            __ self.size __ 0:
                self.tail = None
        elif index __ self.size - 1:
            cur = self.tail.prev
            __ cur:
                cur.next = None
            self.tail = self.tail.prev

            self.size -= 1

            __ self.size __ 0:
                self.head = None
        ____
            cur = self.head
            w__ index - 1 != 0:
                cur = cur.next
                index -= 1

            cur.next = cur.next.next
            cur.next.prev = cur

            self.size -= 1


## Example Execution ##
obj = MyLinkedList()
obj.addAtHead(10)
obj.addAtTail(15)
obj.addAtTail(20)
obj.deleteAtIndex(0)
obj.addAtHead(40)

print(obj.get(1))