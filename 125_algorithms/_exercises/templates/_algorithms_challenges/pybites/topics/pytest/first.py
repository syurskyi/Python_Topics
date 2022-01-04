_______ p__

___ div(a,b):
    try:
        r.. a/b
    except:
        r.. ZeroDivisionError


___ test_div_simple
    ... div(4,2) __ 2

___ test_div_second
    ... div(3,6) __ 0.5

___ test_div_zerodivision
    w__ p__.r..(ZeroDivisionError):
        div(3,0)


#print(div(5,0))