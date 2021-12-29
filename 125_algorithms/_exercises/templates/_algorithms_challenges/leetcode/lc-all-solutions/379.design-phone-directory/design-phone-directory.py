from collections import deque


class PhoneDirectory(object):

  ___ __init__(self, maxNumbers):
    """
    Initialize your data structure here
    @param maxNumbers - The maximum numbers that can be stored in the phone directory.
    :type maxNumbers: int
    """
    self.taken = [True] * maxNumbers
    self.q = deque([i for i in range(0, maxNumbers)])

  ___ get(self):
    """
    Provide a number which is not assigned to anyone.
    @return - Return an available number. Return -1 if none is available.
    :rtype: int
    """
    __ self.q:
      self.taken[self.q[0]] = False
      return self.q.popleft()
    return -1

  ___ check(self, number):
    """
    Check if a number is available or not.
    :type number: int
    :rtype: bool
    """
    return self.taken[number]

  ___ release(self, number):
    """
    Recycle or release a number.
    :type number: int
    :rtype: void
    """
    __ not self.taken[number]:
      self.taken[number] = True
      self.q.append(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
