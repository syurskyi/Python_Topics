import os

fnames = sorted([name for name in os.listdir() if name.endswith('.py')])
print(fnames)