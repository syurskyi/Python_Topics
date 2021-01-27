#   Created by Elshad Karimov on 18/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

from LinkedList import LinkedList

___ nthToLast(ll, n
    pointer1 = ll.head
    pointer2 = ll.head

    ___ i __ range(n
        __ pointer2 __ N..:
            r_ N..
        pointer2 = pointer2.next

    w__ pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    r_ pointer1

customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(nthToLast(customLL, 3))