file = open('data.txt', 'a') # open in append mode: doesn't erase
file.write('The Life of Brian') # added at end of existing data
file.close()

open('data.txt').read() # open and read entire file
# 'Hello file world!\nBye file world.\nThe Life of Brian'