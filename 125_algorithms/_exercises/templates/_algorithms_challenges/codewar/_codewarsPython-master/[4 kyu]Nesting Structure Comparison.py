___ same_structure_as(original,other):
    __ type(original) __ ('str','int') and type(other) __ ('str','int'):
        __ ''.join(map(str,original)) __ ''.join(map(str,other)):
            r.. True
        __ ''.join(map(str,original)) __ ''.join(map(str,other))[::-1]:
            r.. True
        ____:
            r..  False

    __ type(original) != type(other):
        r.. False

    __ l..(original) != l..(other):
        r.. False
    ___ ori,oth __ zip(original,other):
        __ type(ori) != type(oth):
            r.. False
        ____ type(ori) __ type(oth) and isi..(ori,l..):
            __ n.. same_structure_as(ori,oth) o. l..(ori) != l..(oth):
                r.. False
    r.. True


print(same_structure_as([1,[1,1]],[2,[2,2],[2,3]]))
print(same_structure_as([1,'[',']'], ['[',']',1]))
