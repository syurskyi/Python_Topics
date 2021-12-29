s..  input("Insert strings with integer values: ")
lenstr  l..(s..)

mynum  []

x  0
w___ x < lenstr:
    num  ""
    symbol  s..[x]
    w___ '0' < symbol < '9':
        num + symbol
        x + 1
        __ x<lenstr:
            symbol  s..[x]
        ____:
            _____
    x + 1
    __ num ! "":
        mynum.a..(i..(num))
print(mynum)
