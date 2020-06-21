# %%
'''
### Making Objects Callable
'''

# %%
'''
We can make instances of our classes callables by implementing the `__call__` method.
'''

# %%
'''
Let's first see a simple example:
'''

# %%
class Person:
    def __call__(self):
        print('__call__ called...')

# %%
p = Person()

# %%
'''
And now we can use `p` as a callable too:
'''

# %%
type(p)

# %%
p()

# %%
'''
This is actually quite useful, and is widely used by Python itself.
'''

# %%
'''
For example, the `functools` module has a `partial` function that we can use to create partial functions, like this:
'''

# %%
from functools import partial

# %%
def my_func(a, b, c):
    return a, b, c

# %%
'''
We can call this function with three arguments, but we could also create a partial function that essentially pre-sets 
some of the positional arguments:
'''

# %%
partial_func = partial(my_func, 10, 20)

# %%
'''
And now we can (indirectly) call `my_func` using `partial_func` using only an argument for `c`, with `a` and `b` 
pre-set to `10` and `20` respectively:
'''

# %%
partial_func(30)

# %%
'''
So I referred to `partial` as a function, but in reality it's just a callable (and this is why in Python we generally 
refer to things as callables, not just functions, because an object might be callable without being an actual function). 
In fact, we've seen this before with properties - these are callables, but they are not functions!
'''

# %%
'''
Back to `partial`, you'll notice that the `type` of `partial` is not a `function` at all!
'''

# %%
type(partial)

# %%
'''
So the type is `type` which means `partial` is actually a class, not a function.
We can easily re-create a simplified approximation of `partial` ourselves using the `__call__` method in a custom class.
'''

# %%
class Partial:
    def __init__(self, func, *args):
        self._func = func
        self._args = args
        
    def __call__(self, *args):
        return self._func(*self._args, *args)

# %%
partial_func = Partial(my_func, 10, 20)

# %%
type(partial_func)

# %%
partial_func(30)

# %%
'''
Many such "functions" in Python are actually just general callables. The distinction is often not important.
'''

# %%
'''
There is a built-in function in Python, `callable` that can be used to determine if an object is callable:
'''

# %%
callable(print)

# %%
callable(partial)

# %%
callable(partial_func)

# %%
'''
As you can see our `Partial` class **instance** is callable, but the `Person` class instances will not be (the class 
itself is callable of course):
'''

# %%
class Person:
    def __init__(self, name):
        self.name = name

# %%
callable(Person)

# %%
p = Person('Alex')

# %%
callable(p)

# %%
'''
#### Example: Cache with a cache-miss counter
'''

# %%
'''
Let's take a look at another example. I want to implement a dictionary to act as a cache, but I also want to keep track 
of the cache misses so I can later evaluate if my caching strategy is effective or not.
'''

# %%
'''
The `defaultdict` class can be useful as a cache.
Recall that I can specify a default callable to use when requesting a non-existent key from a `defaultdict`:
'''

# %%
from collections import defaultdict

# %%
def default_value():
    return 'N/A'

# %%
d = defaultdict(default_value)

# %%
d['a']

# %%
d.items()

# %%
'''
Now, I want to use this `default_value` callable to keep track of the number of times it has been called - this will 
tell me how may times a non-existent key was requested from my `defaultdict`.
'''

# %%
'''
I could try to create a global counter, and use that in my `default_value` function:
'''

# %%
miss_counter = 0

# %%
def default_value():
    global miss_counter
    miss_counter += 1
    return 'N/A'

# %%
'''
And now we can use it this way:
'''

# %%
d = defaultdict(default_value)

# %%
d['a'] = 1
d['a']
d['b']
d['c']

# %%
miss_counter

# %%
'''
This works, but is not very good - the `default_value` function **relies** on us having a global `miss_counter` 
variable - if we don't have it our function won't work. Additionally we cannot use it to keep track of different 
cache instances since they would all use the same instance of `miss_counter`.
'''

# %%
del miss_counter

# %%
d = defaultdict(default_value)

# %%
try:
    d['a']
except NameError as ex:
    print(ex)

# %%
'''
So nmaybe we can just pass in the counter (defined in our current scope) we want to use to the `default_value` function:
'''

# %%
def default_value(counter):
    counter += 1
    return 'N/A'

# %%
'''
But this **won't work**, because counter is now local to the function so the local `counter` will be incremented, not 
the `counter` from the outside scope.
'''

# %%
'''
Instead, we could use a class to maintain both a counter state, and return the default value for a cache miss:
'''

# %%
class DefaultValue:
    def __init__(self):
        self.counter = 0
        
    def __iadd__(self, other):
        if isinstance(other, int):
            self.counter += other
            return self
        raise ValueError('Can only increment with an integer value.')

# %%
'''
So we can use this class a a counter:
'''

# %%
default_value_1 = DefaultValue()

# %%
default_value_1 += 1

# %%
default_value_1.counter

# %%
'''
So this works as a counter, but `default_value_1` is not callable, which is what we need to the `defaultdict`.
So let's make it callable, and implement the behavior we need:
'''

# %%
class DefaultValue:
    def __init__(self):
        self.counter = 0
        
    def __iadd__(self, other):
        if isinstance(other, int):
            self.counter += other
            return self
        raise ValueError('Can only increment with an integer value.')
        
    def __call__(self):
        self.counter += 1
        return 'N/A'

# %%
'''
And now we can use this as our default callable for our default dicts:
'''

# %%
def_1 = DefaultValue()
def_2 = DefaultValue()

# %%
cache_1 = defaultdict(def_1)
cache_2 = defaultdict(def_2)

# %%
cache_1['a'], cache_1['b']

# %%
def_1.counter

# %%
cache_2['a']

# %%
def_2.counter

# %%
'''
As one last little enhancement, I'm going to make the returned default value an instance attribute for more flexibility:
'''

# %%
class DefaultValue:
    def __init__(self, default_value):
        self.default_value = default_value
        self.counter = 0
        
    def __iadd__(self, other):
        if isinstance(other, int):
            self.counter += other
            return self
        raise ValueError('Can only increment with an integer value.')
        
    def __call__(self):
        self.counter += 1
        return self.default_value

# %%
'''
And now we could use it this way:
'''

# %%
cache_def_1 = DefaultValue(None)
cache_def_2 = DefaultValue(0)

cache_1 = defaultdict(cache_def_1)
cache_2 = defaultdict(cache_def_2)

# %%
cache_1['a'], cache_1['b'], cache_1['a']

# %%
cache_def_1.counter

# %%
cache_2['a'], cache_2['b'], cache_2['c']

# %%
cache_def_2.counter

# %%
'''
So the `__call__` method can essentially be used to make **instances** of our classes callable.
This is also very useful to create **decorator** classes.
Oftn we just use closures to create decorators, but sometimes it is easier to use a class instead, or if we want our 
class to provide functionality beyond just being used as a decorator.
'''

# %%
'''
Let's look at an example.
'''

# %%
'''
#### Example: Profiling Functions
'''

# %%
'''
For simplicity I will assume here that we only want to decorate functions defined at the module level. For creating a 
decorator that also works for methods (bound functions) we have to do a bit more work and will need to understand 
descriptors - more on descriptors later.
'''

# %%
'''
So we want to easily be able to keep track of how many times our functions are called and how long they take to run on 
average.
'''

# %%
'''
Although we could cretainly implement code directly inside our function to do this, it becomes repetitive if we need 
to do it for multiple functions - so a decorator is ideal for that.
Let's look at how we can use a decorator class to keep track of how many times our function is called and also keep 
track of the time it takes to run on average.
'''

# %%
'''
We could certainly try a closure-based approach, maybe something like this:
'''

# %%
from time import perf_counter
from functools import wraps

def profiler(fn):
    counter = 0
    total_elapsed = 0
    avg_time = 0
    
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal counter
        nonlocal total_elapsed
        nonlocal avg_time
        counter += 1
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        total_elapsed += (end - start)
        avg_time = total_elapsed / counter
        return result
    
    # we need to give a way to our users to look at the
    # counter and avg_time values - spoiler: this won't work!
    inner.counter = counter
    inner.avg_time = avg_time
    return inner

# %%
'''
So, we added `counter` and `avg_time` as attributes to the `inner` function (the decorated function) - that works but 
looks a little weird - also notice that we calculate `avg_time` every time we call our decorated fuinction, even 
though the user may never request it - seems wasteful.
'''

# %%
from time import sleep
import random

random.seed(0)

@profiler
def func1():
    sleep(random.random())

# %%
func1(), func1()

# %%
func1.counter

# %%
'''
Hmm, that's weird - `counter` still shows zero. This is because we have to understand what we did in the decorator - 
we made `inner.counter` the value of `counter` **at the time the decorator function was called** - this is **not** 
the counter value that we keep updating!!
'''

# %%
'''
So instead we could try to fix it this way:
'''

# %%
from time import perf_counter
from functools import wraps

def profiler(fn):
    _counter = 0
    _total_elapsed = 0
    _avg_time = 0
    
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal _counter
        nonlocal _total_elapsed
        nonlocal _avg_time
        _counter += 1
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        _total_elapsed += (end - start)
        return result
    
    # we need to give a way to our users to look at the
    # counter and avg_time values - but we need to make sure
    # it is using a cell reference!
    def counter():
        # this will now be a closure with a cell pointing to 
        # _counter
        return _counter
    
    def avg_time():
        return _total_elapsed / _counter
    
    inner.counter = counter
    inner.avg_time = avg_time
    return inner

# %%
@profiler
def func1():
    sleep(random.random())

# %%
func1(), func1()

# %%
func1.counter()

# %%
func1.avg_time()

# %%
'''
OK, so that works, but it's a little convoluted. In this case a decorator class will be much easier to write and read!
'''

# %%
class Profiler:
    def __init__(self, fn):
        self.counter = 0
        self.total_elapsed = 0
        self.fn = fn
        
    def __call__(self, *args, **kwargs):
        self.counter += 1
        start = perf_counter()
        result = self.fn(*args, **kwargs)
        end = perf_counter()
        self.total_elapsed += (end - start)
        return result
        
    @property
    def avg_time(self):
        return self.total_elapsed / self.counter
        
        

# %%
'''
So we can now use `Profiler` as a decorator!
'''

# %%
@Profiler
def func_1(a, b):
    sleep(random.random())
    return (a, b)

# %%
func_1(1, 2)

# %%
func_1.counter

# %%
func_1(2, 3)

# %%
func_1.counter

# %%
func_1.avg_time

# %%
'''
And of course we can use it for other functions too:
'''

# %%
@Profiler
def func_2():
    sleep(random.random())

# %%
func_2(), func_2(), func_2()

# %%
func_2.counter, func_2.avg_time

# %%
'''
As you can see, it was much easier to implement this more complex decorator using a class and the `__call__` method 
than using a purely function approach. But of course, if the decorator is simple enough to implement using a functional 
approach, that's my preferred way of doing things! 
Just because I have a hammer does not mean everything is a nail!!
'''

# %%
