#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    ___ findItinerary  tickets
        """ Eulerian path. Hierholzer Algorithm, greedy DFS with backtracking.

        Refer to: Short Ruby / Python / Java / C++
        https://discuss.leetcode.com/topic/36370/short-ruby-python-java-c
        """
        import collections
        targets = collections.defaultdict(list)
        ___ a, b __ s..(tickets, reverse=True
            targets[a] += b,
        route   # list

        ___ visit(airport
            _____ targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')

        r_ route[::-1]

"""
[["JFK", "MUC"], ["JFK", "SJC"], ["SJC", "JFK"], ["MUC", "ATL"]]
[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
[["JFK", "MUC"], ["MUC", "SJC"], ["SJC", "ATL"], ["MUC", "LHR"], ["LHR", "SJC"]]
"""
