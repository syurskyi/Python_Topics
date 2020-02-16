# c_ VendingMachine
#
#     total_revenue _ 0 # Total revenue of all vending machines in the system
#
#     snack_prices _ {"candy": 2.00, "soda": 1.50, "chips": 3.00, "cookies": 3.50}
#
#     # Instance attributes
#     ___  -  inventory serial days_until_maintenance
#         ?  ? # dictionary with {<snack>: <amount>} as key-value pairs. Possible snacks: candy, soda, chips, cookies. Keys written in lowercase.
#         .revenue = 0           # Initially, when an instance of the vending machine is created, the revenue is 0 and it's updated with each sale.
#         ?  ?
#         ?  ?
#
#     # Method that displays an interactive menu to process a sale.
#     # Displays the options, gets user input to select the snack, and calls
#     # another method to process the sale.
#     ___ sales_menu ?
#
#         # The user has the option to buy several types of snacks
#         # so the program is repeated if the user indicates that he/she
#         # would like to buy another snack
#         w___ T..
#
#             greetings = "\nWelcome! I have:\n"
#             request = "\nPlease enter the number of the item: "
#
#             # Print a welcome message with the snacks available
#             print g..
#
#             i _ 1
#             ___ snack __ ?i..
#                 print("(" + st. ? + ") " + s__.ca..
#                 ? +_ 1
#
#             # Get the user input (option selected)
#             cust_input = in. in.. r..
#
#             # Repeat if the input doesn't meet the requirements
#             w___ ? <= 0 or ? > le. ?i..
#                 print("Please enter a number from 1 to", le. ?i..
#                 # Get the user input (option selected)
#                 cust_input = in. in.. r..
#
#             # Display appropriate message
#             ?pr.. li.. ?i...ke..||? - 1].lo..
#             answer = in. in.. ("\nWould you like to buy another snack?\nEnter 1 for YES and 0 for NO: "))
#
#             # If the customer does not wish to buy another snack
#             __ no. ?
#                 b..
#
#
#     # Method that processes the sale by asking the user how many snacks of that type
#     # he/she would like to buy and calls another method to opdate the inventory
#     ___ process_sale  option # option must be in lowercase
#
#         print("\nYou selected: @"  ?.ca..
#
#         __ ?i.. ? > 0
#
#             # Display current snack inventory and product
#             print("Great! I currently have @ @ in my inventory\n"  ?i... ?|, ?
#
#             # Ask for the number of snacks
#             num_items = in. in..("How many @ would you like to buy?\n"  ?
#
#             # Handle cases where user might enter a negative number or zero
#             w___ ? <_ 0
#                 print("Please enter a positive integer")
#                 num_items = in. in.. ("\nHow many @ would you like to buy?\n"  ?
#
#             # Update inventory if there are enough snacks available
#             __ ? <_ ?i.. ?
#                 ?re.. o.. nu..
#
#                 # Update the machine's revenue
#                 total = ?up.. o.. nu..
#
#                 print("That would be: $ " + st. to..
#
#                 # Display a message confirming the purchase and current inventory
#                 print("\nThank you for your purchase!")
#                 print("Now I have @ @ and my revenue is $@"  ?i.. option| o.. ?re..
#
#             ____
#                 print("I don't have so many @. Sorry! :("  ?
#
#         ____
#             print("I don't have any more @. Sorry! :("  ?
#
#
#     # Method that updates the vending machine's (instance) inventory by
#     # decrementing the availability of the snack chosen.
#     ___ remove_from_inventory option num_items
#         ?i.. ?| -_ nu..
#
#     # Update the revenue of the instance of VendingMachine
#     # and update the class attribute total revenue.
#     ___ update_revenue  option num_items
#         # Find price of the snack
#         price = ?fi.. o..
#
#         # Update Instance and class
#         ?re.. +_ nu.. * pr..
#         V__.to.. += nu.. * p..
#
#         r_ nu.. * pr..
#
#     # Find the price of the snack selected in the class attribute
#     # and r_ it
#     ___ find_snack_price  snack
#         r_ V__.sn.. ?
#
#     # Method that prints a message with the total revenue of the instance of VendingMachine
#     ___ display_revenue ?
#         print("The total revenue of this vending machine is:", ?r..
#
#
# # Subclasses =============================================================================================
#
#
# c_ HospitalVendingMachine ?
#     pass
#
#     # Complete the class
#
#
#
# c_ SchoolVendingMachine ?
#     pass
#
#     # Complete the class
#
#
# # Instances =============================================================================================
#
# floor_machine = VendingMachine({"candy": 36, "soda": 15, "chips": 40, "cookies": 120}, "011423424", 24)
# floor_machine.sales_menu()
#
# hospital_machine = HospitalVendingMachine({"candy": 32, "soda": 50, "chips": 45, "cookies": 80}, "03223424", 15)
# ##hospital_machine.sales_menu()
#
# school_machine = SchoolVendingMachine({"candy": 36, "soda": 15, "chips": 40, "cookies": 120}, "0534424", 2)
# ##school_machine.sales_menu()
