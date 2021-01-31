_____ ?, __

___ start
    reads = ?.aN..('Read')
    searchFolder = ''
    ___ r __ reads:
        filepath = r['file'].gV..()
        __ no. __.pa__.exists(filepath):
            filename = __.pa__.b__(filepath)
            __ no. searchFolder:
                searchFolder = ?.getFilename('Select Folder')
                __ __.pa__.isfile(searchFolder):
                    searchFolder = __.pa__.d..(searchFolder)
            __ searchFolder:
                ___ pa__, dirs, files __ __.walk(searchFolder):
                    __ filename __ files:
                        newPath = __.pa__.join(pa__, filename)
                        r['file'].sV..(newPath.replace('\\','/'))
                        break
