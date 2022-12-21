c_ Solution o..
    ___ simplifyPath  path
        """
        :type path: str
        :rtype: str
        """
        result =    # list
        plist = path.split('/')
        ___ pos __ plist:
            __ pos:
                __ pos __ '..':
                    try:
                        # up one level
                        result.pop()
                    except:
                        # arrive top level
                        result =    # list
                ____ pos != '.':
                    result.append(pos)
        r_ '/'+'/'.join(result)