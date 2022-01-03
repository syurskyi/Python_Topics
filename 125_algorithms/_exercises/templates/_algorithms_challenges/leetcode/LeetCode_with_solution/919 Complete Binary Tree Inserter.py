#!/usr/bin/python3
"""
A complete binary tree is a binary tree in which every level, except possibly
the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary
tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with
head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value
node.val = v so that the tree remains complete, and returns the value of the
parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.

Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs =
[[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]

Note:
The initial given tree is complete and contains between 1 and 1000 nodes.
CBTInserter.insert is called at most 10000 times per test case.
Every value of a given or inserted node is between 0 and 5000.
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


____ collections _______ deque


c_ CBTInserter:
    ___ - , root: TreeNode):
        """
        Maintain a dequeue of insertion candidates
        Insertion candidates are non-full nodes (superset of leaf nodes)
        BFS to get the insertion candidates

        During insertion, insert the node to the first insertion candidate's
        child. Then, the inserting node is the last in the candidate queue
        """
        candidates = deque()
        root = root
        q = [root]  # can also use deque
        w.... q:
            cur_q    # list
            ___ e __ q:
                __ e.left:
                    cur_q.a..(e.left)
                __ e.right:
                    cur_q.a..(e.right)
                __ n.. e.left o. n.. e.right:
                    # non-full node
                    candidates.a..(e)
            q = cur_q

    ___ insert(self, v: int) -> int:
        pi = candidates[0]
        node = TreeNode(v)
        __ n.. pi.left:
            pi.left = node
        ____:
            pi.right = node

        __ pi.left a.. pi.right:
            candidates.popleft()

        candidates.a..(node)
        r.. pi.val

    ___ get_root(self) -> TreeNode:
        r.. root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
