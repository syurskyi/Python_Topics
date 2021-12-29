class Logger(object):

  ___ __init__(self):
    """
    Initialize your data structure here.
    """
    self.d = {}

  ___ shouldPrintMessage(self, timestamp, message):
    """
    Returns true if the message should be printed in the given timestamp, otherwise returns false.
    If this method returns false, the message will not be printed.
    The timestamp is in seconds granularity.
    :type timestamp: int
    :type message: str
    :rtype: bool
    """
    __ message not in self.d:
      self.d[message] = timestamp
      return True
    elif timestamp - self.d[message] >= 10:
      self.d[message] = timestamp
      return True
    return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
