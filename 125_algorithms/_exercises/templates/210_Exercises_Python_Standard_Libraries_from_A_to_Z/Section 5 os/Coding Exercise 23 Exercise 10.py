import os

fnames = [f"{str(i).zfill(3)}_sales.csv" for i in range(1, 25)]
paths = [os.path.join(os.getcwd(), fname) for fname in fnames]
print(paths)