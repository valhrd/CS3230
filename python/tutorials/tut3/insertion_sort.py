def insertion_sort(arr: list[int]):
    for i in range(len(arr)):
        x = arr[i]
        saved_j = i
        for j in range(i - 1, -1, -1):
            if arr[j] > x:
                arr[j + 1] = arr[j]
                saved_j = j
            else:
                break
        arr[saved_j] = x

def is_sorted(arr: list[int]) -> bool:
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            return False
    return True

if __name__ == '__main__':
    import random
    N = 100
    arr = [random.randint(0, 1000) for _ in range(N)]
    insertion_sort(arr)
    print(arr)
    print(f"Is sorted?: {is_sorted(arr)}")