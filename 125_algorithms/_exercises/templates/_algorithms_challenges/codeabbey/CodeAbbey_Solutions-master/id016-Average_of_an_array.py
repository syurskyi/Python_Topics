___ cleanData(data
        array =   # list
        ___ x __ data:
                __ x != '0' or 0:
                        array.append(x)
        r_ array

___ average(amount
        answer =   # list
        ___ x __ range(amount
                array = raw_input().split()
                array = cleanData(array)
                total, average, y = 0,0,0
                w___ y < le.(array
                        total += int(array[y])
                        y+=1
                        average = "%.02f" % ((float(total)) / float(le.(array)))
                        average = int(round(float(average)))
                answer.append(str(average))
        print(' '.join(answer))
average(input())
