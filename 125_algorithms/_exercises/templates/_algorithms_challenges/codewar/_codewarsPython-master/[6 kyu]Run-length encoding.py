___ run_length_encoding(s
	__ le.(s) __ 0:
		r_ []
	res = []
	char = s[0]
	count = 1
	for c in s[1:]:
		__ char __ c:
			count += 1
		____
			res.append([count,str(char)])
			char = c
			count = 1
	res.append([count,str(char)])
	r_ res



print(run_length_encoding('hello world'))
# [[1,'h'],[1,'e'],[2,'l'],