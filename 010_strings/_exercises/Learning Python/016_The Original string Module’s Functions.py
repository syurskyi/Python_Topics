import string
S = 'a+b+c+'
x = S.replace('+', 'spam')
print(x)
import string
y = string.replace(S, '+', 'spam')
print(y)
