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

c_ PeekingIterator(object):
  ___ - , iterator):
    """
    Initialize your data structure here.
    :type iterator: Iterator
    """
    iter = iterator
    nextElem = N..

  ___ peek
    """
    Returns the next element in the iteration without advancing the iterator.
    :rtype: int
    """
    __ nextElem:
      r.. nextElem
    __ iter.hasNext():
      nextElem = iter.next()
    r.. nextElem

  ___ next
    """
    :rtype: int
    """
    ret = nextElem

    __ nextElem:
      nextElem = N..
      r.. ret

    r.. iter.next()

  ___ hasNext
    """
    :rtype: bool
    """
    r.. (nextElem __ n.. N..) o. iter.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
