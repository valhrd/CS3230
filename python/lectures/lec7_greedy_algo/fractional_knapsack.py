# TC: O(nW^2) for n items and knapsack weight W
def dp_fractional_knapsack(knapsack_weight: int, items: list[tuple[int, int]]) -> int:
    n = len(items)
    W = knapsack_weight
    m = [[0] * (n + 1) for _ in range(W + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            weight, value = items[i - 1]
            m[i][j] = max([m[i - 1][j - partial] + partial * value / weight for partial in range(min(j, weight) + 1)])
    return m[n][W]

# TC: O(nlogn) for n items (Dominated by sorting the valeu-to-weight ratios in descending order)
def greedy_fractional_knapsack(knapsack_weight: int, items: list[tuple[int, int]]) -> int:
    value_to_weight_ratios = [(v / w, w) for w, v in items]
    value_to_weight_ratios.sort(reverse=True)

    best_value = 0
    for ratio, weight in value_to_weight_ratios:
        if knapsack_weight > 0:
            t = min(weight, knapsack_weight)
            best_value += ratio * t
            knapsack_weight -= t
        else:
            break
    return best_value

if __name__ == '__main__':
    knapsack_weight = 4
    # List of (weight, value) pairs
    items = [
        (1, 100),
        (5, 100),
        (3, 30),
        (4, 20),
    ]
    print(f"DP answer: {dp_fractional_knapsack(knapsack_weight, items)}")
    print(f"Greedy answer: {greedy_fractional_knapsack(knapsack_weight, items)}")