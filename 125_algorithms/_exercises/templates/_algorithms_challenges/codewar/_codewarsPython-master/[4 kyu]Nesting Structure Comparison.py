___ same_structure_as(original,other
    __ type(original) in ('str','int') and type(other) in ('str','int'
        __ ''.join(map(str,original)) __ ''.join(map(str,other)):
            r_ True
        __ ''.join(map(str,original)) __ ''.join(map(str,other))[::-1]:
            r_ True
        ____
            r_  False

    __ type(original) != type(other
        r_ False

    __ le.(original) != le.(other
        r_ False
    ___ ori,oth in zip(original,other
        __ type(ori) != type(oth
            r_ False
        ____ type(ori) __ type(oth) and isinstance(ori,list
            __ not same_structure_as(ori,oth) or le.(ori) != le.(oth
                r_ False
    r_ True


print(same_structure_as([1,[1,1]],[2,[2,2],[2,3]]))
print(same_structure_as([1,'[',']'], ['[',']',1]))
