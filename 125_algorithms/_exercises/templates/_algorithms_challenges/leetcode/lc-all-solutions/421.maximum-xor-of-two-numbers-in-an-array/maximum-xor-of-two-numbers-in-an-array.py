class TrieNode(object):
  ___ __init__(self, bit_ N..
    self.isWord = False
    self.word = N..
    self.one = N..
    self.zero = N..


count = 0


class Solution(object):
  ___ findMaximumXOR(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    ___ dfs(root, num, mask):
      __ n.. root:
        r..
      __ mask __ 0x00:
        self.ans = max(self.ans, root.word ^ num)
        r..
      __ mask & num:
        __ root.zero:
          dfs(root.zero, num, mask >> 1)
        ____:
          dfs(root.one, num, mask >> 1)
      ____:
        __ root.one:
          dfs(root.one, num, mask >> 1)
        ____:
          dfs(root.zero, num, mask >> 1)

    __ l..(nums) < 2:
      r.. 0
    root = TrieNode()
    self.ans = float("-inf")
    ___ num __ nums:
      mask = 0x80000000
      p = root
      ___ i __ r..(0, 32):
        node = N..
        __ num & mask:
          __ n.. p.one:
            node = TrieNode()
            p.one = node
          ____:
            node = p.one
        ____:
          __ n.. p.zero:
            node = TrieNode()
            p.zero = node
          ____:
            node = p.zero
        p = node
        mask = mask >> 1
      p.isWord = True
      p.word = num
    ___ num __ nums:
      dfs(root, num, 0x80000000)
    r.. self.ans
