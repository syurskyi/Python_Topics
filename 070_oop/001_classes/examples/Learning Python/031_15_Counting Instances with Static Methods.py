class Spam:
    numInstances = 0                         # Use static method for class data
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances():
        print("Number of instances:", Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)

a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()                 # Call as simple function
a.printNumInstances()                    # Instance argument not passed


class Sub(Spam):
    def printNumInstances():                 # Override a static method
        print("Extra stuff...")              # But call back to original
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)

a = Sub()
b = Sub()
a.printNumInstances()                    # Call from subclass instance
# Number of instances: 2
# Sub.printNumInstances()                  # Call from subclass itself
# Number of instances: 2
# Spam.printNumInstances()
# Number of instances: 2

class Other(Spam):
    pass                       # Inherit static method verbatim

c = Other()
c.printNumInstances()
# Number of instances: 3
