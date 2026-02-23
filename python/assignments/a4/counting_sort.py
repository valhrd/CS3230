def counting_sort(arr: list[tuple[int, int]]) -> list[tuple[int, int]]:
    assert min([num for num, _ in arr]) >= 0

    mx = max([num for num, _ in arr])
    count = [0] * (mx + 1)

    # Count frequencies
    for n, _ in arr:
        count[n] += 1

    # Accumulate counts
    for i in range(mx):
        count[i + 1] += count[i]
    
    # Create sorted array
    res = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        num, tag = arr[i]
        res[count[num] - 1] = (num, tag)
        count[num] -= 1
    return res

def is_sorted_and_stable(arr: list[tuple[int, int]]) -> bool:
    # Comparison based of tuple comparison
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            return False
    return True

if __name__ == '__main__':
    import random
    from collections import Counter

    n = 100
    k = 50
    counter = Counter()
    arr = []
    for _ in range(n):
        num = random.randint(0, k)
        arr.append((num, counter[num]))
        counter[num] += 1

    print("Before sorted".center(60, '='), '\n', arr)
    sorted_arr = counting_sort(arr)
    print("After sorted".center(60, '='), '\n', sorted_arr)
    print("Verify".center(60, '='),
          '\n', f"Same elements?: {Counter(arr) == Counter(sorted_arr)}",
          '\n', f"Sorted and Stable?: {is_sorted_and_stable(sorted_arr)}"
    )
