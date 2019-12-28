# %%
'''
### Project 1 - Unit Testing
'''

# %%
'''
As you can imagine to fully test this code is going to take quite a bit of effort. I'm not going to do this here, 
so I very well may have bugs in my code. 
'''

# %%
'''
In practice, a whole suite of tests should be written to ensure this code is working properly.
'''

# %%
'''
If you're thinking this will be as much work as writing the code itself - well... It will probably be **more** work.
In my experience, designing and implementing unit tests takes longer than writing the code in the first place!
'''

# %%
'''
Here's a manual approach to a bit of integration testing:
'''

# %%
'''
First, our code:
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
        conf_code = self.generate_confirmation_code(Account._transaction_codes['interest'])
        self._balance += interest
        return conf_code

# %%
a = Account('A100', 'Eric', 'Idle', timezone=TimeZone('MST', -7, 0), initial_balance=100)
print(a.balance)
print(a.deposit(150.02))
print(a.balance)
print(a.withdraw(0.02))
print(a.balance)
Account.set_interest_rate(1.0)
print(a.get_interest_rate())
print(a.pay_interest())
print(a.balance)
print(a.withdraw(1000))

# %%
'''
OK, so that works, but of course we really need to test things a whole lot more, including various scenarios 
(like withdrawing with insufficient funds, and so on). Also our tests really need to be easily repeatable so we can 
re-run our tests every time we make a code change.
For that I'm going to introduce you to the `unitest` framework in Python.
In production environments, a 3rd party library (that leverages `unittest`) is used that extends the base `unittest` 
framework. But for now, `unittest` will work just fine for us.
'''

# %%
'''
Normally, unit tests are invoked from the command line, which in turn sets up a test runner and seamlessly runs 
our tests. In this case, so I can stay within a Jupyter Notebook I'll have to add a few extra chunks of code to set up 
a test runner manually - this is usually not necessary.
'''

# %%
import unittest

# %%
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

# %%
'''
Let's see how some simple tests are setup and executed:
'''

# %%
class TestAccount(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(1, 1)

# %%
run_tests(TestAccount)

# %%
'''
In cases where the a test fails:
'''

# %%
class TestAccount(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(1, 0)

# %%
run_tests(TestAccount)

# %%
'''
So now we can write some simple unit tests. The only thing is that each unit test should be a function in the class 
that starts with the word `test` - that way it is automatically identified as a unit test.
We also have the option of defining setup and tear down functionality - these are just methods that will be executed 
before **each** test method, and right **after**. - here's a simple example that shows how that works:
'''

# %%
class TestAccount(unittest.TestCase):
    def setUp(self):
        print('Running setup...')
        self.account_number = 'A100'
        
    def tearDown(self):
        print('Running tear down...')
        
    def test_1(self):
        self.account_number = 'A200'
        self.assertTrue('A200', self.account_number)
        
    def test_2(self):
        self.assertTrue('A100', self.account_number)

# %%
run_tests(TestAccount)

# %%
'''
Even, if the test fails, the tear down method will still run:
'''

# %%
class TestAccount(unittest.TestCase):
    def setUp(self):
        print('Running setup...')
        
    def tearDown(self):
        print('Running tear down...')
        
    def testOK(self):
        self.assertTrue(False)

# %%
run_tests(TestAccount)

# %%
'''
So we could use `setUp` to maybe create some bank accounts that we can use throughout our tests. Remember that 
`TestAccount` is a class, so we can create instance attributes in the `setUp` method, and access them in any of the 
instance methods (like the test methods).
Another thing to watch out for is that there is no guarantee of the order in which the unit tests are run. 
Best practice is that unit tests should be independent of each other.
'''

# %%
'''
Let's add some simple unit tests for the TimeZone class first:
'''

# %%
class TestAccount(unittest.TestCase):
   
    def test_create_timezone(self):
        tz = TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)
        
    def test_timezones_equal(self):
        tz1 = TimeZone('ABC', -1, -30)
        tz2 = TimeZone('ABC', -1, -30)
        self.assertEqual(tz1, tz2)
        
    def test_timezones_not_equal(self):
        tz = TimeZone('ABC', -1, -30)
        
        test_timezones = (
            TimeZone('DEF', -1, -30),
            TimeZone('ABC', -1, 0),
            TimeZone('ABC', 1, -30)
        )
        for test_tz in test_timezones:
            self.assertNotEqual(tz, test_tz)

# %%
run_tests(TestAccount)

# %%
'''
Notice how we needed to run multiple scenarios for testing non-equal time zones. This is a fairly common occurrence,
 and there's a better way to set this up so we actually have separate tests, that are distinguishable from each other
  (it's slightly easier when using pytest, but the end result is similar):
'''

# %%
class TestAccount(unittest.TestCase):
    
    def test_create_timezone(self):
        tz = TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)
        
    def test_timezones_equal(self):
        tz1 = TimeZone('ABC', -1, -30)
        tz2 = TimeZone('ABC', -1, -30)
        self.assertEqual(tz1, tz2)
        
    def test_timezones_not_equal(self):
        tz = TimeZone('ABC', -1, -30)
        
        test_timezones = (
            TimeZone('DEF', -1, -30),
            TimeZone('ABC', -1, 0),
            TimeZone('ABC', 1, -30)
        )
        for i, test_tz in enumerate(test_timezones):
            with self.subTest(test_number=i):
                self.assertNotEqual(tz, test_tz)

# %%
run_tests(TestAccount)

# %%
'''
Where this might be handy is in the case of a test failure:
'''

# %%
class TestAccount(unittest.TestCase):
    
    def test_create_timezone(self):
        tz = TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)
        
    def test_timezones_equal(self):
        tz1 = TimeZone('ABC', -1, -30)
        tz2 = TimeZone('ABC', -1, -30)
        self.assertEqual(tz1, tz2)
        
    def test_timezones_not_equal(self):
        tz = TimeZone('ABC', -1, -30)
        
        test_timezones = (
            TimeZone('DEF', -1, -30),
            TimeZone('ABC', -1, 0),
            TimeZone('ABC', 1, -30),
            TimeZone('ABC', -1, -30)
        )
        for i, test_tz in enumerate(test_timezones):
            with self.subTest(test_number=i):
                self.assertNotEqual(tz, test_tz)

# %%
run_tests(TestAccount)

# %%
'''
As you can see we have a message associated with the failed test.
Let's go back and remove that incorrect test:
'''

# %%
class TestAccount(unittest.TestCase):
    
    def test_create_timezone(self):
        tz = TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)
        
    def test_timezones_equal(self):
        tz1 = TimeZone('ABC', -1, -30)
        tz2 = TimeZone('ABC', -1, -30)
        self.assertEqual(tz1, tz2)
        
    def test_timezones_not_equal(self):
        tz = TimeZone('ABC', -1, -30)
        
        test_timezones = (
            TimeZone('DEF', -1, -30),
            TimeZone('ABC', -1, 0),
            TimeZone('ABC', 1, -30)
        )
        for i, test_tz in enumerate(test_timezones):
            with self.subTest(test_number=i):
                self.assertNotEqual(tz, test_tz)

# %%
'''
Now we can start adding additional unit tests for our Account class.
Remember that unit tests are meant to test one specific piece of functionality - don't try to group too much in your 
tests, as otherwise the error messages can become less meaningful, making harder to track down the actual problem.
A recommended practice is either to set up unit tests **before** you write your code, or soon after. Here I left 
writing unit tests to the end, and this leads to badly written, or simply omitted unit tests because it becomes too tedious!
'''

# %%
'''
I'm only going to add a few more tests, and you can continue writing them on your own. We'll use unit tests again,
and introduce additional functionality over time.
'''

# %%
class TestAccount(unittest.TestCase):
    
    def test_create_timezone(self):
        tz = TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)
        
    def test_timezones_equal(self):
        tz1 = TimeZone('ABC', -1, -30)
        tz2 = TimeZone('ABC', -1, -30)
        self.assertEqual(tz1, tz2)
        
    def test_timezones_not_equal(self):
        tz = TimeZone('ABC', -1, -30)
        
        test_timezones = (
            TimeZone('DEF', -1, -30),
            TimeZone('ABC', -1, 0),
            TimeZone('ABC', 1, -30)
        )
        for i, test_tz in enumerate(test_timezones):
            with self.subTest(test_number=i):
                self.assertNotEqual(tz, test_tz)
                
    def test_create_account(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = 100.00
        
        a = Account(account_number, first_name, last_name, tz, balance)
        self.assertEqual(account_number, a.account_number)
        self.assertEqual(first_name, a.first_name)
        self.assertEqual(last_name, a.last_name)
        self.assertEqual(first_name + ' ' + last_name, a.full_name)
        self.assertEqual(tz, a.timezone)
        self.assertEqual(balance, a.balance)

# %%
run_tests(TestAccount)

# %%
'''
One last piece of unit testing functionality, is handling exceptions when they are **expected**, for example creating 
an account with an empty first name should result in a `ValueError` exception. We can write a unit test that will test
this expected exception, and which will fail if the exception is not encountered (or is a different exception).
To do this we need to indicate that an exception is expected, as well as the expected exception class.
'''

# %%
class TestAccount(unittest.TestCase):
    
    def test_create_timezone(self):
        tz = TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)
        
    def test_timezones_equal(self):
        tz1 = TimeZone('ABC', -1, -30)
        tz2 = TimeZone('ABC', -1, -30)
        self.assertEqual(tz1, tz2)
        
    def test_timezones_not_equal(self):
        tz = TimeZone('ABC', -1, -30)
        
        test_timezones = (
            TimeZone('DEF', -1, -30),
            TimeZone('ABC', -1, 0),
            TimeZone('ABC', 1, -30)
        )
        for i, test_tz in enumerate(test_timezones):
            with self.subTest(test_number=i):
                self.assertNotEqual(tz, test_tz)
                
    def test_create_account(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = 100.00
        
        a = Account(account_number, first_name, last_name, tz, balance)
        self.assertEqual(account_number, a.account_number)
        self.assertEqual(first_name, a.first_name)
        self.assertEqual(last_name, a.last_name)
        self.assertEqual(first_name + ' ' + last_name, a.full_name)
        self.assertEqual(tz, a.timezone)
        self.assertEqual(balance, a.balance)
        
    def test_create_account_blank_first_name(self):
        account_number = 'A100'
        first_name = ''
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = 100.00
        
        with self.assertRaises(ValueError):
            a = Account(account_number, first_name, last_name, tz, balance)

# %%
run_tests(TestAccount)

# %%
'''
But, if we were looking for a different exception:
'''

# %%
class TestAccount(unittest.TestCase):
    
    def test_create_timezone(self):
        tz = TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)
        
    def test_timezones_equal(self):
        tz1 = TimeZone('ABC', -1, -30)
        tz2 = TimeZone('ABC', -1, -30)
        self.assertEqual(tz1, tz2)
        
    def test_timezones_not_equal(self):
        tz = TimeZone('ABC', -1, -30)
        
        test_timezones = (
            TimeZone('DEF', -1, -30),
            TimeZone('ABC', -1, 0),
            TimeZone('ABC', 1, -30)
        )
        for i, test_tz in enumerate(test_timezones):
            with self.subTest(test_number=i):
                self.assertNotEqual(tz, test_tz)
                
    def test_create_account(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = 100.00
        
        a = Account(account_number, first_name, last_name, tz, balance)
        self.assertEqual(account_number, a.account_number)
        self.assertEqual(first_name, a.first_name)
        self.assertEqual(last_name, a.last_name)
        self.assertEqual(first_name + ' ' + last_name, a.full_name)
        self.assertEqual(tz, a.timezone)
        self.assertEqual(balance, a.balance)
        
    def test_create_account_blank_first_name(self):
        account_number = 'A100'
        first_name = ''
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = 100.00
        
        with self.assertRaises(TypeError):
            a = Account(account_number, first_name, last_name, tz, balance)

# %%
run_tests(TestAccount)

# %%
'''
As you can start to see, there are a lot of gaps in our `Account` implementation. For example, we allow empty account
numbers, negative starting balances. As you start writing unit tests you will not only discover bugs in your code, 
but also gaps in your design and implementation!
Let's fix our unit test back to expecting a `ValueError`, and write a few more.
'''

# %%
class TestAccount(unittest.TestCase):
    
    def test_create_timezone(self):
        tz = TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)
        
    def test_timezones_equal(self):
        tz1 = TimeZone('ABC', -1, -30)
        tz2 = TimeZone('ABC', -1, -30)
        self.assertEqual(tz1, tz2)
        
    def test_timezones_not_equal(self):
        tz = TimeZone('ABC', -1, -30)
        
        test_timezones = (
            TimeZone('DEF', -1, -30),
            TimeZone('ABC', -1, 0),
            TimeZone('ABC', 1, -30)
        )
        for i, test_tz in enumerate(test_timezones):
            with self.subTest(test_number=i):
                self.assertNotEqual(tz, test_tz)
                
    def test_create_account(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = 100.00
        
        a = Account(account_number, first_name, last_name, tz, balance)
        self.assertEqual(account_number, a.account_number)
        self.assertEqual(first_name, a.first_name)
        self.assertEqual(last_name, a.last_name)
        self.assertEqual(first_name + ' ' + last_name, a.full_name)
        self.assertEqual(tz, a.timezone)
        self.assertEqual(balance, a.balance)
        
    def test_create_account_blank_first_name(self):
        account_number = 'A100'
        first_name = ''
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = 100.00
        
        with self.assertRaises(ValueError):
            a = Account(account_number, first_name, last_name, tz, balance)
            
    def test_account_deposit_ok(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        balance = 100.00
        
        a = Account(account_number, first_name, last_name, initial_balance=balance)
        conf_code = a.deposit(100)
        self.assertEqual(200, a.balance)
        self.assertIn('D-', conf_code)
    
    def test_account_deposit_negative_amount(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        balance = 100.00
        
        a = Account(account_number, first_name, last_name, initial_balance=balance)
        with self.assertRaises(ValueError):
            conf_code = a.deposit(-100)
        
    def test_account_withdraw_ok(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        balance = 100.00
        
        a = Account(account_number, first_name, last_name, initial_balance=balance)
        conf_code = a.withdraw(20)
        self.assertEqual(80, a.balance)
        self.assertIn('W-', conf_code)
        
    
    def test_account_withdraw_overdraw(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        balance = 100.00
        
        a = Account(account_number, first_name, last_name, initial_balance=balance)
        conf_code = a.withdraw(200)
        self.assertIn('X-', conf_code)
        self.assertEqual(balance, a.balance)
        

# %%
run_tests(TestAccount)

# %%
'''
Let's add one more unit test, that checkes to make sure we cannot create accounts with negative balances:
'''

# %%
class TestAccount(unittest.TestCase):
    
    def test_create_timezone(self):
        tz = TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)
        
    def test_timezones_equal(self):
        tz1 = TimeZone('ABC', -1, -30)
        tz2 = TimeZone('ABC', -1, -30)
        self.assertEqual(tz1, tz2)
        
    def test_timezones_not_equal(self):
        tz = TimeZone('ABC', -1, -30)
        
        test_timezones = (
            TimeZone('DEF', -1, -30),
            TimeZone('ABC', -1, 0),
            TimeZone('ABC', 1, -30)
        )
        for i, test_tz in enumerate(test_timezones):
            with self.subTest(test_number=i):
                self.assertNotEqual(tz, test_tz)
                
    def test_create_account(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = 100.00
        
        a = Account(account_number, first_name, last_name, tz, balance)
        self.assertEqual(account_number, a.account_number)
        self.assertEqual(first_name, a.first_name)
        self.assertEqual(last_name, a.last_name)
        self.assertEqual(first_name + ' ' + last_name, a.full_name)
        self.assertEqual(tz, a.timezone)
        self.assertEqual(balance, a.balance)
        
    def test_create_account_blank_first_name(self):
        account_number = 'A100'
        first_name = ''
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = 100.00
        
        with self.assertRaises(ValueError):
            a = Account(account_number, first_name, last_name, tz, balance)
            
    def test_create_account_negative_balance(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        tz = TimeZone('TZ', 1, 30)
        balance = -100.00
        
        with self.assertRaises(ValueError):
            a = Account(account_number, first_name, last_name, tz, balance)
            
    def test_account_deposit_ok(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        balance = 100.00
        
        a = Account(account_number, first_name, last_name, initial_balance=balance)
        conf_code = a.deposit(100)
        self.assertEqual(200, a.balance)
        self.assertIn('D-', conf_code)
    
    def test_account_deposit_negative_amount(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        balance = 100.00
        
        a = Account(account_number, first_name, last_name, initial_balance=balance)
        with self.assertRaises(ValueError):
            conf_code = a.deposit(-100)
        
    def test_account_withdraw_ok(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        balance = 100.00
        
        a = Account(account_number, first_name, last_name, initial_balance=balance)
        conf_code = a.withdraw(20)
        self.assertEqual(80, a.balance)
        self.assertIn('W-', conf_code)
        
    
    def test_account_withdraw_overdraw(self):
        account_number = 'A100'
        first_name = 'FIRST'
        last_name = 'LAST'
        balance = 100.00
        
        a = Account(account_number, first_name, last_name, initial_balance=balance)
        conf_code = a.withdraw(200)
        self.assertIn('X-', conf_code)
        self.assertEqual(balance, a.balance)
        

# %%
run_tests(TestAccount)

# %%
'''
Oh-oh, we are not raising an exception! That's a bug in our code.
So, let's fix it, and re-run the tests:
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
        
        self._balance = Account.validate_real_number(initial_balance, min_value=0)
        
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
        if len(str(value).strip()) == 0:
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
        conf_code = self.generate_confirmation_code(Account._transaction_codes['interest'])
        self._balance += interest
        return conf_code

# %%
run_tests(TestAccount)

# %%
'''
Now our tests pass!
'''

# %%
'''
And so on... !
You should add at least a few more unit tests to this to get some extra practice.
'''

# %%
