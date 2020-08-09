win_dic = {'S':'P','P':'R','R':'S'}
___ i in range(int(input())):
    count1 = 0
    count2 = 0
    a = list(map(str,input().split()))
    ___ j in a:
        __ j[0] __ j[1]:
            pass
        ____ j[1] __ win_dic[j[0]]:
            count1 += 1
        ____
            count2 += 1
    __ count1 > count2:
        print('1',end=' ')
    ____
        print('2',end=' ')