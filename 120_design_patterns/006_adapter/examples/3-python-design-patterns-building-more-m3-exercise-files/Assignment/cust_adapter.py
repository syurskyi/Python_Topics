from abs_adapter import AbsAdapter

class CustAdapter(AbsAdapter):
    @property
    def name(self):
        return '{} {}'.format(
            self.adaptee.first_name,
            self.adaptee.last_name
        )

    @property
    def first_name(self):
        return self.adaptee.first_name

    @property
    def last_name(self):
        return self.adaptee.last_name

    @property
    def address(self):
        return self.adaptee.address


    @property
    def number(self):
        return self.adaptee.address.split()[0]

    @property
    def street(self):
        return ' '.join(self.adaptee.address.split(maxsplit=2)[1:])
