import os

paths = [os.path.join(os.getcwd(), f'dir_{str(i).zfill(2)}') for i in range(1, 14)]

for path in paths:
    if not os.path.exists(path):
        os.mkdir(path)

os.rmdir(os.path.join(os.getcwd(), 'dir_13'))
fnames = [fname for fname in sorted(os.listdir()) if len(fname) == 6]
print(fnames)