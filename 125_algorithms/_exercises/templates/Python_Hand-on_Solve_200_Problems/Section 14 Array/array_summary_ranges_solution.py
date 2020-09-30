# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""
Given a sorted integer array without duplicates,
return the summary of its ranges.
For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""

input_array _ [0,1,2,4,5,7]
# input_array = [1,2,3,6,9,11,12,13,14,19,20]

start_0
result _   # list

# i=0
# while i <= len(input_array)-1:
#     print(i, input_array[i])
#     i = i+1


while start < le.(input_array):
    
    # initial end at start position     
    end _ start

    # continue to move the end pointer if the gap is 1 with beside number
    # only continue to move if index end+1 is inside array     
    while end+1<le.(input_array) an. ((input_array[end+1] - input_array[end]) __ 1):
        end _ end + 1

    # add range to result after calculate     
    __ end!_start:
        result.ap..("{0}-->{1}".f..(input_array[start], input_array[end]))
        print(result)
    ____
        result.ap..("{0}".f..(input_array[start]))
        print(result)
        
    # change to next range
    start _ end+1

print(result)


            


