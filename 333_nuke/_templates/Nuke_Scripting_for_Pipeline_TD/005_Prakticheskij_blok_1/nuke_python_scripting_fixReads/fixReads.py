_____ ?, __

___ start
    reads = ?.allNodes('Read')
    searchFolder = ''
    ___ r __ reads:
        filepath = r['file'].getValue()
        __ no. __.pa__.exists(filepath):
            filename = __.pa__.b__(filepath)
            __ no. searchFolder:
                searchFolder = ?.getFilename('Select Folder')
                __ __.pa__.isfile(searchFolder):
                    searchFolder = __.pa__.dirname(searchFolder)
            __ searchFolder:
                ___ pa__, dirs, files __ __.walk(searchFolder):
                    __ filename __ files:
                        newPath = __.pa__.join(pa__, filename)
                        r['file'].setValue(newPath.replace('\\','/'))
                        break
