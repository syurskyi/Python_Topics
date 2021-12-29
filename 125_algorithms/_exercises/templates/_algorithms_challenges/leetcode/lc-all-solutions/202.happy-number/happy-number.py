class Solution(object):
  ___ isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    record = {}
    sq_sum = 0
    while n != 1:
      sq_sum = 0
      sub_num = n
      while sub_num > 0:
        sq_sum += (sub_num % 10) * (sub_num % 10)
        sub_num /= 10
      __ sq_sum __ record:
        r.. False
      ____:
        record[sq_sum] = 1
      n = sq_sum
    r.. True
