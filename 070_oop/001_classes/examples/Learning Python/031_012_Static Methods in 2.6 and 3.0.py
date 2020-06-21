### file: spam.py

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    def printNumInstances(self):
        print("Number of instances created: ", Spam.numInstances)

# from spam import Spam
a = Spam()                   # Cannot call unbound class methods in 2.6
b = Spam()                   # Methods expect a self object by default
c = Spam()

# Spam.printNumInstances()
# TypeError: unbound method printNumInstances() must be called with Spam instance
# as first argument (got nothing instead)
# a.printNumInstances()
# TypeError: printNumInstances() takes no arguments (1 given)

# from spam import Spam
# a = Spam()                       # Can call functions in class in 3.0
# b = Spam()                       # Calls through instances still pass a self
# c = Spam()

# Spam.printNumInstances()         # Differs in 3.0
# Number of instances created:  3
# a.printNumInstances()
# TypeError: printNumInstances() takes no arguments (1 given)

# Spam.printNumInstances()             # Fails in 2.6, works in 3.0
# instance.printNumInstances()         # Fails in both 2.6 and 3.0
