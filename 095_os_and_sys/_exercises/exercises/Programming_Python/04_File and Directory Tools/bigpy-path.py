"""
Find the largest Python source file on the module ______ search path.
Skip already-visited directories, normalize path and case so they will
match properly, and include line counts in pprinted result. It's not
enough to use os.environ['PYTHONPATH']: this is a subset of sys.path.
"""

______ ___, __, pprint
trace _ 0  # 1=dirs, 2=+files

visited  _ {}
allsizes _ []
___ srcdir __ ___.p..:
    ___ (thisDir, subsHere, filesHere) __ __.w..(srcdir):
        __ trace > 0: print(thisDir)
        thisDir _ __.p...n..(thisDir)
        fixcase _ __.p...normcase(thisDir)
        __ fixcase __ visited:
            continue
        ____
            visited[fixcase] _ True
        ___ filename __ filesHere:
            __ filename.e_w_('.py'):
                __ trace > 1: print('...', filename)
                pypath _ __.p...j..(thisDir, filename)
                ___
                    pysize _ __.p...getsize(pypath)
                ______ __.error:
                    print('skipping', pypath, ___.exc_info()[0])
                ____
                    pylines _ le.(o..(pypath, 'rb').readlines())
                    allsizes.ap..((pysize, pylines, pypath))

print('By size...')
allsizes.sort()
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])

print('By lines...')
allsizes.sort(key_lambda x: x[1])
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])
