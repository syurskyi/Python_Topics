#!/usr/bin/python3
"""
We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this
node), then we output the value of this node.  (If the depth of a node is D, the
depth of its immediate child is D+1.  The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.


Example 1:
Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:
Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]


Example 3:
Input: "1-401--349---90--88"
Output: [1,401,null,349,88,90]


Note:
The number of nodes in the original tree is between 1 and 1000.
Each node will have a value between 1 and 10^9.
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..

____ c.. _______ OrderedDict


c_ Solution:
    ___ recoverFromPreorder  S: s..) __ TreeNode:
        """
        map: node -> depth
        stack of pi (incompleted)
        """
        depth = 0
        # parse
        n = l..(S)
        i = 0
        root = N..
        stk    # list
        w.... i < n:
            __ S[i] __ "-":
                depth += 1
                i += 1
            ____:
                j = i
                w.... j < n a.. S[j] != "-":
                    j += 1

                val = i..(S[i:j])

                # construct
                cur = TreeNode(val)
                __ depth __ 0:
                    root = cur
                    stk = [(depth, root)]
                ____:
                    ... stk
                    w.... stk[-1][0] != depth - 1:
                        stk.pop()

                    _, pi = stk[-1]
                    __ n.. pi.left:
                        pi.left = cur
                    ____ n.. pi.right:
                        pi.right = cur
                        stk.pop()
                    ____:
                        r..
                    stk.a..((depth, cur))

                depth = 0
                i = j

        r.. root

    ___ recoverFromPreorder_error  S: s..) __ TreeNode:
        """
        map: node -> depth
        stack of pi (incompleted)
        """
        depth = 0
        depths = OrderedDict()
        # parse
        n = l..(S)
        i = 0
        w.... i < n:
            __ S[i] __ "-":
                depth += 1
                i += 1
            ____:
                j = i
                w.... j < n a.. S[j] != "-":
                    j += 1

                val = i..(S[i:j])
                depths[val] = depth
                depth = 0
                i = j

        # construct
        stk    # list
        root = N..
        ___ k, v __ depths.i..:
            cur = TreeNode(k)
            __ v __ 0:
                root = cur
                stk = [root]
            ____:
                ... stk
                w.... depths[stk[-1].val] != v - 1:
                    stk.pop()

                __ n.. stk[-1].left:
                    stk[-1].left = cur
                ____ n.. stk[-1].right:
                    stk[-1].right = cur
                    stk.pop()
                ____:
                    r..
                stk.a..(cur)

        r.. root


__ _______ __ _______
    ... Solution().recoverFromPreorder("5-4--4")
    ... Solution().recoverFromPreorder("1-2--3--4-5--6--7")
