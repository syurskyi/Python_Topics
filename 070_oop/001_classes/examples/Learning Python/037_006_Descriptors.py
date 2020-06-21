#
# class Descriptor:
#     "docstring goes here"
#     def __get__(self, instance, owner): ...        # Return attr value
#     def __set__(self, instance, value): ...        # Return nothing (None)
#     def __delete__(self, instance): ...            # Return nothing (None)
#
#


class Descriptor(object):
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')

class Subject:
    attr = Descriptor()             # Decriptor instance is class attr

X = Subject()

X.attr

Subject.attr

class D:
    def __get__(*args): print('get')

class C:
    a = D()

X = C()
X.a                                 # Runs inherited descriptor __get__

C.a

X.a = 99                            # Stored on X, hiding C.a
X.a

list(X.__dict__.keys())

Y = C()
Y.a                                 # Y still inherits descriptor

C.a

class D:
    def __get__(*args): print('get')
    def __set__(*args): raise AttributeError('cannot set')

class C:
    a = D()

X = C()
X.a                                 # Routed to C.a.__get__
# get
# X.a = 99           # ERROR                 # Routed to C.a.__set__
# # AttributeError: cannot set
