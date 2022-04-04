# Segment tree node
c_ STNode(o..
  ___ - , start, end
    start = start
    end = end
    total = 0
    left = N..
    right = N..


c_ SegmentedTree(o..
  ___ - , nums, start, end
    root = buildTree(nums, start, end)

  ___ buildTree  nums, start, end
    __ start > end:
      r.. N..

    __ start __ end:
      node = STNode(start, end)
      node.total = nums[start]
      r.. node

    mid = start + (end - start) / 2

    root = STNode(start, end)
    root.left = buildTree(nums, start, mid)
    root.right = buildTree(nums, mid + 1, end)
    root.total = root.left.total + root.right.total
    r.. root

  ___ updateVal  i, val
    ___ updateVal(root, i, val
      __ root.start __ root.end:
        root.total = val
        r.. val
      mid = root.start + (root.end - root.start) / 2
      __ i <_ mid:
        updateVal(root.left, i, val)
      ____
        updateVal(root.right, i, val)

      root.total = root.left.total + root.right.total
      r.. root.total

    r.. updateVal(root, i, val)

  ___ sumRange  i, j
    ___ rangeSum(root, start, end
      __ root.start __ start a.. root.end __ end:
        r.. root.total

      mid = root.start + (root.end - root.start) / 2
      __ j <_ mid:
        r.. rangeSum(root.left, start, end)
      ____ i >_ mid + 1:
        r.. rangeSum(root.right, start, end)
      ____
        r.. rangeSum(root.left, start, mid) + rangeSum(root.right, mid + 1, end)

    r.. rangeSum(root, i, j)


c_ NumArray(o..
  ___ - , nums
    """
    initialize your data structure here.
    :type nums: List[int]
    """
    stTree = SegmentedTree(nums, 0, l..(nums) - 1)

  ___ update  i, val
    """
    :type i: int
    :type val: int
    :rtype: int
    """
    r.. stTree.updateVal(i, val)

  ___ sumRange  i, j
    """
    sum of elements nums[i..j], inclusive.
    :type i: int
    :type j: int
    :rtype: int
    """
    r.. stTree.sumRange(i, j)

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
