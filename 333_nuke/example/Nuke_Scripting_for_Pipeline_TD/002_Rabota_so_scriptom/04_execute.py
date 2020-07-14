import nuke
import os
def incNamePath(path):
    nameExt = os.path.basename(path)
    name, ext = os.path.splitext(nameExt)
    dir = os.path.dirname(path)
    splt = name.split('_')
    nameNum = '01'
    if len(splt) > 1:
        num = splt[-1]
        if num.isdigit():
            nameNum = int(num) + 1
            nzero = len(num)
            if nzero < 2: nzero = 2
            if nzero > len(str(nameNum)):
                nameNum = str(nameNum).zfill(nzero)
            nName = '_'.join(splt[:-1]) + '_' + nameNum
        else:
            nName = '_'.join(splt) + '_' + nameNum
    else:
        nName = name + '_' + str(nameNum)
    result = '/'.join([dir,nName+ext])
    return result
    

map( lambda x: x['reload'].execute(), nuke.allNodes('Read'))

for r in nuke.allNodes('Read'):
    f = incNamePath(r['file'].getValue())
    w = nuke.nodes.Write(inputs=[r], file=f)
#    w['Render'].execute()
    nuke.execute(w, 1, 1)
