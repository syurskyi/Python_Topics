# %%
'''
### Back to Instance Properties
'''

# %%
'''
Let's try using `WeakKeyDictionary` to store our instance data in our data descriptor.
Basically, this is exactly the same as what we were doing before, but instead of using a standard dictionary 
(that potentially causes memory leaks), we'll use a `WeakKeyDictionary`.
'''

# %%
'''
Recall what we had before:
'''

# %%
class IntegerValue:
    def __init__(self):
        self.values = {}
        
    def __set__(self, instance, value):
        self.values[instance] = int(value)
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(instance)

# %%
'''
Now, we are going to refactor this to use the weak key dictionary:
'''

# %%
import weakref

# %%
class IntegerValue:
    def __init__(self):
        self.values = weakref.WeakKeyDictionary()
        
    def __set__(self, instance, value):
        self.values[instance] = int(value)
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(instance)

# %%
'''
And that's all there is to it. We now have weak references instead of strong references in our dictionary, 
and the dictionary cleans up after itself (removes "dead" entries) when the reference object has been destroyed 
by the GC.
'''

# %%
class Point:
    x = IntegerValue()

# %%
p = Point()
print(hex(id(p)))

# %%
p.x = 100.1

# %%
p.x

# %%
Point.x.values.keyrefs()

# %%
'''
And if we delete `p`, thereby deleting the last strong reference to that object:
'''

# %%
del p

# %%
Point.x.values.keyrefs()

# %%
'''
So this is almost a perfect general solution:
1. We do not need to store the data in the instances themseves (so we can handle objects whose class uses `__slots__`)
2. We are protected from memory leaks
But this only works for **hashable** objects.
'''

# %%
'''
So, now let's try to address this hashability issue.
'''

# %%
'''
Since we cannot use the object itself as the key in a dictionary (weak or otherwise), we could try using the `id` 
of the object (which is an int) as the key in a standard dictionary:
'''

# %%
class IntegerValue:
    def __init__(self):
        self.values = {}
        
    def __set__(self, instance, value):
        self.values[id(instance)] = int(value)
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(id(instance))

# %%
'''
Now we can use this approach with non-hashable objects:
'''

# %%
class Point:
    x = IntegerValue()
    
    def __init__(self, x):
        self.x = x
        
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x

# %%
p = Point(10.1)

# %%
p.x

# %%
p.x = 20.2

# %%
p.x

# %%
id(p), Point.x.values

# %%
'''
Now we no longer have a memory leak:
'''

# %%
import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

# %%
p_id = id(p)

# %%
ref_count(p_id)

# %%
del p

# %%
ref_count(p_id)

# %%
'''
But, we now have a "dead" entry in our dictionary - that memory address is still present as a key. Now, you might think 
it's not a big deal, but Python does reuse memory addresses, so we could run into potential issues there 
(where the data descriptor would have a value for a property already set from a previous object), 
and also the fact that our dictionary is cluttered with these dead entries:
'''

# %%
Point.x.values

# %%
'''
So we need a way to determine if the object has been destroyed.
'''

# %%
'''
We know that weak references are aware of when objects are destroyed:
'''

# %%
p = Point(10.1)
weak_p = weakref.ref(p)

# %%
print(hex(id(p)), weak_p)  
# again note how I need to use print to avoid affecting the ref count

# %%
ref_count(id(p))

# %%
'''
And if I remove the last strong reference to `p`:
'''

# %%
del p

# %%
print(weak_p)

# %%
'''
You can see that the weak reference was made aware of that change - in fact we can as well, by specifying 
a **callback** function that Python will call once the weak reference becomes dead (i.e. the object was destroyed 
by the GC):
'''

# %%
def obj_destroyed(obj):
    print(f'{obj} is being destroyed')

# %%
p = Point(10.1)
w = weakref.ref(p, obj_destroyed)

# %%
del p

# %%
'''
As you can see the callback function receives the weak ref object as the argument.
'''

# %%
'''
So, we can use this to our advantage in our data descriptor, by registering a callback that we can use to remove 
the "dead" entry from our values dictionary.
This means we do need to store a weak reference to the object as well - we'll do that in the value of the `values`
 dictionary as part of a tuple containing a weak reference to the object, and the corresponding value):
'''

# %%
class IntegerValue:
    def __init__(self):
        self.values = {}
        
    def __set__(self, instance, value):
        self.values[id(instance)] = (weakref.ref(instance, self._remove_object), 
                                     int(value)
                                    )
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            value_tuple = self.values.get(id(instance))
            return value_tuple[1]  # return the associated value, not the weak ref
        
    def _remove_object(self, weak_ref):
        print(f'removing dead entry for {weak_ref}')
        # how do we find that weak reference?

# %%
'''
Let's just make sure our call back is being called as expected:
'''

# %%
class Point:
    x = IntegerValue()

# %%
p1 = Point()
p2 = Point()

# %%
p1.x, p2.x = 10.1, 100.1

# %%
p1.x, p2.x

# %%
'''
Now let's delete those objects:
'''

# %%
ref_count(id(p1)), ref_count(id(p2))

# %%
del p1

# %%
del p2

# %%
'''
OK, so now all that's left is to remove the corresponding entry from the dictionary. Problem is that we do not have 
the object itself at that point (and therefore do not have it's id either), so we cannot get to the dictionary item 
using the key - we'll simply have to iterate through the values in the dictionary until we find the value whose 
first item is the weak reference that caused the call back:
'''

# %%
class IntegerValue:
    def __init__(self):
        self.values = {}
        
    def __set__(self, instance, value):
        self.values[id(instance)] = (weakref.ref(instance, self._remove_object), 
                                     int(value)
                                    )
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            value_tuple = self.values.get(id(instance))
            return value_tuple[1]  # return the associated value, not the weak ref
        
    def _remove_object(self, weak_ref):
        reverse_lookup = [key for key, value in self.values.items()
                         if value[0] is weak_ref]
        if reverse_lookup:
            # key found
            key = reverse_lookup[0]
            del self.values[key]

# %%
class Point:
    x = IntegerValue()

# %%
p = Point()

# %%
p.x = 10.1

# %%
p.x

# %%
Point.x.values

# %%
'''
Now let's delete our (only) strong reference to `p`:
'''

# %%
ref_count(id(p))

# %%
del p

# %%
Point.x.values

# %%
'''
And as you can see our dictionary was cleaned up.
'''

# %%
'''
There is one last caveat, when we create weak references to objects, the weak reference objects are actually stored in 
the instance itself, in a property called `__weakref__`:
'''

# %%
class Person:
    pass

# %%
Person.__dict__

# %%
'''
Notice that `__weakref__` attribute. It is technically a data descriptor:
'''

# %%
hasattr(Person.__weakref__, '__get__'), hasattr(Person.__weakref__, '__set__')

# %%
'''
And instances will therefore have that property:
'''

# %%
p = Person()

# %%
hasattr(p, '__weakref__')

# %%
print(p.__weakref__)

# %%
'''
As you can see, that `__weakref__` attribute exists, but is currently `None`.

Now let's create a weak reference to `p`:
'''

# %%
w = weakref.ref(p)

# %%
'''
And `__weakref__` is no longer `None` (internally it is implemented as doubly linked list of all the weak references 
to that object - but this is an implementation detail and Python does not expose functionality to iterate through 
the weak references ourselves)
'''

# %%
p.__weakref__

# %%
'''
Now the problem if we use slots, is that the instances will no longer have that attribute!
'''

# %%
class Person:
    __slots__ = 'name',

# %%
Person.__dict__

# %%
'''
As you can see `__weakref__` is no longer an attribute in our class, and the instances do not have it:
'''

# %%
p = Person()

# %%
hasattr(p, '__weakref__')

# %%
'''
So, the problem is that we can no longer create weak references to this object!!
'''

# %%
try:
    weakref.ref(p)
except TypeError as ex:
    print(ex)

# %%
'''
In order to enable weak references in objects that use slots, we need to specify `__weakref__` as one of the slots:
'''

# %%
class Person:
    __slots__ = 'name', '__weakref__'

# %%
Person.__dict__

# %%
'''
As you can see `__weakref__` is back, and exists in our instances:
'''

# %%
p = Person()

# %%
hasattr(p, '__weakref__')

# %%
'''
Which means we can create weak references to our `Person` object again:
'''

# %%
w = weakref.ref(p)

# %%
'''
So, if we want to use data descriptors using weak references (whether using our own dictionary or a weak key dictionary)
with classes that define slots, we'll need to make sure we add `__weakref__` to the slots!
'''

# %%
'''
Let's do another example using this latest technique:
'''

# %%
class ValidString:
    def __init__(self, min_length=0, max_length=255):
        self.data = {}
        self._min_length = min_length
        self._max_length = max_length
        
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('Value must be a string.')
        if len(value) < self._min_length:
            raise ValueError(
                f'Value should be at least {self._min_length} characters.'
            )
        if len(value) > self._max_length:
            raise ValueError(
                f'Value cannot exceed {self._max_length} characters.'
            )
        self.data[id(instance)] = (weakref.ref(instance, self._finalize_instance), 
                                   value
                                  )
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            value_tuple = self.data.get(id(instance))
            return value_tuple[1]  
        
    def _finalize_instance(self, weak_ref):
        reverse_lookup = [key for key, value in self.data.items()
                         if value[0] is weak_ref]
        if reverse_lookup:
            # key found
            key = reverse_lookup[0]
            del self.data[key]

# %%
'''
We can now use `ValidString` as many times as we need:
'''

# %%
class Person:
    __slots__ = '__weakref__',
    
    first_name = ValidString(1, 100)
    last_name = ValidString(1, 100)
    
    def __eq__(self, other):
        return (
            isinstance(other, Person) and 
            self.first_name == other.first_name and 
            self.last_name == other.last_name
        )
    
class BankAccount:
    __slots__ = '__weakref__',
    
    account_number = ValidString(5, 255)
    
    def __eq__(self, other):
        return (
            isinstance(other, BankAccount) and 
            self.account_number == other.account_number
        )

# %%
p1 = Person()

# %%
try:
    p1.first_name = ''
except ValueError as ex:
    print(ex)

# %%
p2 = Person()

# %%
p1.first_name, p1.last_name = 'Guido', 'van Rossum'
p2.first_name, p2.last_name = 'Raymond', 'Hettinger'

# %%
b1, b2 = BankAccount(), BankAccount()

# %%
b1.account_number, b2.account_number = 'Savings', 'Checking'

# %%
p1.first_name, p1.last_name

# %%
p2.first_name, p2.last_name

# %%
b1.account_number, b2.account_number

# %%
'''
We can look at the data dictionary in each of the data descriptor instances:
'''

# %%
Person.first_name.data

# %%
Person.last_name.data

# %%
BankAccount.account_number.data

# %%
'''
And if our objects are garbage collected:
'''

# %%
del p1
del p2
del b1
del b2

# %%
Person.first_name.data

# %%
Person.last_name.data

# %%
BankAccount.account_number.data

# %%
'''
we can see that our dictionaries were cleaned up too!
'''

# %%
'''
OK, so this was a long journey, but it now allows us to handle classes that use slots and are not hashable. 
Depending on your needs, you may not need all this functionality (for example your objects may be guaranteed 
to be hashable and supports weak refs, in which case you can use the weak key dictionary approach), or maybe 
your class is guaranteed not to use slots (or contains `__dict__` as one of the slots), in which case you can 
just use the instance itself for storage (although the name to use is still an outstanding issue).
'''

# %%
'''
We'll circle back to using the instance for storage instead of using the data descripor itself in the next set of 
lectures.
'''

# %%
