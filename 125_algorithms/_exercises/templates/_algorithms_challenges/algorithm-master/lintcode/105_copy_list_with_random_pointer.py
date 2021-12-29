"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


"""
using hashmap
time: O(2n) => O(n)
space: O(n)
"""
class Solution:
    ___ copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        N = {}
        dummy = tail = RandomListNode(-1)

        w.... head:
            node = RandomListNode(head.label)
            node.random = head.random
            tail.next = node
            N[head] = node
            tail = tail.next
            head = head.next

        head = dummy.next
        w.... head:
            __ head.random:
                head.random = N[head.random]
            head = head.next

        r.. dummy.next


"""
temply save in n.next
time: O(3n) => O(n)
space: O(1)


example: 1->2->3

copy_next/
    |--------->|
    1 -> 1' -> 2 -> 2' -> 3 -> 3'
replace_random/
         |--------->|
    |----+---->|    |
    1 -> 1' -> 2 -> 2' -> 3 -> 3'
split_list/
    |--------->|
    1    ->    2    ->    3
         1'   ->    2'   ->    3'
         |--------->|
"""
class Solution:
    ___ copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        __ n.. head:
            r..

        tail = head
        node = N..
        w.... tail:
            node = RandomListNode(tail.label)
            node.random = tail.random
            node.next = tail.next
            tail.next = node
            tail = tail.next.next

        tail = head
        w.... tail:
            __ tail.next a.. tail.random:
                tail.next.random = tail.random.next
            tail = tail.next.next

        node = tail = head.next
        w.... tail a.. tail.next:
            tail.next = tail.next.next
            tail = tail.next

        r.. node
