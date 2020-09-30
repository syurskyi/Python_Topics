fp = open("C:/Users/USER/Desktop/Python Projects/Python_File/Python.txt")
data =   # list

i = fp.readline()
while i != '':
    data.append(i)
    i = fp.readline()
fp.close()
print(data)