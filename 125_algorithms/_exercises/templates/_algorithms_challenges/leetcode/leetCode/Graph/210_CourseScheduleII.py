#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    """
    Topological Sort:
    1. Find a "start nodes" which have no incoming edges;
    2. delete the node, update the graph. Then goto 1
    If all the nodes can be deleted, then can finish the course.
    """
    ___ findOrder  numCourses, prerequisites
        edges_hash = {i: [] ___ i __ r..(numCourses)}
        in_degree = [0] * numCourses
        ___ edge __ prerequisites:
            edges_hash[edge[1]].append(edge[0])
            in_degree[edge[0]] += 1

        correct_orders   # list
        availables = [i ___ i, v __ enumerate(in_degree) __ v __ 0]
        _____ availables:
            course = availables[0]
            correct_orders.append(course)
            del availables[0]
            ___ co __ edges_hash[course]:
                in_degree[co] -= 1
                __ in_degree[co] __ 0:
                    availables.append(co)
        __ n.. s..(in_degree
            r_ correct_orders
        ____
            r_ []

__ __name__ __ '__main__':
    sol = Solution()
    print sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    print sol.findOrder(4, [[1, 0], [2, 0], [0, 1], [3, 2]])
