class StandardMessages:

	@staticmethod
	def welcome_message():
		print('Welcome to my Application')

	@staticmethod
	def end_application():
		print('Press enter to close...')
		_ = input()

	@staticmethod
	def display_validation_error(field_name: str):
		print('You did not give proper {}'.format(field_name))
