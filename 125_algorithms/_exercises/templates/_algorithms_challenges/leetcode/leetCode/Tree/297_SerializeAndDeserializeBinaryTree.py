#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# The leetcode way
c.. Codec:
    ___ serialize  root
        data   # list
        node_queue = [root]
        start = 0
        _____ start < l..(node_queue
            node = node_queue[start]
            start += 1
            __ node:
                data.a.. str(node.val))
                node_queue.a.. node.left)
                node_queue.a.. node.right)
            ____
                data.a.. "null")
        # Remove the tail null node.
        _____ data a.. data[-1] __ "null":
            del data[-1]
        r_ ",".join(data)

    ___ deserialize  data
        __ n.. data:
            r_ None

        # Get all the nodes.
        data_list = data.split(",")
        length = l..(data_list)
        node_list = [0] * length
        ___ i __ r..(length
            __ data_list[i] __ "null":
                node_list[i] = None
            ____
                node_list[i] = TreeNode(int(data_list[i]))

        # Build the tree.
        offset = 1
        cur_pos = 0
        _____ offset < length:
            __ node_list[cur_pos]:
                node_list[cur_pos].left = node_list[offset]
                offset += 1
                __ offset < length:
                    node_list[cur_pos].right = node_list[offset]
                    offset += 1
                ____
                    ______
            ____
                pass
            cur_pos += 1

        r_ node_list[0]


c.. Codec_2:
    # Refer to: Recursive preorder, Python and C++, O(n)
    # https://leetcode.com/discuss/66147/recursive-preorder-python-and-c-o-n
    ___ serialize  root
        ___ helper(node
            __ node:
                vals.a.. str(node.val))
                helper(node.left)
                helper(node.right)
            ____
                vals.a.. '#')

        vals   # list
        helper(root)
        r_ ' '.join(vals)

    ___ deserialize  data
        ___ helper(
            val = next(vals)
            __ val __ '#':
                r_ None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            r_ node

        vals = iter(data.split())
        r_ helper()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))(codec.deserialize("1,null,3,4,5"))

"""
[]
[1,2,null,3,4]
[1,2,3,null,4,null,5,null,6,7]
"""
