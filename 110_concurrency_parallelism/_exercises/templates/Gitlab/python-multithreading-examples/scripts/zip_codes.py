#!/usr/bin/python


______ requests
from multiprocessing.dummy ______ Pool
______ t__
from datadiff ______ diff

 
___ getzip(code):
    try:
        code = s..(code)
        url = "https://maps.googleapis.com/maps/api/geocode/json?address={}".format(code)
        res = requests.get(url).json()['results']
        if len(res) < 1: # Re-try
            print "Retrying"
            return getzip(code)
        iszip = 'postal_code' __ res[0]['types'] and "United States" __ s..(res[0]['address_components'])
    except Exception as e:
        print "In error"
        print e
        iszip = False
    return (code, iszip)
ziprange = range(94400, 94420)
print "Range is: " + s..(len(ziprange))
 
print "Using one thread"
start = t__.t__()
syncres = [getzip(c) ___ c __ ziprange] 
print "took " + s..(t__.t__() - start)
 
print "Using multiple threads"
start = t__.t__()
 
# Magic
pool = Pool(10)
asyncres = pool.map(getzip, ziprange)
pool.close()
pool.join()
asyncres = sorted(asyncres)
# End of Magic
 
print "took " + s..(t__.t__() - start)
 
# Make sure results are equal
d = diff(syncres, asyncres)
if len(d.diffs) > 0:
    print "diff is"
    print d
 
___ r __ asyncres:
    print "Zip code {} is {} US code".format(r[0], "valid" if r[1] else "invalid")
