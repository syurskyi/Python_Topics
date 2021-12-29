str  input("Insert strings with integer values: ")
lenstr  len(str)

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
        else:
            _____
    x + 1
    __ num ! "":
        mynum.append(i..(num))
print(mynum)
