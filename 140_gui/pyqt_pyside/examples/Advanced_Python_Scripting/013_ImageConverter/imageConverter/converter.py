import os

iconvert = 'C:/Program Files/Side Effects Software/Houdini 16.0.736/bin/iconvert.exe'


def convert(src, trg=None):
    if trg:
        if not os.path.exists(trg):
            os.makedirs(trg)
        elif os.path.isfile(trg):
            trg = os.path.dirname(trg)
        basename = os.path.basename(src)
        name, ext = os.path.splitext(basename)
        trg = os.path.join(trg, name+'.exr')
    else:
        trg = os.path.splitext(src)[0] + '.exr'

    cmd = ' '.join([iconvert, src, trg])
    os.popen(cmd)

convert('C:/Users/serge/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/013_ImageConverter/texture.jpg')