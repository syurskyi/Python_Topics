_____ ?, __

___ start
    reads _ ?.aN..('Read')
    searchFolder _ ''
    ___ r __ reads:
        filepath _ r['file'].gV..()
        __ no. __.pa__.e..(filepath):
            filename _ __.pa__.b__(filepath)
            __ no. searchFolder:
                searchFolder _ ?.getFilename('Select Folder')
                __ __.pa__.isfile(searchFolder):
                    searchFolder _ __.pa__.d..(searchFolder)
            __ searchFolder:
                ___ pa__, dirs, files __ __.walk(searchFolder):
                    __ filename __ files:
                        newPath _ __.pa__.j..(pa__, filename)
                        r['file'].sV..(newPath.replace('\\','/'))
                        break
