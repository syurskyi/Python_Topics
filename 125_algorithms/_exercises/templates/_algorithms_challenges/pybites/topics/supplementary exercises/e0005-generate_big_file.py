____ random _______ choice
____ string _______ ascii_uppercase

fh = open('bigfile.txt', 'w')

___ i __ r..(1,1000000):
    word = ''.join(choice(ascii_uppercase) ___ i __ r..(50))
    word = word + '\n'
    fh.write(word)

fh.close()