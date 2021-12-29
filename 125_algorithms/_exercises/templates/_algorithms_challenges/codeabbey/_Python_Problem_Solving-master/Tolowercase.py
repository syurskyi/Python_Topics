s ='HEELLLLOO'
string = ''
___ i __ r..(l..(s)):
    __ 'A='<= s[i] <= 'Z':
        string += chr((ord(s[i])) + 32)
    ____:
        string += s[i]
print(string)