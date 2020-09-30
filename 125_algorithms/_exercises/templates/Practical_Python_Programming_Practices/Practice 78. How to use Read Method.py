fp _ open("C:/Users/USER/Desktop/Python Projects/Python_File/Python.txt")
data _ fp.read()
fp.close()

print(repr(data))

data _ data.split('\n')
print(data)