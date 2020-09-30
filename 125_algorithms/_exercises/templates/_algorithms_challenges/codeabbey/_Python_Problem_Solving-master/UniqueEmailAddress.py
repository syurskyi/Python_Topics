x = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

store_add =   # list
count = 0
___ i __ x:
    i = list(i)
    j = 0
    plus_check = False
    string = ''
    w___ i[j]!= '@':
        __ plus_check __ False:
            __ i[j] __ '.':
                i.pop(j)
            ____ i[j] __ '+':
                plus_check = True
            ____
                j += 1
                pass
        ____
            i.pop(j)
    string = ''.join(i)
    __ string not __ store_add:
        store_add.append(string)
        count += 1
    
r_(count)