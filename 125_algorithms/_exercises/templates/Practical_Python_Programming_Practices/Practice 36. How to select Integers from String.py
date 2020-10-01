st. _ i..("Insert strings with integer values: ")
lenstr _ le.(st.)

mynum _   # list

x _ 0
w___ x < lenstr:
    num _ ""
    symbol _ st.[x]
    w___ '0' <_ symbol <_ '9':
        num +_ symbol
        x +_ 1
        __ x<lenstr:
            symbol _ st.[x]
        ____
            b..
    x +_ 1
    __ num !_ "":
        mynum.ap..(in.(num))
print(mynum)
