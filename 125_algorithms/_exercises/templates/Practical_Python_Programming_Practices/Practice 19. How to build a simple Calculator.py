print("Zero operation terminates program!")
while T..:
    o _ input("Choose Opearator(+, -, *, /): ")
    __ o __ "0":
        break
    __ o __ ('+','-','*','/'):
        x _ fl..(input("Enter the value of x = "))
        y _ fl..(input("Enter the value of y = "))
        __ o __ '+':
            print("%.2f" % (x+y))
        elif o __ '-':
            print("%.2f" % (x-y))
        elif o __ '*':
            print("%.2f" % (x*y))
        elif o __ '/':
            __ y !_ 0:
                print("%.2f" % (x / y))
            ____
                print("Error! Division by zero...")
        ____
            print("Invalid operator")
