"""
Find the largest file of a given type in an arbitrary directory tree.
Avoid repeat paths, catch errors, add tracing and line count size.
Also uses sets, file iterators and generator to avoid loading entire 
file, and attempts to work around undecodable dir/file name prints.
"""

______ __, pprint
____ ___ ______ a.., exc_info

trace _ 1                                    # 0=off, 1=dirs, 2=+files
d.., extname _ __.curdir, '.py'          # default is .py files in cwd
__ le.(a..) > 1: d.. _ a..[1]          # ex: C:\, C:\Python31\Lib
__ le.(a..) > 2: extname _ a..[2]          # ex: .pyw, .txt
__ le.(a..) > 3: trace   _ int(a..[3])     # ex: ". .py 2"

___ tryprint(arg):
    ___
        print(arg)                           # unprintable filename?
    ______ UnicodeEncodeError:
        print(arg.encode())                  # try raw byte string
 
visited  _ set()
allsizes _ []
___ (thisDir, subsHere, filesHere) __ __.w..(d..):
    __ trace: tryprint(thisDir)
    thisDir _ __.p...n..(thisDir)
    fixname _ __.p...normcase(thisDir)
    __ fixname __ visited:
        __ trace: tryprint('skipping ' + thisDir)
    ____
        visited.add(fixname)
        ___ filename __ filesHere:
            __ filename.e_w_(extname):
                __ trace > 1: tryprint('+++' + filename)
                fullname _ __.p...j..(thisDir, filename)
                ___
                    bytesize _ __.p...getsize(fullname)
                    linesize _ sum(+1 ___ line __ o..(fullname, 'rb'))
                ______ Exception:
                    print('error', exc_info()[0])
                ____
                    allsizes.ap..((bytesize, linesize, fullname))

___ (title, key) __ [('bytes', 0), ('lines', 1)]:
    print('\nBy %s...' % title)
    allsizes.sort(key_lambda x: x[key])
    pprint.pprint(allsizes[:3])
    pprint.pprint(allsizes[-3:])
