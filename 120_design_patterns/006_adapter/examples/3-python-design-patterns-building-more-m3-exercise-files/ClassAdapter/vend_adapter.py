from customer import Customer
from vendor import Vendor

class VendorAdapter(Vendor, Customer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def address(self):
        return '{} {}'.format(
            self.number, self.street
        )
