#!/usr/bin/python3
"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go
downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000
to 1,000,000.
"""
# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


____ collections _______ defaultdict


c_ Solution:
    ___ - ):
        count = 0

    ___ pathSum(self, root: TreeNode, target: i..) __ i..:
        """
        The path does not need to start or end at the root or a leaf, but it
        must go downwards (traveling only from parent nodes to child nodes).

        Downward path
        """
        dfs(root, target, 0, defaultdict(i..))
        r.. count

    ___ dfs(self, node, target, cur_sum, prefix_sum_counter):
        __ n.. node:
            r..

        cur_sum += node.val
        # delta = target - cur_sum  # error
        delta = cur_sum - target
        count += prefix_sum_counter[delta]
        __ delta __ 0:
            count += 1

        prefix_sum_counter[cur_sum] += 1
        dfs(node.left, target, cur_sum, prefix_sum_counter)
        dfs(node.right, target, cur_sum, prefix_sum_counter)
        prefix_sum_counter[cur_sum] -= 1
        

c_ SolutionComplex:
    ___ pathSum(self, root, s..):
        """
        Brute force: two dfs, O(n^2)

        Prefix sum in Tree, starting from root - O(n)
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        count = [0]  # pass as a reference
        dfs(root, s.., 0, {}, count)
        r.. count[0]

    ___ dfs(self, root, s.., cur_sum, prefix_sum, count):
        """
        Root to node sum
        prefix_sum: Dict[int, int], sum -> count
        """
        __ n.. root:
            r..

        cur_sum += root.val
        # ∃ prefix_sum: cur_sum - prefix_sum = sum
        diff = cur_sum - s..
        __ diff __ prefix_sum:
            count[0] += prefix_sum[diff]
        __ diff __ 0:  # trivial case
            count[0] += 1

        prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1
        dfs(root.left, s.., cur_sum, prefix_sum, count)
        dfs(root.right, s.., cur_sum, prefix_sum, count)
        prefix_sum[cur_sum] -= 1  # pop to save space
