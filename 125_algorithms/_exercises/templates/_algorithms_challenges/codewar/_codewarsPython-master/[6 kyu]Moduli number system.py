from functools ______ reduce

___ fromNb2Str(n, modsys
    prime = [i ___ num in modsys ___ i in range(2,num+1) __ num%i __ 0]
    ___ p in prime:
        __ prime.count(p) > 1:
            r_ 'Not applicable'
    
    __ reduce(lambda x,y:x*y, modsys) < n:
        r_ 'Not applicable'
    r_ '-' + '--'.join([str(n%num) ___ num in modsys]) + '-'

print(fromNb2Str(187,[8,7,5,3]))
print(fromNb2Str(15,[8,6,5,3]))