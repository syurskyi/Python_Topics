# %%
'''
### Automatic Values
'''

# %%
'''
Enumerations have a builtin mechanism to auto assign values to members.
'''

# %%
'''
This is often useful when you migth have a simple associated integer value that is sequential, 
for example `1, 2, 3, 4, ...`
'''

# %%
'''
We can easily let enums assign their own values this way, using the `auto()` function in the enum module.

By default it will use sequential integers, starting at `1`:
'''

# %%
import enum

# %%
class State(enum.Enum):
    WAITING = enum.auto()
    STARTED = enum.auto()
    FINISHED = enum.auto()

# %%
for member in State:
    print(member.name, member.value)

# %%
'''
We can actually mix in our own values too, but we have to be really careful - nothing in the Python documentation 
states what will/will not work - their only advice is ```Care must be taken if you mix auto with other values```. 
That's not saying much, and so I **never** mix auto-generated values and my own - just to be on the safe side.
'''

# %%
'''
This seems to work fine:
'''

# %%
class State(enum.Enum):
    WAITING = 5
    STARTED = enum.auto()
    FINISHED = enum.auto()

# %%
for member in State:
    print(member.name, member.value)

# %%
'''
But observe what happens here:
'''

# %%
class State(enum.Enum):
    WAITING = enum.auto()
    STARTED = 1
    FINISHED = enum.auto()
    
for member in State:
    print(member.name, member.value)
    
State.__members__

# %%
'''
As you can see, `STARTED` ended up being an alias for `WAITING` - not what my intention was.
Using `@unique` does not solve the issue, although it does make it immediately clear that there is a problem:
'''

# %%
try:
    @enum.unique
    class State(enum.Enum):
        WAITING = enum.auto()
        STARTED = 1
        FINISHED = enum.auto()
except ValueError as ex:
    print(ex)

# %%
'''
Enum classes use the `_generate_next_value_` method to generate these automatic values, and we can actually override 
this to provide our implementation of an automatic value. The default implemtation currently generates a sequence 
of numbers, but the actual algorithm is an implementation detail - i.e. we cannot rely on any specific sequence 
of values being generated.

Wecan however override it if we wish:
'''

# %%
class State(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        print(name, start, count, last_values)
        return 100
    
    a = enum.auto()
    b = enum.auto()
    c = enum.auto()

# %%
'''
As we can see the `last_values` property is a list of all the preceding values used for member. The `count` property 
is simply the number of enum members already created (including aliases!). The `name` property 
is the name of the member. The `start` argument is actually only used when we create enumerations using a functional 
approach (very similar to how we created named tuples) - but I am not going to cover this in this course 
(feel free to explore the Python docs, it's quite straightforward).
'''

# %%
'''
Let's see a more interesting example of how we could use this override. Let's say we want the associated values 
to be random integers, where we do not want duplicates.
'''

# %%
import random

random.seed(0)

class State(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        while True:
            new_value = random.randint(1, 100)
            if new_value not in last_values:
                return new_value
            
    a = enum.auto()
    b = enum.auto()
    c = enum.auto()

# %%
for member in State:
    print(member.name, member.value)

# %%
'''
Another example, shown in the Python docs is using the string of the member name as the value. In this example 
I choose to title case the name:
'''

# %%
class State(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.title()  
    
    WAITING = enum.auto()
    STARTED = enum.auto()
    FINISHED = enum.auto()
    
for member in State:
    print(member.name, member.value)

# %%
'''
If we want to make our `_generate_next_value_` implementation reusable across more than one enumeration, 
we could create an enumeration that only implements this functionality, and then use that as the parent class 
to our other enumerations:
'''

# %%
class NameAsString(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

# %%
class Enum1(NameAsString):
    A = enum.auto()
    B = enum.auto()
    
class Enum2(NameAsString):
    WAIT = enum.auto()
    RUNNING = enum.auto()
    FINISHED = enum.auto()

# %%
for member in Enum1:
    print(member.name, member.value)
    
for member in Enum2:
    print(member.name, member.value)

# %%
'''
### Note
'''

# %%
'''
Sometimes, we don't actually care about the associated value for each member. In that case we can certainly
use `auto()`, but the problem might be that users of our enumeration rely on that associated value.
'''

# %%
'''
Later, if we want to add items to the enumeration (somewhere in the middle), our users' code would break.
'''

# %%
'''
We might therefore want to discourage our users from ever using the associated value, and only using the keys.
'''

# %%
'''
Although we can (and should) document this, we can also enforce this using a simple trick. We assign an instance of 
`object` as the value for each member. There is very little our users can then do with that value, and so 
we are ensuring their safety.
'''

# %%
class State(enum.Enum):
    WAIT = object()
    RUNNING = object()
    FINISHED = object()

# %%
State.WAIT, State.RUNNING, State.FINISHED

# %%
'''
In order for a user to use the value, they would have to first get a handle to the object instance itself - 
they would never get that back from a literal string, integer, etc.
'''

# %%
'''
Now, instead of remembering to use `object()` for every member, we could use a base class to make it reusable 
(and a consistent implementation), and the auto functionality:
'''

# %%
class ValuelessEnum(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return object()
    
class State(ValuelessEnum):
    WAIT = enum.auto()
    RUNNING = enum.auto()
    FINISHED = enum.auto()
    
class Errors(ValuelessEnum):
    NumberError = enum.auto()
    IndexError = enum.auto()
    TimeoutError = enum.auto()

# %%
State.WAIT, Errors.TimeoutError

# %%
'''
By using a base class, we could technically change our implementation of how the values are generated
without having to touch our subclassed enumerations:
'''

# %%
class ValuelessEnum(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        while True:
            new_value = random.randint(1, 100)
            if new_value not in last_values:
                return new_value
    
class State(ValuelessEnum):
    WAIT = enum.auto()
    RUNNING = enum.auto()
    FINISHED = enum.auto()
    
class Errors(ValuelessEnum):
    NumberError = enum.auto()
    IndexError = enum.auto()
    TimeoutError = enum.auto()

# %%
State.WAIT, Errors.TimeoutError

# %%
'''
### Auto and Aliases
'''

# %%
'''
I want to touch back on the `count` argument of `_generate_next_value_` when are are dealing with aliases.
'''

# %%
'''
Since the default implementation of `_generate_next_value_` generates sequential integer numbers, we can never 
create aliases using this default.
'''

# %%
'''
However, nothing stops us from doing so when we have our own implementation of that function. In that case `count` 
will reflect the number of items created, **including** any aliases.
'''

# %%
class Aliased(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        print(f'count={count}')
        if count % 2 == 1:
            # odd, make this member an alias of the previous one
            return last_values[-1]
        else:
            # make a new value
            return last_values[-1] + 1
       
    GREEN = 1
    GREEN_ALIAS = 1
    RED = 10
    CRIMSON = enum.auto()
    BLUE = enum.auto()
    AQUA = enum.auto()

# %%
'''
As you can see `_generate_next_value_` was called for the last three members of our enum, and reflect the number of 
items that were created to that point, including aliases.
'''

# %%
list(Aliased)

# %%
Aliased.__members__

# %%
