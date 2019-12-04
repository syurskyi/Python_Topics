class Spam:
    def doit(self, message):
        print(message)

print('#' * 23 + ' normal operation')
object1 = Spam()
object1.doit('hello world22222')


print('#' * 23 + ' Bound method')
object1 = Spam()
x = object1.doit        # Bound method object: instance+function
x('hello world')        # Same effect as object1.doit('...')


print('#' * 23 + ' Bound method')
object1 = Spam()
t = Spam.doit           # Unbound method object (a function in 3.0: see ahead)
t(object1, 'howdy')     # Pass in instance (if the method expects one in 3.0)


class Eggs:
    def m1(self, n):
        print(n)

    def m2(self):
        x = self.m1     # Another bound method object
        x(42)           # Looks like a simple function

Eggs().m2()             # Prints 42
