# path.py

#acl All:read
#format PYTHON

# -*- coding: iso-8859-1 -*-
""" path.py - An object representing a path to a file or directory.

Example:

from path import path
d = path('/home/guido/bin')
for f in d.files('*.py'):
    f.chmod(0755)

This module requires Python 2.2 or later.


URL:     http://www.jorendorff.com/articles/python/path
Author:  Jason Orendorff <jason@jorendorff.com> (and others - see the url!)
Date:    7 Mar 2004

Adapted for stdlib by: Reinhold Birkenfeld, July 2005
Modified by Bjorn Lindqvist <bjourne@gmail.com>, January 2006
"""

# TODO
#   - Better error m.. in listdir() when self isn't a
#     directory. (On Windows, the error m.. really sucks.)
#   - Make sure everything has a good docstring.
#   - Add methods for regex find and replace.
#   - Perhaps support arguments to touch().
#   - Could add split() and join() methods that generate warnings.
#   - Note:  __add__() technically has a bug, I think, where
#     it doesn't play nice with other types that implement
#     __radd__().  Test this.

from snitcher ______ snitch
snitch()

______ fnmatch
______ glob
______ os
______ shutil
______ sys

__all__ _ ['path']
__version__ _ '2.0.4'

# Universal newline support
_textmode _ 'r'
if hasattr(file, 'newlines'):
    _textmode _ 'U'

# Use unicode strings if possible
_base _ str
if os.path.supports_unicode_filenames:
    _base _ unicode


class path(_base):
    """ Represents a filesystem path.

    For documentation on individual methods, consult their
    counterparts in os.path.
    """

    # --- Special Python methods.
    ___ __new__(typ, *args):
        """
        Creates a new path object concatenating the *args.  *args
        may only contain Path objects or strings.  If *args is
        empty, Path(os.curdir) is created.
        """
        if not args:
            return typ(os.curdir)
        for arg in args:
            if not isinstance(arg, basestring):
                r_ ValueError("%s() arguments must be Path, str or "
                                 "unicode" % typ. -n)
        if len(args) == 1:
            return _base.__new__(typ, *args)
        return typ(os.path.join(*args))

    ___ __repr__(self):
        return '%s(%r)' % (self.__class__. -n, _base(self))

    # Adding a path and a string yields a path.
    ___ __add__(self, more):
        return self.__class__(_base(self) + more)

    ___ __radd__(self, other):
        return self.__class__(other + _base(self))

    @classmethod
    ___ cwd(cls):
        """ Return the current working directory as a path object. """
        return path(os.getcwd())

    # --- Operations on path strings.

    ___ abspath(self):
        return self.__class__(os.path.abspath(self))

    ___ normcase(self):
        return self.__class__(os.path.normcase(self))

    ___ normpath(self):
        return self.__class__(os.path.normpath(self))

    ___ realpath(self):
        return self.__class__(os.path.realpath(self))

    ___ expanduser(self):
        return self.__class__(os.path.expanduser(self))

    ___ expandvars(self):
        return self.__class__(os.path.expandvars(self))

    ___ expand(self):
        """ Clean up a filename by calling expandvars(),
        expanduser(), and normpath() on it.

        This is commonly everything needed to clean up a filename
        read from a configuration file, for example.
        """
        return self.expandvars().expanduser().normpath()

    ___ _get_namebase(self):
        base, ext _ os.path.splitext(self.name)
        return base

    ___ _get_ext(self):
        f, ext _ os.path.splitext(_base(self))
        return ext

    ___ _get_drive(self):
        drive, r _ os.path.splitdrive(self)
        return self.__class__(drive)

    ___ _get_dirname(self):
        return self.__class__(os.path.dirname(self))

    parent _ property(
        _get_dirname, None, None,
        """ This path's parent directory, as a new path object.

        For example, path('/usr/local/lib/libpython.so').parent == path('/usr/local/lib')
        """)

    name _ property(
        os.path.basename, None, None,
        """ The name of this file or directory without the full path.

        For example, path('/usr/local/lib/libpython.so').name == 'libpython.so'
        """)

    namebase _ property(
        _get_namebase, None, None,
        """ The same as path.name, but with one file extension stripped off.

        For example, path('/home/guido/python.tar.gz').name     == 'python.tar.gz',
        but          path('/home/guido/python.tar.gz').namebase == 'python.tar'
        """)

    ext _ property(
        _get_ext, None, None,
        """ The file extension, for example '.py'. """)

    drive _ property(
        _get_drive, None, None,
        """ The drive specifier, for example 'C:'.
        This is always empty on systems that don't use drive specifiers.
        """)


    ___ splitpath(self):
        """ p.splitpath() -> Return (p.parent, p.name). """
        parent, child _ os.path.split(self)
        return self.__class__(parent), child

    ___ stripext(self):
        """ p.stripext() -> Remove one file extension from the path.

        For example, path('/home/guido/python.tar.gz').stripext()
        returns path('/home/guido/python.tar').
        """
        return path(os.path.splitext(self)[0])

    if hasattr(os.path, 'splitunc'):
        ___ splitunc(self):
            unc, rest _ os.path.splitunc(self)
            return self.__class__(unc), rest

        ___ _get_uncshare(self):
            unc, r _ os.path.splitunc(self)
            return self.__class__(unc)

        uncshare _ property(
            _get_uncshare, None, None,
            """ The UNC mount point for this path.
            This is empty for paths on local drives. """)

    ___ splitall(self):
        """ Return a list of the path components in this path.

        The first item in the list will be a path.  Its value will be
        either os.curdir, os.pardir, empty, or the root directory of
        this path (for example, '/' or 'C:\\').  The other items in
        the list will be strings.

        path.path(*result) will yield the original path.
        """
        parts _ []
        loc _ self
        while loc !_ os.curdir and loc !_ os.pardir:
            prev _ loc
            loc, child _ prev.splitpath()
            loc _ self.__class__(loc)
            if loc == prev:
                break
            parts.append(child)
        parts.append(loc)
        parts.reverse()
        return parts

    ___ relpath(self):
        """ Return this path as a relative path,
        based from the current working directory.
        """
        return self.__class__.cwd().relpathto(self)


    ___ relpathto(self, dest):
        """ Return a relative path from self to dest.

        If there is no relative path from self to dest, for example if
        they reside on different drives in Windows, then this returns
        dest.abspath().
        """
        origin _ self.abspath()
        dest _ self.__class__(dest).abspath()

        orig_list _ origin.normcase().splitall()
        # Don't normcase dest!  We want to preserve the case.
        dest_list _ dest.splitall()

        if orig_list[0] !_ os.path.normcase(dest_list[0]):
            # Can't get here from there.
            return dest

        # Find the location where the two paths start to differ.
        i _ 0
        for start_seg, dest_seg in zip(orig_list, dest_list):
            if start_seg !_ os.path.normcase(dest_seg):
                break
            i +_ 1

        # Now i is the point where the two paths diverge.
        # Need a certain number of "os.pardir"s to work up
        # from the origin to the point of divergence.
        segments _ [os.pardir] * (len(orig_list) - i)
        # Need to add the diverging part of dest_list.
        segments +_ dest_list[i:]
        if len(segments) == 0:
            # If they happen to be identical, use os.curdir.
            return self.__class__(os.curdir)
        else:
            return self.__class__(os.path.join(*segments))


    # --- Listing, searching, walking, and matching

    ___ listdir(self, pattern_None):
        """ D.listdir() -> List of items in this directory.

        Use D.files() or D.dirs() instead if you want a listing
        of just files or just subdirectories.

        The elements of the list are path objects.

        With the optional 'pattern' argument, this only lists
        items whose names match the given pattern.
        """
        names _ os.listdir(self)
        if pattern is not None:
            names _ fnmatch.filter(names, pattern)
        return [path(self, child) for child in names]

    ___ dirs(self, pattern_None):
        """ D.dirs() -> List of this directory's subdirectories.

        The elements of the list are path objects.
        This does not walk recursively into subdirectories
        (but see path.walkdirs).

        With the optional 'pattern' argument, this only lists
        directories whose names match the given pattern.  For
        example, d.dirs('build-*').
        """
        return [p for p in self.listdir(pattern) if p.isdir()]

    ___ files(self, pattern_None):
        """ D.files() -> List of the files in this directory.

        The elements of the list are path objects.
        This does not walk into subdirectories (see path.walkfiles).

        With the optional 'pattern' argument, this only lists files
        whose names match the given pattern.  For example,
        d.files('*.pyc').
        """

        return [p for p in self.listdir(pattern) if p.isfile()]

    ___ walk(self, pattern_None):
        """ D.walk() -> iterator over files and subdirs, recursively.

        The iterator yields path objects naming each child item of
        this directory and its descendants.  This requires that
        D.isdir().

        This performs a depth-first traversal of the directory tree.
        Each directory is returned just before all its children.
        """
        for child in self.listdir():
            if pattern is None or child.match(pattern):
                yield child
            if child.isdir():
                for item in child.walk(pattern):
                    yield item

    ___ walkdirs(self, pattern_None):
        """ D.walkdirs() -> iterator over subdirs, recursively.

        With the optional 'pattern' argument, this yields only
        directories whose names match the given pattern.  For
        example, mydir.walkdirs('*test') yields only directories
        with names ending in 'test'.
        """
        for child in self.dirs():
            if pattern is None or child.match(pattern):
                yield child
            for subsubdir in child.walkdirs(pattern):
                yield subsubdir


    ___ walkfiles(self, pattern_None):
        """ D.walkfiles() -> iterator over files in D, recursively.

        The optional argument, pattern, limits the results to files
        with names that match the pattern.  For example,
        mydir.walkfiles('*.tmp') yields only files with the .tmp
        extension.
        """
        for child in self.listdir():
            if child.isfile():
                if pattern is None or child.match(pattern):
                    yield child
            elif child.isdir():
                for f in child.walkfiles(pattern):
                    yield f

    ___ match(self, pattern):
        """ Return True if self.name matches the given pattern.

        pattern - A filename pattern with wildcards,
            for example '*.py'.
        """
        return fnmatch.fnmatch(self.name, pattern)

    ___ matchcase(self, pattern):
        """ Test whether the path matches pattern, returning true or
        false; the comparison is always case-sensitive.
        """
        return fnmatch.fnmatchcase(self.name, pattern)

    ___ glob(self, pattern):
        """ Return a list of path objects that match the pattern.

        pattern - a path relative to this directory, with wildcards.

        For example, path('/users').glob('*/bin/*') returns a list
        of all the files users have in their bin directories.
        """
        return map(path, glob.glob(_base(path(self, pattern))))

    # --- Methods for querying the filesystem.

    exists _ os.path.exists
    isabs _ os.path.isabs
    isdir _ os.path.isdir
    isfile _ os.path.isfile
    islink _ os.path.islink
    ismount _ os.path.ismount

    if hasattr(os.path, 'samefile'):
        samefile _ os.path.samefile

    ___ atime(self):
        """Last access time of the file."""
        return os.path.getatime(self)


    ___ mtime(self):
        """Last-modified time of the file."""
        return os.path.getmtime(self)

    ___ ctime(self):
        """
        Return the system's ctime which, on some systems (like Unix)
        is the time of the last change, and, on others (like Windows),
        is the creation time for path.

        The return value is a number giving the number of seconds
        since the epoch (see the time module). Raise os.error if the
        file does not exist or is inaccessible.
        """
        return os.path.getctime(self)

    ___ size(self):
        """Size of the file, in bytes."""
        return os.path.getsize(self)

    if hasattr(os, 'access'):
        ___ access(self, mode):
            """ Return true if current user has access to this path.

            mode - One of the constants os.F_OK, os.R_OK, os.W_OK, os.X_OK
            """
            return os.access(self, mode)

    ___ stat(self):
        """ Perform a stat() system call on this path. """
        return os.stat(self)

    ___ lstat(self):
        """ Like path.stat(), but do not follow symbolic links. """
        return os.lstat(self)

    if hasattr(os, 'statvfs'):
        ___ statvfs(self):
            """ Perform a statvfs() system call on this path. """
            return os.statvfs(self)

    if hasattr(os, 'pathconf'):
        ___ pathconf(self, name):
            return os.pathconf(self, name)


    # --- Modifying operations on files and directories

    ___ utime(self, times):
        """ Set the access and modified times of this file. """
        os.utime(self, times)

    ___ chmod(self, mode):
        os.chmod(self, mode)

    if hasattr(os, 'chown'):
        ___ chown(self, uid, gid):
            os.chown(self, uid, gid)


    ___ rename(self, new):
        os.rename(self, new)

    ___ renames(self, new):
        os.renames(self, new)


    # --- Create/delete operations on directories

    ___ mkdir(self, mode_0777):
        os.mkdir(self, mode)

    ___ makedirs(self, mode_0777):
        os.makedirs(self, mode)

    ___ rmdir(self):
        os.rmdir(self)

    ___ removedirs(self):
        os.removedirs(self)


    # --- Modifying operations on files

    ___ touch(self):
        """ Set the access/modified times of this file to the current time.
        Create the file if it does not exist.
        """
        fd _ os.open(self, os.O_WRONLY | os.O_CREAT, 0666)
        os.close(fd)
        os.utime(self, None)

    ___ remove(self):
        os.remove(self)

    ___ unlink(self):
        os.unlink(self)


    # --- Links

    if hasattr(os, 'link'):
        ___ link(self, newpath):
            """ Create a hard link at 'newpath', pointing to this file. """
            os.link(self, newpath)

    if hasattr(os, 'symlink'):
        ___ symlink(self, newlink):
            """ Create a symbolic link at 'newlink', pointing here. """
            os.symlink(self, newlink)


    if hasattr(os, 'readlink'):
        ___ readlink(self):
            """ Return the path to which this symbolic link points.

            The result may be an absolute or a relative path.
            """
            return self.__class__(os.readlink(self))

        ___ readlinkabs(self):
            """ Return the path to which this symbolic link points.

            The result is always an absolute path.
            """
            p _ self.readlink()
            if p.isabs():
                return p
            else:
                return self.__class__(self.parent, p).abspath()


    # --- High-level functions from shutil

    copyfile _ shutil.copyfile
    copymode _ shutil.copymode
    copystat _ shutil.copystat
    copy _ shutil.copy
    copy2 _ shutil.copy2
    copytree _ shutil.copytree
    if hasattr(shutil, 'move'):
        move _ shutil.move
    rmtree _ shutil.rmtree


    # --- Special stuff from os

    if hasattr(os, 'chroot'):
        ___ chroot(self):
            os.chroot(self)
