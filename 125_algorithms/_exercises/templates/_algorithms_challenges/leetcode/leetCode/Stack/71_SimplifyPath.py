#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ simplifyPath  path
        """
        :type path: str
        :rtype: str
        """
        __ n.. path:
            r_ "/"

        stack   # list
        path_str = ""
        index = 0
        _____ index < l..(path
            char = path[index]
            __ char __ "/":
                # './' respresent current directory
                __ path_str __ "." or path_str __ "":
                    path_str = ""

                # '../' represent parent directory
                ____ path_str __ "..":
                    __ stack:
                        stack.pop()
                    path_str = ""

                # 'path/': push path to stack
                ____
                    stack.a.. path_str)
                    path_str = ""
            ____
                path_str += char
            index += 1

        # Append the last path
        __ path_str __ "..":
            __ stack:
                stack.pop()
        ____ path_str __ "." or path_str __ "":
            pass
        ____
            stack.a.. path_str)
        r_ "/" + "/".join(stack)

"""
""
"/"
"/.."
"/home.as//"
"/home.as"
"/a/./b/../../c/"
"/a/./b/../../c/../"
"/a/./b/c/../.."
"/..."
"""
