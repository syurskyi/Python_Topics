# %%
'''
### Project 1 - Transactions
'''

# %%
'''
Our code so far:
'''

# %%
import itertools
import numbers
from datetime import timedelta, datetime
from collections import namedtuple


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
Now it's time to add in support for the various transaction methods:
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
    
    def deposit(self, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Deposit value must be a real number.')
        if value <= 0:
            raise ValueError('Deposit value must be a positive number.')
        
        # get transaction code
        transaction_code = Account._transaction_codes['deposit']
        
        # generate a confirmation code
        conf_code = self.generate_confirmation_code(transaction_code)
        
        # make deposit and return conf code
        self._balance += value
        return conf_code
    
    def withdraw(self, value):
        # hmmm... repetitive code! we'll need to fix this
        # TODO: refactor a function to validate a valid positive number
        #       and use in __init__, deposit and 
        
        accepted = False
        if self.balance - value < 0:
            # insufficient funds - we'll reject this transaction
            transaction_code = Account._transaction_codes['rejected']
        else:
            transaction_code = Account._transaction_codes['withdraw']
            accepted = True
            
        conf_code = self.generate_confirmation_code(transaction_code)
        
        # Doing this here in case there's a problem generating a confirmation code
        # - do not want to modify the balance if we cannot generate a transaction code successfully
        if accepted:
            self._balance -= value
            
        return conf_code
    
    def pay_interestt(self):
        interest = self.balance * Account.get_interest_rate() / 100
        conf_code = self.generate_confirmation_code(Account._transaction_codes['interest'])
        self._balance += interest
        return conf_code

# %%
a = Account('A100', 'Eric', 'Idle', TimeZone('MST', -7, 0), 100.0)

# %%
a.balance

# %%
a.deposit(100)

# %%
a.balance

# %%
a.withdraw(100)

# %%
a.balance

# %%
a.withdraw(1000)

# %%
a.balance

# %%
'''
#### Refactoring
'''

# %%
'''
So now, let's refactor some code. We have to do that real positive number validation. We'll deal with it in the same 
we dealt with the name validations, except we won't be storing anything - this is going to be a good candidate 
for a static method.
While we're at it, we'll modify our `__init__` method as well to validate the balance. Remember I had stated in 
the project description that balances should never be negative. So, I'm going to introduce a subtle bug here where 
the initialization will validate that the initial balance is a real number, but will not validate that 
it be non-negative. We'll "catch" that bug later.
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
        
        self._balance = Account.validate_real_number(initial_balance)
        
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
        
    @staticmethod
    def validate_real_number(value, min_value=None):
        if not isinstance(value, numbers.Real):
            raise ValueError('Value must be a real number.')
            
        if min_value is not None and value < min_value:
            raise ValueError(f'Value must be at least {min_value}')
            
        # validation passed, return valid value
        return value
    
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
    
    def deposit(self, value):
        value = Account.validate_real_number(value, min_value=0.01)
       
        # get transaction code
        transaction_code = Account._transaction_codes['deposit']
        
        # generate a confirmation code
        conf_code = self.generate_confirmation_code(transaction_code)
        
        # make deposit and return conf code
        self._balance += value
        return conf_code
    
    def withdraw(self, value):
        value = Account.validate_real_number(value, min_value=0.01)
        accepted = False
        if self.balance - value < 0:
            # insufficient funds - we'll reject this transaction
            transaction_code = Account._transaction_codes['rejected']
        else:
            transaction_code = Account._transaction_codes['withdraw']
            accepted = True
            
        conf_code = self.generate_confirmation_code(transaction_code)
        
        # Doing this here in case there's a problem generating a confirmation code
        # - do not want to modify the balance if we cannot generate a transaction code successfully
        if accepted:
            self._balance -= value
            
        return conf_code
    
    def pay_interest(self):
        interest = self.balance * Account.get_interest_rate() / 100
        conf_code = self.generate_confirmation_code(self._transaction_codes['interest'])
        self._balance += interest
        return conf_code

# %%
'''
We should now be seeing exceptions when using non-real or negative numbers
'''

# %%
a = Account('A100', 'Eric', 'Idle', initial_balance=100)

# %%
try:
    a.deposit(-100)
except ValueError as ex:
    print(ex)

# %%
try:
    a.withdraw("100")
except ValueError as ex:
    print(ex)

# %%
'''
So this is where I am going to leave this implementation. In reality, there are a lof of other things we should consider
 such as additional validations, defining equality for two `Account` instances, and so on.
Also, one major piece we have not really done is any kind of testing! We manually tested various pieces as
we were coding, but there are multiple problems with this:
- the tests are not easily repeatable - every time we change code in our `Account` class we **really** 
need to re-run all the tests to make sure everything still works as expected and we have not broken anything.
- our tests were woefully inadequate - we tested just a few cases, and almost no edge cases.
For serious production work, we need to test at least at the following levels:
- unit testing - where we test each piece of code in isolation and make sure all code branches are tested, 
edge cases are tested, etc (coverage)
- integration testing - where we test that multiple parts of our code works together correctly. For example, 
testing that multiple account creation, deposits, interest deposits, withdrawals, confirmation codes, etc work properly
as a whole.
'''

# %%
