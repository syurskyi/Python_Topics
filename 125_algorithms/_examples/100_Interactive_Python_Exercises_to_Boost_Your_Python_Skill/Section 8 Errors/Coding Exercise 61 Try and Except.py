x = 1
y = '2'
try:
    print(x + y)
except TypeError: # Better to be specific about the error you expect
    print(int(x) + int(y))