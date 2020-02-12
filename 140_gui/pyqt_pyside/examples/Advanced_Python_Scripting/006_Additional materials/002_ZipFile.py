from zipfile import ZipFile
import os

src = 'C:/Users/Sergej/Dropbox/nuke/.nuke/example/Example Panel.py'
zFile = 'C:/Users/Sergej/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/006_Additional materials/archive.zip'

zf = ZipFile(zFile, 'w')
zf.write(src, os.path.basename(src))
zf.close()

trg = 'C:/Users/Sergej/Dropbox/nuke/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced_Python_Scripting/006_Additional materials/'
zf = ZipFile(zFile, 'r')

zf.namelist()