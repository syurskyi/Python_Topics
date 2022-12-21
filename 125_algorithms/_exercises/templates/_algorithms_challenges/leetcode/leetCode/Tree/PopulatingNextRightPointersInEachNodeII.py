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
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL

使用 BFS 和列表的额外空间的话 I 和 II没有任何区别...

待添加 O(1) 空间算法。

beat 72%.

测试地址：
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/

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
                        
                    next_nodes.append(i.left)
                __ i.right:
                    __ next_nodes:
                        next_nodes[-1].next = i.right
                    
                    next_nodes.append(i.right)
            
            current = next_nodes
            next_nodes   # list
            