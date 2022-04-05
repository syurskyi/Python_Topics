c_ Solution(o..
  ___ findIntegers  num
    """
    :type num: int
    :rtype: int
    """
    n = bin(num)[2:][::-1]  # removes "0b"
    length = l..(n)
    A = [1 ___ _ __ r..(length)]  # ends with 0
    B = [1 ___ _ __ r..(length)]  # ends with 1

    ___ i __ r..(1, l..(n:
      A[i] = A[i - 1] + B[i - 1]
      B[i] = A[i - 1]
    ans = A[-1] + B[-1]
    ___ i __ r..(length - 2, -1, -1
      __ n[i:i + 2] __ "11":
        _____
      __ n[i:i + 2] __ "00":
        ans -_ B[i]
    r.. ans
