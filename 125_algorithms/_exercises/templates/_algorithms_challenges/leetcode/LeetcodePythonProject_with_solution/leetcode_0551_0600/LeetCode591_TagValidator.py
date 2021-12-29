'''
Created on Sep 5, 2017

@author: MT
'''

class Solution(object):
    ___ isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        _______ re
        code = re.sub(r'<!\[CDATA\[.*?\]\]>|t', '-', code)
        prev = N..
        w.... code != prev:
            prev = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
        r.. code __ 't'
