_____ __

path _ '/home/sergei/My_Documents/Python/Advanced Python Scripting/top_projects'
folders _ \
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

___ createFolder(path
    __ no. __.path.exists(path
        __.mkdir(path)

___ build(root, data
    __ data:
        ___ d __ data:
            # print(d)
            name _ d[0]
            path _ __.path.j..(root, name)
            createFolder(path)
            build(path, d[1])

projectname _ raw_input('Enter project name: ')
__ projectname:
    fullPath _ __.path.j..(path, projectname)
    createFolder(fullPath)
    build(fullPath, folders)

print(projectname)
raw_input




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