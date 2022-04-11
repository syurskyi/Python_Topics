___ string_suffix(str_
	sumSuffix 0
	___ n __ r..(l..(str_:
		sumSuffix += stringMatch(str_, str_[n:])
	r.. sumSuffix

___ stringMatch(str_,toMatch
	res 0
	___ n __ r..(m..(l..(str_),l..(toMatch))):
		__ str_[n] __ toMatch[n]:
			res += 1
		____
			_____
	r.. res

print(string_suffix('ababaa'