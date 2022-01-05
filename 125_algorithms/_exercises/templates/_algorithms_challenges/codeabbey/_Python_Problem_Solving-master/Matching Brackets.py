#take the number of strings that are needed to be checked
___ i __ r..(i..(input())):
    #accept the string
    s__ = input()
    #store_str is used to store only the brackets
    store_str    # list
    #para list is used to check whether the character in string is equal to elements of para
    para = ['(',')','[',']','<','>','{','}']
    # p Dictionary is used to store the pair of the parenthesis
    p = {'(':')','[':']','<':'>','{':'}'}
    
    #here we remove all alphabets, digits and unwanted special characters
    ___ j __ s__:
        #if in para list then only form the list
        __ j __ para:
            store_str.a..(j)

    #First step is to check if there are any pair next to each other if yes then pop those two elements from list
    ___ j __ r..(l..(store_str)):
        ___ k __ r..(0, l..(store_str)):
            #try and except are used because if a particular key is not present in dictionary p, it can throw error
            ___
                __ p[store_str[k]] __ s..(store_str[k+1]):
                    store_str.pop(k)
                    store_str.pop(k)
            ______:
                p..
        __ l..(store_str) __ 1:
            print('0',end=' ')
            checker = F..
            break
        ____ l..(store_str) __ 0:
            print('1',end= ' ')
            checker = F..
            break
        ____:
            checker = T..
            p..
    #Step two is once the element next to each other which were pair are removed.
    #then we are left with nested loops
    #if the starting element and the last element of the list are same then pop, else the give string is not nested properly
    # and the result is 0
    __ checker __ T..:
        w.... l..(store_str) != 1:
            ___
                __ p[store_str[0]] __ store_str[-1]:
                    store_str.pop(0)
                    store_str.pop(-1)
                ____:
                    break
            ______:
                break
        __ l..(store_str) __ 0:
            print('1',end=' ')
        ____ l..(store_str) __ 1 o. l..(store_str) > 1:
            print('0',end=' ')