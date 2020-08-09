amount_values = int(input())
results = []

___ get_seq(Xnext, counter=0
    __(Xnext __ 1
        r_ counter
    ____
        __(Xnext % 2 __ 0
            r_ get_seq(Xnext/2, counter+1)
        ____
            r_ get_seq(3*Xnext+1, counter+1)

XList = list(map(int, input().split()))
___ i in XList:
    seq = get_seq(i)
    results.append(seq)

print(*results)