# Time Complexity: O(MN) where M is length of A, N is length of B
# Space Complexity: O(MN) (O(min{M, N}) if we are just looking for the length of the longest possible subsequence)
def lcs(A: str, B: str) -> str:
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + (A[i - 1] == B[j - 1]))

    p, q = m, n
    res = []
    # Backtracking
    while p > 0 and q > 0:
        if A[p - 1] == B[q - 1]:
            res.append(A[p - 1])
            p -= 1
            q -= 1
        else:
            if dp[p - 1][q] > dp[p][q - 1]:
                p -= 1
            else:
                q -= 1
    res.reverse()
    return ''.join(res), dp[-1][-1]

if __name__ == '__main__':
    A = "aasbdescbd"
    B = "acbsdcdeb"
    print("Longest Common Subsequence found: {}, Length: {}".format(*lcs(A, B)))