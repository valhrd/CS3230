def minimise_abs_diff(arr: list[int]) -> int:
    n = len(arr)
    T = sum(arr)
    dp = [False] * (T + 1)

    dp[0] = True
    dp[arr[0]] = True
    
    for i in range(1, n):
        temp = [False] * (T + 1)
        temp[0] = True
        for j in range(1, T + 1):
            temp[j] = dp[j]
            if arr[i] <= j:
                temp[j] |= dp[j - arr[i]]
        dp = temp
    
    res = float('inf')
    for S_Y in range(len(dp)):
        if dp[S_Y]:
            res = min(res, abs(T - 3 * S_Y))
    return res
    
def brute_force_min(arr: list[int]) -> int:
    def dfs(X, Y, index, res):
        if index == len(arr):
            res[0] = min(res[0], abs(X - 2 * Y))
            return
        dfs(X + arr[index], Y, index + 1, res)
        dfs(X, Y + arr[index], index + 1, res)
    
    res = [float('inf')]
    dfs(0, 0, 0, res)
    return res[0]

if __name__ == '__main__':
    import random
    arr = [random.randint(0, 10) for _ in range(15)]
    print(f"Array: {arr}")
    print(f"DP Attempt Result: {minimise_abs_diff(arr)}")
    print(f"Brute Force Result: {brute_force_min(arr)}")