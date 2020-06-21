
class C:
   @staticmethod                                 # Decoration syntax
   def meth():
       ...

class C:
   def meth():
       ...
   meth = staticmethod(meth)                     # Rebind name



class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    @staticmethod
    def printNumInstances():
        print("Number of instances created: ", Spam.numInstances)

a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()      # Calls from both classes and instances work now!
a.printNumInstances()         # Both print "Number of instances created:  3"
