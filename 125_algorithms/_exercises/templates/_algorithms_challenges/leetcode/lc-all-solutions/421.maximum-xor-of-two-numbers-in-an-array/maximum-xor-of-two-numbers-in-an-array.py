class TrieNode(object):
  ___ __init__(self, bit_ N..
    self.isWord = False
    self.word = None
    self.one = None
    self.zero = None


count = 0


class Solution(object):
  ___ findMaximumXOR(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    ___ dfs(root, num, mask):
      __ not root:
        return
      __ mask == 0x00:
        self.ans = max(self.ans, root.word ^ num)
        return
      __ mask & num:
        __ root.zero:
          dfs(root.zero, num, mask >> 1)
        else:
          dfs(root.one, num, mask >> 1)
      else:
        __ root.one:
          dfs(root.one, num, mask >> 1)
        else:
          dfs(root.zero, num, mask >> 1)

    __ len(nums) < 2:
      return 0
    root = TrieNode()
    self.ans = float("-inf")
    for num in nums:
      mask = 0x80000000
      p = root
      for i in range(0, 32):
        node = None
        __ num & mask:
          __ not p.one:
            node = TrieNode()
            p.one = node
          else:
            node = p.one
        else:
          __ not p.zero:
            node = TrieNode()
            p.zero = node
          else:
            node = p.zero
        p = node
        mask = mask >> 1
      p.isWord = True
      p.word = num
    for num in nums:
      dfs(root, num, 0x80000000)
    return self.ans
