line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]
print(col1)
print(col3)
line = 'aaa bbb ccc'
cols = line.split()
print(cols)
line = 'bob,hacker,40'
print(line.split(','))
line = "i'mSPAMaSPAMlumberjack"
print(line.split('SPAM'))
