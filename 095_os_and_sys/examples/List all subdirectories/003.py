import os

print()
print(50 * '#')
print('# ####### listdir')
print()

# folder path
dir_path = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)

# print()
# print(50 * '#')
# print('# ####### listdir')
# print()
#
# import os
#
# def get_files(path):
#     for file in os.listdir(path):
#         if os.path.isfile(os.path.join(path, file)):
#             yield file
#
# for file in get_files(r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'):
#     print(file)
#
# import os
#
# print()
# print(50 * '#')
# print('# ####### listdir')
# print()
#
# # folder path
# dir_path = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'
#
# # list file and directories
# res = os.listdir(dir_path)
# print(res)
#
# print()
# print(50 * '#')
# print('# ####### walk')
# print()
# from os import walk
#
# # folder path
# dir_path = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'
#
# # list to store files name
# res = []
# for (dir_path, dir_names, file_names) in walk(dir_path):
#     res.extend(file_names)
# print(res)
#
# print()
# print(50 * '#')
# print('# ####### walk')
# print()
#
# from os import walk
#
# # folder path
# dir_path = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'
# res = []
# for (dir_path, dir_names, file_names) in walk(dir_path):
#     res.extend(file_names)
#     # don't look inside any subdirectory
#     break
# print(res)

# print()
# print(50 * '#')
# print('# ####### scandir')
# print()
#
# import os
#
# # get all files inside a specific folder
# dir_path = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'
# for path in os.scandir(dir_path):
#     if path.is_file():
#         print(path.name)
#
# print()
# print(50 * '#')
# print('# ####### glob')
# print()
#
# import glob
#
# # search all files inside a specific folder
# # *.* means file name with any extension
# dir_path = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python\*.*'
# res = glob.glob(dir_path)
# print(res)
#
# print()
# print(50 * '#')
# print('# ####### glob')
# print()
#
# import glob
#
# # search all files inside a specific folder
# # *.* means file name with any extension
# dir_path = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python\**\*.*'
# for file in glob.glob(dir_path, recursive=True):
#     print(file)
#
# print()
# print(50 * '#')
# print('# ####### pathlib')
# print()
#
# import pathlib
#
# # folder path
# dir_path = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'
#
# # to store file names
# res = []
#
# # construct path object
# d = pathlib.Path(dir_path)
#
# # iterate directory
# for entry in d.iterdir():
#     # check if it a file
#     if entry.is_file():
#         res.append(entry)
# print(res)