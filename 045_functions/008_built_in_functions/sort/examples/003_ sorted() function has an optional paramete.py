L = ["cccc", "b", "dd", "aaa"]

print "Normal sort :", sorted(L)

print "Sort with len :", sorted(L, key = len)

# Output :
# Normal sort : ['aaa', 'b', 'cccc', 'dd']
# Sort with len : ['b', 'dd', 'aaa', 'cccc']
