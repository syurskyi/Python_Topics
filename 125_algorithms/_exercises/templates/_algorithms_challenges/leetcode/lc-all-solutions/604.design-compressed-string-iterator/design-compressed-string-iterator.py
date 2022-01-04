c_ StringIterator(object):

  ___ - , compressedString):
    """
    :type compressedString: str
    """
    data = compressedString
    idx = -1
    decodeNext()

  ___ decodeNext
    idx += 1
    __ idx + 1 < l..(data):
      cur = data[idx]
      end = idx + 1
      w.... end < l..(data) a.. data[end].isdigit
        end += 1
      print
      end
      num = i..(data[idx + 1:end])
      idx = end - 1

  ___ next
    """
    :rtype: str
    """
    __ hasNext
      ret = cur
      num -= 1
      __ num <= 0:
        decodeNext()
      r.. ret
    r.. " "

  ___ hasNext
    """
    :rtype: bool
    """
    r.. idx < l..(data) a.. num > 0

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
