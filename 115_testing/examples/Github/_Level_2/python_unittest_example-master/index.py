import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def format_one(line):
	entry = dict(color=line[3], firstname=line[1], 
						lastname=line[0], phonenumber=format_phone_number(line[2]),
						zipcode=line[4])
	return entry
	

def format_two(line):
	entry = dict(color=line[2], firstname=line[0], 
						lastname=line[1], phonenumber=format_phone_number(line[4]),
						zipcode=line[3])
	return entry


def format_three(line):
	entry = dict(color=line[4], firstname=line[0], 
						lastname=line[1], phonenumber=format_phone_number(line[3]),
						zipcode=line[2])
	return entry


def parse_phone_number(element):
	'''
	ensure each phone number contains the correct
	number of digits.
	'''
	digits = ''
	for x in element:
		if x.isdigit():
			digits += x
	if len(digits) == 10:
		return True
	else:
		return False

def format_phone_number(phone):
	'''output phone numbers in correct format'''
	digits = ''
	for x in phone:
		if x.isdigit():
			digits += x
	formatted = digits[0:3] + '-' + digits[3:6] + '-' + digits[6:]
	return formatted



def parse_lines(line):
	'''
	If the line has fewer than 4 elements, its index
	should be added to the 'errors' list immediately
	to avoid errors. The line format type is determined
	by the zipcode's index, since it's the most easily
	identifiable (length = 5 and starts with a digit).
	If an error is found with phone number length, it
	is also added to errors; otherwise, return the 
	elements like to the appropriate formatting function.
	'''
	if len(line) < 4:
		return None

	elif len(line[4]) == 5 and line[4][0].isdigit():
		if parse_phone_number(line[2]):
			return format_one(line)


	elif len(line[3]) == 5 and line[3][0].isdigit():
		if parse_phone_number(line[4]):
			return format_two(line)


	elif len(line[2]) == 5 and line[2][0].isdigit():
		if parse_phone_number(line[3]):
			return format_three(line)
	else:
		return None

def split_line(line):
	'''
	split the line into a list of its words.
	If there are 4 elements instead of 5, indicating
	a firstname lastname with no comma, split these
	on the first space.
	'''
	data_list = line.rstrip().split(', ')
	if len(data_list) == 4:
		firstn = data_list[0].split(' ')[0]
		lastn = data_list[0].split(' ')[1]
		return [firstn, lastn] + data_list[1:]
	else:
		return data_list

def parse_file(input_file):
	'''
	Parse the file by line. If the line is successfully
	parsed, the dict object is added to entries list.
	If there was incomplete data, its index is added
	to the errors list. After the last line is parsed,
	entries are sorted on lastname, firstname and 
	combined with errors to cinstruct the final object.
	'''
	entries = []
	errors = []

	for idx, line in enumerate(input_file):
		data_list = split_line(line)
		contact = parse_lines(data_list)

		if contact is not None:
			entries.append(contact)
		else:
			errors.append(idx)

	sorted_entries = sorted(entries, key=lambda x:
					(x['lastname'], x['firstname']))

	data = dict(entries=sorted_entries, errors=errors)
	return data

def parse_filename(input_filename):
	with open(input_filename) as f:
		return parse_file(f)

def write_output(filename, data):
	with open(filename, 'w') as f:
		json.dump(data, f, sort_keys=True, indent=2)

def convert_file(input_filename, output_filename):
	data = parse_filename(input_filename)
	write_output(output_filename, data)

def main():
	input_filename = os.path.join(__location__, 'data.in')
	output_filename = os.path.join(__location__, 'result.json')
	convert_file(input_filename, output_filename)


if __name__ == '__main__':
	main()