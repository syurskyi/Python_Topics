import os

os.mkdir('documents')

dirnames = [f'{str(i).zfill(2)}_sales' for i in range(1, 13)]
for dirname in dirnames:
    path = os.path.join('documents', dirname)
    os.mkdir(path)

print(sorted(os.listdir('documents')))