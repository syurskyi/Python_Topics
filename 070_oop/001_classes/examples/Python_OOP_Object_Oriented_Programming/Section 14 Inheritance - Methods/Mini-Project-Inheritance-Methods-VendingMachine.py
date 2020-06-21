class VendingMachine:
 
    total_revenue = 0 # Total revenue of all vending machines in the system
 
    snack_prices = {"candy": 2.00, "soda": 1.50, "chips": 3.00, "cookies": 3.50}
 
    # Instance attributes
    def __init__(self, inventory, serial, days_until_maintenance):
        self.inventory = inventory # dictionary with {<snack>: <amount>} as key-value pairs. Possible snacks: candy, soda, chips, cookies. Keys written in lowercase.
        self.revenue = 0           # Initially, when an instance of the vending machine is created, the revenue is 0 and it's updated with each sale.
        self.serial = serial
        self.days_until_maintenance = days_until_maintenance
 
    # Method that displays an interactive menu to process a sale.
    # Displays the options, gets user input to select the snack, and calls
    # another method to process the sale.
    def sales_menu(self):
 
        # The user has the option to buy several types of snacks
        # so the program is repeated if the user indicates that he/she
        # would like to buy another snack
        while True:
 
            greetings = "\nWelcome! I have:\n"
            request = "\nPlease enter the number of the item: "
 
            # Print a welcome message with the snacks available
            print(greetings)
 
            i = 1
            for snack in self.inventory:
                print("(" + str(i) + ") " + snack.capitalize())
                i += 1
 
            # Get the user input (option selected)
            cust_input = int(input(request))
 
            # Repeat if the input doesn't meet the requirements
            while cust_input <= 0 or cust_input > len(self.inventory):
                print("Please enter a number from 1 to", len(self.inventory))
                # Get the user input (option selected)
                cust_input = int(input(request))
        
            # Display appropriate message
            self.process_sale(list(self.inventory.keys())[cust_input - 1].lower())
            answer = int(input("\nWould you like to buy another snack?\nEnter 1 for YES and 0 for NO: "))
 
            # If the customer does not wish to buy another snack
            if not answer:
                break
 
 
    # Method that processes the sale by asking the user how many snacks of that type
    # he/she would like to buy and calls another method to opdate the inventory
    def process_sale(self, option): # option must be in lowercase
        
        print("\nYou selected: %s" % option.capitalize())
        
        if self.inventory[option] > 0:
            
            # Display current snack inventory and product
            print("Great! I currently have %d %s in my inventory\n" % (self.inventory[option], option))
            
            # Ask for the number of snacks
            num_items = int(input("How many %s would you like to buy?\n" % option))
 
            # Handle cases where user might enter a negative number or zero
            while num_items <= 0:
                print("Please enter a positive integer")
                num_items = int(input("\nHow many %s would you like to buy?\n" % option))
 
            # Update inventory if there are enough snacks available
            if num_items <= self.inventory[option]:
                self.remove_from_inventory(option, num_items)
                
                # Update the machine's revenue
                total = self.update_revenue(option, num_items)
 
                print("That would be: $ " + str(total))
 
                # Display a message confirming the purchase and current inventory
                print("\nThank you for your purchase!")
                print("Now I have %d %s and my revenue is $%d" % (self.inventory[option], option, self.revenue))
                
            else:
                print("I don't have so many %s. Sorry! :(" % option)
                
        else:
            print("I don't have any more %s. Sorry! :(" % option)
 
 
    # Method that updates the vending machine's (instance) inventory by
    # decrementing the availability of the snack chosen.
    def remove_from_inventory(self, option, num_items):
        self.inventory[option] -= num_items
 
    # Update the revenue of the instance of VendingMachine
    # and update the class attribute total revenue.
    def update_revenue(self, option, num_items):
        # Find price of the snack
        price = self.find_snack_price(option)
 
        # Update Instance and class
        self.revenue += num_items * price
        VendingMachine.total_revenue += num_items * price
 
        return num_items * price
 
    # Find the price of the snack selected in the class attribute
    # and return it
    def find_snack_price(self, snack):
        return VendingMachine.snack_prices[snack]        
        
    # Method that prints a message with the total revenue of the instance of VendingMachine
    def display_revenue(self):
        print("The total revenue of this vending machine is:", self.revenue)
                      
 
# Subclasses =============================================================================================
            
 
class HospitalVendingMachine(VendingMachine):
    pass
 
    # Complete the class
 
        
 
class SchoolVendingMachine(VendingMachine):
    pass
 
    # Complete the class
 
 
# Instances =============================================================================================
 
floor_machine = VendingMachine({"candy": 36, "soda": 15, "chips": 40, "cookies": 120}, "011423424", 24)
floor_machine.sales_menu()
 
hospital_machine = HospitalVendingMachine({"candy": 32, "soda": 50, "chips": 45, "cookies": 80}, "03223424", 15)
##hospital_machine.sales_menu()
 
school_machine = SchoolVendingMachine({"candy": 36, "soda": 15, "chips": 40, "cookies": 120}, "0534424", 2)
##school_machine.sales_menu()
