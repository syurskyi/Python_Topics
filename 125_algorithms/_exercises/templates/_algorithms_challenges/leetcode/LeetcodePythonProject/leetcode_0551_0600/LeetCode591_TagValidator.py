'''
Created on Sep 5, 2017

@author: MT
'''

class Solution(object
    ___ isValid(self, code
        """
        :type code: str
        :rtype: bool
        """
        ______ re
        code = re.sub(r'<!\[CDATA\[.*?\]\]>|t', '-', code)
        prev = None
        w___ code != prev:
            prev = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
        r_ code __ 't'
