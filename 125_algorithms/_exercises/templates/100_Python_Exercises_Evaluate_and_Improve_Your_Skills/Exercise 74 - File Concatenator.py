#Concatenate the two txt files into one file
______ pandas

data1 _ pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 _ pandas.read_csv("sampledata_x_2.txt")
data12 _ pandas.concat([data1, data2])
data12.to_csv("sampledata12.txt", index_None)

print(data12)
