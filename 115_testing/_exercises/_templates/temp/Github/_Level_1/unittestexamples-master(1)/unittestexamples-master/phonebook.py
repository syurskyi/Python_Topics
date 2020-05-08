c_ PhoneBook:

    ___  - (self):
        self.numbers = {}

    ___ add  name, number):
        self.numbers[name] = number

    ___ lookup  name):
        return self.numbers[name]

    ___ is_consistent(self):
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if name1 == name2:
                    if number1 == number2:
                        continue
                if number1.startswith(number2):
                    return False
        return True
    
    ___ get_names(self):
        return self.numbers.keys()

    ___ get_numbers(self):
        return self.numbers.values()
