# Create List of Dictionary Values

markdict={"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
marklist=list(markdict.items())
print(marklist)


# sorted()

markdict = {"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
marklist = sorted(markdict.items(), key=lambda x:x[1])
sortdict = dict(marklist)
print(sortdict)

# Sort Dict using itemgetter()

import operator

markdict = {"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
marklist= sorted(markdict.items(), key=operator.itemgetter(1))
sortdict=dict(marklist)
print(sortdict)

# sorted()

markdict = {"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
marklist=sorted((value, key) for (key,value) in markdict.items())
sortdict=dict([(k,v) for v,k in marklist])
print(sortdict)
