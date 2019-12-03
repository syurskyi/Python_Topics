import time

def timer(label='', trace=True):             # On decorator args: retain args
    def onDecorator(func):                   # On @: retain decorated func
        def onCall(*args, **kargs):          # On calls: call original
            start   = time.clock()           # State is scopes + func attr
            result  = func(*args, **kargs)
            elapsed = time.clock() - start
            onCall.alltime += elapsed
            if trace:
                format = '%s%s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format % values)
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator

# Test on functions

@timer(trace=True, label='[CCC]==>')
def listcomp(N):                             # Like listcomp = timer(...)(listcomp)
    return [x * 2 for x in range(N)]         # listcomp(...) triggers onCall

@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))   # list for 3.0 views

for func in (listcomp, mapcall):
    result = func(5)                  # Time for this call, all calls, return value
    func(5000000)
    print(result)
    print('allTime = %s\n' % func.alltime)   # Total time for all calls

# Test on methods

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay

    @timer()
    def giveRaise(self, percent):            # giveRaise = timer()(giverRaise)
        self.pay *= (1.0 + percent)          # tracer remembers giveRaise

    @timer(label='**')
    def lastName(self):                      # lastName = timer(...)(lastName)
        return self.name.split()[-1]         # alltime per class, not instance

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
bob.giveRaise(.10)
sue.giveRaise(.20)                           # runs onCall(sue, .10)
print(bob.pay, sue.pay)
print(bob.lastName(), sue.lastName())        # runs onCall(bob), remembers lastName
print('%.5f %.5f' % (Person.giveRaise.alltime, Person.lastName.alltime))

# Expected output

# [CCC]==>listcomp: 0.00002, 0.00002
# [CCC]==>listcomp: 1.19636, 1.19638
# [0, 2, 4, 6, 8]
# allTime = 1.19637775192
#
# [MMM]==>mapcall: 0.00002, 0.00002
# [MMM]==>mapcall: 2.29260, 2.29262
# [0, 2, 4, 6, 8]
# allTime = 2.2926232943
#
# giveRaise: 0.00001, 0.00001
# giveRaise: 0.00001, 0.00002
# 55000.0 120000.0
# **lastName: 0.00001, 0.00001
# **lastName: 0.00001, 0.00002
# Smith Jones
# 0.00002 0.00002




### question 2


traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        if not __debug__:
            return aClass
        else:
            class onInstance:
                def __init__(self, *args, **kargs):
                    self.__wrapped = aClass(*args, **kargs)
                def __getattr__(self, attr):
                    trace('get:', attr)
                    if failIf(attr):
                        raise TypeError('private attribute fetch: ' + attr)
                    else:
                        return getattr(self.__wrapped, attr)
                def __setattr__(self, attr, value):
                    trace('set:', attr, value)
                    if attr == '_onInstance__wrapped':
                        self.__dict__[attr] = value
                    elif failIf(attr):
                        raise TypeError('private attribute change: ' + attr)
                    else:
                        setattr(self.__wrapped, attr, value)
            return onInstance
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))


# Test code: split me off to another file to reuse decorator

@Private('age')                             # Person = Private('age')(Person)
class Person:                               # Person = onInstance with state
    def __init__(self, name, age):
        self.name = name
        self.age  = age                     # Inside accesses run normally

X = Person('Bob', 40)
print(X.name)                               # Outside accesses validated
X.name = 'Sue'
print(X.name)
#print(X.age)    # FAILS unles "python -O"
#X.age = 999     # ditto
#print(X.age)    # ditto

@Public('name')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

X = Person('bob', 40)                       # X is an onInstance
print(X.name)                               # onInstance embeds Person
X.name = 'Sue'
print(X.name)
#print(X.age)    # FAILS unless "python �O main.py"
#X.age = 999     # ditto
#print(X.age)    # ditto



