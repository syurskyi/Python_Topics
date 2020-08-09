class Solution:
    # @param path, a string
    # @return a string
    ___ simplifyPath(self, path
        ps = path.split('/')[1:]
        res = []
        ___ d in ps:
            __ d __ '..':
                __ res:
                    res.pop()
            ____ d __ '.' or d __ '':
                pass
            ____
                res.append(d)
        r_ '/' + '/'.join(res)
