import nuke, os

def start():
    reads = nuke.allNodes('Read')
    searchFolder = ''
    for r in reads:
        filepath = r['file'].getValue()
        if not os.path.exists(filepath):
            filename = os.path.basename(filepath)
            if not searchFolder:
                searchFolder = nuke.getFilename('Select Folder')
                if os.path.isfile(searchFolder):
                    searchFolder = os.path.dirname(searchFolder)
            if searchFolder:
                for path, dirs, files in os.walk(searchFolder):
                    if filename in files:
                        newPath = os.path.join(path, filename)
                        r['file'].setValue(newPath.replace('\\','/'))
                        break
