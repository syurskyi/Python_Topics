# EXAMPLE OF A SCOPING PROBLEM:
total = 0


def increment():
	total += 1
	return total


print(increment()) # Error!
# "I can't find a variable named total in this function"

