def stooge_sort(arr: list[int], start: int, end: int):
    # Base case of array length 2
    if end - start == 1:
        if arr[start + 1] < arr[start]:
            arr[start], arr[start + 1] = arr[start + 1], arr[start]
        return
    
    t = (end - start + 1) // 3
    first_third = start + t
    second_third = end - t
    stooge_sort(arr, start, second_third)
    stooge_sort(arr, first_third, end)
    stooge_sort(arr, start, second_third)

def is_sorted(arr: list[int]) -> bool:
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            return False
    return True

if __name__ == '__main__':
    import random
    N = 100
    arr = [random.randint(0, 1000) for _ in range(N)]
    stooge_sort(arr, 0, len(arr) - 1)
    print(arr)
    print(f"Is sorted?: {is_sorted(arr)}")
