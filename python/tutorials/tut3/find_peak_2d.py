def find_peak(matrix: list[list[int]], topleft: tuple[int], bottomright:tuple[int]):
    a, b = topleft
    c, d = bottomright
    m, n = (a + c) // 2, (b + d) // 2

    local_max = -float('inf')
    position = None

    if c - a < 3 or d - b < 3:
        for i in range(a, c + 1):
            for j in range(b, d + 1):
                if matrix[i][j] > local_max:
                    local_max = matrix[i][j]
                    position = (i, j)
        return position

    # Scan window frame
    for i in [a, m, c]:
        for j in range(b, d + 1):
            if matrix[i][j] > local_max:
                local_max = matrix[i][j]
                position = (i, j)
    for j in [b, n, d]:
        for i in range(a, c + 1):
            if matrix[i][j] > local_max:
                local_max = matrix[i][j]
                position = (i, j)
    
    # Check if peak
    p, q = position
    DIR = [0,1,0,-1,0]
    for i in range(4):
        np, nq = p + DIR[i], q + DIR[i + 1]
        if not (0 <= np < len(matrix) and 0 <= nq < len(matrix[0])):
            continue
        if matrix[np][nq] > matrix[p][q]:
            if a < np < m:
                if b < nq < n:
                    return find_peak(matrix, (a + 1, b + 1), (m - 1, n - 1))
                else:
                    return find_peak(matrix, (a + 1, n + 1), (m - 1, d - 1))
            else:
                if b < nq < n:
                    return find_peak(matrix, (m + 1, b + 1), (c - 1, n - 1))
                else:
                    return find_peak(matrix, (m + 1, n + 1), (c - 1, d - 1))
    return position

if __name__ == '__main__':
    import random
    arr = [
        [1,1,1,1,1,1,1],
        [1,10,1,1,1,1,1],
        [1,1,8,1,1,1,1],
        [1,1,7,1,1,1,1],
        [1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1],
    ]
    for row in arr:
        print(row)

    print(find_peak(arr, (0, 0), (6, 6)))