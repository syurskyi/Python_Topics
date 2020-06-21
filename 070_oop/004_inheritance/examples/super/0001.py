# The super() builtin returns a proxy object (temporary object of the superclass) that allows us to access methods
# of the base class.

# In Python, super() has two major use cases:
#
# Allows us to avoid using the base class name explicitly
# Working with Multiple Inheritance
# Example 1: super() with Single Inheritance
# In the case of single inheritance, it allows us to refer base class by super().

class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')

class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')

d1 = Dog()

# Output
#
# Dog has four legs.
# Dog is a warm-blooded animal.
# Here, we called the __init__() method of the Mammal class (from the Dog class) using code
#
# super().__init__('Dog')
# instead of
#
# Mammal.__init__(self, 'Dog')
# Since we do not need to specify the name of the base class when we call its members, we can easily change the base class name (if we need to).
#
# # changing base class to CanidaeFamily

# class Dog(CanidaeFamily):
#   def __init__(self):
#     print('Dog has four legs.')
#
#    # no need to change this
#     super().__init__('Dog')

# The super() builtin returns a proxy object, a substitute object that can call methods of the base class
# via delegation. This is called indirection (ability to reference base object with super())
# Since the indirection is computed at the runtime, we can use different base classes
# at different times (if we need to).
#
# Example 2: super() with Multiple Inheritance

class Animal:
  def __init__(self, Animal):
    print(Animal, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)

class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammal):
    print(NonWingedMammal, "can't fly.")
    super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammal):
    print(NonMarineMammal, "can't swim.")
    super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')

d = Dog()
print('')
bat = NonMarineMammal('Bat')

# Output
#
# Dog has 4 legs.
# Dog can't swim.
# Dog can't fly.
# Dog is a warm-blooded animal.
# Dog is an animal.
#
# Bat can't swim.
# Bat is a warm-blooded animal.
# Bat is an animal.

# Method Resolution Order (MRO)
# Method Resolution Order (MRO) is the order in which methods should be inherited in the presence
# of multiple inheritance. You can view the MRO by using the __mro__ attribute.
#
Dog.__mro__
# (<class 'Dog'>,
# <class 'NonMarineMammal'>,
# <class 'NonWingedMammal'>,
# <class 'Mammal'>,
# <class 'Animal'>,
# <class 'object'>)
# Here is how MRO works:
#
# A method in the derived calls is always called before the method of the base class.
# In our example, Dog class is called before NonMarineMammal or NoneWingedMammal. These two classes are called before
# Mammal, which is called before Animal, and Animal class is called before the object.
# If there are multiple parents like Dog(NonMarineMammal, NonWingedMammal), methods of NonMarineMammal
# is invoked first because it appears first.
