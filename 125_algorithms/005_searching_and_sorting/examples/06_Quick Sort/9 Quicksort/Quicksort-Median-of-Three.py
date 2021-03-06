def quicksort(lst, low, high):
    # If the interval [low, high] is valid
    if low < high: 
        # Partition the list and get the partitioning index.
        pivot_index = partition(lst, low, high) 
  
        # Sort the elements in the list
        # that come before and after the partition 
        quicksort(lst, low, pivot_index-1) 
        quicksort(lst, pivot_index+1, high)

# Using Lomuto's Partition Scheme
def partition(lst, low, high):

    # ====================================
    # Pivot chosen using Median of Three
    
    middle = (low + high)//2
    
    if lst[middle] < lst[low]:
        swap(lst, middle, low)
        
    if lst[high] < lst[low]:
        swap(lst, low, high)
        
    if lst[middle] < lst[high]:
        swap(lst, middle, high)
    
    pivot = lst[high]

    # ====================================

    i = low - 1     
  
    for j in range(low, high): 
        # If the current element is smaller than
        # or equal to pivot 
        if lst[j] <= pivot: 
            # Increment index
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
             
    lst[i+1], lst[high] = lst[high], lst[i+1] 
    return i+1

# Swap the elements a and b in the list lst
def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
