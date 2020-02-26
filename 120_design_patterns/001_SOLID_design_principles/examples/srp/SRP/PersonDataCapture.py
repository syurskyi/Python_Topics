from SRP.Person import Person


class PersonDataCapture:

	@staticmethod
	def capture() -> Person:
		output = Person()

		print('Enter your first name: ')
		output.first_name = input()

		print('Enter your last name: ')
		output.last_name = input()

		return output
