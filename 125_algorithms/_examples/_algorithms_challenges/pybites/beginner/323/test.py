from functools import reduce

#list = [1,2,3,4,5,6,7,8]
list = []

if list:
    new_list = reduce(lambda x,y: x+y, list)
    print(new_list)
else:
    print('empty')
    print(list)