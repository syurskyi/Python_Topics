import os
# source=input('source file to pyuic5:\n')
source='raw_gui_latest.ui'
destination = source.replace('.ui','_latest.py')
myCmd ='pyuic5 -x '+source+' -o '+destination
print('successfully changed ',source+' to '+destination)

os.system(myCmd)

#pyuic -x source.ui -o destination.py
