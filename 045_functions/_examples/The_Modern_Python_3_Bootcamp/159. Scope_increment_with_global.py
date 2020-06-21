total = 0


def increment():
	global total  # use the global variable total
	total += 1
	return total


print(increment())  # 1
print(increment())  # 2
print(increment())  # 3

