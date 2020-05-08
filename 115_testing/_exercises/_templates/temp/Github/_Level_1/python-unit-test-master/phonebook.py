c_ PhoneBook:
    # pycharm smart refactoring advised to create methods on the phonebook class
    ___  - (self):
        self.numbers = {}

    ___ add  name, number):
        self.numbers[name] = number

    ___ lookup  name):
        return self.numbers[name]

    ___ is_consistent(self):
        # loop over phonebook entries in double loop to compare entries
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                # if names are the same i'm comparing entry with itself
                if name1 == name2:
                    continue
                # look at 2 numbers to make sure one doesnt start with the other
                if number1.startswith(number2):
                    return False
        return True
