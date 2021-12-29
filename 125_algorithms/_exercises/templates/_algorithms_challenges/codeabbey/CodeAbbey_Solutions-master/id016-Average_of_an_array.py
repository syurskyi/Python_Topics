___ cleanData(data):
        array    # list
        ___ x __ data:
                __ x != '0' o. 0:
                        array.a..(x)
        r.. array

___ average(amount):
        answer    # list
        ___ x __ r..(amount):
                array = raw_input().s..
                array = cleanData(array)
                total, average, y = 0,0,0
                w.... y < l..(array):
                        total += int(array[y])
                        y+=1
                        average = "%.02f" % ((float(total)) / float(l..(array)))
                        average = int(round(float(average)))
                answer.a..(s..(average))
        print(' '.join(answer))
average(input())
