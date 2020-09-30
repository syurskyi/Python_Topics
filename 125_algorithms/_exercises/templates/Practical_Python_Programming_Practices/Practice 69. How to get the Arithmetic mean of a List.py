___ avg_list(first):
    last = len(first)
    sum = 0
    ___ i __ first:
        sum += i
    r_ sum/last

x = input("Insert some integer values: ")
x = x.split()
___ i __ range(len(x)):
    x[i] = int(x[i])

average = avg_list(x)

print("The result of the average =",round(average,2))