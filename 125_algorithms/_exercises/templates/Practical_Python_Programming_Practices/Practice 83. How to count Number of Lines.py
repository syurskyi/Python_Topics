lines = 0
words = 0
letters = 0

fp = "C:/Users/USER/Desktop/Python Projects/Python_File/Python.txt"

___ line __ open(fp):
    lines += 1
    letters += len(line)

    pos = 'out'
    ___ letter __ line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
print("Lines: ",lines)
print("Words: ",words)
print("Letters: ",letters)