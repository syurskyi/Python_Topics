# Add Binary
# Question: Given two binary strings, return their sum (also a binary string).
# For example,
# a = "11"
# b = "1"
# Return "100".
# Solutions:
c_ Solution:
    ___ addBinary( a, b):
        length _ ma.(le.(a),le.(b)) + 1
        su. _ ['0' ___ i __ ra..(length)]
        __ le.(a) <_ le.(b):
            a _ '0' * ( le.(b) - le.(a) ) + a
        __ le.(a) > le.(b):
            b _ '0' * ( le.(a) - le.(b) ) + b
        Carry _ 0
        i _ le.(a) - 1
        w___ i >_ 0:
            __ in.(a[i]) + in.(b[i]) + Carry __ 3:
                su.[i+1] _ '1'
                Carry _ 1
            ____ in.(a[i]) + in.(b[i]) + Carry __ 2:
                su.[i+1] _ '0'
                Carry _ 1
            ____ in.(a[i]) + in.(b[i]) + Carry __ 1:
                su.[i+1] _ '1'
                Carry _ 0
            ____
                su.[i+1] _ '0'
                Carry _ 0
            i _ i - 1
        __ Carry __ 1:
            su.[0] _ '1'
        __ Carry __ 0:
            su. _ su.[1:length]
        su. _ ''.j..(su.)
        r_ su.

Solution.addBinary("11","1")

c_ Solution:
    ___ addBinary(a, b):
        bia _ in.(a, 2)
        bib _ in.(b, 2)
        su. _ bia + bib
        r_ st.("{0:b}".f..(su.))

Solution.addBinary("1","11")
# *Should only use if asked for shorter solution. It converts binary to integers; sum the integers. And finally formats the answer as binary.