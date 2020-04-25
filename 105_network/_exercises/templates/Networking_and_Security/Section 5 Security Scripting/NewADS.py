#  this requires NTFS on the file system
fh _ o..("file.txt:myfile", _
fh.w..("this is a test")
fh.c..

fh _ o..("file.txt:myfile", "r")
data _ fh.r..(100)
print(data)


