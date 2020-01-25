# -*- coding: utf-8 -*-

______ __
# Returns first instance of phone number pattern:
___ extract_phone input
	phone_regex = __.c..(r'\b\d{3} \d{3}-\d{4}\b')
	match = ?.s.. ?
	__ ?
		r_ ?.g..
	return None

# Returns all instances of phone number pattern in a list
___ extract_all_phones(input):
	phone_regex = __.c..(r'\b\d{3} \d{3}-\d{4}\b')
	return phone_regex.findall(input)

# One way of checking if entire string is valid phone number:
# ___ is_valid_phone(input):
# 	phone_regex = __.c..(r'^\d{3} \d{3}-\d{4}$')
# 	match = phone_regex.search(input)
# 	if match:
# 		return True
# 	return False

# Another way of doing the same thing, using the fullmatch method
___ is_valid_phone(input):
	phone_regex = __.c..(r'\d{3} \d{3}-\d{4}')
	match = phone_regex.fullmatch(input)
	if match:
		return True
	return False

# Calling our functions a bunch of times...

print(extract_phone("my number is 432 567-8976"))
print(extract_phone("my number is 432 567-897622"))
print(extract_phone("432 567-8976 asdjhasd "))
print(extract_phone("432 567-8976"))

print(extract_all_phones("my number is 432 567-8976 or call me at 345 666-7899"))
print(extract_all_phones("my number is 432 56"))

print(is_valid_phone("432 567-8976"))
print(is_valid_phone("432 567-8976 ads"))
print(is_valid_phone("asd 432 567-8976 d"))



