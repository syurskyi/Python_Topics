# %%
'''
### Delegating to Parent
'''

# %%
'''
You'll most likely encounter `super()` in the `__init__` method of custom classes, but delegation is not restricted to
__init__`. You can use `super()` anywhere you need to explicitly instruct Python to use a callable definition that is 
higher up in the inheritance chain. In these cases you only need to use `super()` if there is some ambiguity - i.e. 
your current class overrides an ancestor's callable and you need to specifically tell Python to use the callable 
in the ancestry chain.
'''

# %%
class Person:
    def work(self):
        return 'Person works...'
    
class Student(Person):
    def work(self):
        result = super().work()
        return f'Student works... and {result}'

# %%
s = Student()

# %%
s.work()

# %%
'''
Now the `super().work()` call in the `Student` class looks up the hierarchy chain until it finds the first definition 
for that callable.

We can easily see this:
'''

# %%
class Person:
    def work(self):
        return 'Person works...'
    
class Student(Person):
    pass

class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f'PythonStudent codes... and {result}'

# %%
ps = PythonStudent()

# %%
ps.work()

# %%
'''
Of course every class can delegate up the chain in turn:
'''

# %%
class Person:
    def work(self):
        return 'Person works...'
    
class Student(Person):
    def work(self):
        result = super().work()
        return f'Student studies... and {result}'
    
class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f'PythonStudent codes... and {result}'

# %%
ps = PythonStudent()
ps.work()

# %%
'''
Do note that when there is **no ambiguity** there is no need to use `super()`:
'''

# %%
class Person:
    def work(self):
        return 'Person works...'
    
class Student(Person):
    def study(self):
        return 'Student studies...'
    
class PythonStudent(Student):
    def code(self):
        result_1 = self.work()
        result_2 = self.study()
        return f'{result_1} and {result_2} and PythonStudent codes...'

# %%
ps = PythonStudent()

# %%
ps.code()

# %%
'''
The really important thing to understand is which object (instance) is bound when a delegated method is called. 
It is **always** the calling object:
'''

# %%
class Person:
    def work(self):
        return f'{self} works...'
    
class Student(Person):
    def work(self):
        result = super().work()
        return f'{self} studies... and {result}'

class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f'{self} codes... and {result}'
    

# %%
ps = PythonStudent()

# %%
hex(id(ps))

# %%
ps.work()

# %%
'''
As you can see each of the methods in the parent classes were called bound to the original `PythonStudent` instance 
`ps`.
'''

# %%
'''
What this means is that when a class sets an instance attribute, it will be set in the namespace of the original object. 
Here's a simple example that illustrates this:
'''

# %%
class Person:
    def set_name(self, value):
        print('Setting name using Person set_name method...')
        self.name = value
        
class Student(Person):
    def set_name(self, value):
        print('Student class delegating back to parent...')
        super().set_name(value)

# %%
s = Student()

# %%
'''
As you can see, the dictionary for `s` is currently empty:
'''

# %%
s.__dict__

# %%
'''
But if we call set_name:
'''

# %%
s.set_name('Eric')

# %%
'''
As you can see the `Person` class `set_name` method did the actual work, but the `name` attribute is created in 
the `Student` instance `s`:
'''

# %%
s.__dict__

# %%
'''
So just to re-emphasize, whenever you use `super()`, any `self` in the called methods actually refers to the object 
used to make the initial call.
'''

# %%
'''
One place where this is really handy is in class initialization - we use it to leverage the parent class initializer 
so we don't have to re-write a lot of initialization code in our child class.
'''

# %%
'''
Let's use a simple example first:
'''

# %%
class Person:
    def __init__(self, name):
        self.name = name
        
class Student(Person):
    def __init__(self, name, student_number):
        super().__init__(name)
        self.student_number = student_number

# %%
s = Student('Python', 30)

# %%
s.__dict__

# %%
'''
I do want to point out that if your parent class has initializer and your child class does not, then Python will attempt 
to call the parent `__init__` automatically - because the `__init__` is **inherited** from the parent class!
'''

# %%
class Person:
    def __init__(self):
        print('Person __init__')
        
class Student(Person):
    pass

# %%
s = Student()

# %%
'''
But watch what happens if the parent class requires an argument:
'''

# %%
class Person:
    def __init__(self, name):
        print('Person __init__ called...')
        self.name = name
        
class Student(Person):
    pass

# %%
try:
    s = Student()
except TypeError as ex:
    print(ex)

# %%
'''
In fact, we can pass this argument to the `Student` class and Python will automatically pass it along to the (inherited) 
`Person` class `__init__`:
'''

# %%
s = Student('Alex')

# %%
s.__dict__

# %%
'''
However, if we provide a custom `__init__` in our child class, then Python will not automatically call the parent init:
'''

# %%
class Person:
    def __init__(self):
        print('Person __init__ called...')
        
class Student(Person):
    def __init__(self):
        print('Student __init__ called...')

# %%
s = Student()

# %%
'''
To do so, we need to call `super().__init__`:
'''

# %%
class Person:
    def __init__(self):
        print('Person __init__ called...')

class Student(Person):
    def __init__(self):
        super().__init__()
        print('Student __init__ called...')

# %%
s = Student()

# %%
'''
Let's take a look at a more practical example:
'''

# %%
'''
Let's first create a `Circle` class:
'''

# %%
from math import pi
from numbers import Real

class Circle:
    def __init__(self, r):
        self._r = r
        self._area = None
        self._perimeter = None
        
    @property
    def radius(self):
        return self._r
    
    @radius.setter
    def radius(self, r):
        if isinstance(r, Real) and r > 0:
            self._r = r
            self._area = None
            self._perimeter = None
        else:
            raise ValueError('Radius must a positive real number.')
            
    @property
    def area(self):
        if self._area is None:
            self._area = pi * self.radius ** 2
        return self._area
            
    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * pi * self.radius
        return self._perimeter

# %%
'''
Now let's make a specialized circle class, a `UnitCircle` which is simply a circle with a radius of `1`:
'''

# %%
class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)

# %%
'''
And now we can use it this way:
'''

# %%
u = UnitCircle()

# %%
u.radius, u.area, u.perimeter

# %%
'''
Now one thing that's off here is that we can actually set the radius on the `UnitCircle` - which we probably don't want 
to allow.
My approach here is to redefine the `radius` property in the unit circle class and disallow setting the radius 
altogether:
'''

# %%
class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)
        
    @property
    def radius(self):
        return super().radius

# %%
u = UnitCircle()

# %%
u.radius

# %%
u.radius = 10

# %%
'''
Note how my overriding property uses `super().radius` - I cannot use `self.radius` as that would be trying to call 
the radius getter defined in the `UnitCircle` class (the one I am currently defining) - instead I specifically want 
to access the property from the parent class.
'''

# %%
'''
Finally I want to come back to another example that also helps underscore the fact that methods called via `super()` 
are still bound to the original (child) object, and hence will use methods defined in the child class if they override 
any in the parent class - this is a little tricky, but fundamental to understand:
'''

# %%
class Person:
    def method_1(self):
        print('Person.method_1')
        self.method_2()
        
    def method_2(self):
        print('Person.method_2')
        
class Student(Person):
    def method_1(self):
        print('Student.method_1')
        super().method_1()
        

# %%
s = Student()
s.method_1()

# %%
'''
So `Student.method_1` called `Person.method_1` via `super`, which in turn called `Person.method_2` - all of these 
methods were bound to the `Student` instance `s`.
'''

# %%
'''
Now watch what happens when we also override `method_2` in the `Student` class:
'''

# %%
class Person:
    def method_1(self):
        print('Person.method_1')
        self.method_2()
        
    def method_2(self):
        print('Person.method_2')
        
class Student(Person):
    def method_1(self):
        print('Student.method_1')
        super().method_1()
        
    def method_2(self):
        print('Student.method_2')

# %%
s = Student()
s.method_1()

# %%
'''
Since `self.method_2()` in the Person class was called from `s`, that `self` is the instance `s`, and hence `method_2` 
from the `Student` class was called, not the one defined in the `Person` class!
'''

# %%
