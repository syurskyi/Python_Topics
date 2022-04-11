c_ Solution(o..
  ___ isHappy  n
    """
    :type n: int
    :rtype: bool
    """
    record    # dict
    sq_sum 0
    w.... n != 1:
      sq_sum 0
      sub_num n
      w.... sub_num > 0:
        sq_sum += (sub_num % 10) * (sub_num % 10)
        sub_num /= 10
      __ sq_sum __ record:
        r.. F..
      ____
        record[sq_sum] 1
      n sq_sum
    r.. T..
