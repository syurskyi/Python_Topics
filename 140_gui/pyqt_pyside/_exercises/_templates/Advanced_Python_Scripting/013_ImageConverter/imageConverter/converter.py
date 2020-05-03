_____ os

iconvert _ 'C:/Program Files/Side Effects Software/Houdini 16.0.736/bin/iconvert.exe'


___ convert(src, trg_None
    __ trg:
        __ no. os.path.exists(trg
            os.makedirs(trg)
        ____ os.path.isfile(trg
            trg _ os.path.dirname(trg)
        basename _ os.path.basename(src)
        name, ext _ os.path.splitext(basename)
        trg _ os.path.j..(trg, name+'.exr')
    ____
        trg _ os.path.splitext(src)[0] + '.exr'

    cmd _ ' '.j..([iconvert, src, trg])
    os.popen(cmd)

convert('C:/Users/serge/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/013_ImageConverter/texture.jpg')