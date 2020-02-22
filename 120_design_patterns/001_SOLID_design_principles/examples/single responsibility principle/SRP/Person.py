class Person:
	def __init__(self):
		self.firstName = None
		self.lastName = None

	@property
	def first_name(self):
		return self.firstName

	@first_name.setter
	def first_name(self, first_name):
		self.firstName = first_name

	@property
	def last_name(self):
		return self.lastName

	@last_name.setter
	def last_name(self, last_name):
		self.lastName = last_name
