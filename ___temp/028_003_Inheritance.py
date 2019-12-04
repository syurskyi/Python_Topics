# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
class Super:
    def __init__(self, x):
        ...default code...

class Sub(Super):
    def __init__(self, x, y):
        Super.__init__(self, x)             # Run superclass __init__
        ...custom code...                   # Do my init actions

I = Sub(1, 2)
'''
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class Super:
    def method(self):
        print('in Super.method')


class Sub(Super):
    def method(self):                    # Override method
        print('starting Sub.method')     # Add actions here
        Super.method(self)               # Run default action
        print('ending Sub.method')

x = Super()                              # Make a Super instance
print('#' * 23 + ' Runs Super.method')
x.method()                               # Runs Super.method

x = Sub()                                # Make a Sub instance
print('#' * 23 + ' Runs Sub.method, calls Super.method')
x.method()                               # Runs Sub.method, calls Super.method


# ## file: specialize.py


class Super:
    def method(self):
        print('#' * 23 + ' Default behavior')
        print('in Super.method')           # Default behavior
    def delegate(self):
        self.action()                      # Expected to be defined


class Inheritor(Super):                    # Inherit method verbatim
    pass


class Replacer(Super):                     # Replace method completely
    def method(self):
        print('#' * 23 + ' Replace method completely')
        print('in Replacer.method')


class Extender(Super):                     # Extend method behavior
    def method(self):
        print('#' * 23 + ' Extend method behavior')
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')


class Provider(Super):                     # Fill in a required method
    def action(self):
        print('#' * 23 + ' Fill in a required method')
        print('in Provider.action')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()

