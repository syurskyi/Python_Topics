c_ Solution:
    ___ findJudge  N: i.., trust: List[List[i..]])   i..:
        __ N__1:
            r_ 1
        d1={}
        d2={}
        ___ i, j __ trust:
            __ j __ d1:
                d1[j]+=1
            ____
                d1[j]=1
            __ i __ d2:
                d2[i]+=1
            ____
                d2[i]=1
        ___ i,j __ d1.items():
            __ j__N-1:
                __ i not __ d2:
                    r_ i
        r_ -1
                    
