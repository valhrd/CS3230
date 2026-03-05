# The variant of this problem on LeetCode uses this definition of W
def W(values: list[int], a: int, b: int, c: int) -> int:
    return values[a] * values[b] * values[c]

def triangulate(values: list[int]) -> int:
    n = len(values)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n - 2):
        dp[i][i + 2] = W(values, i, i + 1, i + 2)
    
    for d in range(3, n):
        for k in range(n - d):
            dp[k][k + d] = min([dp[k][j] + W(values, k, j, k + d) + dp[j][k + d] for j in range(k + 1, k + d)])
    
    return dp[0][n - 1]

if __name__ == '__main__':
    import random

    N = 10
    values = [random.randint(1, 20) for _ in range(N)]
    values = [1,3,1,4,1,5]
    print(values)
    print(triangulate(values))