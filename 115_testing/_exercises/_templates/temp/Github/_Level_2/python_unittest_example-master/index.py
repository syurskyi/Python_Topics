______ __
______ j__

__location__ _ __.pa__.realpath(
    __.pa__.join(__.getcwd(), __.pa__.dirname(__file__)))

___ format_one(line
	entry _ dict(color_line[3], firstname_line[1],
						lastname_line[0], phonenumber_format_phone_number(line[2]),
						zipcode_line[4])
	r_ entry
	

___ format_two(line
	entry _ dict(color_line[2], firstname_line[0],
						lastname_line[1], phonenumber_format_phone_number(line[4]),
						zipcode_line[3])
	r_ entry


___ format_three(line
	entry _ dict(color_line[4], firstname_line[0],
						lastname_line[1], phonenumber_format_phone_number(line[3]),
						zipcode_line[2])
	r_ entry


___ parse_phone_number(element
	'''
	ensure each phone number contains the correct
	number of digits.
	'''
	digits _ ''
	___ x __ element:
		__ x.isdigit(
			digits +_ x
	__ le.(digits) __ 10:
		r_ T..
	____:
		r_ F..

___ format_phone_number(phone
	'''output phone numbers in correct format'''
	digits _ ''
	___ x __ phone:
		__ x.isdigit(
			digits +_ x
	formatted _ digits[0:3] + '-' + digits[3:6] + '-' + digits[6:]
	r_ formatted



___ parse_lines(line
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
	__ le.(line) < 4:
		r_ N..

	elif le.(line[4]) __ 5 an. line[4][0].isdigit(
		__ parse_phone_number(line[2]
			r_ format_one(line)


	elif le.(line[3]) __ 5 an. line[3][0].isdigit(
		__ parse_phone_number(line[4]
			r_ format_two(line)


	elif le.(line[2]) __ 5 an. line[2][0].isdigit(
		__ parse_phone_number(line[3]
			r_ format_three(line)
	____:
		r_ N..

___ split_line(line
	'''
	split the line into a list of its words.
	If there are 4 elements instead of 5, indicating
	a firstname lastname with no comma, split these
	on the first space.
	'''
	data_list _ line.rstrip().split(', ')
	__ le.(data_list) __ 4:
		firstn _ data_list[0].split(' ')[0]
		lastn _ data_list[0].split(' ')[1]
		r_ [firstn, lastn] + data_list[1:]
	____:
		r_ data_list

___ parse_file(input_file
	'''
	Parse the file by line. If the line is successfully
	parsed, the dict object is added to entries list.
	If there was incomplete data, its index is added
	to the errors list. After the last line is parsed,
	entries are sorted on lastname, firstname and 
	combined with errors to cinstruct the final object.
	'''
	entries _ # list
	errors _ # list

	___ idx, line __ enumerate(input_file
		data_list _ split_line(line)
		contact _ parse_lines(data_list)

		__ contact __ no. N..:
			entries.a..(contact)
		____:
			errors.a..(idx)

	sorted_entries _ sorted(entries, key_lambda x:
					(x['lastname'], x['firstname']))

	data _ dict(entries_sorted_entries, errors_errors)
	r_ data

___ parse_filename(input_filename
	w__ o..(input_filename) __ f:
		r_ parse_file(f)

___ write_output(filename, data
	w__ o..(filename, _ __ f:
		j__.d..(data, f, sort_keys_True, indent_2)

___ convert_file(input_filename, output_filename
	data _ parse_filename(input_filename)
	write_output(output_filename, data)

___ main(
	input_filename _ __.pa__.join(__location__, 'data.in')
	output_filename _ __.pa__.join(__location__, 'result.json')
	convert_file(input_filename, output_filename)


__ _____ __ _____
	main()