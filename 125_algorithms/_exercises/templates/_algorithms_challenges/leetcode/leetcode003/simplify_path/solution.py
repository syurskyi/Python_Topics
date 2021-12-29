class Solution:
    # @param path, a string
    # @return a string
    ___ simplifyPath(self, path):
        ps = path.split('/')[1:]
        res = []
        for d in ps:
            __ d == '..':
                __ res:
                    res.pop()
            elif d == '.' or d == '':
                pass
            else:
                res.append(d)
        return '/' + '/'.join(res)
