# Segment tree node
class STNode(object):
  ___ __init__(self, start, end):
    self.start = start
    self.end = end
    self.total = 0
    self.left = None
    self.right = None


class SegmentedTree(object):
  ___ __init__(self, nums, start, end):
    self.root = self.buildTree(nums, start, end)

  ___ buildTree(self, nums, start, end):
    __ start > end:
      return None

    __ start == end:
      node = STNode(start, end)
      node.total = nums[start]
      return node

    mid = start + (end - start) / 2

    root = STNode(start, end)
    root.left = self.buildTree(nums, start, mid)
    root.right = self.buildTree(nums, mid + 1, end)
    root.total = root.left.total + root.right.total
    return root

  ___ updateVal(self, i, val):
    ___ updateVal(root, i, val):
      __ root.start == root.end:
        root.total = val
        return val
      mid = root.start + (root.end - root.start) / 2
      __ i <= mid:
        updateVal(root.left, i, val)
      else:
        updateVal(root.right, i, val)

      root.total = root.left.total + root.right.total
      return root.total

    return updateVal(self.root, i, val)

  ___ sumRange(self, i, j):
    ___ rangeSum(root, start, end):
      __ root.start == start and root.end == end:
        return root.total

      mid = root.start + (root.end - root.start) / 2
      __ j <= mid:
        return rangeSum(root.left, start, end)
      elif i >= mid + 1:
        return rangeSum(root.right, start, end)
      else:
        return rangeSum(root.left, start, mid) + rangeSum(root.right, mid + 1, end)

    return rangeSum(self.root, i, j)


class NumArray(object):
  ___ __init__(self, nums):
    """
    initialize your data structure here.
    :type nums: List[int]
    """
    self.stTree = SegmentedTree(nums, 0, len(nums) - 1)

  ___ update(self, i, val):
    """
    :type i: int
    :type val: int
    :rtype: int
    """
    return self.stTree.updateVal(i, val)

  ___ sumRange(self, i, j):
    """
    sum of elements nums[i..j], inclusive.
    :type i: int
    :type j: int
    :rtype: int
    """
    return self.stTree.sumRange(i, j)

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
