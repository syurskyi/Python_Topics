class PhoneBook:
    # pycharm smart refactoring advised to create methods on the phonebook class
    def __init__(self):
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def is_consistent(self):
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
