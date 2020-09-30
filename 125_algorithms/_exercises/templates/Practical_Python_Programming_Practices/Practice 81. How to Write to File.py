fp _ open("C:/Users/USER/Desktop/Python Projects/Python_File/Python.txt",'w')

fp.write("Hello World 1 \n")
fp.write("Hello World 2 \n")

fp.writelines("Hello World 3 \n")
text _ ["Hello World 4 \n","Hello World 5 \n", "Hello World 6"]
fp.writelines(text)

fp.close()

fp _ open("C:/Users/USER/Desktop/Python Projects/Python_File/Python.txt")
print(fp.read
fp.close()