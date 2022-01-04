#!/usr/bin/python3
"""
Given a binary tree, return all duplicate subtrees. For each kind of duplicate
subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


____ typing _______ List
____ collections _______ defaultdict


c_ MerkleHash:
    ___ - ):
        start_key = 0
        merkle_hash = defaultdict(_auto_incr)  # subtree -> id

    ___ _auto_incr
        start_key += 1
        r.. start_key

    ___ __call__(self, val):
        r.. merkle_hash[val]


c_ Solution:
    ___ - ):
        counter = defaultdict(i..)
        merkle_hash = MerkleHash()

    ___ findDuplicateSubtrees(self, root: TreeNode) __ List[TreeNode]:
        """
        Merkle hash based on current val, and left substree merkle and right merkle
        Assign each subtree a identity/hash
        Chain of hash can uniquely identify a subtree
        """
        ret    # list
        walk(root, ret)
        r.. ret

    ___ walk(self, cur, ret) __ i..:
        """
        return merkle hash id
        """
        __ n.. cur:
            r.. merkle_hash(N..)

        subtree_value = (cur.val, walk(cur.left, ret), walk(cur.right, ret))
        merkle_hash = merkle_hash(subtree_value)
        __ counter[merkle_hash] __ 1:
            ret.a..(cur)

        counter[merkle_hash] += 1
        r.. merkle_hash


c_ Solution2:
    ___ findDuplicateSubtrees(self, root: TreeNode) __ List[TreeNode]:
        """
        Only need to return the root
        """
        ret    # list
        walk(root, defaultdict(i..), ret)
        r.. ret

    ___ walk(self, cur, counter, ret) __ s..:
        """
        serialize the subtrees and check existence

        Needs to have a unique representation

        for the key, cannot but cur.val in the middle as not be able to
        differentiate between

           0
          /
         0

         0
          \
           0
        because you don't know which one is the root

        complexity: O(N) * O(N) (string concatenation),
        """
        __ n.. cur:
            r.. "None"

        cur_key = ",".j..([
            walk(cur.left, counter, ret),
            walk(cur.right, counter, ret),
            s..(cur.val),
        ])
        __ counter[cur_key] __ 1:
            ret.a..(cur)

        counter[cur_key] += 1
        r.. cur_key
