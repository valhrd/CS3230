# Time Complexity: O(T * C) where T is the target value, C is the number of denominations given
# Space Complexity: O(T) (can be reduced to O(C) with more complex handling)
# Similar reasoning to 0-1 Knapsack problem this is NOT a polynomial time algorithm
def change_coins(target: int, coins: list[int]) -> int:
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for v in range(len(dp)):
        for c in coins:
            if c <= v:
                dp[v] = min(dp[v], dp[v - c] + 1)
    return dp[target]

if __name__ == '__main__':
    coins = [1,10,25]
    target = 30
    print(change_coins(target, coins))