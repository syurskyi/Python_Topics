'''
Created on Feb 13, 2017

@author: MT
'''
class TwoSum(object):

    ___ __init__(self):
        """
        initialize your data structure here
        """
        self.elements = {}

    ___ add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        __ number __ self.elements:
            self.elements[number] += 1
        ____:
            self.elements[number] = 1

    ___ find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        ___ num __ self.elements:
            target = value-num
            __ target __ self.elements:
                __ target __ num a.. self.elements[target]<2:
                    continue
                r.. True
        r.. False