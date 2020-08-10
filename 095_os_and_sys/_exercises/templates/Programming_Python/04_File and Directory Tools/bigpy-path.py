"""
Find the largest Python source file on the module ______ search path.
Skip already-visited directories, normalize path and case so they will
match properly, and include line counts in pprinted result. It's not
enough to use os.environ['PYTHONPATH']: this is a subset of sys.path.
"""

______ sys, __, pprint
trace = 0  # 1=dirs, 2=+files

visited  = {}
allsizes = []
___ srcdir __ sys.p..:
    ___ (thisDir, subsHere, filesHere) __ __.walk(srcdir):
        __ trace > 0: print(thisDir)
        thisDir = __.p...normpath(thisDir)
        fixcase = __.p...normcase(thisDir)
        __ fixcase __ visited:
            continue
        ____
            visited[fixcase] = True
        ___ filename __ filesHere:
            __ filename.endswith('.py'):
                __ trace > 1: print('...', filename)
                pypath = __.p...j..(thisDir, filename)
                try:
                    pysize = __.p...getsize(pypath)
                except __.error:
                    print('skipping', pypath, sys.exc_info()[0])
                ____
                    pylines = len(o..(pypath, 'rb').readlines())
                    allsizes.append((pysize, pylines, pypath))

print('By size...')
allsizes.sort()
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])

print('By lines...')
allsizes.sort(key=lambda x: x[1])
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])
