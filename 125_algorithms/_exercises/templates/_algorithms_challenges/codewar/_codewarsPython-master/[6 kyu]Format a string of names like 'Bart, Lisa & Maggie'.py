___ namelist(names):
    namelist =  [name['name'] for name in names]
    __ len(namelist) <= 1:
    	return ''.join(namelist)
    else:
    	lastTwo = ' & '.join(namelist[-2:])
    	first = [n + ',' for n in namelist[:-2]]
    	first.append(lastTwo)
    	return ' '.join(first)
