import os

rootdir = "/"

for curr, dirs, files in os.walk(rootdir):

    for f in files:
        print ('%s/%s' % (curr, f))

