# %%
'''
### Solution - Part 2
'''

# %%
'''
Here's where we left off in the last video:
'''

# %%
import numbers
import unittest

# %%
class TestIntegerField(unittest.TestCase):
    @staticmethod
    def create_test_class(min_, max_):
        obj = type('TestClass', (), {'age': IntegerField(min_, max_)})
        return obj()
        
    def test_set_age_ok(self):
        """Tests that valid values can be assigned/retrieved"""
        min_ = 5
        max_ = 10
        obj = self.create_test_class(min_, max_)
        valid_values = range(min_, max_)
        
        for i, value in enumerate(valid_values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)
                
    def test_set_age_invalid(self):
        """Tests that invalid values raise ValueErrors"""
        min_ = -10
        max_ = 10
        obj = self.create_test_class(min_, max_)
        bad_values = list(range(min_ - 5, min_))
        bad_values += list(range(max_ + 1, max_ + 5))
        bad_values += [10.5, 1 + 0j, 'abc', (1, 2)]
        
        for i, value in enumerate(bad_values):
            with self.subTest(test_number=i):
                with self.assertRaises(ValueError):
                    obj.age = value
                    
    def test_class_get(self):
        """Tests that class attribute retrieval returns the descriptor instance"""
        obj = self.create_test_class(0, 0)
        obj_class = type(obj)
        self.assertIsInstance(obj_class.age, IntegerField)
        
    def test_set_age_min_only(self):
        """Tests that we can specify a min value only"""
        min_ = 0
        max_ = None
        obj = self.create_test_class(min_, max_)
        values = range(min_, min_ + 100, 10)
        for i, value in enumerate(values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)
                
    def test_set_age_max_only(self):
        """Tests that we can specify a max value only"""
        min_ = None
        max_ = 10
        obj = self.create_test_class(min_, max_)
        values = range(max_ - 100, max_, 10)
        for i, value in enumerate(values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)
                
    def test_set_age_no_limits(self):
        """Tests that we can use IntegerField without any limits at all"""
        min_ = None
        max_ = None
        obj = self.create_test_class(min_, max_)
        values = range(-100, 100, 10)
        for i, value in enumerate(values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)

class TestCharField(unittest.TestCase):
    @staticmethod
    def create_test_class(min_, max_):
        obj = type('TestClass', (), {'name': CharField(min_, max_)})
        return obj()
        
    def test_set_name_ok(self):
        """Tests that valid values can be assigned/retrieved"""
        min_ = 1
        max_ = 10
        obj = self.create_test_class(min_, max_)
        valid_lengths = range(min_, max_)
        
        for i, length in enumerate(valid_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                obj.name = value
                self.assertEqual(value, obj.name)
            
    def test_set_name_invalid(self):
        """Tests that invalid values raise ValueErrors"""
        min_ = 5
        max_ = 10
        obj = self.create_test_class(min_, max_)
        bad_lengths = list(range(min_ - 5, min_))
        bad_lengths += list(range(max_ + 1, max_ + 5))
        for i, length in enumerate(bad_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                with self.assertRaises(ValueError):
                    obj.name = value
                    
    def test_class_get(self):
        """Tests that class attribute retrieval returns the descriptor instance"""
        obj = self.create_test_class(0, 0)
        obj_class = type(obj)
        self.assertIsInstance(obj_class.name, CharField)
        
    def test_set_name_min_only(self):
        """Tests that we can specify a min length only"""
        min_ = 0
        max_ = None
        obj = self.create_test_class(min_, max_)
        valid_lengths = range(min_, min_ + 100, 10)
        for i, length in enumerate(valid_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                obj.name = value
                self.assertEqual(value, obj.name)
    
    def test_set_name_min_negative_or_none(self):
        """Tests that setting a negative or None length results in a zero length"""
        obj = self.create_test_class(-10, 100)
        self.assertEqual(type(obj).name._min, 0)
        self.assertEqual(type(obj).name._max, 100)
        
        obj = self.create_test_class(None, None)
        self.assertEqual(type(obj).name._min, 0)
        self.assertIsNone(type(obj).name._max)
        
    def test_set_name_max_only(self):
        """Tests that we can specify a max length only"""
        min_ = None
        max_ = 10
        obj = self.create_test_class(min_, max_)
        valid_lengths = range(max_ - 100, max_, 10)
        for i, length in enumerate(valid_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                obj.name = value
                self.assertEqual(value, obj.name)
                
    def test_set_name_no_limits(self):
        """Tests that we can use CharField without any limits at all"""
        min_ = None
        max_ = None
        obj = self.create_test_class(min_, max_)
        valid_lengths = range(0, 100, 10)
        for i, length in enumerate(valid_lengths):
            value = 'a' * length
            with self.subTest(test_number=i):
                obj.name = value
                self.assertEqual(value, obj.name)
                
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

# %%
class IntegerField:
    def __init__(self, min_, max_):
        self._min = min_
        self._max = max_

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self.prop_name} must be an integer.')
        if self._min is not None and value < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min}.')
        if self._max is not None and value > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max}')
        instance.__dict__[self.prop_name] = value
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)
    
    
class CharField:
    def __init__(self, min_=None, max_=None):
        min_ = min_ or 0  # in case min_ is None
        min_ = max(min_, 0)  # replaces negative value with zero
        self._min = min_
        self._max = max_

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.prop_name} must be a string.')
        if self._min is not None and len(value) < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min} chars.')
        if self._max is not None and len(value) > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max} chars')
        instance.__dict__[self.prop_name] = value
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

# %%
'''
And of course, our unit tests should run just fine:
'''

# %%
run_tests(TestIntegerField)

# %%
run_tests(TestCharField)

# %%
'''
As you may noticed, quite a bit of code was redundant between the `IntegerField` and `CharField` descriptors.
So, let's restructure things a bit to make use of inheritance for the common bits.
'''

# %%
'''
Notice that the implementation of `__set_name__` and `__get__` are actually identical. The `__init__` methods are 
slightly different, but there is still some commonality. And same goes for the `__set__` - although the validations 
are different, the storage mechanism is the same - so we could factor that out.
'''

# %%
'''
We're going to create a base class as follows:
'''

# %%
class BaseValidator:
    def __init__(self, min_=None, max_=None):
        self._min = min_
        self._max = max_
        
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)
        
    def validate(self, value):
        # this will need to be implemented specifically by each subclass
        # here we just default to not raising any exceptions
        pass
    
    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.prop_name] = value

# %%
'''
Of course we can use this `BaseValidator` directly, but it won't be very useful:
'''

# %%
class Person:
    name = BaseValidator()

# %%
p = Person()

# %%
p.name = 'Alex'

# %%
p.name

# %%
'''
Now let's leverage this class to create our integer and char descriptors:
'''

# %%
class IntegerField(BaseValidator):
    def validate(self, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self.prop_name} must be an integer.')
        if self._min is not None and value < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min}.')
        if self._max is not None and value > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max}')

# %%
class CharField(BaseValidator):
    def __init__(self, min_, max_):
        min_ = max(min_ or 0, 0)
        super().__init__(min_, max_)
        
    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.prop_name} must be a string.')
        if self._min is not None and len(value) < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min} chars.')
        if self._max is not None and len(value) > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max} chars')
        

# %%
'''
And this should work just as before. Lucky for us we don't have to test anything manually, we can just re-run 
our unit tests and make sure nothing broke!
'''

# %%
run_tests(TestIntegerField)

# %%
run_tests(TestCharField)

# %%
'''
Woohoo!!
'''

# %%
'''
One thing I want to mention here: now that we are using unittests, and iterating our development, 
using Jupyter notebooks, even with relatively simple programs like this one, is getting unwieldy. 
Best would be to use a proper Python app, with a root and multiple modules, including one for unit tests.
An IDE like PyCharm or VSCode works really great, but of course you can choose to use any text editor, 
and the command line to run your app instead of an IDE.
'''

# %%
