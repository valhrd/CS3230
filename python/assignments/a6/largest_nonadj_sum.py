def largest_nonadj_sum(arr: list[int]) -> int:
    n = len(arr)
    if n == 0:
        return 0
    elif n <= 2:
        return max(0, max(arr))
    
    a, b = max(arr[0], 0), max(max(arr[0:2]), 0)
    for i in range(2, n):
        a, b = b, max(a + arr[i], b)
    return b

indices = []
def brute_force(arr: list[int]) -> int:
    res = [0]
    indices = [()]
    def f(i, curr, last_included, res, indices, lst):
        if i == len(arr):
            if curr > res[0]:
                res[0] = curr
                indices[0] = tuple(lst)
            return
        if not last_included:
            lst.append(i)
            f(i + 1, curr + arr[i], True, res, indices, lst)
            lst.pop()
        f(i + 1, curr, False, res, indices, lst)
    f(0, 0, False, res, indices, [])
    return res[0], indices[0]

if __name__ == '__main__':
    import random

    N = 20
    all_correct = True
    for _ in range(1000):
        arr = [random.randint(-20, 20) for _ in range(N)]
        dp_res = largest_nonadj_sum(arr)
        answer, indices = brute_force(arr)
        if dp_res != answer:
            print(arr)
            print(f"Answers differ!: DP: {dp_res}, Brute Force: {answer}")
            all_correct = False
            break
    
    if all_correct:
        print("DP is correct algorithm")