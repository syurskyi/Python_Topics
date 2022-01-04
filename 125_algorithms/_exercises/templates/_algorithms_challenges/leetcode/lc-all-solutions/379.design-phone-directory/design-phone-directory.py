____ c.. _______ d..


c_ PhoneDirectory(object):

  ___ - , maxNumbers):
    """
    Initialize your data structure here
    @param maxNumbers - The maximum numbers that can be stored in the phone directory.
    :type maxNumbers: int
    """
    taken = [T..] * maxNumbers
    q = d..([i ___ i __ r..(0, maxNumbers)])

  ___ get
    """
    Provide a number which is not assigned to anyone.
    @return - Return an available number. Return -1 if none is available.
    :rtype: int
    """
    __ q:
      taken[q[0]] = F..
      r.. q.popleft()
    r.. -1

  ___ check(self, number):
    """
    Check if a number is available or not.
    :type number: int
    :rtype: bool
    """
    r.. taken[number]

  ___ release(self, number):
    """
    Recycle or release a number.
    :type number: int
    :rtype: void
    """
    __ n.. taken[number]:
      taken[number] = T..
      q.a..(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
