"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""
__author__ = 'Danyang'


c_ Solution(o..
    ___ simplifyPath  p..
        """
        use "." as intermediate

        :param path: a string
        :return: a string
        """
        p.. = p...s..("/")
        p.. = f.. l.... x: x n.. __ ("", " ", "."), p..)

        # modify the content of the list, not the structure.
        ___ idx __ x..(l..(p..:
            val = p..[idx]
            __ val __ "..":
                p..[idx] = "."

                # rm a previous meaningful part
                i = idx-1
                w.... i >_ 0 a.. p..[i] __ ".": i -_ 1
                __ i >_ 0: p..[i] = "."  # avoid path[-1]

        p.. = f.. l.... x: x n.. __ (".",), p..)

        __ n.. p..:
            r.. "/"

        p.. = map(l.... x: "/"+x, p..)
        r.. "".j..(p..)


__ _______ __ _______
    ... Solution().simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///") __ "/e/f/g"
    ... Solution().simplifyPath("/a/./b/../../c/") __ "/c"
    ... Solution().simplifyPath("/../") __ "/"