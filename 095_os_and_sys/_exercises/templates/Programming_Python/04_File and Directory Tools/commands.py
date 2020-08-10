#!/usr/local/bin/python
from ___ ______ argv
from scanfile ______ scanner
class UnknownCommand(Exception): pass

___ processLine(line):                      # define a function
    __ line[0] == '*':                      # applied to each line
        print("Ms.", line[1:-1])
    elif line[0] == '+':
        print("Mr.", line[1:-1])            # strip first and last char: \n
    ____
        raise UnknownCommand(line)          # raise an exception

filename = 'data.txt'
__ len(argv) == 2: filename = argv[1]       # allow filename cmd arg
scanner(filename, processLine)              # start the scanner


"""
commands = {'*': 'Ms.', '+': 'Mr.'}     # data is easier to expand than code?

def processLine(line):
    try:
        print(commands[line[0]], line[1:-1])
    except KeyError:
        raise UnknownCommand(line)

scanner(argv[1], processLine)
"""