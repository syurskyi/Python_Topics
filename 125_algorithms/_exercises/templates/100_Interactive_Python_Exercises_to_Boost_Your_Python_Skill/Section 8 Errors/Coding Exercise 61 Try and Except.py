x _ 1
y _ '2'
try:
    print(x + y)
except TypeError: # Better to be specific about the error you expect
    print(in.(x) + in.(y))