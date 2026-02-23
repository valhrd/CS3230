def radix_sort(arr: list[int], base: int = 2) -> list[int]:
    assert min(arr) >= 0 and base > 1

    def bits(n):
        res = 0
        while n > 0:
            res += 1
            n //= base
        return res
    
    upper = bits(max(arr))
    prev = arr.copy()
    for i in range(upper):
        buckets = [[] for _ in range(base)]
        for j in range(len(prev)):
            buckets[(prev[j] // (base ** i)) % base].append(prev[j])
        
        temp = []
        for subseq in buckets:
            temp.extend(subseq)
        prev = temp
    return prev

if __name__ == '__main__':
    import random
    from collections import Counter

    n = 1000
    k = 250
    arr = [random.randint(0, k) for _ in range(n)]
    print("Before sorted".center(60, '='), '\n', arr)
    sorted_arr = radix_sort(arr, base=10)
    print("After sorted".center(60, '='), '\n', sorted_arr)
    print("Verify".center(60, '='), '\n', f"Same number of elements?: {Counter(arr) == Counter(sorted_arr)}")