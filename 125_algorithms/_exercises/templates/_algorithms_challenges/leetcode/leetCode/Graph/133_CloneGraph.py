#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

c.. Solution o..
    ___ cloneGraph  node
        __ n.. node:
            r_ None

        copyed_node_pair _ # dict
        copy_head = UndirectedGraphNode(node.label)
        copy_head.neighbors   # list
        copyed_node_pair[node] = copy_head

        nodes_stack   # list
        nodes_stack.append(node)
        _____ nodes_stack:
            one_node = nodes_stack.pop()

            ___ neighbor __ one_node.neighbors:
                __ neighbor n.. __ copyed_node_pair:
                    copy_node = UndirectedGraphNode(neighbor.label)
                    copy_node.neighbors   # list
                    copyed_node_pair[neighbor] = copy_node
                    nodes_stack.append(neighbor)

                copyed_node_pair[one_node].neighbors.append(
                    copyed_node_pair[neighbor])

        r_ copy_head

"""
{0,0,0}
{0,1,2#1,2#2,2}
"""
