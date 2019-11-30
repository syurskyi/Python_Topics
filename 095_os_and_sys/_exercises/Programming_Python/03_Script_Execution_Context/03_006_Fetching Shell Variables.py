import os
print(os.environ.keys())
# KeysView(<os._Environ object at 0x013B8C70>)

print('#' * 52)
print(list(os.environ.keys()))
# ['TMP', 'COMPUTERNAME', 'USERDOMAIN', 'PSMODULEPATH', 'COMMONPROGRAMFILES',
#...many more deleted...
# 'NUMBER_OF_PROCESSORS', 'PROCESSOR_LEVEL', 'USERPROFILE', 'OS', 'PUBLIC', 'QTJAVA']
# ######################################################################################################################

print('#' * 52)
print(os.environ['TEMP'])
# 'C:\\Users\\mark\\AppData\\Local\\Temp'
# ######################################################################################################################

print('#' * 52)
print(os.environ['PYTHONPATH'])
# 'C:\\PP4thEd\\Examples;C:\\Users\\Mark\\temp'
# ######################################################################################################################

print('#' * 52)
for srcdir in os.environ['PYTHONPATH'].split(os.pathsep):
    print(srcdir)

# C:\PP4thEd\Examples
# C:\Users\Mark\temp
# ######################################################################################################################

print('#' * 52)
import sys
print(sys.path[:3])
# ['', 'C:\\PP4thEd\\Examples', 'C:\\Users\\Mark\\temp']
# ######################################################################################################################