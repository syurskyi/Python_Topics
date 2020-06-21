class classic:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError

x = classic()
print('#' * 23 + ' Runs __getattr__')
print(x.age)                                 # Runs __getattr__

# x.name                                # Runs __getattr__
# AttributeError


class newprops(object):
    def getage(self):
        return 40
    age = property(getage, None, None, None)  # get, set, del, docs

x = newprops()
print('#' * 23 + ' Runs getage')
print(x.age)                                         # Runs getage

# x.name                                        # Normal fetch
# AttributeError: newprops instance has no attribute 'name'


class newprops(object):
    def getage(self):
        return 40

    def setage(self, value):
        print('set age:', value)
        self._age = value
    age = property(getage, setage, None, None)

x = newprops()
print('#' * 23 + ' Runs getage')
print(x.age)                                         # Runs getage

x.age = 42                                    # Runs setage

print('#' * 23 + ' Normal fetch; no getage call')
print(x._age)                                        # Normal fetch; no getage call

x.job = 'trainer'                             # Normal assign; no setage call
print('#' * 23 + ' Normal fetch; no getage call')
print(x.job)                                         # Normal fetch; no getage call


class classic:
    def __getattr__(self, name):              # On undefined reference
        if name == 'age':
            return 40
        else:
            raise AttributeError

    def __setattr__(self, name, value):       # On all assignments
        print('set:', name, value)
        if name == 'age':
            self.__dict__['_age'] = value
        else:
            self.__dict__[name] = value

x = classic()
print('#' * 23 + ' Runs __getattr__')
print(x.age)                                         # Runs __getattr__

x.age = 41                                    # Runs __setattr__
print('#' * 23 + ' Defined: no __getattr__ call')
print(x._age)                                        # Defined: no __getattr__ call

print('#' * 23 + ' Defined: no __getattr__ call')
x.job = 'trainer'                             # Runs __setattr__ again
print(x.job)                                         # Defined: no __getattr__ call
