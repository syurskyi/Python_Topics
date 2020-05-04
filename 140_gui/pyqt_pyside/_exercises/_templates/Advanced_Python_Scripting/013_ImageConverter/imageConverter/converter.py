_____ __

iconvert _ 'C:/Program Files/Side Effects Software/Houdini 16.0.736/bin/iconvert.exe'


___ convert(src, trg_None
    __ trg:
        __ no. __.path.exists(trg
            __.makedirs(trg)
        ____ __.path.isfile(trg
            trg _ __.path.d_n..(trg)
        b.. _ __.path.b..(src)
        name, ext _ __.path.splitext(b..)
        trg _ __.path.j..(trg, name+'.exr')
    ____
        trg _ __.path.splitext(src)[0] + '.exr'

    cmd _ ' '.j..([iconvert, src, trg])
    __.popen(cmd)

convert('C:/Users/serge/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/013_ImageConverter/texture.jpg')