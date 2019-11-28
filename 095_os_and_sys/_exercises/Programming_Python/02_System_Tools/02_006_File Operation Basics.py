# open('file').read() # read entire file into string
# open('file').read(N) # read next N bytes into string
# open('file').readlines() # read entire file into line strings list
# open('file').readline() # read next line, through '\n'

file = open('spam.txt', 'w') # create file spam.txt
file.write(('spam' * 15) + '\n') # write text: returns #characters written
# 21
file.close()
file = open('spam.txt') # or open('spam.txt').read()
text = file.read() # read into a string
print(text)
# 'spamspamspamspamspam\n'