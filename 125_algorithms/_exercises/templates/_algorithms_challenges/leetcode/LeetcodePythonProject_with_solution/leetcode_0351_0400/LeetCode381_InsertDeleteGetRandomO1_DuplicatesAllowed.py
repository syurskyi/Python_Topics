'''
Created on Apr 1, 2017

@author: MT
'''

c_ RandomizedCollection(o..
    ___ -
        vals    # list
        pos    # dict
    
    ___ insert  val
        vals.a..(val)
        __ val __ pos:
            pos[val].add(l..(vals)-1)
            r.. F..
        ____
            pos[val] s..([l..(vals)-1])
            r.. T..
    
    ___ remove  val
        __ val __ pos:
            lastVal vals[-1]
            ind pos[val].p.. )
            vals[ind] lastVal
            __ pos[lastVal]:
                pos[lastVal].add(ind)
                pos[lastVal].discard(l..(vals)-1)
            vals.p.. )
            __ n.. pos[val]:
                del pos[val]
            r.. T..
        r.. F..
    
    ___ getRandom
        _______ r__
        r.. r__.c..(vals)
    