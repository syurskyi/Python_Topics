x _ abs(in.(input("Insert integer values only: ")))

su. _ 0
mul _ 1

while x !_ 0:
    digit _ x%10
    su. +_ digit
    mul *_ digit

    x _ x/10

print("Sum of digit = ",su.)
print("Product of digit = ",mul)