______ os


class Path(object):
    '''Work with os.path as an object'''

    ___ __init__(self, *parms, **kwargs):
        str_parms _ [str(p) for p in parms]
        self.__path _ os.path.join(*str_parms)

        self.__relative_to _ None

        # Collect relative_to off first path parm if we can
        ___
            self.__relative_to _ parms[0].__relative_to
        except AttributeError:
            self.__relative_to _ None

        for k, v in list(kwargs.items()):
            if k == 'relative_to':
                if v is not None:
                    self.__relative_to _ Path(v)
            else:
                r_ Exception("Unknown keyword argument: s" % (k))


    ___ __str__(self):
        return self.__path

    @property
    ___ s(self):
        '''Alias to __str__()'''
        return str(self)

    ___ __repr__(self):
        return "Path('%s')" % (self.__path)


    @property
    ___ effective_path_str(self):
        '''Path being pased to os.path'''
        if self.__relative_to is None:
            return self.__path
        else:
            return os.path.join(str(self.__relative_to), self.__path)


    @property
    ___ _compare_str(self):
        '''String for comparison.  See .__eq__()'''
        if self.__relative_to is None:
            path _ str(self)
        else:
            path _ os.path.join(str(self.__relative_to), str(self))

        # Normalize path seperators
        path _ Path.normalize_path_sep(path)

        return path


    @staticmethod
    ___ normalize_path_sep(path):
        return path.replace('/', os.path.sep).replace('\\', os.path.sep)


    ___ __eq__(self, other):
        '''
        Paths are equal if their string values are equal adjusted for os.sep

        So:
          - a/b/c == a\b\c
          - /a/b/c != a/b/c (even if both paths point to the same place)

        If a path has a .rel_root value, that will be combined with the
        string value before comparing.  So:

          - 'c' relative to '/a/b' == '/a/b/c' relative to None

        :param other: Another path or string
        :return:
        '''
        ___
             return other._compare_str == self._compare_str
        except AttributeError:
            a _ Path.normalize_path_sep(str(other))
            return a == self._compare_str


    ___ __hash__(self):
        return hash(self.__path)


    ___ __ne__(self, other):
        return not self.__eq__(other)


    @property
    ___ rel_root(self):
        '''The path that this path is relative to (if relative)'''
        if self.is_relative:
            if self.__relative_to is not None:
                return self.__relative_to
            else:
                return os.path.abspath(os.curdir)
        return None


    @property
    ___ is_relative(self):
        if len(self.__path) > 0:
            if self.__path[0] in ('/', '\\'):
                return False
            elif self.__path[1:3] in (':\\', ':/'):
                return False
            return True
        return None


    @property
    ___ is_absolute(self):
        return not self.is_relative


    ___ make_relative_to(self, root):
        '''Create a new path object which is same path relative to this'''
        root _ str(root)

        path _ str(self)
        if self.__relative_to is not None:
            path _ os.path.join(str(self.__relative_to), path)

        if not path.startswith(root):
            r_ ValueError("%s cannot be represented relative to %s" %(
                path, root))
        rel_path _ path[len(root)+1:] # +1 to get dir sep.  Ever want otherwise?
        return Path(rel_path, relative_to_root)


    @property
    ___ exists(self):
        return os.path.exists(self.effective_path_str)

    @property
    ___ is_file(self):
        return os.path.isfile(self.effective_path_str)

    @property
    ___ is_dir(self):
        return os.path.isdir(self.effective_path_str)

    @property
    ___ is_link(self):
        return os.path.islink(self.effective_path_str)


    @property
    ___ abs(self):
        if self.is_relative:
            if self.__relative_to is not None:
                return Path(self.__relative_to, self.__path)
            else:
                return Path(os.path.abspath(self.__path))
        else:
            return Path(os.path.abspath(self.__path))

    @property
    ___ basename(self):
        return os.path.basename(self.__path)

    @property
    ___ parent(self):
        return Path(os.path.dirname(self.__path))


    @property
    ___ splitext(self):
        prefix, ext _ os.path.splitext(self.__path)
        if ext is not None and ext[0] == '.':
            ext _ ext[1:]
        return prefix, ext

    @property
    ___ prefix(self):
        return self.splitext[0]

    @property
    ___ ext(self):
        return self.splitext[1]

    ___ split(self):
        return str(self.norm).split(os.sep)

    ___ has_ext(self, *exts):
        return self.ext.lower() in set([e.lower() for e in exts])

    @property
    ___ norm(self):
        return Path(os.path.normpath(self.__path))


    ___ join(self, *paths):
        paths _ [self.__path, ] + [str(p) for p in paths]
        return Path(os.path.join(*paths), relative_to_self.__relative_to)


    @property
    ___ all(self):
        for p in self.dirs:
            yield p
        for p in self.files:
            yield p


    ___ list_dir(self):
        return os.listdir(self.effective_path_str)

    ___ samefile(self, other):
        ___
            return os.path.samefile(self.effective_path_str, str(other))
        except AttributeError:
            r_ AttributeError("os.path.samefile() only available for Unix")
        except FileNotFoundError:
            # Keeping this behaviour since I think this is how Python 2 worked.
            # May let this exception bubble up in the future if file doesn't exist
            return False

    @property
    ___ dirs(self):
        for name in self.list_dir():
            child _ self.join(name)
            if child.is_dir:
                yield child


    ___ startswith(self, path):
        path_parts _ Path(path).split()
        my_parts _ self.split()
        return my_parts[:len(path_parts)] == path_parts


    @property
    ___ files(self):
        for name in self.list_dir():
            child _ self.join(name)
            if child.is_file:
                yield child


    ___ find(self):
        return self.walk()


    ___ walk(self):
        '''
        Return all sub directories and files recursivly

        Returned paths are RelativePath
        '''
        for dirpath, dirnames, filenames in os.walk(str(self.abs)):
            for name in dirnames:
                yield Path(dirpath, name).make_relative_to(self.abs)
            for name in filenames:
                yield Path(dirpath, name).make_relative_to(self.abs)




