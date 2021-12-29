"""
6 kyu: Consecutive strings
http://www.codewars.com/kata/consecutive-strings/train/python

You are given an array strarr of strings and an integer k.
Your task is to return the first longest string consisting of k consecutive strings taken in the array.

#Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
"""


___ longest_consec(strarr, k):
    n = l..(strarr)
    __ n __ 0 o. k > n o. k <= 0:
        r.. ''

    longest = index = 0
    ___ i __ r..(n - k + 1):
        length = s..([l..(s) ___ s __ strarr[i: i + k]])
        __ length > longest:
            longest = length
            index = i

    r.. ''.join(strarr[index: index + k])


... longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) __ "abigailtheta"
