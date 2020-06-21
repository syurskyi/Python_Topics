#  this requires NTFS on the file system
fh = open("file.txt:myfile", "w")
fh.write("this is a test")
fh.close()

fh = open("file.txt:myfile", "r")
data = fh.read(100)
print(data)


