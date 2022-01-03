'''
Created on Apr 1, 2017

@author: MT
'''

c_ RandomizedCollection(object):
    ___ - ):
        vals    # list
        pos    # dict
    
    ___ insert(self, val):
        vals.a..(val)
        __ val __ pos:
            pos[val].add(l..(vals)-1)
            r.. F..
        ____:
            pos[val] = set([l..(vals)-1])
            r.. T..
    
    ___ remove(self, val):
        __ val __ pos:
            lastVal = vals[-1]
            ind = pos[val].pop()
            vals[ind] = lastVal
            __ pos[lastVal]:
                pos[lastVal].add(ind)
                pos[lastVal].discard(l..(vals)-1)
            vals.pop()
            __ n.. pos[val]:
                del pos[val]
            r.. T..
        r.. F..
    
    ___ getRandom
        _______ random
        r.. random.choice(vals)
    