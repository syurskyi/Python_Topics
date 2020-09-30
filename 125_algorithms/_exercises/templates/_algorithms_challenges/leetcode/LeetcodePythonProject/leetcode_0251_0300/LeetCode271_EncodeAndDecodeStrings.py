'''
Created on Mar 5, 2017

@author: MT
'''

class Codec(object
    ___ encode(self, strs
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        r_ ''.join('%d:%s' % (le.(s), s) ___ s __ strs)
    
    ___ decode(self, s
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        arr =   # list
        n = le.(s)
        prev = 0
        i = 0
        w___ i < n:
            __ s[i] __ ':':
                sub = s[prev:i]
                j = i
                w___ j < n and s[j] != '#':
                    j += 1
                __ s[i+1:j].isdigit() and int(s[i+1:j]) __ le.(sub
                    arr.append(sub)
                    i = j
                    prev = i+1
            i += 1
        r_ arr
    
    ___ decode_orig(self, s
        result =   # list
        i = 0
        w___ i < le.(s
            j = s.find(':', i)
            i = j+1+int(s[i:j])
            result.append(s[j+1:i])
        r_ result