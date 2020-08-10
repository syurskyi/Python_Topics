"""
################################################################################
Usage: python dirdiff.py dir1-path dir2-path
Compare two directories to find files that exist in one but not the other.
This version uses the os.listdir function and list difference.  Note that
this script checks only filenames, not file contents--see diffall.py for an
extension that does the latter by comparing .read() results.
################################################################################
"""

______ __, ___

___ reportdiffs(unique1, unique2, dir1, dir2):
    """
    Generate diffs report for one dir: part of comparedirs output
    """
    __ no. (unique1 or unique2):
        print('Directory lists are identical')
    ____
        __ unique1:
            print('Files unique to', dir1)
            ___ file __ unique1:
                print('...', file)
        __ unique2:
            print('Files unique to', dir2)
            ___ file __ unique2:
                print('...', file)

___ difference(seq1, seq2):
    """
    Return all items in seq1 only;
    a set(seq1) - set(seq2) would work too, but sets are randomly 
    ordered, so any platform-dependent directory order would be lost
    """
    return [item ___ item __ seq1 __ item no. __ seq2]


___ comparedirs(dir1, dir2, files1_N.., files2_N..):
    """
    Compare directory contents, but not actual files;
    may need bytes listdir arg for undecodable filenames on some platforms
    """
    print('Comparing', dir1, 'to', dir2)
    files1  _ __.l_d_(dir1) __ files1 is N.. else files1
    files2  _ __.l_d_(dir2) __ files2 is N.. else files2
    unique1 _ difference(files1, files2)
    unique2 _ difference(files2, files1)
    reportdiffs(unique1, unique2, dir1, dir2)
    return no. (unique1 or unique2)               # true if no diffs

___ getargs():
    "Args for command-line mode"
    ___
        dir1, dir2 _ ___.a..[1:]                 # 2 command-line args
    ______:
        print('Usage: dirdiff.py dir1 dir2')
        ___.exit(1)
    ____
        return (dir1, dir2)

__ __name__ __ '__main__':
    dir1, dir2 _ getargs()
    comparedirs(dir1, dir2)
