___ string_suffix(str_
	sumSuffix = 0
	___ n in range(le.(str_)):
		sumSuffix += stringMatch(str_, str_[n:])
	r_ sumSuffix

___ stringMatch(str_,toMatch
	res = 0
	___ n in range(min(le.(str_),le.(toMatch))):
		__ str_[n] __ toMatch[n]:
			res += 1
		____
			break
	r_ res

print(string_suffix('ababaa'))