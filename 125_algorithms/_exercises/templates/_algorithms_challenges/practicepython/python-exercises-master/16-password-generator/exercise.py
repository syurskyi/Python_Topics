#! /usr/bin/env python
______ random
______ string


___ generatePass(length
    characters = string.ascii_letters + string.digits + string.punctuation
    r_ ''.join(random.SystemRandom().choice(characters) ___ _ in range(length))

__ __name__ __ '__main__':
    length = int(raw_input('How long the password should be? '))
    passwd = generatePass(length)
    print('\nThe password generated is: \n%s\n'%passwd)
