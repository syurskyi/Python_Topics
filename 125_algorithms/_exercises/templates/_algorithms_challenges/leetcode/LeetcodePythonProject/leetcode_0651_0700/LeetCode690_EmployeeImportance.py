'''
Created on Oct 24, 2017

@author: MT
'''
"""
# Employee info
class Employee(object
    ___ __init__(self, id, importance, subordinates
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object
    ___ getImportance(self, employees, id
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        hashmap = {}
        for emp in employees:
            hashmap[emp.id] = hashmap.get(emp.id, []) + [emp]
        queue = []
        for emp in employees:
            __ emp.id __ id:
                queue.append(emp)
        res = 0
        w___ queue:
            emp = queue.pop(0)
            subs = emp.subordinates
            res += emp.importance
            for sub in subs:
                queue += hashmap.get(sub, [])
        r_ res
