_____ ?
_____ __

___ fixRead

    reads = ?.aN..('Read')
    searchFolder = ''

    ___ r __ reads:
        filepath = r['file'].gV..()
        __ no. __.pa__.e..(filepath):
            filename = __.pa__.b__(filepath)
            __ no. searchFolder:
                searchFolder = ?.getFilename('Select Folder')
                __ __.pa__.isfile(searchFolder):
                    searchFolder = __.pa__.d..(searchFolder)
            __ searchFolder:
                ___ pa__, dirs, files __ __.walk(searchFolder):
                    __ filename __ files:
                        newPath = __.pa__.j..(pa__, filename)
                        r['file'].sV..(newPath.replace('\\', '/'))
                        break