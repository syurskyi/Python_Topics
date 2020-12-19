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
    def method(self):                 # Override method
        print('starting Sub.method')     # Add actions here
        Super.method(self)            # Run default action
        print('ending Sub.method')

x = Super()                            # Make a Super instance
print('#' * 23 + ' Runs Super.method')
x.method()                              # Runs Super.method

x = Sub()                                # Make a Sub instance
print('#' * 23 + ' Runs Sub.method, calls Super.method')
x.method()                             # Runs Sub.method, calls Super.method


# ## file: specialize.py


class Super:
    ___ method ____
        print('#' * 23 + ' Default behavior')
        print('in Super.method')           # Default behavior
    ___ delegate ____
        ____.action()                      # Expected to be defined


c_ Inheritor S..                    # Inherit method verbatim
    p...


c_ Replacer S..                   # Replace method completely
    ___ method ____
        print('#' * 23 + ' Replace method completely')
        print('in Replacer.method')


c_ Extender S...                     # Extend method behavior
    ___ method____
        print('#' * 23 + ' Extend method behavior')
        print('starting Extender.method')
        S___.m... ____
        print('ending Extender.method')


c_ Provider S..                     # Fill in a required method
    ___ action ____
        print('#' * 23 + ' Fill in a required method')
        print('in Provider.action')


__ _______ __ ________
    ___ klass __ I... R... E..
        print('\n' + ?. -n + '...')
        k__ .m..
    print('\nProvider...')
    x = P..
    ?.d..

