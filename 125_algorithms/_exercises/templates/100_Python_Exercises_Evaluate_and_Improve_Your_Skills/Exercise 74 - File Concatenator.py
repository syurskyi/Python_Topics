#Concatenate the two txt files into one file
_______ pandas

data1  pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2  pandas.read_csv("sampledata_x_2.txt")
data12  pandas.concat([data1, data2])
data12.to_csv("sampledata12.txt", indexNone)

print(data12)
