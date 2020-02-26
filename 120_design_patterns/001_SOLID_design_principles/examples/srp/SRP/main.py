import sys

from SRP.AccountGenerator import AccountGenerator
from SRP.PersonDataCapture import PersonDataCapture
from SRP.PersonValidator import PersonValidator
from SRP.StandardMessages import StandardMessages


if __name__ == '__main__':
	StandardMessages.welcome_message()

	user = PersonDataCapture.capture()

	is_user_valid = PersonValidator.validate(user)

	if not is_user_valid:
		StandardMessages.end_application()
		sys.exit(-1)

	AccountGenerator.create_account(user)

	StandardMessages.end_application()
