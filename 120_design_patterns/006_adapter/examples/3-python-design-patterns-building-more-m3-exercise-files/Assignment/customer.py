class Customer(object):
    def __init__(self, first_name, last_name, address):
        self._first_name = first_name
        self._last_name = last_name
        self._address = address

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def address(self):
        return self._address
