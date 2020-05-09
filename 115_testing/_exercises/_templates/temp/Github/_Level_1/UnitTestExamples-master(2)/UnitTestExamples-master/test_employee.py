______ u__
____ employee ______ Employee

c_ TestEmployee?.?

	??
	___ setUpClass ___
		print('setupClass')

	"""
	@classmethod applies to a class instead of an attribute.
	setUpClass and tearDownClass is used when you want to do something
	only once before a test. 
	"""

	??
	___ tearDownClass ___
		print('teardownClass')

	___ setUp
		emp_1 _ Employee('Alex', 'Apple', 200000)
		emp_2 _ Employee('Barry', 'Banana', 100000)

	"""
	Setup allows to not repeat creating instances. Note how emp_1
	and emp_2 are commented out below)
	"""

	___ tearDown
		p..
	"""
	Teardown is used when you test write files to a directory
	and later need to delete those files.
	"""

	___ test_email
	#	emp_1 = Employee('Alex', 'Apple', 200000)
	#	emp_2 = Employee('Barry', 'Banana', 100000)

		aE..(emp_1.email, 'Alex.Apple@email.com')
		aE..(emp_2.email, 'Barry.Banana@email.com')

		emp_1.first _ 'Cathy'
		emp_2.first _ 'David'

		aE..(emp_1.email, 'Cathy.Apple@email.com')
		aE..(emp_2.email, 'David.Banana@email.com')

	___ test_fullname
	#	emp_1 = Employee('Alex', 'Apple', 200000)
	#	emp_2 = Employee('Barry', 'Banana', 100000)

		aE..(emp_1.fullname, 'Alex Apple')
		aE..(emp_2.fullname, 'Barry Banana')

		emp_1.first _ 'Cathy'
		emp_2.first _ 'David'

		aE..(emp_1.fullname, 'Cathy Apple')
		aE..(emp_2.fullname, 'David Banana')

	___ test_apply_raise
	#	emp_1 = Employee('Alex', 'Apple', 200000)
	#	emp_2 = Employee('Barry', 'Banana', 100000)

		aE..(emp_1.fullname, 'Alex Apple')
		aE..(emp_2.fullname, 'Barry Banana')

		emp_1.apply_raise()
		emp_2.apply_raise()

		aE..(emp_1.pay, 210000)
		aE..(emp_2.pay, 105000)


__ _____ __ _____
	?.?
