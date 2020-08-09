class Solution(object
  ___ isHappy(self, n
    """
    :type n: int
    :rtype: bool
    """
    record = {}
    sq_sum = 0
    w___ n != 1:
      sq_sum = 0
      sub_num = n
      w___ sub_num > 0:
        sq_sum += (sub_num % 10) * (sub_num % 10)
        sub_num /= 10
      __ sq_sum in record:
        r_ False
      ____
        record[sq_sum] = 1
      n = sq_sum
    r_ True
