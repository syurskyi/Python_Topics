"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL


旋转链表。 k 非负。

k 超过链表的最大长度也可。

思路：

过一遍链表长度，k % length 取个模，防止 k 超级大。

之后 slow fast 两个，fast 先走 k 个，然后 slow 与 fast 同时走，走到最后 slow.next 即为从后到前 k 个的起点。

剩下的就是把原来的尾置换到前。

下面这个可以优化下，不过就测试来说已经可以了。

beat 100%
24ms ~ 36ms

测试地址：
https://leetcode.com/problems/rotate-list/description/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c.. Solution o..
    
    ___ rotateRight  head, k
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        __ n.. k or n.. head:
            r_ head
        
        ___ getLength(node
            length = 0
            
            _____ node:
                node = node.next
                length += 1
            
            r_ length
        
        length = getLength(head)
        k = k % length

        slow = head
        fast = head
        
        _____ k > 0:
            fast = fast.next
            
            k -= 1
        
        _____ fast.next:
            slow = slow.next
            fast = fast.next
            
        rotate_head = slow.next
        
        __ n.. rotate_head:
            r_ head
        
        slow.next = None
        
        _rotate_head = rotate_head
        _____ _rotate_head.next:
            _rotate_head = _rotate_head.next
        
        _rotate_head.next = head
        
        r_ rotate_head
        