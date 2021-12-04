import os

fnames = [f"{str(i).zfill(2)}_sales.csv" for i in range(1, 25)]
paths = [os.path.join(os.getcwd(), '2020', fname) if idx < 12
         else os.path.join(os.getcwd(), '2021', fname)
         for idx, fname in enumerate(fnames)]

for path in paths:
    print(path)