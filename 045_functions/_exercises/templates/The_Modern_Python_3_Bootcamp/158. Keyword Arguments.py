def exponent(num, power=2):
    return num ** power

# Order doesn't matter anymore, if we use key word arguments:


print(exponent(num=2, power=3))  # 8
print(exponent(power=3, num=2))  # 8

# Without keywords args, order still matters:
print(exponent(3, 4))  # 81
print(exponent(4, 3))  # 64
