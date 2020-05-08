# Corey Schafer
# Python Tutorial: Unit Testing Your Code with the unittest Module
# https://www.youtube.com/watch?v=6tNS--WetLI

c_ Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    ___  -   first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    ___ email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    ___ fullname(self):
        return '{} {}'.format(self.first, self.last)

    ___ apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    ___ monthly_schedule  month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'


