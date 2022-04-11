c_ TrieNode(o..
  ___ - , bit_ N..
    isWord F..
    word N..
    one N..
    zero N..


count 0


c_ Solution(o..
  ___ findMaximumXOR  nums
    """
    :type nums: List[int]
    :rtype: int
    """

    ___ dfs(root, num, mask
      __ n.. root:
        r..
      __ mask __ 0x00:
        ans m..(ans, root.word ^ num)
        r..
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

    __ l..(nums) < 2:
      r.. 0
    root TrieNode()
    ans f__("-inf")
    ___ num __ nums:
      mask 0x80000000
      p root
      ___ i __ r..(0, 32
        node N..
        __ num & mask:
          __ n.. p.one:
            node TrieNode()
            p.one node
          ____
            node p.one
        ____
          __ n.. p.zero:
            node TrieNode()
            p.zero node
          ____
            node p.zero
        p node
        mask mask >> 1
      p.isWord T..
      p.word num
    ___ num __ nums:
      dfs(root, num, 0x80000000)
    r.. ans
