lines _ 0
words _ 0
letters _ 0

fp _ "C:/Users/USER/Desktop/Python Projects/Python_File/Python.txt"

___ line __ open(fp):
    lines +_ 1
    letters +_ le.(line)

    pos _ 'out'
    ___ letter __ line:
        __ letter !_ ' ' an. pos __ 'out':
            words +_ 1
            pos _ 'in'
        elif letter __ ' ':
            pos _ 'out'
print("Lines: ",lines)
print("Words: ",words)
print("Letters: ",letters)