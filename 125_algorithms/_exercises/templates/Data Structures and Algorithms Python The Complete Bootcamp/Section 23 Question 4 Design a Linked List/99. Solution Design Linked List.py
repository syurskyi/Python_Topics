c_ ListNode:
    ___  -   val):
        val  val
        prev  N..
        next  N..


c_ MyLinkedList:

    ___  -
        head  N..
        tail  N..
        size  0

    ___ get  index):
        __ index < 0 o. index > size:
            r_ -1

        cur  head

        w__ index ! 0:
            cur  cur.next
            index  index - 1

        r_ cur.val

    ___ addAtHead  val):
        new_node  ListNode(val)

        __ head __ N..:
            head  new_node
            tail  new_node
        ____
            new_node.next  head
            head.prev  new_node
            head  new_node

        size + 1

    ___ addAtTail  val):
        new_node  ListNode(val)

        __ head __ N..:
            head  new_node
            tail  new_node
        ____
            new_node.prev  tail
            tail.next  new_node
            tail  new_node

        size + 1

    ___ addAtIndex  index, val):
        __ index < 0 o. index > size:
            r_
        ____ index __ 0:
            addAtHead(val)
        ____ index __ size:
            addAtTail(val)
        ____
            cur  head
            w__ index - 1 ! 0:
                cur  cur.next
                index - 1

            new_node  ListNode(val)

            new_node.next  cur.next
            cur.next.prev  new_node
            cur.next  new_node
            new_node.prev  cur

            size + 1

    ___ deleteAtIndex  index):
        __ index < 0 o. index > size:
            r_
        ____ index __ 0:
            cur  head.next
            __ cur:
                cur.prev  N..

            head  head.next
            size - 1

            __ size __ 0:
                tail  N..
        ____ index __ size - 1:
            cur  tail.prev
            __ cur:
                cur.next  N..
            tail  tail.prev

            size - 1

            __ size __ 0:
                head  N..
        ____
            cur  head
            w__ index - 1 ! 0:
                cur  cur.next
                index - 1

            cur.next  cur.next.next
            cur.next.prev  cur

            size - 1


## Example Execution ##
obj  MyLinkedList()
obj.addAtHead(10)
obj.addAtTail(15)
obj.addAtTail(20)
obj.deleteAtIndex(0)
obj.addAtHead(40)

print(obj.get(1))