______ unittest
______ os
______ json
____ percolate ______ parse_file, split_line, parse_phone_number, parse_lines, format_one, format_two, format_three, format_phone_number

__location__ _ os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

c_ TestFormatOne(unittest.TestCase):
	
	___ test
		line _ ['Chandler', 'Kerri', '(623)-668-9293', 'pink', '12345']
		line_dict _ {
			"color": "pink",
			"firstname": "Kerri",
			"lastname": "Chandler",
			"phonenumber": "623-668-9293",
			"zipcode": "12345"
			}

		assertEqual(
			format_one(line), line_dict)

c_ TestFormatTwo(unittest.TestCase):

	___ test
		line _ ['James', 'Murphy', 'yellow', '83880', '018 154 6474']
		line_dict _ {
			"color": "yellow",
			"firstname": "James",
			"lastname": "Murphy",
			"phonenumber": "018-154-6474",
			"zipcode": "83880"
			}

		assertEqual(
			format_two(line), line_dict)

c_ TestFormatThree(unittest.TestCase):
	___ test
		line _ ['Booker T.', 'Washington', '87360', '373 781 7380', 'yellow']
		line_dict _ {
			"color": "yellow",
			"firstname": "Booker T.",
			"lastname": "Washington",
			"phonenumber": "373-781-7380",
			"zipcode": "87360"
			}

		assertEqual(
			format_three(line), line_dict)

c_ TestSplitLines(unittest.TestCase):
	___ test1
		line _ 'James Murphy, yellow, 83880, 018 154 6474'
		l _ ['James', 'Murphy', 'yellow', '83880', '018 154 6474']
		
		assertEqual(split_line(line), l)

	___ test2
		line _ 'Booker T., Washington, 87360, 373 781 7380, yellow'
		l _ ['Booker T.', 'Washington', '87360', '373 781 7380', 'yellow']


c_ TestParsePhoneNumber(unittest.TestCase):
	___ testFalse
		assertEqual(
			parse_phone_number('123-12-1234'), False)

	___ testTrue
		assertEqual(
			parse_phone_number('123 456 7890'), True)

c_ TestFormatPhoneNumber(unittest.TestCase):
	___ test
		assertEqual(
			format_phone_number('1231231234'), '123-123-1234')

c_ TestParseLines(unittest.TestCase):

	___ test_error
		'''
		In case of an error, parse_lines() should
		return the line's index.
		'''
		line _ split_line('Chandler, Kerri, (623)-668-9293, pink, 123123121')
		assertEqual(
			parse_lines(line), None)

	___ test_format_one
		line _ split_line('Chandler, Kerri, (623)-668-9293, pink, 12345')

		line_dict _ {
			"color": "pink",
			"firstname": "Kerri",
			"lastname": "Chandler",
			"phonenumber": "623-668-9293",
			"zipcode": "12345"
			}

		assertEqual(
			parse_lines(line), line_dict)

	___ test_format_two
		line _ split_line('James Murphy, yellow, 83880, 018 154 6474')
		line_dict _ {
			"color": "yellow",
			"firstname": "James",
			"lastname": "Murphy",
			"phonenumber": "018-154-6474",
			"zipcode": "83880"
			}

		assertEqual(
			parse_lines(line), line_dict)

	___ test_format_three
		line _ split_line('Booker T., Washington, 87360, 373 781 7380, yellow')
		line_dict _ {
			"color": "yellow",
			"firstname": "Booker T.",
			"lastname": "Washington",
			"phonenumber": "373-781-7380",
			"zipcode": "87360"
			}

		assertEqual(
			parse_lines(line), line_dict)

c_ TestParseFile(unittest.TestCase):
	___ test
		lines _ ['Booker T., Washington, 87360, 373 781 7380, yellow',
				'Chandler, Kerri, (623)-668-9293, pink, 123123121',
				'James Murphy, yellow, 83880, 018 154 6474',
				'asdfawefawea']

		expected_output _ {
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

		assertEqual(parse_file(lines), expected_output)




if __name__ == '__main__':
	unittest.main()