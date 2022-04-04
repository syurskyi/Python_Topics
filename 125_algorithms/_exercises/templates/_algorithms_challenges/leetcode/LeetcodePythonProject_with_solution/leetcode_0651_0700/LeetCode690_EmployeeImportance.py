'''
Created on Oct 24, 2017

@author: MT
'''
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
c_ Solution(o..
    ___ getImportance  employees, id
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        hashmap    # dict
        ___ emp __ employees:
            hashmap[emp.id] = hashmap.g.. emp.id, []) + [emp]
        queue    # list
        ___ emp __ employees:
            __ emp.id __ id:
                queue.a..(emp)
        res = 0
        w.... queue:
            emp = queue.p.. 0)
            subs = emp.subordinates
            res += emp.importance
            ___ sub __ subs:
                queue += hashmap.g.. sub, [])
        r.. res
