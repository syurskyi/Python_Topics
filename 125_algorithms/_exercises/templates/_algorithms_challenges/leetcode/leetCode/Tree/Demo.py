#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-08-21 09:49:20


___ inorderTraversal  root
    tree_stack   # list
    inorder_tra   # list
    _____ root or tree_stack:
        # Go along the left child
        __ root:
            tree_stack.append(root)
            root = root.left
        # Meet a left, go back to the parent node
        ____
            node = tree_stack.pop()
            inorder_tra.append(node.val)
            root = node.right

    r_ inorder_tra
