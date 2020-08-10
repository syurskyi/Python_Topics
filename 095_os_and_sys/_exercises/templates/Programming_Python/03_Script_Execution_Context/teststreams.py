"read numbers till eof and show squares"

___ interact():
    print('Hello stream world')                     # print sends to sys.stdout
    while True:
        ___
            reply _ input('Enter a number>')        # input reads sys.stdin
        ______ EOFError:
            break                                   # raises an ______ on eof
        ____                                       # input given as a string
            num _ int(reply)
            print("%d squared is %d" % (num, num ** 2))
    print('Bye')

__ __name__ __ '__main__':
    interact()                                      # when run, not imported
