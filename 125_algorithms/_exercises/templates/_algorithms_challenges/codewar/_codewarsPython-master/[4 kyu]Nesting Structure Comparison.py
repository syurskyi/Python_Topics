___ same_structure_as(original,other):
    __ type(original) in ('str','int') and type(other) in ('str','int'):
        __ ''.join(map(str,original)) == ''.join(map(str,other)):
            return True
        __ ''.join(map(str,original)) == ''.join(map(str,other))[::-1]:
            return True
        else:
            return  False

    __ type(original) != type(other):
        return False

    __ len(original) != len(other):
        return False
    for ori,oth in zip(original,other):
        __ type(ori) != type(oth):
            return False
        elif type(ori) == type(oth) and isinstance(ori,list):
            __ not same_structure_as(ori,oth) or len(ori) != len(oth):
                return False
    return True                


print(same_structure_as([1,[1,1]],[2,[2,2],[2,3]]))
print(same_structure_as([1,'[',']'], ['[',']',1]))
