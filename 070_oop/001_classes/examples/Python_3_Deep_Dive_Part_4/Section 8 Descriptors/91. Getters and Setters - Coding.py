# %%
'''
### Getters and Setters
'''

# %%
'''
So far we have seen how the `__get__` method is called when we assign an instance of a descriptors to a class attribute.
But we can access that attribute either from the class itself, or the instance - as we saw in the last lecture, 
both accesses end up calling the `__get__` method.
'''

# %%
'''
But what changes are the arguments passed to the method. Let's explore this:
'''

# %%
from datetime import datetime

class TimeUTC:
    def __get__(self, instance, owner_class):
        print(f'__get__ called, self={self}, instance={instance}, owner_class={owner_class}')
        return datetime.utcnow().isoformat()

# %%
class Logger1:
    current_time = TimeUTC()
    
class Logger2:
    current_time = TimeUTC()

# %%
'''
Now let's access `current_time` from the class itself:
'''

# %%
Logger1.current_time

# %%
'''
As you can see, the `instance` was `None` - this was because we called the descriptor from the `Logger1` class, 
not an instance of it. The `owner_class` tells us this descriptor instance is defined in the `Logger1` class.
The same holds if we use `Logger2`:
'''

# %%
Logger2.current_time

# %%
'''
But if we call the descriptor via an instance instead:
'''

# %%
l1 = Logger1()
print(hex(id(l1)))

# %%
l1.current_time

# %%
'''
As you can see, `instance` is now the `l1` instance, and the owner class is still `Logger1`.
The sme holds for instance of `Logger2`:
'''

# %%
l2 = Logger2()
print(hex(id(l2)))
l2.current_time

# %%
'''
This means that we can differentiate, inside our `__get__` method whether the descriptor was accessed via the class 
or via an instance.
Typically when a descriptor is access from the class we return the descriptor instance, and when accessed from the 
instance we return the instance specific value we want:
'''

# %%
from datetime import datetime

class TimeUTC:
    def __get__(self, instance, owner_class):
        if instance is None:
            # called from class
            return self
        else:
            # called from instance
            return datetime.utcnow().isoformat()

# %%
class Logger:
    current_time = TimeUTC()

# %%
Logger.current_time

# %%
l = Logger()

# %%
l.current_time

# %%
'''
This is consistent with the way properties work:
'''

# %%
class Logger:
    @property
    def current_time(self):
        return datetime.utcnow().isoformat()

# %%
Logger.current_time

# %%
'''
This returned the property instance, whereas calling it from an instance:
'''

# %%
l = Logger()
l.current_time

# %%
'''
Now, there is one subtle point we have to understand when we create multiple instances of a class that uses a descriptor 
as a class attribute.
'''

# %%
'''
Since the descriptor is assigned to an **class attribute**, all instances of the class will **share** the same 
descriptor instance!
'''

# %%
class TimeUTC:
    def __get__(self, instance, owner_class):
        if instance is None:
            # called from class
            return self
        else:
            # called from instance
            print(f'__get__ called in {self}')
            return datetime.utcnow().isoformat()
        
class Logger:
    current_time = TimeUTC()

# %%
l1 = Logger()
l2 = Logger()

# %%
'''
But look at the `current_time` for each of those instances
'''

# %%
l1.current_time, l2.current_time

# %%
'''
As you can see the **same** instance of `TimeUTC` was used.
'''

# %%
'''
This does not matter in this particular example, since we just return the current time, but watch what happens if 
our property relies on some kind of state in the descriptor:
'''

# %%
class Countdown:
    def __init__(self, start):
        self.start = start + 1
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            self.start -= 1
            return self.start

# %%
class Rocket:
    countdown = Countdown(10)

# %%
'''
Now let's say we want to launch two rockets:
'''

# %%
rocket1 = Rocket()
rocket2 = Rocket()

# %%
'''
And let's start the countdown for each one:
'''

# %%
rocket1.countdown

# %%
rocket2.countdown

# %%
rocket1.countdown

# %%
'''
As you can see, the current countdown value is shared by both `rocket1` and `rocket2` instances of `Rocket` - this is 
because the `Countdown` instance is a class attribute of `Rocket`. So we have to be careful how we deal with instance 
level state.
'''

# %%
'''
The `__set__` method works in a similar way to `__get__` but it is used when we assign a value to the class attribute.
'''

# %%
class IntegerValue:
    def __set__(self, instance, value):
        print(f'__set__ called, instance={instance}, value={value}')
        
    def __get__(self, instance, owner_class):
        if instance is None:
            print('__get__ called from class')
        else:
            print(f'__get__ called, instance={instance}, owner_class={owner_class}')

# %%
class Point2D:
    x = IntegerValue()
    y = IntegerValue()

# %%
Point2D.x

# %%
p = Point2D()

# %%
p.x

# %%
p.x = 100

# %%
'''
So, where should we store the values `x` and `y`? 
Many "tutorials" I see on the web naively store the value in the descriptor itself:
'''

# %%
class IntegerValue:
    def __set__(self, instance, value):
        self._value = int(value)
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self._value

# %%
class Point2D:
    x = IntegerValue()
    y = IntegerValue()

# %%
'''
At first blush, this seems to work just fine:
'''

# %%
p1 = Point2D()

# %%
p1.x = 1.1
p1.y = 2.2

# %%
p1.x, p1.y

# %%
'''
But, remember the point I was making about the instance of the descriptor (`IntegeraValue` in this case) being shared 
by all instances of the class (`Point2D` in this case)?
'''

# %%
p2 = Point2D()

# %%
p2.x, p2.y

# %%
'''
And of course if we set the value:
'''

# %%
p2.x = 100.9

# %%
p2.x, p1.x

# %%
'''
So, obviously using the descriptor instance dictionary for storage at the instance level is probably not going 
to work in most cases!
'''

# %%
'''
And this is the reason both the `__get__` and `__set__` methods need to know which instance we are dealing with.
'''

# %%
