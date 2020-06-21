class C1:
    def meth1(self): self.X = 88         # I assume X is mine

    def meth2(self): print(self.X)


class C2:
    def metha(self): self.X = 99         # Me too

    def methb(self): print(self.X)


class C3(C1, C2):
    pass
I = C3()                                 # Only 1 X in I!



### file: private.py


class C1:
    def meth1(self): self.__X = 88       # Now X is mine

    def meth2(self): print(self.__X)     # Becomes _C1__X in I


class C2:
    def metha(self): self.__X = 99       # Me too

    def methb(self): print(self.__X)     # Becomes _C2__X in I


class C3(C1, C2): pass
I = C3()                                 # Two X names in I

I.meth1(); I.metha()
print(I.__dict__)
I.meth2(); I.methb()


class Super:
    def method(self):                  # A real application method
        pass


class Tool:
    def __method(self):                 # Becomes _Tool__method
        pass

    def other(self): self.__method()       # Use my internal method


class Sub1(Tool, Super):
    pass

    def actions(self): self.method()       # Runs Super.method as expected


class Sub2(Tool):
    def __init__(self): self.method = 99   # Doesn't break Tool.__method

