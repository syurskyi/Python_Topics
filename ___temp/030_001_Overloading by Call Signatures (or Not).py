class C:
    def meth(self, x):
        pass
    def meth(self, x, y, z):
        pass
# Type-based selections can always be coded using the type-testing ideas we met in
# Chapters 4 and 9, or the argument list tools introduced in Chapter 18:

class C:
    def meth(self, *args):
        if len(args) == 1:
            pass
        elif type(arg[0]) == int:
            pass


# your code to expect an object interface, not a specific data type. That way, it will be
# useful for a broader category of types and applications, both now and in the future:

class C:
    def meth(self, x):
        x.operation()                   # Assume x does the right thing

