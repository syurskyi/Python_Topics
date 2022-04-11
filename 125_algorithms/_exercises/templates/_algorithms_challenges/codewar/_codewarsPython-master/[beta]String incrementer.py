_______ __
___ increment_string(strng
    strMatch __.m..(r'([\w]*)(\d*)',strng)
    stringPart,numberPart strMatch.group(1),strMatch.group(2)
    number __.m..(r'0*(\d*)',numberPart).group(1)
    number 1 __ l..(number) __ 0 ____ i..(number) + 1
    __ l..(s..(number >_ l..(numberPart
        number number
    ____ :
        number ('0' * (l..(numberPart) - l..(s..(number)))) + s..(number)
    r.. stringPart + s..(number)
    


print(increment_string('foobar123'
print(increment_string('foobar0056'
print(increment_string('foobar'
print(increment_string('035'
print(increment_string(''
print(increment_string('p)L2_9:0R[800755806{OtCsowX8847280959000119'