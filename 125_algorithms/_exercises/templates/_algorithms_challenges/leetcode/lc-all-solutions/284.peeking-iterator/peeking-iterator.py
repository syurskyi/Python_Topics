# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object
#     ___ __init__(self, nums
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     ___ hasNext(self
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     ___ next(self
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object
  ___ __init__(self, iterator
    """
    Initialize your data structure here.
    :type iterator: Iterator
    """
    self.iter = iterator
    self.nextElem = None

  ___ peek(self
    """
    Returns the next element in the iteration without advancing the iterator.
    :rtype: int
    """
    __ self.nextElem:
      r_ self.nextElem
    __ self.iter.hasNext(
      self.nextElem = self.iter.next()
    r_ self.nextElem

  ___ next(self
    """
    :rtype: int
    """
    ret = self.nextElem

    __ self.nextElem:
      self.nextElem = None
      r_ ret

    r_ self.iter.next()

  ___ hasNext(self
    """
    :rtype: bool
    """
    r_ (self.nextElem is not None) or self.iter.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# w___ iter.hasNext(
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
