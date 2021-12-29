'''
Created on Mar 5, 2017

@author: MT
'''

class Codec(object):
    ___ encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join('%d:%s' % (len(s), s) for s in strs)
    
    ___ decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        arr = []
        n = len(s)
        prev = 0
        i = 0
        while i < n:
            __ s[i] == ':':
                sub = s[prev:i]
                j = i
                while j < n and s[j] != '#':
                    j += 1
                __ s[i+1:j].isdigit() and int(s[i+1:j]) == len(sub):
                    arr.append(sub)
                    i = j
                    prev = i+1
            i += 1
        return arr
    
    ___ decode_orig(self, s):
        result = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j+1+int(s[i:j])
            result.append(s[j+1:i])
        return result