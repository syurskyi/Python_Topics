c_ Solution:
    ___ compareVersion  version1: str, version2: str) -> int:
        l1=list(map(int,version1.split('.')))
        l2=list(map(int,version2.split('.')))
        __ l1__l2:
            r_(0)
        
        a=l.. l1)
        b=l.. l2)
        
        __ a>b:
            ___ i __ r.. a-b):
                l2.append("0")
        
        ____
            ___ i __ r.. b-a):
                l1.append("0")
            
        ___ i __ r.. l.. l1)):
            __ int(l1[i])>int(l2[i]):
                r_(1)
            
            ____ int(l1[i])<int(l2[i]):
                r_(-1)
            
            ____
                pass
        
        r_(0)
