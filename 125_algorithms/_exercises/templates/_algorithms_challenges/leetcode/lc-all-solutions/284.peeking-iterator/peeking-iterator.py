# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
  ___ __init__(self, iterator):
    """
    Initialize your data structure here.
    :type iterator: Iterator
    """
    self.iter = iterator
    self.nextElem = None

  ___ peek(self):
    """
    Returns the next element in the iteration without advancing the iterator.
    :rtype: int
    """
    __ self.nextElem:
      return self.nextElem
    __ self.iter.hasNext():
      self.nextElem = self.iter.next()
    return self.nextElem

  ___ next(self):
    """
    :rtype: int
    """
    ret = self.nextElem

    __ self.nextElem:
      self.nextElem = None
      return ret

    return self.iter.next()

  ___ hasNext(self):
    """
    :rtype: bool
    """
    return (self.nextElem is not None) or self.iter.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
