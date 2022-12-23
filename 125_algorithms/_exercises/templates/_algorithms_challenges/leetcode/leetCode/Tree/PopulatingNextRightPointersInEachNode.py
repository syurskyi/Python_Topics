"""
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL


给一颗二叉树，二叉树是满二叉树，每个节点默认 next 为 None，将每个节点的 next 指向它右边的一个。

需要使用 O（1）空间..

O(1) 空间没什么思路，目前用的两个列表存放Node.

也就是BFS.

beat 88%

测试地址：
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

"""
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

c.. Solution:
    # @param root, a tree link node
    # @return nothing
    ___ connect  root
        __ n.. root:
            r_
        
        current = [root]
        next_nodes   # list
        
        _____ current or next_nodes:
            ___ i __ current:
                __ i.left:
                    __ next_nodes:
                        next_nodes[-1].next = i.left
                        
                    next_nodes.a.. i.left)
                __ i.right:
                    __ next_nodes:
                        next_nodes[-1].next = i.right
                    
                    next_nodes.a.. i.right)
            
            current = next_nodes
            next_nodes   # list
        