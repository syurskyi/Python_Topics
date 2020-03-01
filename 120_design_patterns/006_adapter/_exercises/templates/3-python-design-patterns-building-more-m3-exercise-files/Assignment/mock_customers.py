from customer import Customer
from vend_cust_adapter import VendCustAdapter

MOCKCUSTOMERS = (
    VendCustAdapter(Customer('Pizza', 'Love', '33 Pepperoni Lane')),
    VendCustAdapter(Customer('Happy', 'and Green', '25 Kale St.')),
    VendCustAdapter(Customer('Sweet', 'Tooth', '42 Chocolate Ave.'))
)
