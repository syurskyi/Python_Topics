from abs_adapter import AbsAdapter

class VendAdapter(AbsAdapter):
    @property
    def name(self):
        return self.adaptee.name

    @property
    def first_name(self):
        return self.adaptee.name.split()[0]

    @property
    def last_name(self):
        return ' '.join(self.adaptee.name.split(maxsplit=2)[1:])

    @property
    def address(self):
        return '{} {}'.format(
            self.adaptee.number,
            self.adaptee.street
        )

    @property
    def number(self):
        return self.adaptee.number

    @property
    def street(self):
        return self.adaptee.street
