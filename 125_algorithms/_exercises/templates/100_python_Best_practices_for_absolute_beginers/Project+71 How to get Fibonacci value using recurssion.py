def fibinacci(x):
    __ x __ 1 or x __ 2:
        return 1
    return fibinacci(x-1) + fibinacci(x-2)
print(fibinacci(10))