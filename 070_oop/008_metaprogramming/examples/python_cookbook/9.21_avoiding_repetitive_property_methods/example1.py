def typed_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}'.format(name, expected_type))
        setattr(self, storage_name, value)
    return prop

# Example use
class Person:
    name = typed_property('name', str)
    age = typed_property('age', int)
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    p = Person('Dave', 39)
    p.name = 'Guido'
    try:
        p.age = 'Old'
    except TypeError as e:
        print(e)


# Problem
# You are writing classes where you are repeatedly having to define property methods that
# perform common tasks, such as type checking. You would like to simplify the code so
# there is not so much code repetition.
# Solution
# Consider a simple class where attributes are being wrapped by property methods:

# As you can see, a lot of code is being written simply to enforce some type assertions on
# attribute values. Whenever you see code like this, you should explore different ways of
# simplifying it. One possible approach is to make a function that simply defines the
# property for you and returns it. For example:

# Discussion
# This recipe illustrates an important feature of inner function or closures—namely, their
# use in writing code that works a lot like a macro. The typed_property() function in
# this example may look a little weird, but it’s really just generating the property code for
# you and returning the resulting property object. Thus, when it’s used in a class, it operates
# exactly as if the code appearing inside typed_property() was placed into the
# class definition itself. Even though the property getter and setter methods are accessing
# local variables such as name, expected_type, and storage_name, that is fine—those
# values are held behind the scenes in a closure.
# This recipe can be tweaked in an interesting manner using the functools.partial()
# function. For example, you can do this: