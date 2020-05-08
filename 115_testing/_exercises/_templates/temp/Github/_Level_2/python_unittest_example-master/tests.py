import unittest
import os
import json
from percolate import parse_file, split_line, parse_phone_number, parse_lines, format_one, format_two, format_three, format_phone_number

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

c_ TestFormatOne(unittest.TestCase):
	
	___ test(self):
		line = ['Chandler', 'Kerri', '(623)-668-9293', 'pink', '12345']
		line_dict = {
			"color": "pink",
			"firstname": "Kerri",
			"lastname": "Chandler",
			"phonenumber": "623-668-9293",
			"zipcode": "12345"
			}

		self.assertEqual(
			format_one(line), line_dict)

c_ TestFormatTwo(unittest.TestCase):

	___ test(self):
		line = ['James', 'Murphy', 'yellow', '83880', '018 154 6474']
		line_dict = {
			"color": "yellow",
			"firstname": "James",
			"lastname": "Murphy",
			"phonenumber": "018-154-6474",
			"zipcode": "83880"
			}

		self.assertEqual(
			format_two(line), line_dict)

c_ TestFormatThree(unittest.TestCase):
	___ test(self):
		line = ['Booker T.', 'Washington', '87360', '373 781 7380', 'yellow']
		line_dict = {
			"color": "yellow",
			"firstname": "Booker T.",
			"lastname": "Washington",
			"phonenumber": "373-781-7380",
			"zipcode": "87360"
			}

		self.assertEqual(
			format_three(line), line_dict)

c_ TestSplitLines(unittest.TestCase):
	___ test1(self):
		line = 'James Murphy, yellow, 83880, 018 154 6474'
		l = ['James', 'Murphy', 'yellow', '83880', '018 154 6474']
		
		self.assertEqual(split_line(line), l)

	___ test2(self):
		line = 'Booker T., Washington, 87360, 373 781 7380, yellow'
		l = ['Booker T.', 'Washington', '87360', '373 781 7380', 'yellow']


c_ TestParsePhoneNumber(unittest.TestCase):
	___ testFalse(self):
		self.assertEqual(
			parse_phone_number('123-12-1234'), False)

	___ testTrue(self):
		self.assertEqual(
			parse_phone_number('123 456 7890'), True)

c_ TestFormatPhoneNumber(unittest.TestCase):
	___ test(self):
		self.assertEqual(
			format_phone_number('1231231234'), '123-123-1234')

c_ TestParseLines(unittest.TestCase):

	___ test_error(self):
		'''
		In case of an error, parse_lines() should
		return the line's index.
		'''
		line = split_line('Chandler, Kerri, (623)-668-9293, pink, 123123121')
		self.assertEqual(
			parse_lines(line), None)

	___ test_format_one(self):
		line = split_line('Chandler, Kerri, (623)-668-9293, pink, 12345')

		line_dict = {
			"color": "pink",
			"firstname": "Kerri",
			"lastname": "Chandler",
			"phonenumber": "623-668-9293",
			"zipcode": "12345"
			}

		self.assertEqual(
			parse_lines(line), line_dict)

	___ test_format_two(self):
		line = split_line('James Murphy, yellow, 83880, 018 154 6474')
		line_dict = {
			"color": "yellow",
			"firstname": "James",
			"lastname": "Murphy",
			"phonenumber": "018-154-6474",
			"zipcode": "83880"
			}

		self.assertEqual(
			parse_lines(line), line_dict)

	___ test_format_three(self):
		line = split_line('Booker T., Washington, 87360, 373 781 7380, yellow')
		line_dict = {
			"color": "yellow",
			"firstname": "Booker T.",
			"lastname": "Washington",
			"phonenumber": "373-781-7380",
			"zipcode": "87360"
			}

		self.assertEqual(
			parse_lines(line), line_dict)

c_ TestParseFile(unittest.TestCase):
	___ test(self):
		lines = ['Booker T., Washington, 87360, 373 781 7380, yellow',
				'Chandler, Kerri, (623)-668-9293, pink, 123123121',
				'James Murphy, yellow, 83880, 018 154 6474',
				'asdfawefawea']

		expected_output = {
					"entries": [
					{
					"color": "yellow",
					"firstname": "James",
					"lastname": "Murphy",
					"phonenumber": "018-154-6474",
					"zipcode": "83880"
					},
					{
					"color": "yellow",
					"firstname": "Booker T.",
					"lastname": "Washington",
					"phonenumber": "373-781-7380",
					"zipcode": "87360"
					}
					],
					"errors": [
					1,
					3
					]
					}

		self.assertEqual(parse_file(lines), expected_output)




if __name__ == '__main__':
	unittest.main()