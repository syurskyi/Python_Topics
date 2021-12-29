_______ string
_______ random


class Robot:

    ___ __init__(self):
        self.name = self.generate_name()

    ___ reset(self):
        self.name = self.generate_name()

    ___ generate_name(self):
        random.seed()
        r.. self.random_prefix(2) + self.random_suffix(3)

    ___ random_prefix(self, n):
        r.. ''.join(random.sample(string.ascii_uppercase, n))

    ___ random_suffix(self, n):
        r.. ''.join(random.sample(string.digits, n))
