# Initially
##class Dog:
##    def __init__(self, age):
##        self.age = age

# Intermediate - Making it private.
# Syntax would have to change:
# <obj>.age => <obj>.get_age()
# <obj>.age = <value> => <obj>.set_age(<new_value>)
##class Dog:
##    def __init__(self, age):
##        self._age = age
##
##    def get_age(self):
##        return self._age
##
##    def set_age(self, age):
##        if isinstance(age, int) and 0 < age < 30:
##            self._age = age
##        else:
##            print("Please enter a valid age")

# Using Properties
# Implementations can continue using:
# <obj>.age
# <obj>.age = <value>
# and now the attribute is private
##class Dog:
##    def __init__(self, age):
##        self._age = age
##
##    def get_age(self):
##        print("Running getter")
##        return self._age
##
##    def set_age(self, age):
##        print("Running setter")
##        if isinstance(age, int) and 0 < age < 30:
##            self._age = age
##        else:
##            print("Please enter a valid age")
##
##    age = property(get_age, set_age)


# Using the @property decorator
# More Compact. Many Advantages.
class Dog:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        print("Running getter")
        return self._age

    @age.setter
    def age(self, new_age):
        print("Running setter")
        if isinstance(new_age, int) and 0 < new_age < 30:
            self._age = new_age
        else:
            print("Please enter a valid age")
    
