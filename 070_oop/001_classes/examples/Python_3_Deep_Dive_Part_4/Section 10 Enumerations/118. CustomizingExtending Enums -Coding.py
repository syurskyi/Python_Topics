# %%
'''
### Customizing and Extending Enumerations
'''

# %%
'''
Enumerations, although they behave a little differently than normal classes, are **still** classes.
'''

# %%
'''
This means there are many things we can customize about them.
'''

# %%
'''
Keep in mind that members of the enumerations are **instances** of the enumeration class, so we can implement methods 
in that class, and each member will have that method (boud to itself) available.
'''

# %%
from enum import Enum

# %%
class Color(Enum):
    red = 1
    green = 2
    blue = 3
    
    def purecolor(self, value):
        return {self: value}

# %%
Color.red.purecolor(100), Color.blue.purecolor(200)

# %%
'''
Amongst other things, we can implement some of the "standard" dunder methods. For example we may wish to override 
the default representation:
'''

# %%
Color.red

# %%
class Color(Enum):
    red = 1
    green = 2
    blue = 3
    
    def __repr__(self):
        return f'{self.name} ({self.value})'

# %%
Color.red

# %%
'''
Of course, we can implement other more interesting dunder methods.
'''

# %%
'''
For example, in standard enums, we do not have ordering defined for the members:
'''

# %%
class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

# %%
try:
    Number.ONE > Number.TWO
except TypeError as ex:
    print(ex)

# %%
'''
But in this particular example it might make sense to actually have ordering defined. We can simply implement some 
of the rich comparison operators:
'''

# %%
class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    
    def __lt__(self, other):
        return isinstance(other, Number) and self.value < other.value

# %%
'''
And now we have an ordering defined:
'''

# %%
Number.ONE < Number.TWO

# %%
Number.TWO > Number.ONE

# %%
'''
We could also potentially override the definition for equality (`==`):
'''

# %%
class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    
    def __lt__(self, other):
        return isinstance(other, Number) and self.value < other.value
    
    def __eq__(self, other):
        if isinstance(other, Number):
            return self is other
        elif isinstance(other, int):
            return self.value == other
        else:
            return False

# %%
Number.ONE == Number.ONE

# %%
Number.ONE == 1.0

# %%
Number.ONE == 1

# %%
'''
A good question to ask ourselves is whether our members are still hashable since we implemented
a custom `__eq__` method:
'''

# %%
try:
    hash(Number.ONE)
except TypeError as ex:
    print(ex)

# %%
'''
And of course, they are not. We could remedy this by implementing our own `__hash__` method.
'''

# %%
'''
Going back to ordering:
'''

# %%
class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    
    def __lt__(self, other):
        return isinstance(other, Number) and self.value < other.value

# %%
'''
Although we have `<` (and by reflection `>`) defined, we still do not have operators such as `<=`:
'''

# %%
try:
    Number.ONE <= Number.TWO
except TypeError as ex:
    print(ex)

# %%
'''
We could of course define a `__le__` method, but we could also just use the `@totalordering` decorator:
'''

# %%
from functools import total_ordering

# %%
@total_ordering
class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    
    def __lt__(self, other):
        return isinstance(other, Number) and self.value < other.value

# %%
Number.ONE <= Number.TWO, Number.ONE != Number.TWO

# %%
'''
A slightly more useful application of this ability to implement these special methods might be in this example:
'''

# %%
class Phase(Enum):
    READY = 'ready'
    RUNNING = 'running'
    FINISHED = 'finished'
    
    def __str__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, Phase):
            return self is other
        elif isinstance(other, str):
            return self.value == other
        return False
    
    def __lt__(self, other):
        ordered_items = list(Phase)
        self_order_index = ordered_items.index(self)
        
        if isinstance(other, Phase):
            other_order_index = ordered_items.index(other)
            return self_order_index < other_order_index
        
        if isinstance(other, str):
            try:
                other_member = Phase(other)
                other_order_index = ordered_items.index(other_member)
                return self_order_index < other_order_index
            except ValueError:
                # other is not a value in our enum
                return False
            

# %%
Phase.READY == 'ready'

# %%
Phase.READY < Phase.RUNNING

# %%
Phase.READY < 'running'

# %%
'''
One thing to watch out for, is that, by default, all members of an enumeration are **truthy** - irrespective 
of their value:
'''

# %%
class State(Enum):
    READY = 1
    BUSY = 0    

# %%
bool(State.READY), bool(State.BUSY)

# %%
'''
We can of course override the `__bool__` method to customize this:
'''

# %%
class State(Enum):
    READY = 1
    BUSY = 0    
    
    def __bool__(self):
        return bool(self.value)

# %%
bool(State.READY), bool(State.BUSY)

# %%
'''
So we might implement this ready/not-ready flag in our application by simply testing the truthyness of the member:
'''

# %%
request_state = State.READY

# %%
if request_state:
    print('Launching next query')
else:
    print('Not ready for another query yet')

# %%
'''
We could also easily implement a default associated truth value that reflects the truthyness of the member **values**:
'''

# %%
class Dummy(Enum):
    A = 0
    B = 1
    C = ''
    D = 'python'
    
    def __bool__(self):
        return bool(self.value)

# %%
bool(Dummy.A), bool(Dummy.B), bool(Dummy.C), bool(Dummy.D)

# %%
'''
#### Extending Custom Enumerations
'''

# %%
'''
We can also extend (subclass) our custom enumerations - but only under certain circumstances: as long as 
the enumeration we are extending does not define any **members**:
'''

# %%
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# %%
try:
    class ColorAlpha(Color):
        ALPHA = 4
except TypeError as ex:
    print(ex)

# %%
'''
But this would work:
'''

# %%
class ColorBase(Enum):
    def hello(self):
        return f'{str(self)} says hello!'
    
class Color(ColorBase):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

# %%
Color.RED.hello()

# %%
'''
This might not seem particularly useful (we cannot use subclassing to extended the members), but remember 
that we can add methods to our enumerations - this means we could define a base class that implements some common 
functionality for all our instances, and then extend this enumeration class to concrete enumerations that define 
the members.
'''

# %%
'''
Here's an example of where this might be useful:
'''

# %%
@total_ordering
class OrderedEnum(Enum):
    """Creates an ordering based on the member values. 
    So member values have to support rich comparisons.
    """
    
    def __lt__(self, other):
        if isinstance(other, OrderedEnum):
            return self.value < other.value
        return NotImplemented

# %%
'''
And now we can create other enumerations that will support ordering without having to retype the `__lt__` 
implementation, or even the decorator:
'''

# %%
class Number(OrderedEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    
class Dimension(OrderedEnum):
    D1 = 1,
    D2 = 1, 1
    D3 = 1, 1, 1

# %%
Number.ONE < Number.THREE

# %%
Dimension.D1 < Dimension.D3

# %%
Number.ONE >= Number.ONE

# %%
Dimension.D1 >= Dimension.D2

# %%
'''
Of course we could implement other functionality in our base enum 
(maybe customized `__str__`, `__repr__`, `__bool__`, etc).
'''

# %%
'''
We'll actually come back to this when we discuss auto numbering in enums.
'''

# %%
'''
#### Example
'''

# %%
'''
Here's a handy enumeration that's built-in to Python (handy if you work with http requests that is :-) )
'''

# %%
from http import HTTPStatus

# %%
type(HTTPStatus)

# %%
'''
It's technically an `EnumMeta`, but that's beyond our current scope. Still, it's easy to use and you don't need 
to know anything about meta classes:
'''

# %%
list(HTTPStatus)[0:10]

# %%
HTTPStatus(200)

# %%
HTTPStatus.OK, HTTPStatus.OK.name, HTTPStatus.OK.value

# %%
HTTPStatus(200)

# %%
HTTPStatus['OK']

# %%
'''
It even has a `phrase` property that provides a more readable version of the HTTP status (name):
'''

# %%
HTTPStatus.NOT_FOUND.value, HTTPStatus.NOT_FOUND.name, HTTPStatus.NOT_FOUND.phrase

# %%
'''
Now we could implement similar functionality very easily - maybe for our own error codes in our application:
'''

# %%
class AppStatus(Enum):
    OK = (0, 'No problem!')
    FAILED = (1, 'Crap!')

# %%
AppStatus.OK

# %%
AppStatus.OK.value

# %%
'''
What we really want is to separate the code (lie `0`) from the phrase (like `No problem!`). We could do this:
'''

# %%
class AppStatus(Enum):
    OK = (0, 'No problem!')
    FAILED = (1, 'Crap!')
    
    @property
    def code(self):
        return self.value[0]
    
    @property
    def phrase(self):
        return self.value[1]

# %%
AppStatus.OK.code, AppStatus.OK.phrase

# %%
'''
As you can see, it's close, but not quite the same as `HTTPStatus`...

One major problem is that we can no longer lookup a member by just the code:
'''

# %%
try:
    AppStatus(0)
except ValueError as ex:
    print(ex)

# %%
'''
We would have to do this:
'''

# %%
AppStatus((0, 'No problem!'))

# %%
'''
Not ideal...
'''

# %%
'''
#### Let's dig in...
'''

# %%
'''
OK, so, we can actually fix this issue by making use of the `__new__` method (which we have not studied yet, 
but I did mention it).  Remember that this is the method that gets called to **instantiate** the class -
so it should return a new instance of the class.  Furthemore we'll have it set the value property - for that `Enum` 
has a special class attribute we can use, called `_value_`. 
This is probably going to be a little confusing, but we'll circle back to this later:
'''

# %%
class AppStatus(Enum):
    OK = (0, 'No Problem!')
    FAILED = (1, 'Crap!')
    
    def __new__(cls, member_value, member_phrase):
        # create a new instance of cls
        member = object.__new__(cls)
        
        # set up instance attributes
        member._value_ = member_value
        member.phrase = member_phrase
        return member

# %%
AppStatus.OK.value, AppStatus.OK.name, AppStatus.OK.phrase

# %%
'''
And now even looking up by numeric code works:
'''

# %%
AppStatus(0)

# %%
'''
Now, we could easily break this out into a base class:
'''

# %%
class TwoValueEnum(Enum):
    def __new__(cls, member_value, member_phrase):
        member = object.__new__(cls)
        member._value_ = member_value
        member.phrase = member_phrase
        return member

# %%
'''
And then inherit this for any enumeration where we want to support a value as a `(code, phrase)` tuple:
'''

# %%
class AppStatus(TwoValueEnum):
    OK = (0, 'No Problem!')
    FAILED = (1, 'Crap!')

# %%
AppStatus.FAILED, AppStatus.FAILED.name, AppStatus.FAILED.value, AppStatus.FAILED.phrase

# %%
