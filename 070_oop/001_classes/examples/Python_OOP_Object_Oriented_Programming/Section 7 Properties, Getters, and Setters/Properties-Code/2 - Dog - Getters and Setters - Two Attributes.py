class Dog:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print("Please enter a valid name")

    # Age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if isinstance(age, int) and 0 < age < 30:
            self._age = age
        else:
            print("Please enter a valid age")
