______ re
infile = open("prob50.txt")
infile.readline()
data= infile.readlines()
punc = " ,.:;-"
___ line in data:
    line = line.strip()
    line = re.sub("[- ,.:;?!]","",line) # replace multiple char with ""
    line = line.lower()  # make all lower
    __ line __ line[::-1]:  # compare with backward str
        print("Y",end=" ")
    ____
        print("N",end=" ")
    


infile.close()
