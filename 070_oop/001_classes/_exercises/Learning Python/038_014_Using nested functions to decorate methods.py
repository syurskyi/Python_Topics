# A decorator for both functions and methods

def tracer(func):                        # Use function, not class with __call__
    calls = 0                            # Else "self" is decorator instance only!
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall


# Applies to simple functions

@tracer
def spam(a, b, c):                       # spam = tracer(spam)
    print(a + b + c)                     # onCall remembers spam

spam(1, 2, 3)                            # Runs onCall(1, 2, 3)
spam(a=4, b=5, c=6)


# Applies to class method functions too!

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay

    @tracer
    def giveRaise(self, percent):        # giveRaise = tracer(giverRaise)
        self.pay *= (1.0 + percent)      # onCall remembers giveRaise

    @tracer
    def lastName(self):                  # lastName = tracer(lastName)
        return self.name.split()[-1]

print('methods...')
bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)                       # Runs onCall(sue, .10)
print(sue.pay)
print(bob.lastName(), sue.lastName())    # Runs onCall(bob), lastName in scopes