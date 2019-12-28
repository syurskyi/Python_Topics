# %%
'''
### Project 2 - Solution
'''

# %%
from functools import total_ordering

@total_ordering
class Mod:
    def __init__(self, value, modulus):
        if not isinstance(modulus, int):
            raise TypeError('Unsupported type for modulus')
        if not isinstance(value, int):
            raise TypeError('Unsupported type for value')
        if modulus <= 0:
            raise ValueError('Modulus must be positive')

        self._modulus = modulus
        self._value = value % modulus  # store residue as the value
        
    @property
    def modulus(self):
        return self._modulus
    
    @property
    def value(self):
        return self._value
    
    def __repr__(self):
        return f'Mod({self._value}, {self._modulus})'
    
    def __int__(self):
        # calculates the value (residue)
        return self.value

    def __eq__(self, other):
        # calculates congruence (same equivalence class)
        if isinstance(other, Mod):
            if self.modulus != other.modulus:
                return NotImplemented
            else:
                return self.value == other.value
        elif isinstance(other, int):
            return other % self.modulus == self.value
        else:
            return NotImplemented
    
    def __hash__(self):
        return hash((self.value, self.modulus))
    
    def __neg__(self):
        return Mod(-self.value, self.modulus)
    
    def __add__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value + other.value, self.modulus)
        if isinstance(other, int):
            return Mod(self.value + other, self.modulus)
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self.value = (self.value + other.value) % self.modulus
            return self
        elif isinstance(other, int):
            self.value = (self.value + other) % self.modulus
            return self
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value - other.value, self.modulus)
        if isinstance(other, int):
            return Mod(self.value - other, self.modulus)
        return NotImplemented
    
    def __isub__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self.value = (self.value - other.value) % self.modulus
            return self
        if isinstance(other, int):
            self.value = (self.value - other) % self.modulus
            return self
        return NotImplemented
        
    def __mul__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value * other.value, self.modulus)
        if isinstance(other, int):
            return Mod(self.value * other, self.modulus)
        return NotImplemented
    
    def __imul__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self.value = (self.value * other.value) % self.modulus
            return self
        if isinstance(other, int):
            self.value = (self.value * other) % self.modulus
            return self
        return NotImplemented
    
    def __pow__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value ** other.value, self.modulus)
        if isinstance(other, int):
            # use residue of other, to make computation potentially smaller
            return Mod(self.value ** (other % self.modulus), self.modulus)
        return NotImplemented
    
    def __ipow__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self.value = (self.value ** other.value) % self.modulus
            return self
        if isinstance(other, int):
            # use residue of other, to make computation potentially smaller
            self.value = (self.value ** (other % self.modulus)) % self.modulus
            return self
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return self.value < other.value
        if isinstance(other, int):
            return self.value < other % self.modulus
        return NotImplemented

# %%
'''
You should test this class writing some unit tests!
'''

# %%
'''
OK, so this class implementation seems to work, but I'm not happy about the amount of repetitive code we had to write 
(all those checks to make sure we either have a comparable Mod instance, and then either using the value of the Mod 
instance or the int depending on what was passed in).
I really want to do something about that.
'''

# %%
'''
First thing is I'm going to add a "private" method that will indicate whether two objects are compatible.
 Maybe something like this:
'''

# %%
def _is_compatible(self, other):
    return isinstance(other, int) or (isinstance(other, Mod) and self.modulus == other.modulus)

# %%
'''
But then I'm still left with which value do I use,  `.value` or the `int` itself. So, I'm going to make that part 
of the compatibility check. 
Here, I'm going to use exceptions to indicate an incompatible type, otherwise I'll return the value we should use. 
Something like this:
'''

# %%
def _get_value(self, other):
    if isinstance(other, int):
        return other % self.modulus  # return the residue
    if isinstance(other, Mod) and self.modulus == other.modulues:
        return other.value
    raise TypeError('Incompatible types.')

# %%
'''
And then I can refactor my class accordingly. Also, even though we should technically return `NotImplemented` 
(to allow Python to use reflection), in this case the reflection is not going to be needed, so I'm just going to let 
the `TypeError` exception through.
The only exception to this is for ordering - we **do** want Python to try to reflect a `<` if `>` is not implemented 
(although using `@total_ordering` means this does not really matter anyway).
'''

# %%
from functools import total_ordering

@total_ordering
class Mod:
    def __init__(self, value, modulus):
        if not isinstance(modulus, int):
            raise TypeError('Unsupported type for modulus')
        if not isinstance(value, int):
            raise TypeError('Unsupported type for value')
        if modulus <= 0:
            raise ValueError('Modulus must be positive')

        self._modulus = modulus
        self._value = value % modulus  # store residue as the value
        
    @property
    def modulus(self):
        return self._modulus
    
    @property
    def value(self):
        return self._value
    
    def __repr__(self):
        return f'Mod({self._value}, {self._modulus})'
    
    def __int__(self):
        # calculates the value (residue)
        return self.value

    def _get_value(self, other):
        if isinstance(other, int):
            return other % self.modulus  # return the residue
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return other.value
        raise TypeError('Incompatible types.')
    
    def __eq__(self, other):
        # calculates congruence (same equivalence class)
        other_value = self._get_value(other)
        return other_value == self.value
    
    def __hash__(self):
        return hash((self.value, self.modulus))
    
    def __neg__(self):
        return Mod(-self.value, self.modulus)
    
    def __add__(self, other):
        other_value = self._get_value(other)
        return Mod(self.value + other_value, self.modulus)
    
    def __iadd__(self, other):
        other_value = self._get_value(other)
        self.value = (self.value + other_value) % self.modulus
        return self
    
    def __sub__(self, other):
        other_value = self._get_value(other)
        return Mod(self.value - other_value, self.modulus)
    
    def __isub__(self, other):
        other_value = self._get_value(other)
        self.value = (self.value - other_value) % self.modulus
        return self
    
    def __mul__(self, other):
        other_value = self._get_value(other)
        return Mod(self.value * other_value, self.modulus)
    
    def __imul__(self, other):
        other_value = self._get_value(other)
        self.value = (self.value * other_value) & self.modulus
        return self
    
    def __pow__(self, other):
        other_value = self._get_value(other)
        return Mod(self.value ** other_value, self.modulus)
        
    def __ipow__(self, other):
        other_value = self._get_value(other)
        self.value = (self.value ** other_value) % self.modulus
        return self
    
    def __lt__(self, other):
        # here, raising a TypeError instead of returning NotImplemented
        # would result in Python not trying the reflection - which we DO want
        # although since we are using @total_ordering this does not really matter
        try:
            other_value = self._get_value(other)
            return self.value < other_value
        except TypeError:
            return NotImplemented

# %%
'''
Ok, so this is better, but there still quite a bit of repetitive code for the addition, subtraction, multiplcation and 
power operations - the only thing that changes there is which particular arithmetic operator we are delegating to.
'''

# %%
'''
So, I'm going to use the `operator` module to simplify things even further.
'''

# %%
import operator

# %%
operator.mul(2, 3)

# %%
operator.add(2, 3)

# %%
'''
So, now I'm going to write a generic `_compute` that will perform the requested operation, and return either a new `Mod` 
object, or do the in-place calculation (I'll use an optional keyword-only arg for this).
So, something like this:
'''

# %%
def _perform_operation(self, other, op, *, in_place=False):
    other_value = self._get_value(other)
    new_value = op(self.value, other_value)
    if in_place:
        self.value = new_value % self.modulus
        return self
    else:
        return Mod(new_value, self.modulus)

# %%
'''
Let's add that to our class and refactor one more time:
'''

# %%
from functools import total_ordering

@total_ordering
class Mod:
    def __init__(self, value, modulus):
        if not isinstance(modulus, int):
            raise TypeError('Unsupported type for modulus')
        if not isinstance(value, int):
            raise TypeError('Unsupported type for value')
        if modulus <= 0:
            raise ValueError('Modulus must be positive')

        self._modulus = modulus
        self._value = value % modulus  # store residue as the value
        
    @property
    def modulus(self):
        return self._modulus
    
    @property
    def value(self):
        return self._value
    
    def __repr__(self):
        return f'Mod({self._value}, {self._modulus})'
    
    def __int__(self):
        # calculates the value (residue)
        return self.value

    def _get_value(self, other):
        if isinstance(other, int):
            return other % self.modulus  # return the residue
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return other.value
        raise TypeError('Incompatible types.')
    
    def _perform_operation(self, other, op, *, in_place=False):
        other_value = self._get_value(other)
        new_value = op(self.value, other_value)
        if in_place:
            self.value = new_value % self.modulus
            return self
        else:
            return Mod(new_value, self.modulus)
    
    def __eq__(self, other):
        # calculates congruence (same equivalence class)
        other_value = self._get_value(other)
        return other_value == self.value
    
    def __hash__(self):
        return hash((self.value, self.modulus))
    
    def __neg__(self):
        return Mod(-self.value, self.modulus)
    
    def __add__(self, other):
        return self._perform_operation(other, operator.add)
    
    def __iadd__(self, other):
        return self._perform_operation(other, operator.add, in_place=True)
    
    def __sub__(self, other):
        return self._perform_operation(other, operator.sub)
    
    def __isub__(self, other):
        return self._perform_operation(other, operator.sub, in_place=True)
    
    def __mul__(self, other):
        return self._perform_operation(other, operator.mul)
    
    def __imul__(self, other):
        return self._perform_operation(other, operator.mul, in_place=True)
    
    def __pow__(self, other):
        return self._perform_operation(other, operator.pow)
        
    def __ipow__(self, other):
        return self._perform_operation(other, operator.pow, in_place=True)
    
    def __lt__(self, other):
        # here, raising a TypeError instead of returning NotImplemented
        # would result in Python not trying the reflection - which we DO want
        # although since we are using @total_ordering this does not really matter
        try:
            other_value = self._get_value(other)
            return self.value < other_value
        except TypeError:
            return NotImplemented

# %%
'''
OK, so if you had your unit tests set up, each refactor we did would only have needed re-running the unit tests to make 
sure we did not break anything!
'''