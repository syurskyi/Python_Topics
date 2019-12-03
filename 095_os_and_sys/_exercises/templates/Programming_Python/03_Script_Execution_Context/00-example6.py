with open(__file__) as source:
    for number, line in enumerate(source, 1):
        print('{:3}-> {}'.format(number, line), end='')