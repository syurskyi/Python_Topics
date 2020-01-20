class Selfless:
    def __init__(self, data):
        self.data = data

    def selfless(arg1, arg2):               # A simple function in 3.0
        return arg1 + arg2

    def normal(self, arg1, arg2):           # Instance expected when called
        return self.data + arg1 + arg2

print('#' * 23 + ' Instance passed to self automatically')
X = Selfless(2)
print(X.normal(3, 4))                  # Instance passed to self automatically

print('#' * 23 + ' self expected by method: pass manually')
print(Selfless.normal(X, 3, 4))        # self expected by method: pass manually

print('#' * 23 + ' No instance: works in 3.0, fails in 2.6!')
print(Selfless.selfless(3, 4))         # No instance: works in 3.0, fails in 2.6!


# X.selfless(3, 4)
# TypeError: selfless() takes exactly 2 positional arguments (3 given)

# Selfless.normal(3, 4)
# TypeError: normal() takes exactly 3 positional arguments (2 given)
