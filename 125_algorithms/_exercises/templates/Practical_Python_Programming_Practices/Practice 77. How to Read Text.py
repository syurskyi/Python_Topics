text =   # list
___ i __ open("C:/Users/USER/Desktop/Python Projects/Python_File/Python.txt"):
    text.append(i)
print(text)

___ i __ ra..(len(text)):
    if text[i][-1] == '\n':
        text[i] = text[i][:-1]
print(text)