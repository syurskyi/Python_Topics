from mock_customers import MOCKCUSTOMERS as VENDORS
from mock_vendors import MOCKVENDORS as CUSTOMERS

def main():
    for cust in CUSTOMERS:
        print('Name: %s %s; Address: %s' %
              (cust.first_name, cust.last_name, cust.address))

    for vend in VENDORS:
        print('Name: %s; Address: %s %s' %
              (vend.name, vend.number, vend.street))

if __name__ == '__main__':
    main()
