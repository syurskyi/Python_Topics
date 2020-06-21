def timer(label=''):
    def decorator(func):
        def onCall(*args):          # args passed to function
            pass                    # func retained in enclsing scope
            print(label)            # label retained in enclosing scope
        return onCall
    return decorator                # Returns that actual decorator


@timer('==>')                       # Like listcomp = timer('==>')(listcomp)
def listcomp(N): pass                # listcomp is rebound to decorator


listcomp(...)                       # Really calls decorator


from mytools import timer


@timer(trace=False)                    # No tracing, collect total time
def listcomp(N):
    return [x * 2 for x in range(N)]


x = listcomp(5000)
x = listcomp(5000)
x = listcomp(5000)
print(listcomp)
# <mytools.Timer instance at 0x025C77B0>

print(listcomp.alltime)
# 0.0051938863738243413


@timer(trace=True, label='\t=>')       # Turn on tracing
def listcomp(N):
    return [x * 2 for x in range(N)]


x = listcomp(5000)  #  => listcomp: 0.00155, 0.00155
x = listcomp(5000)  # => listcomp: 0.00156, 0.00311
x = listcomp(5000)  #  => listcomp: 0.00174, 0.00486
print(listcomp.alltime)
# 0.0048562736325408196
