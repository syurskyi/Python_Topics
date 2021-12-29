_______ os, os.path

#DIR = 'C:\\Users\\Swee-Chuan Khoo\\Documents\\covic19_MoH\\covid19-public'
DIR = '.'

""" print([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

for name in os.listdir(DIR):
    if os.path.isfile(os.path.join(DIR, name)):
        print(name)
    elif os.path.isdir(os.path.join(DIR, name)):
        print('Directory ', name) """

filecount, dircount = 0, 0
___ root, dirs, files __ os.walk(DIR):
    ___ name __ files:
        filecount += 1
        print(os.path.join(DIR, name))
    ___ name __ dirs:
        dircount += 1
        print(os.path.join(DIR, name))

print(filecount, dircount)