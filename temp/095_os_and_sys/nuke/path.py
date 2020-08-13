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

____ snitcher ______ snitch
snitch()

______ fnmatch
______ glob
______ __
______ shutil
______ ___

__all__ _ ['path']
__version__ _ '2.0.4'

# Universal newline support
_textmode _ 'r'
__ hasattr(file, 'newlines'):
    _textmode _ 'U'

# Use unicode strings __ possible
_base _ str
__ __.path.supports_unicode_filenames:
    _base _ unicode


c_ path(_base):
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
        __ no. args:
            r_ typ(__.curdir)
        ___ arg __ args:
            __ no. isinstance(arg, basestring):
                r_ ValueError("%s() arguments must be Path, str or "
                                 "unicode" % typ. -n)
        __ le.(args) __ 1:
            r_ _base.__new__(typ, *args)
        r_ typ(__.path.j..(*args))

    ___ __repr__
        r_ '%s(%r)' % (__class__. -n, _base())

    # Adding a path and a string yields a path.
    ___ __add__(, more):
        r_ __class__(_base() + more)

    ___ __radd__(, other):
        r_ __class__(other + _base())

    ??
    ___ cwd(cls):
        """ Return the current working directory as a path object. """
        r_ path(__.getcwd())

    # --- Operations on path strings.

    ___ abspath
        r_ __class__(__.path.abspath())

    ___ normcase
        r_ __class__(__.path.normcase())

    ___ normpath
        r_ __class__(__.path.normpath())

    ___ realpath
        r_ __class__(__.path.realpath())

    ___ expanduser
        r_ __class__(__.path.expanduser())

    ___ expandvars
        r_ __class__(__.path.expandvars())

    ___ expand
        """ Clean up a filename by calling expandvars(),
        expanduser(), and normpath() on it.

        This is commonly everything needed to clean up a filename
        read from a configuration file, for example.
        """
        r_ expandvars().expanduser().normpath()

    ___ _get_namebase
        base, ext _ __.path.splitext(name)
        r_ base

    ___ _get_ext
        f, ext _ __.path.splitext(_base())
        r_ ext

    ___ _get_drive
        drive, r _ __.path.splitdrive()
        r_ __class__(drive)

    ___ _get_dirname
        r_ __class__(__.path.dirname())

    parent _ property(
        _get_dirname, N.., N..,
        """ This path's parent directory, as a new path object.

        For example, path('/usr/local/lib/libpython.so').parent == path('/usr/local/lib')
        """)

    name _ property(
        __.path.basename, N.., N..,
        """ The name of this file or directory without the full path.

        For example, path('/usr/local/lib/libpython.so').name == 'libpython.so'
        """)

    namebase _ property(
        _get_namebase, N.., N..,
        """ The same as path.name, but with one file extension stripped off.

        For example, path('/home/guido/python.tar.gz').name     == 'python.tar.gz',
        but          path('/home/guido/python.tar.gz').namebase == 'python.tar'
        """)

    ext _ property(
        _get_ext, N.., N..,
        """ The file extension, for example '.py'. """)

    drive _ property(
        _get_drive, N.., N..,
        """ The drive specifier, for example 'C:'.
        This is always empty on systems that don't use drive specifiers.
        """)


    ___ splitpath
        """ p.splitpath() -> Return (p.parent, p.name). """
        parent, child _ __.path.split()
        r_ __class__(parent), child

    ___ stripext
        """ p.stripext() -> Remove one file extension from the path.

        For example, path('/home/guido/python.tar.gz').stripext()
        returns path('/home/guido/python.tar').
        """
        r_ path(__.path.splitext()[0])

    __ hasattr(__.path, 'splitunc'):
        ___ splitunc
            unc, rest _ __.path.splitunc()
            r_ __class__(unc), rest

        ___ _get_uncshare
            unc, r _ __.path.splitunc()
            r_ __class__(unc)

        uncshare _ property(
            _get_uncshare, N.., N..,
            """ The UNC mount point for this path.
            This is empty for paths on local drives. """)

    ___ splitall
        """ Return a list of the path components in this path.

        The first item in the list will be a path.  Its value will be
        either os.curdir, os.pardir, empty, or the root directory of
        this path (for example, '/' or 'C:\\').  The other items in
        the list will be strings.

        path.path(*result) will yield the original path.
        """
        parts _ []
        loc _
        while loc !_ __.curdir and loc !_ __.pardir:
            prev _ loc
            loc, child _ prev.splitpath()
            loc _ __class__(loc)
            __ loc __ prev:
                b..
            parts.ap..(child)
        parts.ap..(loc)
        parts.reverse()
        r_ parts

    ___ relpath
        """ Return this path as a relative path,
        based from the current working directory.
        """
        r_ __class__.cwd().relpathto()


    ___ relpathto(, dest):
        """ Return a relative path from self to dest.

        If there is no relative path from self to dest, for example __
        they reside on different drives in Windows, then this returns
        dest.abspath().
        """
        origin _ abspath()
        dest _ __class__(dest).abspath()

        orig_list _ origin.normcase().splitall()
        # Don't normcase dest!  We want to preserve the case.
        dest_list _ dest.splitall()

        __ orig_list[0] !_ __.path.normcase(dest_list[0]):
            # Can't get here from there.
            r_ dest

        # Find the location where the two paths start to differ.
        i _ 0
        ___ start_seg, dest_seg __ zip(orig_list, dest_list):
            __ start_seg !_ __.path.normcase(dest_seg):
                b..
            i +_ 1

        # Now i is the point where the two paths diverge.
        # Need a certain number of "os.pardir"s to work up
        # from the origin to the point of divergence.
        segments _ [__.pardir] * (le.(orig_list) - i)
        # Need to add the diverging part of dest_list.
        segments +_ dest_list[i:]
        __ le.(segments) __ 0:
            # If they happen to be identical, use os.curdir.
            r_ __class__(__.curdir)
        ____
            r_ __class__(__.path.j..(*segments))


    # --- Listing, searching, walking, and matching

    ___ listdir(, pattern_None):
        """ D.listdir() -> List of items in this directory.

        Use D.files() or D.dirs() instead __ you want a listing
        of just files or just subdirectories.

        The elements of the list are path objects.

        With the optional 'pattern' argument, this only lists
        items whose names match the given pattern.
        """
        names _ __.listdir()
        __ pattern is no. N..:
            names _ fnmatch.filter(names, pattern)
        r_ [path(, child) ___ child __ names]

    ___ dirs(, pattern_None):
        """ D.dirs() -> List of this directory's subdirectories.

        The elements of the list are path objects.
        This does not walk recursively into subdirectories
        (but see path.walkdirs).

        With the optional 'pattern' argument, this only lists
        directories whose names match the given pattern.  For
        example, d.dirs('build-*').
        """
        r_ [p ___ p __ listdir(pattern) __ p.isdir()]

    ___ files(, pattern_None):
        """ D.files() -> List of the files in this directory.

        The elements of the list are path objects.
        This does not walk into subdirectories (see path.walkfiles).

        With the optional 'pattern' argument, this only lists files
        whose names match the given pattern.  For example,
        d.files('*.pyc').
        """

        r_ [p ___ p __ listdir(pattern) __ p.isfile()]

    ___ walk(, pattern_None):
        """ D.walk() -> iterator over files and subdirs, recursively.

        The iterator yields path objects naming each child item of
        this directory and its descendants.  This requires that
        D.isdir().

        This performs a depth-first traversal of the directory tree.
        Each directory is returned just before all its children.
        """
        ___ child __ listdir():
            __ pattern is N.. or child.match(pattern):
                yield child
            __ child.isdir():
                ___ item __ child.walk(pattern):
                    yield item

    ___ walkdirs(, pattern_None):
        """ D.walkdirs() -> iterator over subdirs, recursively.

        With the optional 'pattern' argument, this yields only
        directories whose names match the given pattern.  For
        example, mydir.walkdirs('*test') yields only directories
        with names ending in 'test'.
        """
        ___ child __ dirs():
            __ pattern is N.. or child.match(pattern):
                yield child
            ___ subsubdir __ child.walkdirs(pattern):
                yield subsubdir


    ___ walkfiles(, pattern_None):
        """ D.walkfiles() -> iterator over files in D, recursively.

        The optional argument, pattern, limits the results to files
        with names that match the pattern.  For example,
        mydir.walkfiles('*.tmp') yields only files with the .tmp
        extension.
        """
        ___ child __ listdir():
            __ child.isfile():
                __ pattern is N.. or child.match(pattern):
                    yield child
            ____ child.isdir():
                ___ f __ child.walkfiles(pattern):
                    yield f

    ___ match(, pattern):
        """ Return True __ self.name matches the given pattern.

        pattern - A filename pattern with wildcards,
            for example '*.py'.
        """
        r_ fnmatch.fnmatch(name, pattern)

    ___ matchcase(, pattern):
        """ Test whether the path matches pattern, returning true or
        false; the comparison is always case-sensitive.
        """
        r_ fnmatch.fnmatchcase(name, pattern)

    ___ glob(, pattern):
        """ Return a list of path objects that match the pattern.

        pattern - a path relative to this directory, with wildcards.

        For example, path('/users').glob('*/bin/*') returns a list
        of all the files users have in their bin directories.
        """
        r_ map(path, glob.glob(_base(path(, pattern))))

    # --- Methods for querying the filesystem.

    exists _ __.path.exists
    isabs _ __.path.isabs
    isdir _ __.path.isdir
    isfile _ __.path.isfile
    islink _ __.path.islink
    ismount _ __.path.ismount

    __ hasattr(__.path, 'samefile'):
        samefile _ __.path.samefile

    ___ atime
        """Last access time of the file."""
        r_ __.path.getatime()


    ___ mtime
        """Last-modified time of the file."""
        r_ __.path.getmtime()

    ___ ctime
        """
        Return the system's ctime which, on some systems (like Unix)
        is the time of the last change, and, on others (like Windows),
        is the creation time for path.

        The return value is a number giving the number of seconds
        since the epoch (see the time module). Raise os.error __ the
        file does not exist or is inaccessible.
        """
        r_ __.path.getctime()

    ___ size
        """Size of the file, in bytes."""
        r_ __.path.getsize()

    __ hasattr(__, 'access'):
        ___ access(, mode):
            """ Return true __ current user has access to this path.

            mode - One of the constants os.F_OK, os.R_OK, os.W_OK, os.X_OK
            """
            r_ __.access(, mode)

    ___ stat
        """ Perform a stat() system call on this path. """
        r_ __.stat()

    ___ lstat
        """ Like path.stat(), but do not follow symbolic links. """
        r_ __.lstat()

    __ hasattr(__, 'statvfs'):
        ___ statvfs
            """ Perform a statvfs() system call on this path. """
            r_ __.statvfs()

    __ hasattr(__, 'pathconf'):
        ___ pathconf(, name):
            r_ __.pathconf(, name)


    # --- Modifying operations on files and directories

    ___ utime(, times):
        """ Set the access and modified times of this file. """
        __.utime(, times)

    ___ chmod(, mode):
        __.chmod(, mode)

    __ hasattr(__, 'chown'):
        ___ chown(, uid, gid):
            __.chown(, uid, gid)


    ___ rename(, new):
        __.rename(, new)

    ___ renames(, new):
        __.renames(, new)


    # --- Create/delete operations on directories

    ___ mkdir(, mode_0777):
        __.mkdir(, mode)

    ___ makedirs(, mode_0777):
        __.makedirs(, mode)

    ___ rmdir
        __.rmdir()

    ___ removedirs
        __.removedirs()


    # --- Modifying operations on files

    ___ touch
        """ Set the access/modified times of this file to the current time.
        Create the file __ it does not exist.
        """
        fd _ __.o..(, __.O_WRONLY | __.O_CREAT, 0666)
        __.close(fd)
        __.utime(, N..)

    ___ remove
        __.remove()

    ___ unlink
        __.unlink()


    # --- Links

    __ hasattr(__, 'link'):
        ___ link(, newpath):
            """ Create a hard link at 'newpath', pointing to this file. """
            __.link(, newpath)

    __ hasattr(__, 'symlink'):
        ___ symlink(, newlink):
            """ Create a symbolic link at 'newlink', pointing here. """
            __.symlink(, newlink)


    __ hasattr(__, 'readlink'):
        ___ readlink
            """ Return the path to which this symbolic link points.

            The result may be an absolute or a relative path.
            """
            r_ __class__(__.readlink())

        ___ readlinkabs
            """ Return the path to which this symbolic link points.

            The result is always an absolute path.
            """
            p _ readlink()
            __ p.isabs():
                r_ p
            ____
                r_ __class__(parent, p).abspath()


    # --- High-level functions from shutil

    copyfile _ shutil.copyfile
    copymode _ shutil.copymode
    copystat _ shutil.copystat
    copy _ shutil.copy
    copy2 _ shutil.copy2
    copytree _ shutil.copytree
    __ hasattr(shutil, 'move'):
        move _ shutil.move
    rmtree _ shutil.rmtree


    # --- Special stuff from os

    __ hasattr(__, 'chroot'):
        ___ chroot
            __.chroot()
