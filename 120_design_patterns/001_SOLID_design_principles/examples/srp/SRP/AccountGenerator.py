from SRP.Person import Person


class AccountGenerator:

	@staticmethod
	def create_account(user: Person):
		# Create a username for the person
		print('Your username is {}{}'.format(user.first_name[:1], user.last_name))
