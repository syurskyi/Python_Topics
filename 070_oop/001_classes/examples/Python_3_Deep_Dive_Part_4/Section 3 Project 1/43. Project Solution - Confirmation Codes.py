# %%
'''
### Project 1 - Implementing Confirmation Codes
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
    _interest_rate = 0.5  # percentage
    
    _transaction_codes = {
        'deposit': 'D',
        'withdraw': 'W',
        'interest': 'I',
        'rejected': 'X'
    }
    
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
'''
As I mentioned earlier the code should contain:
- the transaction code
- the account number
- the date / time in UTC of the transaction
- the transaction number

Something like:
```D-140568-20190115154500-124```
'''

# %%
'''
Let's first build this function in isolation, and then we'll add it to the class once we're happy with it:
'''

# %%
from datetime import datetime

# %%
def generate_confirmation_code(account_number, transaction_id, transaction_code):
    # main difficulty here is to generate the current time in UTC using this formatting:
    # YYYYMMDDHHMMSS
    dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    return f'{transaction_code}-{account_number}-{dt_str}-{transaction_id}'

# %%
generate_confirmation_code(123, 1000, 'X')

# %%
'''
Now let's incorporate that as an instance method in our class - we won't need to pass account_numberor transaction_id 
- we can get those ourselves from within the class:
'''

# %%
class Account:
    transaction_counter = itertools.count(100)
    _interest_rate = 0.5  # percentage
    
    _transaction_codes = {
        'deposit': 'D',
        'withdraw': 'W',
        'interest': 'I',
        'rejected': 'X'
    }
    
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
        
    def generate_confirmation_code(self, transaction_code):
        # main difficulty here is to generate the current time in UTC using this formatting:
        # YYYYMMDDHHMMSS
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f'{transaction_code}-{self.account_number}-{dt_str}-{next(Account.transaction_counter)}'

# %%
'''
So we can test it out, let's write a dummy transaction method:
'''

# %%
class Account:
    transaction_counter = itertools.count(100)
    _interest_rate = 0.5  # percentage
    
    _transaction_codes = {
        'deposit': 'D',
        'withdraw': 'W',
        'interest': 'I',
        'rejected': 'X'
    }
    
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
        
    def generate_confirmation_code(self, transaction_code):
        # main difficulty here is to generate the current time in UTC using this formatting:
        # YYYYMMDDHHMMSS
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f'{transaction_code}-{self.account_number}-{dt_str}-{next(Account.transaction_counter)}'
    
    def make_transaction(self):
        return self.generate_confirmation_code('dummy')

# %%
a = Account('A100', 'John', 'Cleese', initial_balance=100)

# %%
a.make_transaction()

# %%
a.make_transaction()

# %%
'''
#### Confirmation Parser
'''

# %%
'''
This one is actually going to be a static method. We don't really require the instance to reverse-engineer 
the confirmation code. We could, but then we probably would also want to check that the account number embedded 
in the conformation code is the same as the instance account number we are decoding from. There's not really a need 
for that. The other thing is we want to have a neat dotted notation to recover the various properties of the 
partsed confirmation code. Once again, before jumping into creating a utility class for that, we can really get away 
with a named tuple here instead!
'''

# %%
'''
Let's see what a confirmation code looks like:
```
dummy-A100-20190325224918-101
```
'''

# %%
'''
So, we can split things on a `-` symbol, and we'll have to parse the date time string into an actual date time 
(and we know confirmation codes use UTC dates)
'''

# %%
from collections import namedtuple

Confirmation = namedtuple('Confirmation', 'account_number, transaction_code, transaction_id, time_utc, time')

# %%
class Account:
    transaction_counter = itertools.count(100)
    _interest_rate = 0.5  # percentage
    
    _transaction_codes = {
        'deposit': 'D',
        'withdraw': 'W',
        'interest': 'I',
        'rejected': 'X'
    }
    
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
        
    def generate_confirmation_code(self, transaction_code):
        # main difficulty here is to generate the current time in UTC using this formatting:
        # YYYYMMDDHHMMSS
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f'{transaction_code}-{self.account_number}-{dt_str}-{next(Account.transaction_counter)}'
    
    @staticmethod
    def parse_confirmation_code(confirmation_code, preferred_time_zone=None):
        # dummy-A100-20190325224918-101
        parts = confirmation_code.split('-')
        if len(parts) != 4:
            # really simplistic validation here - would need something better
            raise ValueError('Invalid confirmation code')
        
        # unpack into separate variables
        transaction_code, account_number, raw_dt_utc, transaction_id = parts
        
        # need to convert raw_dt_utc into a proper datetime object
        try:
            dt_utc = datetime.strptime(raw_dt_utc, '%Y%m%d%H%M%S')
        except ValueError as ex:
            # again, probably need better error handling here
            raise ValueError('Invalid transaction datetime') from ex
          
        if preferred_time_zone is None:
            preferred_time_zone = TimeZone('UTC', 0, 0)
            
        if not isinstance(preferred_time_zone, TimeZone):
            raise ValueError('Invalid TimeZone specified.')
            
        dt_preferred = dt_utc + preferred_time_zone.offset
        dt_preferred_str = f"{dt_preferred.strftime('%Y-%m-%d %H:%M:%S')} ({preferred_time_zone.name})"
        
        return Confirmation(account_number, transaction_code, transaction_id, dt_utc.isoformat(), dt_preferred_str)
    
    def make_transaction(self):
        return self.generate_confirmation_code('dummy')

# %%
'''
OK, so let's try this out, and make sure it's working (within reason, this will not catch all badly formatted 
confirmation codes by any means):
'''

# %%
a = Account('A100', 'John', 'Cleese', initial_balance=100)
conf_code = a.make_transaction()
print(conf_code)

# %%
Account.parse_confirmation_code(conf_code)

# %%
Account.parse_confirmation_code(conf_code, TimeZone('MST', -7, 0))

# %%
try:
    Account.parse_confirmation_code('X-A100-asdasd-123')
except ValueError as ex:
    print(ex)

# %%
