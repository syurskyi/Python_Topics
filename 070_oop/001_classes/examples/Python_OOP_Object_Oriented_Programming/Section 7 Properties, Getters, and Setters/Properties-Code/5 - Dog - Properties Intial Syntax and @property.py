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
    
