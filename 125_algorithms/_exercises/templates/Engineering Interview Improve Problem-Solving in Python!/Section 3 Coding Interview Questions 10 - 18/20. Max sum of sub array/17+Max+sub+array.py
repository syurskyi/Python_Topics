# [1, 3, 2, -2, 4, 5] => [1, 3, 2] [4, 5] = 9 => 4, 5
# [] = - 1                  6
# [-1, -3] = -1
# [2] = 0 0
# [-1, 2] = 1 1

# break it down

___ max_sub_array(l):
    index_start  0
    index_end  0
    sum_of_sub_array  0
    new_sub_array_start  0
    sum_of_new_sub_array  0
    for index,val in enumerate(l):
        __ val < 0:
            # figure out the sum
            __ sum_of_sub_array < sum_of_new_sub_array:
                #swap subarray indexes
                index_start  new_sub_array_start
                index_end  index - 1
                sum_of_sub_array  sum_of_new_sub_array
                sum_of_new_sub_array  0
            new_sub_array_start  index + 1
        else:
            sum_of_new_sub_array + val
    
    __ sum_of_sub_array < sum_of_new_sub_array:
        #swap subarray indexes
        index_start  new_sub_array_start
        index_end  len(l) - 1
        sum_of_sub_array  sum_of_new_sub_array
    
    __ sum_of_sub_array __ 0:
        print(-1)
    else:
        print(index_start, index_end)

max_sub_array([2])
    
