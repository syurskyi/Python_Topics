import os

path = '/home/sergei/My_Documents/Python/Advanced Python Scripting/top_projects'
folders = \
[['input',  [
    ['src', []],
    ['doc', []]
    ]],
 ['output', []],
 ['scenes', []],
 ['assets', [
     ['textures', []],
     ['models',[
         ['characters', []],
         ['locations', []]
         ]],
 ]]
]

def createFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)

def build(root, data):
    if data:
        for d in data:
            # print(d)
            name = d[0]
            path = os.path.join(root, name)
            createFolder(path)
            build(path, d[1])

projectname = raw_input('Enter project name: ')
if projectname:
    fullPath = os.path.join(path, projectname)
    createFolder(fullPath)
    build(fullPath, folders)

print(projectname)
raw_input()




# print(fullPath)

# for f in folders:
#    folder = os.path.join(fullPath, f)
#    createFolder(folder)



"""
if not os.path.exists(fullPath):
    os.mkdir(fullPath)

for f in folders:
    folder = os.path.join(fullPath, f)
    # print(folder)
    if not os.path.exists(folder):
        os.mkdir(folder)
"""