from mock_customers import MOCKCUSTOMERS

def main():
    for cust in MOCKCUSTOMERS:
        print('Name: %s; Address: %s'
              % (cust.name, cust.address))

if __name__ == '__main__':
    main()
