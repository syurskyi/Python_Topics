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
    __ not (unique1 or unique2):
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
    return [item ___ item __ seq1 __ item not __ seq2]


___ comparedirs(dir1, dir2, files1=N.., files2=N..):
    """
    Compare directory contents, but not actual files;
    may need bytes listdir arg for undecodable filenames on some platforms
    """
    print('Comparing', dir1, 'to', dir2)
    files1  = __.l_d_(dir1) __ files1 is N.. else files1
    files2  = __.l_d_(dir2) __ files2 is N.. else files2
    unique1 = difference(files1, files2)
    unique2 = difference(files2, files1)
    reportdiffs(unique1, unique2, dir1, dir2)
    return not (unique1 or unique2)               # true if no diffs

___ getargs():
    "Args for command-line mode"
    try:
        dir1, dir2 = ___.argv[1:]                 # 2 command-line args
    except:
        print('Usage: dirdiff.py dir1 dir2')
        ___.exit(1)
    ____
        return (dir1, dir2)

__ __name__ == '__main__':
    dir1, dir2 = getargs()
    comparedirs(dir1, dir2)
