"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..

# Definition for singly-linked list.
c_ ListNode:
    ___ - , x):
        val = x
        next = N..

c_ Solution:
    # class attribute to keep trace the currently processing nodes
    # current_node = None
    ___ - ):
        current_node = N..  # !important, avoid time complexity of look up

    ___ sortedListToBST(self, head):
        """
        dfs
        No O(1) access.
        Bottom-up construction
        :param head: ListNode
        :return: TreeNode
        """
        __ n.. head:
            r.. head

        current_node = head
        length = getLength(head)
        r.. sortedListToBST_dfs(0, length-1)

    ___ sortedListToBST_dfs(self, start, end):
        __ start>end:
            r..
        mid = (start+end)/2
        left_subtree = sortedListToBST_dfs(start, mid-1)
        root = TreeNode(current_node.val)
        current_node = current_node.next
        right_subtree = sortedListToBST_dfs(mid+1, end)

        root.left = left_subtree
        root.right = right_subtree
        r.. root

    ___ getLength(self, head):
        count = 0
        w.... head:
            head = head.next
            count += 1
        r.. count