____ zipfile _____ ZipFile
_____ os

src _ 'C:/Users/Sergej/Dropbox/nuke/.nuke/example/Example Panel.py'
zFile _ 'C:/Users/Sergej/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/006_Additional materials/archive.zip'

zf _ ZipFile(zFile, 'w')
zf.write(src, os.path.basename(src))
zf.close()

trg _ 'C:/Users/Sergej/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/006_Additional materials/'
zf _ ZipFile(zFile, 'r')

zf.namelist()