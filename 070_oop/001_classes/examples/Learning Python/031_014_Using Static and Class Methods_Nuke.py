class Methods:
    def imeth(self, x):            # Normal instance method: passed a self
        print(self, x)

    def smeth(x):                  # Static: no instance passed
        print(x)

    def cmeth(cls, x):             # Class: gets class, not instance
        print(cls, x)

    smeth = staticmethod(smeth)    # Make smeth a static method
    cmeth = classmethod(cmeth)     # Make cmeth a class method



obj = Methods()                # Make an instance

obj.imeth(1)                   # Normal method, call through instance
# <__main__.Methods object...> 1     # Becomes imeth(obj, 1)

Methods.imeth(obj, 2)          # Normal method, call through class
# <__main__.Methods object...> 2     # Instance passed explicitly

Methods.smeth(3)               # Static method, call through class
                                  # No instance passed or expected

obj.smeth(4)                   # Static method, call through instance
                                  # Instance not passed

Methods.cmeth(5)               # Class method, call through class
# <class '__main__.Methods'> 5       # Becomes cmeth(Methods, 5)

obj.cmeth(6)                   # Class method, call through instance
# <class '__main__.Methods'> 6       # Becomes cmeth(Methods, 6)
