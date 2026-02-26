# Time Complexity: O(W * I)
# Space Complexity: O(W * I) (can be reduced to O(W) since we only rely on the previous layer)
# This is NOT a polynomial algorithm since the knapsack volume/weight is expressed in O(log W) length
def knapsack_modified(item_limit: int, knapsack_weight: int, items: list[int]) -> int:
    n = len(items)
    W = knapsack_weight
    R = item_limit
    dp = [[[0] * (R + 1) for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for j in range(1, W + 1):
            for k in range(1, R + 1):
                dp[i][j][k] = dp[i - 1][j][k]
                if weight <= j:
                    dp[i][j][k] = max(dp[i - 1][j - weight][k - 1] + value, dp[i][j][k])
    return dp[n][W][R]

def brute_force(item_limit: int, knapsack_weight: int, items: list[int]) -> int:
    def f(index, curr_val, curr_weight, quantity, res):
        if quantity == item_limit or index == len(items):
            if curr_weight <= knapsack_weight:
                res[0] = max(res[0], curr_val)
            return
        f(index + 1, curr_val, curr_weight, quantity, res)
        f(index + 1, curr_val + items[index][1], curr_weight + items[index][0], quantity + 1, res)
    
    res = [0]
    f(0, 0, 0, 0, res)
    return res[0]

if __name__ == '__main__':
    item_limit = 3
    knapsack_weight = 15
    items = [
        (12, 4),
        (2, 2),
        (1, 1),
        (4, 10),
        (1, 2),
    ]
    print(f"DP Answer: {knapsack_modified(item_limit, knapsack_weight, items)}")
    print(f"Brute Force Solution: {brute_force(item_limit, knapsack_weight, items)}")