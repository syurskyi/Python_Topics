
___ tail(n

    print('Calling tail with n=' + str(n))

    # BASE CASE
    __ n == 0:
        return

    # first of all we do some operations
    # operation = print()
    print(n)

    # make the recursive function call
    tail(n-1)


___ head(n

    print('Calling head() with n=' + str(n))

    __ n == 0:
        return

    # we make the recursive function call
    head(n-1)

    # we can do any operations
    # operation - print()
    print(n)


head(5)
