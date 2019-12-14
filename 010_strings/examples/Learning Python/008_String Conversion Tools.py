# # Python 3.X
# "42" + 1
# TypeError: Can't convert 'int' object to str implicitly
# # Python 2.X
# "42" + 1
# TypeError: cannot concatenate 'str' and 'int' objects

print(int("42"), str(42))  # Convert from/to string
print(repr(42))  # Convert to as-code string
print(str('spam'), repr('spam'))  # 2.X: print str('spam'), repr('spam')
print(str('spam'), repr('spam'))  # Raw interactive echo displays
S = "42"
I = 1
# S + I
# TypeError: Can't convert 'int' object to str implicitly
print(int(S) + I)  # Force addition
print(S + str(I))  # Force concatenation
print(str(3.1415), float("1.5"))
text = "1.234E-10"
print(float(text))  # Shows more digits before 2.7 and 3.1
