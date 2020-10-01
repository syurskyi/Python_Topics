print("Zero operation terminates program!")
w___ T..:
    o _ i..("Choose Opearator(+, -, *, /): ")
    __ o __ "0":
        b..
    __ o __ ('+','-','*','/'):
        x _ fl..(i..("Enter the value of x = "))
        y _ fl..(i..("Enter the value of y = "))
        __ o __ '+':
            print("%.2f" % (x+y))
        ____ o __ '-':
            print("%.2f" % (x-y))
        ____ o __ '*':
            print("%.2f" % (x*y))
        ____ o __ '/':
            __ y !_ 0:
                print("%.2f" % (x / y))
            ____
                print("Error! Division by zero...")
        ____
            print("Invalid operator")
