"""
Given an integer number, find the most frequent digit in it.

Examples:

1998 -> two 9's, one 1, one 8 so return 9
177 -> return 7
2020 -> there is 2 two's, 2 zero's. Return 2 = the first highest hitter
12345 -> all digits occur once, so like the last example return the first digit = 1
Food for thought: how to count things efficiently?

Have fun and keep calm and code in Python!
"""

"""
GENERIC PROBLEM:

How to sort a dictionary using value as a key?

https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
"""

def freq_digit(num: int) -> int:

    dict_num = {}
    num_str = str(num)
    for num in num_str:
        try:
            dict_num[num] += 1
        except:
            dict_num[num] = 1
    m = max(dict_num, key=lambda key: dict_num[key])
    return int(m)


print(freq_digit(748791789189717891789))