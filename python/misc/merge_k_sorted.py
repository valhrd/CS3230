import random
from heapq import *

def merge_k_sorted(arrays):
    # Assuming input is as expected (i.e. all arrays sorted, each array has the same length)
    k = len(arrays)
    n = len(arrays[0])

    # Initialise array of pointers (pointers[i] is the index of the current element we are tracking in the i-th array)
    pointers = [0] * k

    # Initialise minheap with the smallest element of each array
    minheap = [(arrays[i][0], i) for i in range(k)]
    heapify(minheap)

    # Algorithm
    merged_res = []
    while minheap:
        # Pop the smallest element in the minheap
        current, array_index = heappop(minheap)
        # Add to the resultant merged array
        merged_res.append(current)
        # Increment the pointer in the corresponding
        pointers[array_index] += 1
        # Push the next element into the minheap if the pointer is not greater than n - 1
        next_index = pointers[array_index]
        if next_index < n:
            heappush(minheap, (arrays[array_index][next_index], array_index))
    return merged_res

def check_sorted(array):
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            return False
    return True

if __name__ == '__main__':
    # External parameters
    n = 20
    k = 10
    lower_lim = 1
    upper_lim = 1000
    # Randomise k arrays of size n and sort them
    arrays = [
        sorted([random.randint(lower_lim, upper_lim) for _ in range(n)]) for _ in range(k)
    ]
    # Check input
    print("Sorted arrays".center(100, '='))
    for arr in arrays:
        print(arr)

    print("Result".center(100, '='))
    merged_res = merge_k_sorted(arrays)
    print(merged_res)

    print("Sanity Check".center(100, '='))
    print(f"Is sorted?: {check_sorted(merged_res)}")