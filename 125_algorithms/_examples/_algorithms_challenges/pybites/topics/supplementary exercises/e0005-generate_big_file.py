from random import choice
from string import ascii_uppercase

fh = open('bigfile.txt', 'w')

for i in range(1,1000000):
    word = ''.join(choice(ascii_uppercase) for i in range(50))
    word = word + '\n'
    fh.write(word)

fh.close()