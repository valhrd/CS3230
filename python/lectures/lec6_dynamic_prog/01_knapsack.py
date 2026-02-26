# Time Complexity: O(W * I)
# Space Complexity: O(W * I) (can be reduced to O(W) since we only rely on the previous layer)
# This is NOT a polynomial algorithm since the knapsack volume/weight is expressed in O(log W) length
def knapsack_slides(knapsack_weight: int, items: list[int]) -> int:
    n = len(items)
    W = knapsack_weight
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for j in range(1, W + 1):
            dp[i][j] = dp[i - 1][j]
            if weight <= j:
                dp[i][j] = max(dp[i - 1][j - weight] + value, dp[i][j])
    return dp[n][W]     

if __name__ == '__main__':
    knapsack_weight = 15
    items = [
        (12, 4),
        (2, 2),
        (1, 1),
        (4, 10),
        (1, 2),
    ]
    print(knapsack_slides(knapsack_weight, items))