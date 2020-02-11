class BankAccount:

    def __init__(self, owner, init_deposit, number):
        self.owner = owner
        self._init_deposit = init_deposit
        self._number = number

    def show_data(self, show_owner=True):
        print("=== Bank Account ===")
        print("Account Number:", self._number)

        if show_owner:
            print("Owner:", self.owner)
            
        print("Initial Deposit:", self._init_deposit)
            
    
