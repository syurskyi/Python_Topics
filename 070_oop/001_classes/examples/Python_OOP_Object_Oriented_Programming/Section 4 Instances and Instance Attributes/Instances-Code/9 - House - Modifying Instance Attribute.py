class House:

	def  __init__(self, price, square_feet, num_bedrooms, num_bathrooms):
		self.price = price
		self.square_feet = square_feet
		self.num_bedrooms = num_bedrooms
		self.num_bathrooms = num_bathrooms


my_house = House(50000, 2100, 4, 3) 

# Print the current value of the 'price'
# attribute of the instance my_house
print("Current Value:", my_house.price)

# Update the value of the 'price' attribute
# of the instance my_house
my_house.price = 55000

# Print the updated value
print("New Value:", my_house.price)
