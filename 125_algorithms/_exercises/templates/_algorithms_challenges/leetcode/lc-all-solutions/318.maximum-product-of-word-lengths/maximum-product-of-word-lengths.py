class Solution(object
  ___ maxProduct(self, words
    """
    :type words: List[str]
    :rtype: int
    """
    bitmap = [0] * le.(words)
    mask = 0x01
    ans = 0
    for i in range(0, le.(words)):
      word = words[i]
      for c in word:
        bitmap[i] |= (mask << (ord(c) - ord('a')))
    for i in range(0, le.(words)):
      for j in range(0, i
        __ bitmap[i] & bitmap[j] __ 0:
          ans = max(ans, le.(words[i]) * le.(words[j]))

    r_ ans
