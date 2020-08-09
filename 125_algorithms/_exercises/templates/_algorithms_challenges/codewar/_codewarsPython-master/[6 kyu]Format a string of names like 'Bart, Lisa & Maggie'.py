___ namelist(names
    namelist =  [name['name'] ___ name in names]
    __ le.(namelist) <= 1:
    	r_ ''.join(namelist)
    ____
    	lastTwo = ' & '.join(namelist[-2:])
    	first = [n + ',' ___ n in namelist[:-2]]
    	first.append(lastTwo)
    	r_ ' '.join(first)
