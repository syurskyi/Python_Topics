class Polynomial:
    def __init__(self, terms: list):
        self._terms = terms
        self._result = dict()

    # This method is going to multiply two Polynomial objects.
    def multiply(self, s_poly_obj):
        for f_poly in range(0, self.__len__()):
            for s_poly in range(0, s_poly_obj.__len__()):
                the_new_power = self.get_poly()[f_poly].get_power() + s_poly_obj.get_poly()[s_poly].get_power()
                the_new_coefficient = self.get_poly()[f_poly].get_coefficient()\
                                    * s_poly_obj.get_poly()[s_poly].get_coefficient()

                if the_new_power not in self._result:
                    self._result[the_new_power] = the_new_coefficient
                else:
                    self._result[the_new_power] = self._result.get(the_new_power) + the_new_coefficient

    def __len__(self):
        return self._terms.__len__()

    def get_result(self):
        if bool(self._result):
            return self._result
        else:
            return None

    def get_poly(self):
        if self._terms:
            return self._terms
        else:
            return None

    # This method is going to format the answer.
    def print_poly(self):
        print('This is the answer: ', end=' ')
        for p, c in reversed(sorted(self._result.items())):
            if p == 0:
                x = ""
            else:
                x = "x"
            if c >= 1:
                plus = "+"
            else:
                plus = "-"
            print('{0}{1}{2}^{3} '.format(plus, c, x, p), end=' ')
