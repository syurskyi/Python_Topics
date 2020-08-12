npath - Nate's Path Library
===========================

**Work with os.path as Path objects.**

**NOTE:** For Python >= 3.4, you almost certainly want
[pathlib](https://docs.python.org/3/library/pathlib.html)

It seems like 50% of my development time is spent working with file paths.
This library is intended to make much of that path work a bit cleaner
by baking some of my common usage patterns of
[os.path](https://docs.python.org/2/library/os.path.html) right into the 
Path objects.  I'll also change a few of the names to ones that
I can remember easier.

Compatible with Python 2 and Python 3
(Tested with 2.7.10 and 3.3.2).


Key Classes
-----------

**Path** class is used to manipulate paths
 
**File** and **Directory** are used to work with the file system
objects.


Basic Usage
-----------

Setting a path value 

    from npath import Path
    path = Path('path/to/file')
    
    print(str(path))
    
    
Path Joining

    a = Path('/usr/share/man')
    b = Path('en/man1/whatis.1.gz')
    
    a.join(b) == Path('/usr/share/man/en/man1/whatis.1.gz')
    
    # Also:
    a.join('en/man1/whatis.1.gz') == Path('/usr/share/man/en/man1/whatis.1.gz')
    
    
Listing the files in a directory

    from npath import File, Directory
    
    d = Direcotry('/usr/share/man')
    
    for file in d.files:
        print(str(file))


Listing the directories in a directory

    from npath import File, Directory
    
    d = Direcotry('/usr/share/man')
    
    for a_dir in d.dirs:
        print(str(a_dir))


Listing the files and directories in a directory

    from npath import File, Directory
    
    d = Direcotry('/usr/share/man')
    
    for fobj in d.all:
        print(str(fobj))


Recursively walk over all sub files and sub directories of a path

    for fobj in Directory('/usr/share/man').walk():
        if fobj.is_file:
            print ("FILE: %s" % (fobj))
        elif fobj.is_dir:
            print ("DIR:  %s" % (fobj))


Opening a file in a directory

    d = Direcotry('/home/auser')
    fh = d.join('my_file.txt').open('w')
    fh.write("...")
    fh.close()


|                                            | os                                        | npath                                                        |
|--------------------------------------------|-------------------------------------------|--------------------------------------------------------------|
| Base portion of path                       | os.path.basename('my/path')               | Path('my/path').basename                                     |
| Parent portion of path                     | N/A                                       | Path('my/path/to').parent == Path('my/path')                 |
| Absolute path                              | os.path.abspath('my/path')                | Path('my/path').abs                                          |
| Normalized path                            | os.path.normpath('my/path')               | Path('my/path').norm                                         |
| Get file extension                         | os.path.splitext('my/path/myfile.txt')[0] | Path('my/path/myfile.txt') Note: Doesn't include leading '.' |
| Does the path point to an existing object? | os.path.exists('my/path')                 | Path('my/path').exists                                       |
| Does path point to a file?                 | os.path.isfile('my/path')                 | Path('my/path').is_file                                      |
| Does path point to a directory?            | os.path.isdir('my/path')                  | Path('my/path').is_dir                                       |
| Does path point to a link?                 | os.path.islink('my/path')                 | Path('my/path').is_link                                      |
|                                            |                                           |                                                              |
| Get file size                              | os.path.getsize('my/path')                | File('my/path').size                                         |
| Get file MD5 sum                           | Use hashlib                               | File('my/path').md5                                          |


Path Comparisons
----------------

All path comparisons will work between Path objects (which includes
Directory, File, FileObject, and InvalidFileObject) and strings.  Though,
the Path object must be on the left.

These work:
    
    Path('a/b/c') == 'a/b/c'
    File('a/b/c') == 'a/b/c'
    Path('a/b/c') == File('a/b/c')

But, this will not:

    'a/b/c' == Path('a/b/c')
    

A Note on "Relative To" Paths
-----------------------------

One of the needs I often have is to work with a set of paths that are
all relative to a single parent path.  For example, if I'm listing all
of the files under /usr/share/man/en, it may matter to me to remember
that all of those paths are under /usr/share/man/en, even though I want
to work with the relative paths (e.g.: man1/whatis.1.gz).  To support
this need, I've added functionality to the Path object to note hold that
common parent path as an attribute.

    path = Path('man1/whatis.1.gz', relative_to='/usr/share/man/en')
    
    str(path) == 'man1/whatis.1.gz'                         # True
    str(path.rel_root) == '/usr/share/man/en'               # True
    str(path.abs) == '/usr/share/man/en/man1/whatis.1.gz'   # True
    
As paths are manipulated (such as joined), they will retain that
relative root whenever it makes sense.
    
    path = Path('man1', relative_to='/usr/share/man/en')
    str( path.join('whatis.1.gz') ) == '/usr/share/man/en/man1/whatis.1.gz'
    
Also, all the path generators will retain the relative root of their
constructing/parent object.

    for fl in Directory('man1', relative_to='/usr/share/man/en').files:
        assert(fl.rel_root) == '/usr/share/man/en'



Change Log
----------

**v1.0.0**

  - Basic completion with some tests.