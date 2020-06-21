from customer import Customer
from vend_adapter import VendAdapter
from cust_adapter import CustAdapter

class VendCustAdapter(object):
    def __new__(cls, adaptee):
        if isinstance(adaptee, Customer):
            return CustAdapter(adaptee)
        else:
            return VendAdapter(adaptee)
