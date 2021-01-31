_____ ?
_____ __
___ incNamePath(pa__):
    nameExt = __.pa__.b__(pa__)
    name, ext = __.pa__.s__(nameExt)
    dir = __.pa__.d..(pa__)
    splt = name.split('_')
    nameNum = '01'
    __ le.(splt) > 1:
        num = splt[-1]
        __ num.isdigit
            nameNum = in_(num) + 1
            nzero = le.(num)
            __ nzero < 2: nzero = 2
            __ nzero > le.(str(nameNum)):
                nameNum = str(nameNum).zfill(nzero)
            nName = '_'.j..(splt[:-1]) + '_' + nameNum
        ____
            nName = '_'.j..(splt) + '_' + nameNum
    ____
        nName = name + '_' + str(nameNum)
    result = '/'.j..([dir,nName+ext])
    r_ result
    

map( lambda x: x['reload'].execute(), ?.aN..('Read'))

___ r __ ?.aN..('Read'):
    f = incNamePath(r['file'].gV..())
    w = ?.nodes.Write(inputs=[r], file=f)
#    w['Render'].execute()
    ?.execute(w, 1, 1)
