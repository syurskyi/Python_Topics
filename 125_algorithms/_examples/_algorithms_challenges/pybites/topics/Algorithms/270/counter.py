from collections import Counter

def freq_digit(num: int) -> int:
    cnt = Counter(str(num))
    print(type(cnt))
    print(cnt.most_common(1)[0][0])
    templist = [int(i) for i in str(num)]
    return max(templist, key = templist.count)




freq_digit(994145467)