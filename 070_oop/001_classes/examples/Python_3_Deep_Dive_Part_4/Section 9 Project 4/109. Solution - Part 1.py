# %%
'''
### Solution - Part 1
'''

# %%
'''
Let's go ahead and just create the descriptors one by one first:
'''

# %%
import numbers

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
        if value < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min}.')
        if value > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max}')
        instance.__dict__[self.prop_name] = value
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)
    

# %%
'''
Let's just make sure this works as expected:
'''

# %%
class Person:
    age = IntegerField(0, 100)

# %%
p = Person()

# %%
p.age = 5

# %%
p.age

# %%
try:
    p.age = 200
except ValueError as ex:
    print(ex)

# %%
'''
But of course, we really need unit testing. So let's write some unit tests to test this functionality. 
If you're rusty you may want to go back to Project 1 and review the unit test section in there.
'''

# %%
import unittest

def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

# %%
'''
For each test we are going to need a class that defines an instance of our descriptor as an attribute.
'''

# %%
'''
We could do it this way:
'''

# %%
class TestIntegerField(unittest.TestCase):
    class Person:
        age = IntegerField(0, 10)
        
    def test_set_age_ok(self):
        p = self.Person()
        p.age = 0
        self.assertEqual(0, p.age)

# %%
run_tests(TestIntegerField)

# %%
'''
So this kind of testing works just fine, but  our `Person` class `age` is hardcoded to min and max values.
We would ideally like to be able to modify those settings for every test (so we can test later with and without 
those values).
'''

# %%
'''
So, we'll override the descriptor attribute when we run the test!
'''

# %%
class TestIntegerField(unittest.TestCase):
    class Person:
        age = IntegerField(0, 10)
        
    def test_set_age_ok(self):
        min_ = 5
        max_ = 10
        self.Person.age = IntegerField(5, 10)
        p = self.Person()
        
        p.age = 5
        self.assertEqual(5, p.age)

# %%
run_tests(TestIntegerField)

# %%
'''
Hmm... that's not working.
'''

# %%
'''
That's because we defined the instance of our descriptor outside of a class, so the `__set_name__` method was never 
called!
We could fix this by calling `__set_name__` ourselves, but a cleaner approach would be to do a bit of meta programming. 
I'll show you both approaches.
'''

# %%
class TestIntegerField(unittest.TestCase):
    class Person:
        pass
    
    def create_person(self, min_, max_):
        self.Person.age = IntegerField(min_, max_)
        self.Person.age.__set_name__(Person, 'age')
        return self.Person()
        
    def test_set_age_ok(self):
        min_ = 5
        max_ = 10
        p = self.create_person(min_, max_)
        p.age = 5
        self.assertEqual(5, p.age)

# %%
run_tests(TestIntegerField)

# %%
'''
Let's avoid using this hardcoded `Person` class and this weird patching we had to do by creating a class using 
a functional approach instead of a declarative one (using the `class` keyword).
'''

# %%
'''
We already know that the type of any custom class we create is `type`. It is a metaclass, and classes are actually 
instances of the `type` metaclass.
'''

# %%
'''
The `type` metaclass is actually callable, and can be used to create classes, without having to write a `class` 
definition. The constructor for `type` is: `type(class_name, parent_classes, class_attributes)`
where `class_attributes` is a dictionary contain the names and values of the class attributes we want to define for our 
class.
'''

# %%
Person = type('Person', (), {'a': 10})

# %%
type(Person)

# %%
Person.__dict__

# %%
'''
As you can see we have the same as if we had done this:
'''

# %%
class Person:
    age = 10

# %%
type(Person)

# %%
Person.__dict__

# %%
'''
The blank argument we provided is there for inheritance - but we're not using inheritance here, hence the empty tuple.
'''

# %%
'''
So let's refactor our test class to use this approach:
'''

# %%
class TestIntegerField(unittest.TestCase):
    @staticmethod
    def create_test_class(min_, max_):
        obj = type('TestClass', (), {'age': IntegerField(min_, max_)})
        return obj()
        
    def test_set_age_ok(self):
        min_ = 5
        max_ = 10
        p = self.create_test_class(min_, max_)
        p.age = 5
        self.assertEqual(5, p.age)

# %%
run_tests(TestIntegerField)

# %%
'''
OK, now that this is out of the way, let's continue writing our unit tests:
'''

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

# %%
run_tests(TestIntegerField)

# %%
'''
Now let's add failure tests and a check that we have implemented `__get__` such that using it from the class returns 
the descriptor instance.
'''

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
        

# %%
run_tests(TestIntegerField)

# %%
'''
OK, so that's our `IntegerField` so far. Let's modify it (and the unit tests) so that we can optionally not specify
min/max.
'''

# %%
'''
We're actually going to write the tests **first**, run them and make sure they fail, then implement the functionality, 
re-run the tests and make sure they now pass. (This is an example of test-driven development - we write the tests first, 
then implement the functionality making sure our tests fail before, and pass after).
'''

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

# %%
run_tests(TestIntegerField)

# %%
'''
OK, so now that we have the tests written (and that they all fail), let's implement the functionality and re-test:
'''

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
    

# %%
run_tests(TestIntegerField)

# %%
'''
Cool!
Now there are some additional tests we could create, like testing if things work when one of the bounds is `0` 
(this would catch errors such as 
```
if self._min and value < self._min:
```
which would not work correctly for `_min = 0`
But I'll leave this and other tests for you :-)
'''

# %%
'''
Let's move on to the `CharField` descriptor - it's pretty much the same as `IntegerField` so, 
I'm going to copy/paste and refactor. One main difference is that it does not make sense for `min_` to be a negative
number, or to be `None`.
'''

# %%
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
Let's do a quick manual test:
'''

# %%
class Person:
    name = CharField(1, 10)

# %%
p = Person()

# %%
try:
    p.name = ''
except ValueError as ex:
    print(ex)

# %%
try:
    p.name = 'Python Rocks!'
except ValueError as ex:
    print(ex)

# %%
p.name = 'John'

# %%
class Person:
    name = CharField(-10, 10)

# %%
p = Person()
p.name = ''
p.name

# %%
class Person:
    name = CharField(1)

# %%
p = Person()
p.name = "I'm a lumberjack and I'm OK, I sleep all night and I work all day."
p.name

# %%
'''
Of course, we really should write unit tests. These will basically be very similar to the unit tests we created 
for `IntegerField`, so let's get cracking!
'''

# %%
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

# %%
run_tests(TestCharField)

# %%
