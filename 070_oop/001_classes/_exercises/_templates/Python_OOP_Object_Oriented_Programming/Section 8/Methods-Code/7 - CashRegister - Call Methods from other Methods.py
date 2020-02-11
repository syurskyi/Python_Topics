class CashRegister:

    tax = 0.05

    def __init__(self, cashier, serial):
        self.cashier = cashier
        self._serial = serial

    @property
    def serial(self):
        return self._serial

    def display_total(self, subtotal):
        print("=== Welcome to our store ===")
        print("The subtotal is:", subtotal)
        print("The tax is:", self._calculate_tax(subtotal))
        print("-----------------------")
        print("The total is:", self._calculate_total(subtotal))

    def _calculate_total(self, subtotal):
        return subtotal + self._calculate_tax(subtotal)

    def _calculate_tax(self, amount):
        return amount * CashRegister.tax
        
register = CashRegister("Melanie", "3453513")
register.display_total(5022.5)
