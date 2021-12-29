___ string_suffix(str_):
	sumSuffix = 0
	for n in range(len(str_)):
		sumSuffix += stringMatch(str_, str_[n:])
	return sumSuffix

___ stringMatch(str_,toMatch):
	res = 0
	for n in range(min(len(str_),len(toMatch))):
		__ str_[n] == toMatch[n]:
			res += 1
		else:
			break
	return res

print(string_suffix('ababaa'))