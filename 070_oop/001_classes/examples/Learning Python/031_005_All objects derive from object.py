class C: pass

X = C()

print('#' * 23 + ' Type is now class instance was created from')
print(type(X))                           # Type is now class instance was created from

print(type(C))

print(isinstance(X, object))

print('#' * 23 + ' Classes always inherit from object')
print(isinstance(C, object))             # Classes always inherit from object

print(type('spam'))

print(type(str))

print('#' * 23 + ' Same for  built-in types (classes)')
print(isinstance('spam', object))        # Same for  built-in types (classes)

print(isinstance(str, object))

print('#' * 23 + '  All classes are types, and vice versa')
print(type(type))                        # All classes are types, and vice versa

print(type(object))

print('#' * 23 + ' All classes derive from object, even type')
print(isinstance(type, object))          # All classes derive from object, even type

print('#' * 23 + ' Types make classes, and type is a class')
print(isinstance(object, type))          # Types make classes, and type is a class
print(type is object)
