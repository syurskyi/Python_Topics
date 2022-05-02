___ run_length_encoding(s
	__ l..(s) __ 0:
		r..    # list
	res    # list
	char s[0]
	count 1
	___ c __ s 1|
		__ char __ c:
			count += 1
		____
			res.a..([count,s..(char)])
			char c
			count 1
	res.a..([count,s..(char)])
	r.. res



print(run_length_encoding('hello world'
# [[1,'h'],[1,'e'],[2,'l'],