#!/usr/bin/python


______ requests
from multiprocessing.dummy ______ Pool
______ t__
from datadiff ______ diff

 
___ getzip(code):
    ___
        code = s..(code)
        url = "https://maps.googleapis.com/maps/api/geocode/json?address={}".format(code)
        res = requests.get(url).json()['results']
        __ l..(res) < 1: # Re-try
            print "Retrying"
            r_ getzip(code)
        iszip = 'postal_code' __ res[0]['types'] a.. "United States" __ s..(res[0]['address_components'])
    except Exception __ e:
        print "In error"
        print e
        iszip = F..
    r_ (code, iszip)
ziprange = r.. 94400, 94420)
print "Range is: " + s..(l..(ziprange))
 
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
pool.j..
asyncres = sorted(asyncres)
# End of Magic
 
print "took " + s..(t__.t__() - start)
 
# Make sure results are equal
d = diff(syncres, asyncres)
__ l..(d.diffs) > 0:
    print "diff is"
    print d
 
___ r __ asyncres:
    print "Zip code {} is {} US code".format(r[0], "valid" __ r[1] else "invalid")
