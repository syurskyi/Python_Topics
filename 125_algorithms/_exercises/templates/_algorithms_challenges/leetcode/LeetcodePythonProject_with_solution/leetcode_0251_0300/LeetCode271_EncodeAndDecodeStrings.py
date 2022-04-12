'''
Created on Mar 5, 2017

@author: MT
'''

c_ Codec(o..
    ___ encode  strs
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        r.. ''.j..('%d:%s' % (l..(s), s) ___ s __ strs)
    
    ___ decode  s
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        arr    # list
        n l..(s)
        prev 0
        i 0
        w.... i < n:
            __ s[i] __ ':':
                sub s[prev:i]
                j i
                w.... j < n a.. s[j] !_ '#':
                    j += 1
                __ s[i+1:j].i.. a.. i..(s[i+1:j]) __ l..(sub
                    arr.a..(sub)
                    i j
                    prev i+1
            i += 1
        r.. arr
    
    ___ decode_orig  s
        result    # list
        i 0
        w.... i < l..(s
            j s.find(':', i)
            i j+1+i..(s[i:j])
            result.a..(s[j+1:i])
        r.. result