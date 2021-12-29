from collections import Counter
import operator

def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    temp_list = sorted(Counter(numbers).most_common(len(set(numbers))))
    temp_list.sort(key=operator.itemgetter(1))
    #print(type(temp_list[0][1]))
    print(temp_list)

    # you code ...
    #major=999
    #minor=111
    return temp_list[-1][0], temp_list[0][0]


print(major_n_minor([1, 3, 5, 7, 8, 8, 9, 9, 3, 5, 8, 7]))

#[1, 3, 5, 7, 8, 8, 9, 9, 3, 5, 8, 7]