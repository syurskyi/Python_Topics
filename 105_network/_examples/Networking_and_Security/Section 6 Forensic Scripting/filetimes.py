import os, datetime

rootdir = "/Users/kilroy"
searchdate = datetime.date.today()-datetime.timedelta(days=3)

for curr, dirs, files in os.walk(rootdir):

    for f in files:
        try:
            path = "%s/%s" % (curr, f)
            t = datetime.date.fromtimestamp(os.path.getmtime(path))
            if (t > searchdate):
                print("found date %s on file %s" % (t,f))
        except Exception as e:
            no_op = 0