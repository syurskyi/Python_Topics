# %%
'''
### Slots and Single Inheritance
'''

# %%
'''
First let's create a simple class hierarchy that does not use slots:
'''

# %%
class Person:
    def __init__(self, name):
        self.name = name
        
class Student(Person):
    pass

# %%
'''
If we create an instance of `Student`, we'll see that the `name` attribute is stored in the instance dictionary:
'''

# %%
s = Student('Alex')
s.__dict__

# %%
'''
Now let's do the same thing, but use slots for the `Person` class:
'''

# %%
class Person:
    __slots__ = 'name',
    
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

# %%
'''
We know `Person` instances do not have a dictionary:
'''

# %%
p = Person('Eric')
try:
    print(p.__dict__)
except AttributeError as ex:
    print(ex)

# %%
'''
But the sub class does:
'''

# %%
s = Student('Alex')

# %%
s.name, s.__dict__

# %%
'''
As you can see, the `Student` instance `s` has a dictionary - but note that the dictionary does not contain the `name` 
property - that is still stored in a slot.
'''

# %%
'''
So, `name` uses a slot, but the `Student` instance has an instance dictionary, which means we can add instance 
attributes to it:
'''

# %%
s.age = 19

# %%
s.__dict__

# %%
s.name, s.age

# %%
'''
If we want our subclass to only use slots, we just need to specify a `__slots__` class attribute for it too:
'''

# %%
class Student(Person):
    __slots__ = tuple()

# %%
s = Student('Alex')
s.name

# %%
'''
And the `Student` instance no longer has an instance dictionary:
'''

# %%
try:
    print(s.__dict__)
except AttributeError as ex:
    print(ex)

# %%
'''
Of course, we did not add to the slots for the `Student` class, so basically our `Student` instances can only have 
a `name` attribute. We can add additional attributes by just specifying them in the slots for `Student`:
'''

# %%
class Student(Person):
    __slots__ = 'school', 'student_number'
    
    def __init__(self, name, school, student_number):
        super().__init__(name)
        self.school = school
        self.student_number = student_number

# %%
s = Student('James', 'MI6 Prep', '007')

# %%
s.name, s.school, s.student_number

# %%
'''
Although Python does not currently disallow redefining slota in a subclass, it may in the future, and it can also cause 
unexpected behavior, so don't do it.
'''

# %%
'''
When we subclass a slot-less class, and define slots for the subclass, then we get a similar behavior to oiur first 
example - the subclass has both an instance dictionary and slots:
'''

# %%
class Person:
    def __init__(self, name):
        self.name = name
        
class Student(Person):
    __slots__ = 'age', 
    
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

# %%
s = Student('Python', 30)

# %%
s.name, s.age, s.__dict__

# %%
'''
As you can see, the `age` attribute is stored in a slot, but the `name` attribute, defined in the slot-less `Person` 
class ends up in `Student`'s instance dictionary.
'''

# %%
'''
As we'll see later, behave essentially the same as properties - neither of them are actually stored in an instance 
dictionary - the additional effect of slots is that it (may) remove the need for an instance dictionary entirely.
'''

# %%
'''
So, when we define a property in a class, we don't need to specify it in the slots if we want to use slots:
'''

# %%
class Person:
    __slots__ = '_name', 'age'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

# %%
p = Person('Eric', 78)

# %%
'''
So `p` has a property `name` and a (slotted) attribute `age`:
'''

# %%
p.name, p.age

# %%
'''
And we also do not have an instance dictionary:
'''

# %%
try:
    print(p.__dict__)
except AttributeError as ex:
    print(ex)

# %%
'''
So, as we can see neither the property `name` not the slotted attribute `age` are stored in an instance dictionary.
In fact, they are very much related - to something called descriptors, which we'll study later.
But let me just show you a quick preview of it.
'''

# %%
'''
Descriptors are objects that implement certain special functions (of course!) - just like iterators are objects that 
implement the special functions `__iter__` asnd `__next__`.
For data descriptors, we implement the `__get__` and `__set__` methods (some others too, but those are enough for now).
'''

# %%
'''
So let's look at the attributes of the property `name` first:
'''

# %%
hasattr(Person.name, '__get__'), hasattr(Person.name, '__set__')

# %%
'''
And now let's see the slotted attribute `age`:
'''

# %%
hasattr(Person.age, '__get__'), hasattr(Person.age, '__set__')

# %%
'''
Aha! See, both implement these methods!
'''

# %%
'''
And by the way, remember when I said that the `property` class was just a convenience class? Well, in fact it basically 
creates an class for us that implements the `__get__`, `__set__`, etc methods based on the methods we specify 
for `fget`, `fset`, etc respectively.
'''

# %%
'''
Lastly, we have seen that we can have classes that have both a dictionary and slots - we got those when we used 
inheritance.
'''

# %%
'''
But when we define without the `__slots__` attribute then it has an instance dictionary but no slots, and when 
we define `__slots__` it has slots but no instance dictionary.
'''

# %%
'''
We can actually define classes that have both, simply by specifying `__dict__` as **one of the slots**:
'''

# %%
class Person:
    __slots__ = 'name', '__dict__'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# %%
p = Person('Alex', 19)

# %%
p.name, p.age, p.__dict__

# %%
'''
As we can see, we have an instance dictionary (that contains `age` since it was not defined in the `__slots__`, and 
`name` which was defined as a slot however, is not fouind in the instance dictionary.
'''

# %%
'''
Of course, since we have an instance dictionary, we can add and remove arbitrary attributes at "run-time":
'''

# %%
p.school = 'Berkeley'

# %%
p.__dict__

# %%
