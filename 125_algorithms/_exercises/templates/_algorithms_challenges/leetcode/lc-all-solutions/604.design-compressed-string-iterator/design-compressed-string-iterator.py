class StringIterator(object):

  ___ __init__(self, compressedString):
    """
    :type compressedString: str
    """
    self.data = compressedString
    self.idx = -1
    self.decodeNext()

  ___ decodeNext(self):
    self.idx += 1
    __ self.idx + 1 < l..(self.data):
      self.cur = self.data[self.idx]
      end = self.idx + 1
      w.... end < l..(self.data) a.. self.data[end].isdigit():
        end += 1
      print
      end
      self.num = int(self.data[self.idx + 1:end])
      self.idx = end - 1

  ___ next(self):
    """
    :rtype: str
    """
    __ self.hasNext():
      ret = self.cur
      self.num -= 1
      __ self.num <= 0:
        self.decodeNext()
      r.. ret
    r.. " "

  ___ hasNext(self):
    """
    :rtype: bool
    """
    r.. self.idx < l..(self.data) a.. self.num > 0

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
