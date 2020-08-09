class TrieNode(object
  ___ __init__(self, bit=None
    self.isWord = False
    self.word = None
    self.one = None
    self.zero = None


count = 0


class Solution(object
  ___ findMaximumXOR(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """

    ___ dfs(root, num, mask
      __ not root:
        r_
      __ mask __ 0x00:
        self.ans = max(self.ans, root.word ^ num)
        r_
      __ mask & num:
        __ root.zero:
          dfs(root.zero, num, mask >> 1)
        ____
          dfs(root.one, num, mask >> 1)
      ____
        __ root.one:
          dfs(root.one, num, mask >> 1)
        ____
          dfs(root.zero, num, mask >> 1)

    __ le.(nums) < 2:
      r_ 0
    root = TrieNode()
    self.ans = float("-inf")
    for num in nums:
      mask = 0x80000000
      p = root
      for i in range(0, 32
        node = None
        __ num & mask:
          __ not p.one:
            node = TrieNode()
            p.one = node
          ____
            node = p.one
        ____
          __ not p.zero:
            node = TrieNode()
            p.zero = node
          ____
            node = p.zero
        p = node
        mask = mask >> 1
      p.isWord = True
      p.word = num
    for num in nums:
      dfs(root, num, 0x80000000)
    r_ self.ans
