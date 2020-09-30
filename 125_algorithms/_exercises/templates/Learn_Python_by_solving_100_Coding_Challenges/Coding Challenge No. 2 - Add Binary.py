# Add Binary
# Question: Given two binary strings, return their sum (also a binary string).
# For example,
# a = "11"
# b = "1"
# Return "100".
# Solutions:
class Solution:
    ___ addBinary( a, b):
        length = ma.(len(a),len(b)) + 1
        sum = ['0' ___ i __ ra..(length)]
        if len(a) <= len(b):
            a = '0' * ( len(b) - len(a) ) + a
        if len(a) > len(b):
            b = '0' * ( len(a) - len(b) ) + b
        Carry = 0
        i = len(a) - 1
        while i >= 0:
            if int(a[i]) + int(b[i]) + Carry == 3:
                sum[i+1] = '1'
                Carry = 1
            elif int(a[i]) + int(b[i]) + Carry == 2:
                sum[i+1] = '0'
                Carry = 1
            elif int(a[i]) + int(b[i]) + Carry == 1:
                sum[i+1] = '1'
                Carry = 0
            else:
                sum[i+1] = '0'
                Carry = 0
            i = i - 1
        if Carry == 1:
            sum[0] = '1'
        if Carry == 0:
            sum = sum[1:length]
        sum = ''.join(sum)
        r_ sum

Solution.addBinary("11","1")

class Solution:
    ___ addBinary(a, b):
        bia = int(a, 2)
        bib = int(b, 2)
        sum = bia + bib
        r_ str("{0:b}".format(sum))

Solution.addBinary("1","11")
# *Should only use if asked for shorter solution. It converts binary to integers; sum the integers. And finally formats the answer as binary.