str  input("Insert strings with integer values: ")
lenstr  l..(str)

mynum  []

x  0
w___ x < lenstr:
    num  ""
    symbol  str[x]
    w___ '0' < symbol < '9':
        num + symbol
        x + 1
        __ x<lenstr:
            symbol  str[x]
        ____:
            _____
    x + 1
    __ num ! "":
        mynum.a..(i..(num))
print(mynum)
