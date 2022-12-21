# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# https://leetcode.com/problems/path-sum-iii/discuss/91892/Python-solution-with-detailed-explanation
c_ Solution o..
    # def find_paths(self, root, target):
    #     if root:
    #         return int(root.val == target)
    #         + self.find_paths(root.left, target - root.val)
    #         + self.find_paths(root.right, target - root.val)
    #     return 0

    # def pathSum(self, root, sum):
    #     """
    #     :type root: TreeNode
    #     :type sum: int
    #     :rtype: int
    #     """
    #     if root:
    #         return self.find_paths(root, sum)
    #         + self.pathSum(root.left, sum)
    #         + self.pathSum(root.right, sum)
    #     return 0

    ___ pathSumHelper  root, target, so_far, cache
        __ root:
            # complement == 1, root->curr path
            complement = so_far + root.val - target
            __ complement __ cache:
                # S->E path, sum(root->S)-sum(root->E) = target
                result += cache[complement]
            cache[so_far + root.val] = cache.get(so_far + root.val, 0) + 1
            pathSumHelper(root.left, target, so_far + root.val, cache)
            pathSumHelper(root.right, target, so_far + root.val, cache)
            cache[so_far + root.val] -= 1
        r_

    ___ pathSum  root, s..
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        result = 0
        pathSumHelper(root, s.., 0, {0: 1})
        r_ result
