import random

def quicksort(arr: list[int], left: int, right: int):
    # Trivially sorted
    if left >= right:
        return

    pivot_placement = partition(arr, left, right)
    quicksort(arr, left, pivot_placement - 1)
    quicksort(arr, pivot_placement + 1, right)

def partition(arr: list[int], left: int, right: int):
    l = left
    pivot_index = random.randint(left, right)
    pivot = arr[pivot_index]
    # Swap pivot entry with last 
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    for r in range(left, right):
        if arr[r] < pivot:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
    # Place pivot in correct position
    arr[l], arr[right] = arr[right], arr[l]
    return l

if __name__ == '__main__':
    arr = list(range(1, 26))
    random.shuffle(arr)
    print('Before'.center(60, '='))
    print(arr)
    quicksort(arr, 0, len(arr) - 1)
    print('After'.center(60, '='))
    print(arr)