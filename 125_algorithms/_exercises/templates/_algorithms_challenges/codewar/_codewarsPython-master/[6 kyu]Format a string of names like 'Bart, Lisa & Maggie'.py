___ namelist(names
    namelist =  [name['name'] for name in names]
    __ le.(namelist) <= 1:
    	r_ ''.join(namelist)
    ____
    	lastTwo = ' & '.join(namelist[-2:])
    	first = [n + ',' for n in namelist[:-2]]
    	first.append(lastTwo)
    	r_ ' '.join(first)
