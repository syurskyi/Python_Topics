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
    ___ canFinish  numCourses, prerequisites
        course_req_dict _ # dict
        # pre_count: the num of one node's incoming edges.
        pre_count = [0] * numCourses
        ___ edge __ prerequisites:
            __ edge[1] n.. __ course_req_dict:
                course_req_dict[edge[1]] = [edge[0]]
            ____
                course_req_dict[edge[1]].a.. edge[0])
            pre_count[edge[0]] += 1

        # Keep nodes which have no incoming edges.
        available = [i ___ i, v __ enumerate(pre_count) __ v __ 0]
        _____ available:
            course = available[0]
            del available[0]

            ___ post_course __ course_req_dict.get(course, []
                pre_count[post_course] -= 1
                __ pre_count[post_course] __ 0:
                    available.a.. post_course)
        r_ s..(pre_count) __ 0

"""
1
[]
10
[[1,2],[3,4],[4,5],[5,6],[5,8],[5,9]]
10
[[1,2],[3,4],[4,5],[5,6],[5,8],[6,4]]
"""
