# Corey Schafer
# Python Tutorial: Unit Testing Your Code with the unittest Module
# https://www.youtube.com/watch?v=6tNS--WetLI

import unittest
import calc

class TestCalc(unittest.TestCase):

	#def test_add(self): # must start with test_
	#	result = calc.add(2,8)
	#	self.assertEqual(result,11)

	#We can rewrite the above as:
	def test_add(self):
		self.assertEqual(calc.add(2,8),10)
		self.assertEqual(calc.add(-1,1),0)
		self.assertEqual(calc.add(-1,-1),-2)

	def test_subtract(self):
		self.assertEqual(calc.subtract(10,8),2)
		self.assertEqual(calc.subtract(10,10),0)
		self.assertEqual(calc.subtract(-1,2),-3)

	def test_multiply(self):
		self.assertEqual(calc.multiply(2,5),10)
		self.assertEqual(calc.multiply(-1,1),-1)
		self.assertEqual(calc.multiply(-1,-1),1)

	def test_divide(self):
		self.assertEqual(calc.divide(10,2),5)
		self.assertEqual(calc.divide(-10,2),-5)
		self.assertEqual(calc.divide(-1,-1),1)
		
		self.assertRaises(ValueError, calc.divide,10,0)
	#	Can also use a context manager to check ValueError:
		with self.assertRaises(ValueError):
			calc.divide(10,0)

	def test_power(self):
		self.assertEqual(calc.power(2,4),16)
		self.assertEqual(calc.power(0,1),0)
		self.assertEqual(calc.power(-1,-1),-1)
		self.assertEqual(calc.power(10,0),1)
		self.assertEqual(calc.power(0,0),1)

# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

"""
Use Terminal to run test using:
	python -m unittest test_calc.py

"""

"""
Instead of typing in python -m unittest test_calc.py,
we can abbreviate by placing the following at the bottom
of the test_calc.py file:

if __name__ == '__main__':
	unittest.main()


This will allow you to run the test using:
	python test_calc.py

"""


if __name__ == '__main__':
	unittest.main()

"""
If an AssertionError is produced, the first value is what is
the output produced by the function and the second is what
you hardcoded as the expectation. 
"""


