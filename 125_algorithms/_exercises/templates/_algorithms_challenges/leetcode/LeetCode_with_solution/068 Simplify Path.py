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


c_ Solution(object):
    ___ simplifyPath(self, path):
        """
        use "." as intermediate

        :param path: a string
        :return: a string
        """
        path = path.s..("/")
        path = filter(l.... x: x n.. __ ("", " ", "."), path)

        # modify the content of the list, not the structure.
        ___ idx __ xrange(l..(path)):
            val = path[idx]
            __ val __ "..":
                path[idx] = "."

                # rm a previous meaningful part
                i = idx-1
                w.... i >= 0 a.. path[i] __ ".": i -= 1
                __ i >= 0: path[i] = "."  # avoid path[-1]

        path = filter(l.... x: x n.. __ (".",), path)

        __ n.. path:
            r.. "/"

        path = map(l.... x: "/"+x, path)
        r.. "".j..(path)


__ __name__ __ "__main__":
    ... Solution().simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///") __ "/e/f/g"
    ... Solution().simplifyPath("/a/./b/../../c/") __ "/c"
    ... Solution().simplifyPath("/../") __ "/"