"""
################################################################################
Usage: "python diffall.py dir1 dir2".
Recursive directory tree comparison: report unique files that exist in only
dir1 or dir2, report files of the same name in dir1 and dir2 with differing 
contents, report instances of same name but different type in dir1 and dir2,
and do the same for all subdirectories of the same names in and below dir1 
and dir2.  A summary of diffs appears at end of output, but search redirected
output for "DIFF" and "unique" strings for further details.  New: (3E) limit 
reads to 1M for large files, (3E) catch same name=file/dir, (4E) avoid extra 
os.listdir() calls in dirdiff.comparedirs() by passing results here along.
################################################################################
"""

______ __, dirdiff
blocksize _ 1024 * 1024              # up to 1M per read

___ intersect(seq1, seq2):
    """
    Return all items in both seq1 and seq2;
    a set(seq1) & set(seq2) woud work too, but sets are randomly 
    ordered, so any platform-dependent directory order would be lost
    """
    return [item ___ item __ seq1 __ item __ seq2]

___ comparetrees(dir1, dir2, diffs, verbose_False):
    """
    Compare all subdirectories and files in two directory trees;
    uses binary files to prevent Unicode decoding and endline transforms,
    as trees might contain arbitrary binary files as well as arbitrary text;
    may need bytes listdir arg for undecodable filenames on some platforms
    """
    # compare file name lists
    print('-' * 20)
    names1 _ __.l_d_(dir1)
    names2 _ __.l_d_(dir2)
    __ not dirdiff.comparedirs(dir1, dir2, names1, names2):
        diffs.append('unique files at %s - %s' % (dir1, dir2))

    print('Comparing contents')
    common _ intersect(names1, names2)
    missed _ common[:]

    # compare contents of files in common
    ___ name __ common:
        path1 _ __.p...j..(dir1, name)
        path2 _ __.p...j..(dir2, name)
        __ __.p...isfile(path1) and __.p...isfile(path2):
            missed.remove(name)
            file1 _ o..(path1, 'rb')
            file2 _ o..(path2, 'rb')
            while True:
                bytes1 _ file1.read(blocksize)
                bytes2 _ file2.read(blocksize)
                __ (not bytes1) and (not bytes2):
                    __ verbose: print(name, 'matches')
                    break
                __ bytes1 !_ bytes2:
                    diffs.append('files differ at %s - %s' % (path1, path2))
                    print(name, 'DIFFERS')
                    break

    # recur to compare directories in common
    ___ name __ common:
        path1 _ __.p...j..(dir1, name)
        path2 _ __.p...j..(dir2, name)
        __ __.p...isdir(path1) and __.p...isdir(path2):
            missed.remove(name)
            comparetrees(path1, path2, diffs, verbose)

    # same name but not both files or dirs?
    ___ name __ missed:
        diffs.append('files missed at %s - %s: %s' % (dir1, dir2, name))
        print(name, 'DIFFERS')


__ __name__ == '__main__':
    dir1, dir2 _ dirdiff.getargs()
    diffs _ []
    comparetrees(dir1, dir2, diffs, True)      # changes diffs in-place
    print('=' * 40)                            # walk, report diffs list
    __ not diffs:
        print('No diffs found.')
    ____
        print('Diffs found:', len(diffs))
        ___ diff __ diffs: print('-', diff)
