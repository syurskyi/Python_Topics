# %%
'''
### The `__new__` Method
'''

# %%
'''
We've studied the `__init__` method quite a bit so far. It is basically a method that gets called right after the class 
instance has been created, usually invoked when we call the Class with arguments to instantiate an instance.
'''

# %%
'''
The `__new__` method is the method that is invoked to actually create the new object, as an instance of the desired 
class.
'''

# %%
'''
Since the `object` class provides a default implementation for `__new__` we rarely have to bother with it, but sometimes 
we want to intercept the instance creation to tweak things a bit.
'''

# %%
'''
The `__new__` method, unlike the `__init__` method is actually a **static** method, not an **instance** method. 
Which kinds of make sense since the instance does not exist yet - that's what the `__new__` method is trying to create.

Why it's not a **class** method is more complicated. We'll see why that's the case as we explore `__new__`.
'''

# %%
'''
Remember how we create instances of a class - we call the class with whatever arguments we need to initialize the class 
state:

```
p = Person(name, age)
```
'''

# %%
'''
The creation of the class instance is then done in two steps:
1. The `__new__` method is called. It receives, as arguments, the class object we want an instance of, and any 
additional arguments we pass to the creation call (e.g. `name` and `age`). It should return a new instance of the class 
(and it may have used the arguments to initialize stuff in the class too, 
that's up to how you write your `__new__ method)
2. If the object returned by `__new__` is an instance of the class specified in the call to `__new__`, then 
the `__init__` method is also called. The `__init__` method is an instance method and does not return anything 
(well, it returns None).
'''

# %%
'''
The `__new__` method is present in the `object` class, so we can easily use it to create an instance of a class,
without calling the class itself.

Let's take a look:
'''

# %%
class Point:
    pass

# %%
p = object.__new__(Point)

# %%
type(p)

# %%
'''
So as you see, we created an instance of `Point` by using the `__new__` method defined in `object`.
'''

# %%
'''
Let's take that a step further and include the initialization as well:
'''

# %%
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# %%
p = object.__new__(Point)

# %%
p.__init__(10, 20)

# %%
p.__dict__

# %%
'''
One thing to note is that although `object.__new__` will accept `*args` and `**kwargs` it does not actually use them:
'''

# %%
p = object.__new__(Point, 10, 20)

# %%
p.__dict__

# %%
'''
Remember that this automatic chaining of `__new__` and `__init__` happens when we create a class using it as a callable 
(e.g.  `Person(10, 20)`).
'''

# %%
'''
So, since `__new__` is just another method, we can choose to override it in our custom classes.
'''

# %%
class Point:
    def __new__(cls, x, y):
        print('Creating instance...', x, y)
        instance = object.__new__(cls)  # delegate to object.__new__
        return instance  # don't forget to return the new instance!
    
    def __init__(self, x, y):
        print('Initializing instance...', x, y)
        self.x = x
        self.y = y

# %%
p = Point(10, 20)

# %%
'''
What's interesting also about the `__new__` method is that we can override it even when we inherit from the **built-in** 
types, whereas often the same does not work with `__init__` (we'll come back to the topic of inheriting from built-in 
types later when we look at abstract base classes.)

Let's see an example of this:
'''

# %%
class Squared(int):
    def __new__(cls, x):
        return super().__new__(cls, x**2)  # delegate creating an int instance to the int class itself

# %%
result = Squared(4)

# %%
result

# %%
'''
Anf of course, the `type` of result is `Squared`:
'''

# %%
type(result)

# %%
'''
But, it is **also** an `int` since we **inherited** from `int`:
'''

# %%
isinstance(result, int)

# %%
'''
Trying to do this using `__init__` would not work - the built-in `__init__` for integers does not actually do anything, 
and does not allow for an argument to be passed:
'''

# %%
class Squared(int):
    def __init__(self, x):
        print('calling init...')
        super().__init__(x ** 2)

# %%
try:
    result = Squared(4)
except TypeError as ex:
    print(ex)

# %%
'''
Most often when we override the `__new__` method we use delegation to the parent class to do some of the work.
But of course, as we saw just now we don't have to, we can just use `object.__new__` directly. 
'''

# %%
'''
Here's how we did it using `object` explicitly:
'''

# %%
class Person:
    def __new__(cls, name):
        print(f'Person: Instantiating {cls.__name__}...')
        instance = object.__new__(cls)
        return instance
        
    def __init__(self, name):
        print(f'Person: Initializing instance...')
        self.name = name

# %%
p = Person('Guido')

# %%
'''
But the problem here is that this technique does not play well with inheritance.
'''

# %%
'''
Let's do the same thing with a sub class of `Person`:
'''

# %%
class Student(Person):
    def __new__(cls, name, major):
        print(f'Student: Instantiating {cls.__name__}...')
        instance = object.__new__(cls)
        return instance
    
    def __init__(self, name, major):
        print(f'Student: Initializing instance...')
        super().__init__(name)
        self.major = major

# %%
s = Student('John', 'Major')

# %%
'''
You'll notice that the `__new__` method of `Person` was not called - that's because we called `object.__new__` directly.

So instead we really should do it this way:
'''

# %%
class Person:
    def __new__(cls, name):
        print(f'Person: Instantiating {cls.__name__}...')
        instance = super().__new__(cls)
        return instance
        
    def __init__(self, name):
        print(f'Person: Initializing instance...')
        self.name = name
        
class Student(Person):
    def __new__(cls, name, major):
        print(f'Student: Instantiating {cls.__name__}...')
        instance = super().__new__(cls, name)
        return instance
    
    def __init__(self, name, major):
        print(f'Student: Initializing instance...')
        super().__init__(name)
        self.major = major

# %%
s = Student('John', 'Major')

# %%
'''
So why override `__new__`? We saw one example where we can inherit from a built-in type and modify the behavior 
(the `Squared` class - the value is still an `int`, since we inherited from `int`
'''

# %%
'''
It allows us to tweak how the class is created. For example we could inject some extra attributes onto the class before 
creating the instance:
'''

# %%
class Square:
    def __new__(cls, w, l):
        cls.area = lambda self: self.w * self.l
        # or use setattr(cls, 'area', lambda self: self.w * self.l)
        instance = super().__new__(cls)  
        return instance
    
    def __init__(self, w, l):
        self.w = w
        self.l = l

# %%
s = Square(3, 4)

# %%
s.area()

# %%
'''
As you see we injected a function into the class before creating it. We could also tweak the instance before returning 
it.
'''

# %%
class Square:
    def __new__(cls, w, l):
        setattr(cls, 'area', lambda self: self.w * self.l)
        instance = super().__new__(cls)
        instance.w = w
        instance.l = l
        return instance

# %%
'''
Notice that since we are setting the instance variables inside the `__new__`, we don't even need to provide 
an override for the `__init__`.
'''

# %%
s = Square(3, 4)

# %%
s.__dict__

# %%
s.area()

# %%
'''
Keep in mind that `__new__` is a static method, and we can also invoke it explicitly ourselves - we just need 
to remember that we need to pass the class (type) we want to create an instance of to the `__new__` method as the first 
argument.
'''

# %%
s = Square.__new__(Square, 3, 4)

# %%
s.__dict__, s.area()

# %%
'''
Another important point. Remember that I said that when we call `MyClass(args, kwargs)`, it will essentially call:
```
MyClass.__new__(MyClass, args, kwargs)
```
'''

# %%
'''
But that's not the only thing that happens - the `__init__` is also automatically called right after.
**But only if the type returned by `__new__` matches the type specified as the first argument of `__new__`**
'''

# %%
'''
Let's see this:
'''

# %%
class Person:
    def __new__(cls, name):
        print(f'Creating instance of {cls.__name__}... not really...')
        instance = str(name)
        return instance

# %%
p = Person('Alex')

# %%
p, type(p)

# %%
'''
As you can see, we requested a new instance of `Person`, but `__new__` ignored that and created an instance of `str` 
instead.
'''

# %%
'''
Now let's add an init method:
'''

# %%
class Person:
    def __new__(cls, name):
        print(f'Creating instance of {cls.__name__}... not really...')
        instance = str(name)
        return instance
    
    def __init__(self, name):
        print('Init called...')
        self.name = name

# %%
p = Person('Raymond')

# %%
type(p), p

# %%
'''
As you can see the `__init__` was not called - and that makes sense - if `__new__` is not returning an instance 
of `Person` it does not make sense to invoke the `__init__` for `Person`, nor for the newly created instance 
(the signature might not even be compatible!)
'''

# %%
'''
One more point to make, is that if we override the `__new__` method, there is probably no reason to also override 
the `__init__` method, since we can take care of any custom initialization in the `__new__` method ourselves.
'''

# %%
class Person:
    def __new__(cls, name, age):
        instance = super().__new__(cls)
        instance.name = name
        instance.age = age
        return instance

# %%
p = Person('Guido', 42)

# %%
p.__dict__