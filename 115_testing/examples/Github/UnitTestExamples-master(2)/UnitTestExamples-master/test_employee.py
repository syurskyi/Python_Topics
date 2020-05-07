import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('setupClass')

	"""
	@classmethod applies to a class instead of an attribute.
	setUpClass and tearDownClass is used when you want to do something
	only once before a test. 
	"""

	@classmethod
	def tearDownClass(cls):
		print('teardownClass')

	def setUp(self):
		self.emp_1 = Employee('Alex', 'Apple', 200000)
		self.emp_2 = Employee('Barry', 'Banana', 100000)

	"""
	Setup allows to not repeat creating instances. Note how emp_1
	and emp_2 are commented out below)
	"""

	def tearDown(self):
		pass
	"""
	Teardown is used when you test write files to a directory
	and later need to delete those files.
	"""

	def test_email(self):
	#	emp_1 = Employee('Alex', 'Apple', 200000)
	#	emp_2 = Employee('Barry', 'Banana', 100000)

		self.assertEqual(self.emp_1.email, 'Alex.Apple@email.com')
		self.assertEqual(self.emp_2.email, 'Barry.Banana@email.com')

		self.emp_1.first = 'Cathy'
		self.emp_2.first = 'David'

		self.assertEqual(self.emp_1.email, 'Cathy.Apple@email.com')
		self.assertEqual(self.emp_2.email, 'David.Banana@email.com')

	def test_fullname(self):
	#	emp_1 = Employee('Alex', 'Apple', 200000)
	#	emp_2 = Employee('Barry', 'Banana', 100000)

		self.assertEqual(self.emp_1.fullname, 'Alex Apple')
		self.assertEqual(self.emp_2.fullname, 'Barry Banana')

		self.emp_1.first = 'Cathy'
		self.emp_2.first = 'David'

		self.assertEqual(self.emp_1.fullname, 'Cathy Apple')
		self.assertEqual(self.emp_2.fullname, 'David Banana')

	def test_apply_raise(self):
	#	emp_1 = Employee('Alex', 'Apple', 200000)
	#	emp_2 = Employee('Barry', 'Banana', 100000)

		self.assertEqual(self.emp_1.fullname, 'Alex Apple')
		self.assertEqual(self.emp_2.fullname, 'Barry Banana')

		self.emp_1.apply_raise()
		self.emp_2.apply_raise()

		self.assertEqual(self.emp_1.pay, 210000)
		self.assertEqual(self.emp_2.pay, 105000)


if __name__ == '__main__':
	unittest.main()
