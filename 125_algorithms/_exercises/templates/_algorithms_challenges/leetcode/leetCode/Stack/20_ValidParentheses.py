#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ isValid  s
        """
        :type s: str
        :rtype: bool
        """
        parenthes_stack   # list
        match_rule = {")": "(", "]": "[", "}": "{"}
        ___ symble __ s:
            __ symble __ "(" or symble __ "[" or symble __ "{":
                parenthes_stack.a.. symble)

            ____
                # Check if stack top matches the current ), ] or }.
                __ (parenthes_stack a..
                        parenthes_stack[-1] __ match_rule[symble]
                    parenthes_stack.pop()
                ____
                    r_ False
        # Have some symbles that is not matched.
        __ parenthes_stack:
            r_ False

        r_ True

"""
""
"["
"()()()()[]"
"()((()){})"
"""
