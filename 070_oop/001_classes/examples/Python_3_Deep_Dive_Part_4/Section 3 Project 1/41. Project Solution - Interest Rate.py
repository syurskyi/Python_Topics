# %%
'''
### Project 1 - Interest Rate
'''

# %%
'''
Our code so far:
'''

# %%
import itertools
import numbers
from datetime import timedelta

class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name).strip()) == 0:
            raise ValueError('Timezone name cannot be empty.')
            
        self._name = str(name).strip()
        # technically we should check that offset is a
        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('Hour offset must be an integer.')
        
        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError('Minutes offset must be an integer.')
            
        if offset_minutes < -59 or offset_minutes > 59:
            raise ValueError('Minutes offset must between -59 and 59 (inclusive).')
            
        # for time delta sign of minutes will be set to sign of hours
        offset = timedelta(hours=offset_hours, minutes=offset_minutes)

        # offsets are technically bounded between -12:00 and 14:00
        # see: https://en.wikipedia.org/wiki/List_of_UTC_time_offsets
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and +14:00.')
            
        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes
        self._offset = offset
        
    @property
    def offset(self):
        return self._offset
    
    @property
    def name(self):
        return self._name
    
    def __eq__(self, other):
        return (isinstance(other, TimeZone) and 
                self.name == other.name and 
                self._offset_hours == other._offset_hours and
                self._offset_minutes == other._offset_minutes)
    def __repr__(self):
        return (f"TimeZone(name='{self.name}', "
                f"offset_hours={self._offset_hours}, "
                f"offset_minutes={self._offset_minutes})")

# %%
class Account:
    transaction_counter = itertools.count(100)
    
    def __init__(self, account_number, first_name, last_name, timezone=None, initial_balance=0):
        # in practice we probably would want to add checks to make sure these values are valid / non-empty
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        
        if timezone is None:
            timezone = TimeZone('UTC', 0, 0)
        self.timezone = timezone
        
        self._balance = float(initial_balance)  # force use of floats here, but maybe Decimal would be better
        
    @property
    def account_number(self):
        return self._account_number
    
    @property 
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        self.validate_and_set_name('_first_name', value, 'First Name')
        
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name('_last_name', value, 'Last Name')
        
    # also going to create a full_name computed property, for ease of use
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
        
    @property
    def timezone(self):
        return self._timezone
    
    @property
    def balance(self):
        return self._balance
    
    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('Time zone must be a valid TimeZone object.')
        self._timezone = value
            
    def validate_and_set_name(self, property_name, value, field_title):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, property_name, value)

# %%
'''
The interest rate is common across all bank accounts, so we can use a class attribute for it. 
We haven't studied how to write class properties (we'll see how when we look at descriptors), so for now we could just 
use a bare attribute - not ideal, but let's try that first.
'''

# %%
class Account:
    transaction_counter = itertools.count(100)
    interest_rate = 0.5  # percentage
    
    def __init__(self, account_number, first_name, last_name, timezone=None, initial_balance=0):
        # in practice we probably would want to add checks to make sure these values are valid / non-empty
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        
        if timezone is None:
            timezone = TimeZone('UTC', 0, 0)
        self.timezone = timezone
        
        self._balance = float(initial_balance)  # force use of floats here, but maybe Decimal would be better
        
    @property
    def account_number(self):
        return self._account_number
    
    @property 
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        self.validate_and_set_name('_first_name', value, 'First Name')
        
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name('_last_name', value, 'Last Name')
        
    # also going to create a full_name computed property, for ease of use
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
        
    @property
    def timezone(self):
        return self._timezone
    
    @property
    def balance(self):
        return self._balance
    
    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('Time zone must be a valid TimeZone object.')
        self._timezone = value
            
    def validate_and_set_name(self, property_name, value, field_title):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, property_name, value)

# %%
a1 = Account(1234, 'Monty', 'Python', initial_balance=0)
a2 = Account(2345, 'John', 'Cleese', initial_balance=0)

# %%
a1.interest_rate, a2.interest_rate

# %%
Account.interest_rate = 0.025

# %%
a1.interest_rate, a2.interest_rate

# %%
'''
If we don't feel comfortable with the bare attribute and want to validate changing the interest rate, then we could use
 a more Java-like approach with getter and setter class methods. 
We'll start by changing the class variable name to indicate it is a "private" attribute, then add a getter and a 
setter class method:
'''

# %%
class Account:
    transaction_counter = itertools.count(100)
    _interest_rate = 0.5  # percentage
    
    def __init__(self, account_number, first_name, last_name, timezone=None, initial_balance=0):
        # in practice we probably would want to add checks to make sure these values are valid / non-empty
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        
        if timezone is None:
            timezone = TimeZone('UTC', 0, 0)
        self.timezone = timezone
        
        self._balance = float(initial_balance)  # force use of floats here, but maybe Decimal would be better
        
    @property
    def account_number(self):
        return self._account_number
    
    @property 
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        self.validate_and_set_name('_first_name', value, 'First Name')
        
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name('_last_name', value, 'Last Name')
        
    # also going to create a full_name computed property, for ease of use
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
        
    @property
    def timezone(self):
        return self._timezone
    
    @property
    def balance(self):
        return self._balance
    
    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('Time zone must be a valid TimeZone object.')
        self._timezone = value
          
    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate
    
    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Interest rate must be a real number')
        if value < 0:
            raise ValueError('Interest rate cannot be negative.')
        cls._interest_rate = value
        
    def validate_and_set_name(self, property_name, value, field_title):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, property_name, value)

# %%
Account.get_interest_rate()

# %%
Account.set_interest_rate(10)

# %%
Account.get_interest_rate()

# %%
try:
    Account.set_interest_rate(-10)
except ValueError as ex:
    print(ex)

# %%
try:
    Account.set_interest_rate(1+1j)
except ValueError as ex:
    print(ex)

# %%
