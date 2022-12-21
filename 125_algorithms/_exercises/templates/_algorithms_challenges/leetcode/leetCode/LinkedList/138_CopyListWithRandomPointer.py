#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

c.. Solution o..
    # Hash table way, easy to understand. O(n) space costed.
    ___ copyRandomList  head
        __ n.. head:
            r_ None

        node_hash _ # dict
        cur_node = head
        _____ cur_node:
            cur_copy = RandomListNode(cur_node.label)
            node_hash[cur_node] = cur_copy
            cur_node = cur_node.next

        keep_head = node_hash[head]
        _____ head:
            head_copy = node_hash[head]
            head_copy.next = node_hash.get(head.next, None)
            head_copy.random = node_hash.get(head.random, None)
            head = head.next
        r_ keep_head

    # Solution 2, beats 85% of python submisssions.  Refer to:
    # https://leetcode.com/discuss/22421/solution-constant-space-complexity-linear-time-complexity
    ___ copyRandomList_1  head
        __ n.. head:
            r_ None

        # First round: make copy of each node,
        # and link them together side-by-side in a single list.
        cur_node = head
        _____ cur_node:
            next_node = cur_node.next
            copy_node = RandomListNode(cur_node.label)
            cur_node.next = copy_node
            copy_node.next = next_node
            cur_node = next_node

        # Second round: assign random pointers for the copy nodes.
        cur_node = head
        _____ cur_node:
            random_node = cur_node.random
            __ random_node:
                cur_node.next.random = random_node.next
            cur_node = cur_node.next.next

        # Third round: restore the original list, and extract the copy list.
        cur_node = head
        dummy_node = cur_copy_node = RandomListNode(0)
        _____ cur_node:
            next_node = cur_node.next.next
            # extract the copy list
            copy_node = cur_node.next
            cur_copy_node.next = copy_node
            cur_copy_node = copy_node
            # restore the original list
            cur_node.next = next_node
            cur_node = next_node

        r_ dummy_node.next
