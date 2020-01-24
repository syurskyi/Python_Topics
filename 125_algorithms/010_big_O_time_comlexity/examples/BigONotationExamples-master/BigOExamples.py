import time
# Big O Notation Examples


# 1. Constant O(1)
def constant(n):
    return "This returns: " + str(1) + " (regardless of n's value)"


# 2. Logarithmic O(log n) - Binary Search
def logarithmic(n, item):
    start, end, item_found = 0, len(n)-1, False
    start_time = time.time()

    while start <= end and not item_found:
        middle = (start + end)//2

        if n[middle] == item:
            item_found = True
        else:
            if item < n[middle]:
                end = middle-1
            else:
                start = middle + 1
    end_time = time.time()

    return "Took: " + str(end_time - start_time) + " Answer: " + str(item_found)


# 3. Linear O(n) - Prints out each value in n
def linear(n):
    start_time = time.time()
    for i in n:
        print(i)
    end_time = time.time()

    return "Took: " + str(end_time - start_time)


# 4.  Linearithmic time O(n log n) - Heapsort Example
def heapsort(n):

    start_time = time.time()
    length = len(n)
    endList = []
    last_parent_node = (len(n) // 2) - 1

    for i in range(last_parent_node, -1, -1):
        max_heapify(n, i)

    for i in range(length - 1, -1, -1):
        n[i], n[0] = n[0], n[i]
        endList.append(n[i])
        n.pop(i)
        max_heapify(n, 0)

    end_time = time.time()

    return "Took: " + str(end_time - start_time) + " Answer: " + str(endList[::-1])


def max_heapify(heap, root):
    left, right, largest = None, None, root

    if 2 * root + 1 < len(heap):
        left = 2 * root + 1

    if 2 * (root + 1) < len(heap):
        right = 2 * (root + 1)

    if left is not None and heap[left] > heap[root]:
        largest = left

    if right is not None and heap[right] > heap[largest]:
        largest = right

    if largest != root:
        heap[root], heap[largest] = heap[largest], heap[root]
        max_heapify(heap, largest)


# 5. Quadratic O(n^2)
def quadratic(n):
    ops = []
    start_time = time.time()
    for i in n:
        for j in n:
            ops.append(j)
    end_time = time.time()

    return "Took: " + str(end_time - start_time) + " Answer: " + str(len(ops))


# 6. Exponential O(2^n) - Fibonacci Sequence
def fibonacci(n):
    start_time = time.time()
    x = calc_fib(n)
    end_time = time.time()

    return "Took: " + str(end_time - start_time) + " Answer: " + str(x)


def calc_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calc_fib(n-1) + calc_fib(n-2)
