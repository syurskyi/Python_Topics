x _ input("Insert any value of 'C' or 'F' : ")

unit _ x[-1]
x _ in.(x[0:-1])

__ unit __ 'C' or unit __ 'c':
    x _ round(x*(9/5)+32)
    print(st.(x) + 'F')
elif unit __ 'F' or unit __ 'f':
    x _ round((x-32)*(5/9))
    print(st.(x) + 'C')